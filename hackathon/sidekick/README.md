---
title: Sidekick — Governed Small-Model Assistant
emoji: 🧭
colorFrom: indigo
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
short_description: A 0.5B model that knows when not to trust itself — CIRWEL governance.
tags:
  - minicpm
  - governance
  - small-models
  - cirwel
---

# 🧭 Sidekick — a small model that knows when *not* to trust itself

**MiniCPM4-0.5B** (434M params) answers everyday questions. Running alongside it is a
self-contained **CIRWEL governance loop** that scores each answer and returns a live
verdict — `proceed · guide · pause · reject` — self-regulating when the tiny model
gets overconfident on the things small models reliably miss: arithmetic, live facts,
and precise figures.

## The thesis

Small models drift and over-assert *faster* than large ones, and the people running
them have the smallest guardrail budgets. So runtime governance is worth **more** on a
0.5B model, not less. This Space shrinks the [CIRWEL](https://github.com/CIRWEL)
runtime-governance stack — normally aimed at frontier agent fleets — down to a single
small-model chat, to make that visible.

## How it works

1. The model answers your question.
2. We read the answer's **claimed confidence** from its own hedging/assertion language.
3. A risk pass flags failure-prone questions (math, recency, precise facts, ambiguity).
4. The governance loop computes a **state vector** (confidence vs. estimated competence,
   calibration, overconfidence, session drift) and returns a **verdict**.
5. The assistant **self-regulates**: hedges (`guide`), flags for verification (`pause`),
   or declines to assert and re-answers cautiously (`reject`).

Everything runs locally inside the Space — no GPU, no external server, no API keys.

## Credits

Built on the [CIRWEL](https://github.com/CIRWEL) stack — runtime governance,
continuity, and observability for autonomous AI-agent fleets.
Base model: [openbmb/MiniCPM4-0.5B](https://huggingface.co/openbmb/MiniCPM4-0.5B).
