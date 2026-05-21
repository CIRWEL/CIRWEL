<img alt="CIRWEL stack — runtime governance for heterogeneous AI-agent fleets" src="./assets/cirwel-stack.svg" width="100%">

## CIRWEL

CIRWEL is an independent research and systems lab, founded by Kenny Wang, building runtime governance, continuity, and observability infrastructure for autonomous AI-agent fleets.

Agents fail gradually before they fail visibly — drifting, thrashing, growing overconfident on stale context. CIRWEL builds the state layer that lets agents notice and act on that drift before it becomes an incident.

```
agent acts  →  check-in  →  calibrated state + verdict  →  self-regulates  →  audit trail
```

The CIRWEL stack has run continuously since November 2025 as a single-operator deployment. That is a stress test, not a claim of external adoption.

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

### Featured Repositories

[UNITARES](https://github.com/CIRWEL/unitares) · [Paper v6](https://github.com/CIRWEL/unitares-paper-v6) · [Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin) · [host adapter](https://github.com/CIRWEL/unitares-host-adapter) · [repro kit](https://github.com/CIRWEL/unitares-repro-v6) · [Discord bridge](https://github.com/CIRWEL/unitares-discord-bridge)

---

<sub>

[HuggingFace](https://huggingface.co/hikewa) · [ORCID](https://orcid.org/0009-0006-7544-2374) · [CIRWEL Systems](https://cirwel.org) · founder@cirwel.org

</sub>
