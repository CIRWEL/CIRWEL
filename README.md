<img alt="CIRWEL stack — runtime governance, continuity, and observability for autonomous agent fleets" src="./assets/cirwel-stack.svg" width="100%">

## CIRWEL

CIRWEL is an independent research and systems lab, founded by Kenny Wang, building runtime governance, continuity, and observability infrastructure for autonomous AI-agent fleets.

Agents fail gradually before they fail visibly — drifting, thrashing, growing overconfident on stale context. CIRWEL builds the state layer that lets agents notice and act on that drift before it becomes an incident.

```
agent acts  →  check-in  →  calibrated state + verdict  →  self-regulates  →  audit trail
```

UNITARES is the flagship runtime system. Lumen, the governance plugins, benchmarks, adapters, and Discord bridge are the surrounding stack: testbeds, host integrations, observability surfaces, and research artifacts.

The CIRWEL stack has run continuously since November 2025 as a single-operator deployment. That is a stress test, not a claim of external adoption.

---

### Stack

<table>
<tr>
<td width="50%" valign="top">

**Runtime governance**

[UNITARES](https://github.com/CIRWEL/unitares) is the MCP + HTTP governance server: live state dynamics, class-conditional calibration, intervention verdicts, dialectic recovery, and a shared knowledge graph.

</td>
<td width="50%" valign="top">

**Research and evaluation**

[Paper v6](https://github.com/CIRWEL/unitares-paper-v6) argues fleet-wide normalization breaks under heterogeneous agent populations and proposes class-conditional calibration. DOI [10.5281/zenodo.19647159](https://doi.org/10.5281/zenodo.19647159) · [repro kit](https://github.com/CIRWEL/unitares-repro-v6) · [eisv-lumen](https://github.com/CIRWEL/eisv-lumen) · [dialectic-dataset](https://github.com/CIRWEL/dialectic-dataset)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Embodied continuity**

[Lumen](https://github.com/CIRWEL/anima-mcp) is a Raspberry Pi embodied agent with sensors, display, generated drawings, persistent identity, and UNITARES governance. It is the physical substrate for testing continuity across reboots and environmental change.

</td>
<td width="50%" valign="top">

**Host adapters and operations**

[Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin), [unitares-host-adapter](https://github.com/CIRWEL/unitares-host-adapter), and [hermes-agent](https://github.com/CIRWEL/hermes-agent) connect agent hosts to governance. [unitares-discord-bridge](https://github.com/CIRWEL/unitares-discord-bridge) surfaces events, HUD state, Lumen telemetry, and operator commands in Discord.

</td>
</tr>
</table>

### Featured Repositories

[UNITARES](https://github.com/CIRWEL/unitares) · [Paper v6](https://github.com/CIRWEL/unitares-paper-v6) · [Lumen](https://github.com/CIRWEL/anima-mcp) · [Governance plugin](https://github.com/CIRWEL/unitares-governance-plugin) · [repro kit](https://github.com/CIRWEL/unitares-repro-v6) · [Discord bridge](https://github.com/CIRWEL/unitares-discord-bridge)

---

<sub>

[HuggingFace](https://huggingface.co/hikewa) · [ORCID](https://orcid.org/0009-0006-7544-2374) · [CIRWEL Systems](https://cirwel.org) · founder@cirwel.org

</sub>
