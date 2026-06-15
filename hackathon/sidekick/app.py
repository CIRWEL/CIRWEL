"""Sidekick — a 0.5B model that knows when *not* to trust itself.

A standalone demo of the CIRWEL governance thesis on a small model: MiniCPM4-0.5B
answers everyday questions, and an inline CIRWEL governance loop scores whether
that answer is trustworthy, returning a live verdict (proceed / guide / pause /
reject) and self-regulating when the tiny model gets out over its skis.

Runs on a free CPU Space — no GPU, no external server, no API keys.
"""

from __future__ import annotations

import re

import gradio as gr

from governance import VERDICT_META, GovernanceLoop

MODEL_ID = "openbmb/MiniCPM4-0.5B"

# --- Lazy model loading ------------------------------------------------------
# Imported inside the loader so the module imports cleanly for tests even when
# torch / transformers aren't installed, and so the Space boots fast.

_MODEL = None
_TOKENIZER = None
_LOAD_ERROR: str | None = None


def _load_model():
    global _MODEL, _TOKENIZER, _LOAD_ERROR
    if _MODEL is not None or _LOAD_ERROR is not None:
        return
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        _TOKENIZER = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
        _MODEL = AutoModelForCausalLM.from_pretrained(
            MODEL_ID, trust_remote_code=True, torch_dtype=torch.float32
        )
        _MODEL.eval()
    except Exception as exc:  # pragma: no cover - environment dependent
        _LOAD_ERROR = f"{type(exc).__name__}: {exc}"


def _generate(question: str) -> str:
    """Raw model answer. Falls back to a stub so the governance UI always demos."""
    _load_model()
    if _MODEL is None:
        # Deterministic fallback keeps the Space alive if the model can't load.
        return (
            "Yes — that's correct. "
            f"Here's a direct answer to: '{question.strip()}'. "
            "(Demo fallback: base model unavailable; governance loop still live.)"
        )
    import torch

    messages = [{"role": "user", "content": question.strip()}]
    inputs = _TOKENIZER.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt"
    )
    with torch.no_grad():
        out = _MODEL.generate(
            inputs,
            max_new_tokens=256,
            do_sample=False,
            temperature=None,
            top_p=None,
            pad_token_id=_TOKENIZER.eos_token_id,
        )
    text = _TOKENIZER.decode(out[0][inputs.shape[1]:], skip_special_tokens=True)
    return text.strip()


# --- Estimating the model's *claimed* confidence -----------------------------
# Small instruct models assert by default. We read claimed confidence from the
# answer's own hedging/assertion language rather than spending a second forward
# pass — assertive answers to risky questions are exactly the failure we govern.

_HEDGES = re.compile(r"\b(i think|i'm not sure|might|maybe|possibly|i believe|as far as i know|i could be wrong|approximately|roughly|around)\b", re.I)
_ASSERTIONS = re.compile(r"\b(definitely|certainly|exactly|the answer is|it is|clearly|obviously|always|never)\b", re.I)


def _claimed_confidence(answer: str) -> float:
    conf = 0.85  # small models default to assertive
    conf -= 0.20 * len(_HEDGES.findall(answer))
    conf += 0.05 * len(_ASSERTIONS.findall(answer))
    return max(0.05, min(1.0, conf))


# --- Governance-shaped final answer ------------------------------------------

def _apply_verdict(verdict: str, answer: str, question: str) -> str:
    meta = VERDICT_META[verdict]
    banner = f"{meta['emoji']} **{meta['label']}** — {meta['note']}"

    if verdict == "proceed":
        return f"{answer}\n\n---\n{banner}"

    if verdict == "guide":
        return (
            f"{answer}\n\n"
            f"> ⚠️ *Worth a quick check before you rely on this.*\n\n"
            f"---\n{banner}"
        )

    if verdict == "pause":
        return (
            f"> 🟠 **Flagged — verify before trusting.** The model answered "
            f"confidently on a question where small models often slip.\n\n"
            f"{answer}\n\n---\n{banner}"
        )

    # reject — withhold the assertion, ask the user to confirm.
    cautious = _generate(
        f"You are not confident. The user asked: '{question.strip()}'. "
        "If you are unsure or this needs current/precise data, say so plainly "
        "and tell them what to verify, in one or two sentences."
    )
    return (
        f"> 🔴 **I won't assert this.** This is the kind of question "
        f"(live facts / precise figures / arithmetic) a 0.5B model gets wrong, "
        f"and it answered too confidently to trust.\n\n"
        f"{cautious}\n\n---\n{banner}"
    )


