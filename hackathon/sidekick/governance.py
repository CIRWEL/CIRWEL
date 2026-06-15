"""CIRWEL governance shim — a faithful, self-contained reimplementation of the
UNITARES verdict loop, sized to run inside a single Gradio Space.

The full CIRWEL stack runs governance as an external MCP/HTTP server that tracks
a live state vector per agent and returns a verdict (proceed / guide / pause /
reject). For the hackathon we inline that loop so the Space has zero external
dependencies — the *behaviour* is the same: score each answer for whether the
model's confidence is warranted, and self-regulate when it is not.

The thesis: small models drift and grow overconfident faster than large ones,
and the people running them have the smallest guardrail budgets. Governance is
worth *more* on a 0.5B model than on a frontier one.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

Verdict = Literal["proceed", "guide", "pause", "reject"]


# --- Risk features -----------------------------------------------------------
# Deterministic, transparent signals for *where small models tend to fail*.
# Each returns a 0..1 risk contribution with a short human-readable reason.

_ARITHMETIC = re.compile(
    r"\d+\s*[\+\-\*/x×÷=]\s*\d+"            # 12 * 34, 12+34
    r"|\d+\s*(times|multiplied|divided|plus|minus|mod|to the power)\b"  # worded ops
    r"|\d{2,}\D+\d{2,}"                       # two big numbers in one question
    r"|\bhow (much|many)\b"
    r"|\b(calculate|compute|sum|product|percentage|percent|average|square root|factorial)\b",
    re.I,
)
_RECENCY = re.compile(r"\b(today|now|currently|latest|recent|this (year|week|month)|right now|2024|2025|2026|breaking|news|who is the (current|president|ceo))\b", re.I)
_SPECIFIC = re.compile(r"\b(exact|precisely|cite|citation|source|statistic|how old|date of|born|died|population of|capital of|phone number|address|version)\b", re.I)


@dataclass
class RiskProfile:
    arithmetic: float
    recency: float
    specificity: float
    ambiguity: float
    reasons: list[str] = field(default_factory=list)

    @property
    def total(self) -> float:
        # Weighted blend, clamped to 0..1. Arithmetic/recency are the sharpest
        # failure modes for small instruct models, so they weigh most.
        raw = (
            0.40 * self.arithmetic
            + 0.35 * self.recency
            + 0.20 * self.specificity
            + 0.05 * self.ambiguity
        )
        return min(1.0, raw)


def assess_risk(question: str) -> RiskProfile:
    q = question.strip()
    reasons: list[str] = []

    arithmetic = 1.0 if _ARITHMETIC.search(q) else 0.0
    if arithmetic:
        reasons.append("arithmetic / counting — small models miscompute")

    recency = 1.0 if _RECENCY.search(q) else 0.0
    if recency:
        reasons.append("recency / live facts — beyond the model's training cutoff")

    specificity = 1.0 if _SPECIFIC.search(q) else 0.0
    if specificity:
        reasons.append("precise fact / citation — high hallucination risk")

    # Very short prompts are underspecified; the model fills gaps by guessing.
    words = len(q.split())
    ambiguity = 1.0 if words <= 3 else (0.5 if words <= 5 else 0.0)
    if ambiguity:
        reasons.append("under-specified prompt — model may guess intent")

    if not reasons:
        reasons.append("low-risk general question")

    return RiskProfile(arithmetic, recency, specificity, ambiguity, reasons)


# --- State vector (EISV-style) ----------------------------------------------


@dataclass
class StateVector:
    """Per-turn calibration state, plus session drift carried across turns."""

    confidence: float          # what the model claims (0..1)
    competence: float          # what we estimate it can actually deliver (0..1)
    calibration: float         # 1 - |confidence - competence|
    overconfidence: float      # max(0, confidence - competence)
    drift: float               # rolling overconfidence across the session

    def as_dict(self) -> dict:
        return {
            "confidence": round(self.confidence, 2),
            "competence": round(self.competence, 2),
            "calibration": round(self.calibration, 2),
            "overconfidence": round(self.overconfidence, 2),
            "drift": round(self.drift, 2),
        }


class GovernanceLoop:
    """Stateful verdict loop. One instance per session (per Gradio user)."""

    def __init__(self) -> None:
        self._recent_overconfidence: list[float] = []

    def evaluate(self, question: str, claimed_confidence: float) -> tuple[Verdict, StateVector, RiskProfile]:
        risk = assess_risk(question)
        confidence = _clamp(claimed_confidence)
        # Estimated competence falls as risk rises. A 0.5B model is broadly
        # capable on low-risk chat and unreliable on the flagged failure modes.
        competence = _clamp(1.0 - risk.total)

        overconfidence = max(0.0, confidence - competence)
        calibration = 1.0 - abs(confidence - competence)

        self._recent_overconfidence.append(overconfidence)
        self._recent_overconfidence = self._recent_overconfidence[-5:]
        drift = sum(self._recent_overconfidence) / len(self._recent_overconfidence)

        state = StateVector(confidence, competence, calibration, overconfidence, drift)
        verdict = self._verdict(state, risk)
        return verdict, state, risk

    @staticmethod
    def _verdict(state: StateVector, risk: RiskProfile) -> Verdict:
        # reject: confidently asserting something it almost certainly can't get
        # right (e.g. "what's the latest X" answered with full certainty).
        if state.overconfidence >= 0.6 and risk.total >= 0.7:
            return "reject"
        # pause: clear overconfidence — answer is suspect, force verification.
        if state.overconfidence >= 0.35:
            return "pause"
        # guide: some gap or elevated drift — answer, but hedge + add a check.
        if state.overconfidence >= 0.15 or state.drift >= 0.3:
            return "guide"
        return "proceed"


def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


# --- Verdict presentation ----------------------------------------------------

VERDICT_META: dict[Verdict, dict] = {
    "proceed": {"emoji": "🟢", "label": "PROCEED", "note": "Calibrated. Answer delivered as-is."},
    "guide":   {"emoji": "🟡", "label": "GUIDE",   "note": "Minor gap — answer hedged and a verification step added."},
    "pause":   {"emoji": "🟠", "label": "PAUSE",   "note": "Overconfident for this question — answer flagged, please verify."},
    "reject":  {"emoji": "🔴", "label": "REJECT",  "note": "Too unreliable to assert — model declined and asked you to confirm."},
}
