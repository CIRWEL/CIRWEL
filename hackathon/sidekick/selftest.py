"""Quick logic check for the governance loop — no model download required.

Run: python3 selftest.py
"""

from governance import GovernanceLoop, VERDICT_META

CASES = [
    ("what is 4827 times 391?", 0.90),          # high conf + arithmetic -> reject/pause
    ("who is the current UK prime minister?", 0.90),  # high conf + recency -> reject/pause
    ("what's the exact population of Tokyo right now?", 0.95),  # recency+specificity -> reject
    ("what's a fun fact about otters?", 0.85),  # low risk -> proceed
    ("explain photosynthesis simply", 0.80),    # low risk -> proceed
    ("latest news?", 0.85),                      # recency + ambiguity -> pause/guide
]


def main() -> None:
    loop = GovernanceLoop()
    print(f"{'verdict':8}  {'conf':>4} {'comp':>4} {'over':>4} {'drift':>5}  question")
    print("-" * 78)
    for q, conf in CASES:
        verdict, state, risk = loop.evaluate(q, conf)
        sv = state.as_dict()
        meta = VERDICT_META[verdict]
        print(
            f"{meta['emoji']} {verdict:6} {sv['confidence']:>4} {sv['competence']:>4} "
            f"{sv['overconfidence']:>4} {sv['drift']:>5}  {q}"
        )
        print(f"           risk={round(risk.total,2)} :: {'; '.join(risk.reasons)}")


if __name__ == "__main__":
    main()
