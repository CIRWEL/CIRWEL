# Deploy & share — Sidekick

This is a self-contained Gradio app. It runs free on a **CPU** Hugging Face Space
(no GPU, no API keys). You'll deploy it to your own account (`hikewa`).

## Option A — push with `huggingface_hub` (fastest)

```bash
pip install -U huggingface_hub
huggingface-cli login        # paste a token with *write* scope

python - <<'PY'
from huggingface_hub import create_repo, upload_folder
repo_id = "hikewa/sidekick"          # change the name if you like
create_repo(repo_id, repo_type="space", space_sdk="gradio", exist_ok=True)
upload_folder(
    repo_id=repo_id,
    repo_type="space",
    folder_path="hackathon/sidekick",
    ignore_patterns=["selftest.py", "DEPLOY.md"],   # optional: keep the Space clean
)
print("Deployed: https://huggingface.co/spaces/" + repo_id)
PY
```

The Space will build (installs `requirements.txt`, downloads MiniCPM4-0.5B on first
run) and go live at `https://huggingface.co/spaces/hikewa/sidekick`.

## Option B — git push

1. Create a new **Gradio** Space at https://huggingface.co/new-space (CPU basic, free).
2. Clone it and copy these files in (`app.py`, `governance.py`, `requirements.txt`, `README.md`):
   ```bash
   git clone https://huggingface.co/spaces/hikewa/sidekick
   cp hackathon/sidekick/{app.py,governance.py,requirements.txt,README.md} sidekick/
   cd sidekick && git add . && git commit -m "Sidekick: governed small-model assistant" && git push
   ```

## Verify locally first (optional)

```bash
pip install gradio torch transformers accelerate sentencepiece
cd hackathon/sidekick && python app.py   # opens http://127.0.0.1:7860
```

Logic-only check (no model download): `python hackathon/sidekick/selftest.py`

## Social post draft

> Built a tiny thing: **Sidekick** — a 0.5B model (MiniCPM4) that knows when *not*
> to trust itself. 🧭
>
> A live governance loop scores every answer and flips to ⏸️ pause / 🛑 reject when
> the small model gets overconfident on math, live facts, or precise figures — then
> self-corrects.
>
> The bet: small models need runtime governance *more* than big ones, and their
> operators have the smallest guardrail budgets. Built on the CIRWEL stack.
>
> Try it 👉 https://huggingface.co/spaces/hikewa/sidekick
> #BuildSmall @huggingface @openbmb

> **Note:** this is a standalone public demo, not an official Build Small entry
> (registration closed June 3). It rides the theme to show CIRWEL governance shrunk
> down to a single small model.