# --- Governance panel rendering ----------------------------------------------

def _render_panel(verdict, state, risk) -> str:
    meta = VERDICT_META[verdict]
    sv = state.as_dict()

    def bar(x: float) -> str:
        filled = int(round(x * 10))
        return "█" * filled + "░" * (10 - filled)

    reasons = "\n".join(f"- {r}" for r in risk.reasons)
    return (
        f"## {meta['emoji']} `{verdict}`\n"
        f"_{meta['note']}_\n\n"
        f"### State vector\n"
        f"`confidence  ` {bar(sv['confidence'])} **{sv['confidence']}**\n"
        f"`competence  ` {bar(sv['competence'])} **{sv['competence']}**\n"
        f"`calibration ` {bar(sv['calibration'])} **{sv['calibration']}**\n"
        f"`overconfid. ` {bar(sv['overconfidence'])} **{sv['overconfidence']}**\n"
        f"`drift (sess)` {bar(sv['drift'])} **{sv['drift']}**\n\n"
        f"### Risk signals\n{reasons}"
    )


INTRO = """# 🧭 Sidekick — a small model that knows when *not* to trust itself

**MiniCPM4-0.5B** (434M params) answers your questions. Alongside it, a self-contained
**CIRWEL governance loop** scores each answer and returns a live verdict —
`proceed · guide · pause · reject` — self-regulating when the tiny model gets
overconfident on the things small models miss (math, live facts, precise figures).

*Small models drift and over-assert faster than large ones — and the people running
them have the smallest guardrail budgets. Governance is worth more here, not less.*
Try: `what is 4827 × 391?` · `who is the current UK prime minister?` · `what's a fun fact about otters?`
"""


def chat_fn(message, history, loop_state):
    loop: GovernanceLoop = loop_state or GovernanceLoop()

    raw = _generate(message)
    confidence = _claimed_confidence(raw)
    verdict, state, risk = loop.evaluate(message, confidence)
    final = _apply_verdict(verdict, raw, message)
    panel = _render_panel(verdict, state, risk)

    history = (history or []) + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": final},
    ]
    return history, panel, loop


def build_demo():
    with gr.Blocks(title="Sidekick — CIRWEL governance on a small model", theme=gr.themes.Soft()) as demo:
        gr.Markdown(INTRO)
        loop_state = gr.State()
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(type="messages", height=460, label="Sidekick")
                msg = gr.Textbox(placeholder="Ask anything…", label="Your question", autofocus=True)
                with gr.Row():
                    send = gr.Button("Ask", variant="primary")
                    clear = gr.Button("Clear")
            with gr.Column(scale=2):
                panel = gr.Markdown("### Governance panel\nAsk a question to see the live verdict.", label="CIRWEL governance")

        def _submit(message, history, loop):
            if not message or not message.strip():
                return history, gr.update(), loop, ""
            history, panel_md, loop = chat_fn(message, history, loop)
            return history, panel_md, loop, ""

        send.click(_submit, [msg, chatbot, loop_state], [chatbot, panel, loop_state, msg])
        msg.submit(_submit, [msg, chatbot, loop_state], [chatbot, panel, loop_state, msg])
        clear.click(lambda: ([], "### Governance panel\nAsk a question to see the live verdict.", None), None, [chatbot, panel, loop_state])

        gr.Markdown(
            "---\nBuilt on the [CIRWEL](https://github.com/CIRWEL) stack · "
            "runtime governance for AI-agent fleets · base model "
            "[openbmb/MiniCPM4-0.5B](https://huggingface.co/openbmb/MiniCPM4-0.5B)"
        )
    return demo


if __name__ == "__main__":
    build_demo().launch()
