<img alt="CIRWEL stack — runtime governance for heterogeneous AI-agent fleets" src="./assets/cirwel-stack.svg" width="100%">

## Kenny Wang — CIRWEL Systems

I build **runtime accountability infrastructure for long-lived AI-agent systems**: a self-hosted checkpoint layer that operates *after* deployment, while agents are running. At meaningful checkpoints it binds claims to a process identity, updates a longitudinal state estimate, returns an auditable `proceed` or `pause` action, and preserves the evidence behind it.

The maintainer deployment has run continuously on a single-operator development fleet since **November 2025**. That establishes sustained operation under real load, not incident prevention, predictive utility, or cross-operator generality. External pilots are the next step.

### → [**cirwel.github.io**](https://cirwel.github.io) — the full index

Papers, systems, datasets, and decks, all in one place. **That page is canonical**; this profile is just the front door.

[![Index](https://img.shields.io/badge/▶_Full_index-cirwel.github.io-5eead4?style=for-the-badge&labelColor=0f171f)](https://cirwel.github.io)
[![UNITARES](https://img.shields.io/badge/UNITARES-governance_runtime-1f6feb?style=for-the-badge&labelColor=0f171f)](https://github.com/CIRWEL/unitares)
[![Paper v6](https://img.shields.io/badge/Paper_v6-DOI-8957e5?style=for-the-badge&labelColor=0f171f)](https://doi.org/10.5281/zenodo.19647159)

---

### The work, in four lines

| | | |
|---|---|---|
| **UNITARES** | Governance runtime (MCP + HTTP, Postgres-backed) | Agents check in; it updates a longitudinal state estimate from claims, available outcomes, and behavioral history, then returns a binary `proceed` or `pause` action with a reason. `guide` and `reject` are sub-actions, not peer verdicts. Live since Nov 2025. → [repo](https://github.com/CIRWEL/unitares) |
| **Anima** | Physical longitudinal testbed | Raspberry Pi 4 + sensor stack mapping real temperature, light, humidity, pressure, and system telemetry into EISV trajectories. It produced the 39-day real run behind the real-window portion of the labeled dataset; the richer creature/art interface lives in the repo. → [anima-mcp](https://github.com/CIRWEL/anima-mcp) |
| **Research** | 3 papers / preprints | Information-theoretic fleet governance ([v6, DOI](https://doi.org/10.5281/zenodo.19647159)) · trajectory identity ([Wang 2026b](https://github.com/CIRWEL/trajectory-identity-paper)) · digital proprioception ([Wang 2026c](https://github.com/CIRWEL/digital-proprioception-paper)). |
| **Datasets** | Published telemetry corpora | [32,181 labeled EISV windows](https://huggingface.co/datasets/hikewa/unitares-eisv-trajectories): 20,655 overlapping real windows from one 39-day Raspberry Pi run plus 11,526 synthetic · [verdict-counterfactual repro kit](https://github.com/CIRWEL/unitares-repro-v6). |

**Start here:** [`unitares`](https://github.com/CIRWEL/unitares) → `docker compose up -d --wait && make demo` drives a synthetic agent through six check-ins and prints the policy response at each step.

**Build on it:** [`unitares-sdk`](https://pypi.org/project/unitares-sdk/) on PyPI is the agent-side contract (check-in loop, EISV state, identity anchors). `pip install unitares-sdk`.

### For reviewers

- **What this is:** self-hosted runtime accountability and state estimation for long-lived agent processes, the checkpoint layer between evals/guardrails and incident response.
- **What this is not:** not an output filter, not a sandbox, not a correctness or ethics oracle, and not evidence yet of preventive benefit or cross-operator generality.
- **Current ask:** external pilots and [design partners](./docs/design-partners.md) who already run autonomous agents long enough for drift, calibration, and recovery to matter.

---

<sub>

[Full index ↗](https://cirwel.github.io) · [GitHub](https://github.com/CIRWEL) · [HuggingFace](https://huggingface.co/hikewa) · [ORCID](https://orcid.org/0009-0006-7544-2374) · [CIRWEL Systems](https://cirwel.org) · founder@cirwel.org

</sub>
