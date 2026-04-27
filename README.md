<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/CIRWEL/unitares/master/docs/assets/hero.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/CIRWEL/unitares/master/docs/assets/hero.svg">
  <img alt="UNITARES — runtime governance for heterogeneous AI-agent fleets" src="https://raw.githubusercontent.com/CIRWEL/unitares/master/docs/assets/hero.svg" width="100%">
</picture>

## Kenny Wang

Independent researcher building runtime governance for autonomous AI-agent fleets.

Agents fail gradually before they fail visibly — drifting, thrashing, growing overconfident on stale context. UNITARES gives each agent a calibrated state vector it can read back, and an intervention verdict it can act on, so the agent itself can narrow scope, request review, or stop. State layer, not output filter.

```
agent acts  →  check-in  →  calibrated state + verdict  →  self-regulates  →  audit trail
```

Running continuously since November 2025 as a single-operator deployment — that's a stress test, not a claim of external adoption.

---

### Featured

<table>
<tr>
<td width="50%" valign="top">

**[UNITARES](https://github.com/CIRWEL/unitares)**
Runtime governance server. Coupled ODE state model (energy, integrity, entropy, valence), class-conditional calibration, dialectic recovery, and a shared knowledge graph. MCP + HTTP. 6,200+ tests at 77% coverage.

</td>
<td width="50%" valign="top">

**[Paper v6](https://github.com/CIRWEL/unitares-paper-v6)** — *Information-Theoretic Governance of Heterogeneous Agent Fleets*
Argues fleet-wide normalization breaks under heterogeneous agent populations; proposes class-conditional calibration. 13,310-row counterfactual: 28.9% of basin assignments flip. DOI [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159) · [repro kit](https://github.com/CIRWEL/unitares-repro-v6).

</td>
</tr>
<tr>
<td width="50%" valign="top">

**[Lumen](https://github.com/CIRWEL/anima-mcp)**
Embodied agent on a Raspberry Pi — sensors, TFT display, neural band, UNITARES governance. Physical substrate for testing identity, continuity, and what happens when an agent persists across reboots.

</td>
<td width="50%" valign="top">

**[Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin)**
Client-side adapters for Claude Code, Codex/ChatGPT, and other MCP hosts. Hooks for lifecycle, check-ins, dialectic review, and knowledge-graph workflows.

</td>
</tr>
</table>

### Adapters & ecosystem

[hermes-agent](https://github.com/CIRWEL/hermes-agent) · [unitares-host-adapter](https://github.com/CIRWEL/unitares-host-adapter) · [unitares-discord-bridge](https://github.com/CIRWEL/unitares-discord-bridge) · [eisv-lumen benchmark](https://github.com/CIRWEL/eisv-lumen) · [dialectic-dataset](https://github.com/CIRWEL/dialectic-dataset) · [synthetic-life-manifesto](https://github.com/CIRWEL/synthetic-life-manifesto) · [obtuse-hubris](https://github.com/CIRWEL/obtuse-hubris) (incident case study)

---

<sub>

[HuggingFace](https://huggingface.co/hikewa) · [ORCID](https://orcid.org/0009-0006-7544-2374) · [CIRWEL Systems](https://cirwel.org) · founder@cirwel.org

</sub>
