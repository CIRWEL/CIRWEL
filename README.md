<img alt="CIRWEL stack — runtime governance for heterogeneous AI-agent fleets" src="./assets/cirwel-stack.svg" width="100%">

## CIRWEL

CIRWEL is an independent research and systems lab, founded by Kenny Wang, building runtime governance, continuity, and observability infrastructure for autonomous AI-agent fleets.

Agents fail gradually before they fail visibly — drifting, thrashing, growing overconfident on stale context. CIRWEL builds the state layer that lets agents notice and act on that drift before it becomes an incident.

```
agent acts  →  check-in  →  calibrated state + verdict  →  self-regulates  →  audit trail
```

The CIRWEL stack has run continuously since November 2025 as a single-operator deployment. That is a stress test, not a claim of external adoption.

### For reviewers

- **What this is:** runtime state telemetry for agent fleets after deployment — the layer between evals/guardrails and incident response.
- **What this is not:** not an output filter, not a sandbox, not a universal ethics oracle, and not yet a claim of external adoption.
- **Initial wedge:** teams running long-lived coding, research, or operations agents add one MCP/REST check-in per unit of work plus outcome events from tests, tools, and other hard signals.
- **Current ask:** external pilots and [design partners](./docs/design-partners.md) who already operate autonomous agents long enough for drift, calibration, and recovery to matter.

**Read order:**

1. **3 minutes:** [`unitares`](https://github.com/CIRWEL/unitares) → run `docker compose up` + `make demo`.
2. **10 minutes:** add [`unitares-governance-plugin`](https://github.com/CIRWEL/unitares-governance-plugin), [`unitares-host-adapter`](https://github.com/CIRWEL/unitares-host-adapter), and [`anima-mcp`](https://github.com/CIRWEL/anima-mcp).
3. **30 minutes:** read [`unitares-paper-v6`](https://github.com/CIRWEL/unitares-paper-v6), reproduce §11.6 with [`unitares-repro-v6`](https://github.com/CIRWEL/unitares-repro-v6), and inspect [`eisv-lumen`](https://github.com/CIRWEL/eisv-lumen).

---

### Stack

<table>
<tr>
<td width="50%" valign="top">

**Runtime governance**

[UNITARES](https://github.com/CIRWEL/unitares) is the MCP + HTTP governance server. Agents check in; UNITARES tracks a live state vector per agent and returns a verdict — `proceed`, `guide`, `pause`, or `reject` — so agents self-regulate before circuit breakers fire.

</td>
<td width="50%" valign="top">

**Host integrations**

[Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin), [host adapter](https://github.com/CIRWEL/unitares-host-adapter), and [hermes-agent](https://github.com/CIRWEL/hermes-agent) mount governance into Claude Code, Codex, and other agent hosts.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Peer review on disagree**

When an agent's confidence and the system's assessment diverge, UNITARES runs a short dialectic with peer agents — or an LLM, when no peers are around — before anything halts. Training data: [dialectic-dataset](https://github.com/CIRWEL/dialectic-dataset).

</td>
<td width="50%" valign="top">

**Research and observability**

[Paper v6](https://github.com/CIRWEL/unitares-paper-v6) (concept DOI [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159)) on heterogeneous-fleet calibration · [repro kit](https://github.com/CIRWEL/unitares-repro-v6) for the §11.6 verdict counterfactual · [Discord bridge](https://github.com/CIRWEL/unitares-discord-bridge) for live operator visibility.

</td>
</tr>
</table>

### Research

Papers stay in their own repos so each keeps its DOI, license, and release cadence — this is the index.

- **[UNITARES v6](https://github.com/CIRWEL/unitares-paper-v6)** — information-theoretic governance of heterogeneous agent fleets. Concept DOI [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159) · repro kit [`unitares-repro-v6`](https://github.com/CIRWEL/unitares-repro-v6) reproduces the §11.6 verdict counterfactual.
- **[Trajectory Identity](https://github.com/CIRWEL/trajectory-identity-paper)** — identity for AI agents as a dynamical-systems trajectory signature, validated on Lumen (Raspberry Pi 4, 65 days, 226k observations). Working draft v0.11 · CC BY 4.0.
- **[Digital Proprioception & Allostatic Load](https://github.com/CIRWEL/digital-proprioception-paper)** — the cumulative-deviation hypothesis implemented in a deployed multi-agent system; bridges UNITARES governance to McEwen's allostatic-load framework.

### Featured Repositories

[UNITARES](https://github.com/CIRWEL/unitares) · [Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin) · [host adapter](https://github.com/CIRWEL/unitares-host-adapter) · [Anima/Lumen](https://github.com/CIRWEL/anima-mcp) · [EISV-Lumen](https://github.com/CIRWEL/eisv-lumen) · [Paper v6](https://github.com/CIRWEL/unitares-paper-v6) · [repro kit](https://github.com/CIRWEL/unitares-repro-v6)

---

<sub>

[HuggingFace](https://huggingface.co/hikewa) · [ORCID](https://orcid.org/0009-0006-7544-2374) · [CIRWEL Systems](https://cirwel.org) · founder@cirwel.org

</sub>
