<img alt="CIRWEL — runtime infrastructure for persistent AI agents" src="./assets/cirwel-stack.svg" width="100%">

## CIRWEL

**Runtime infrastructure for persistent AI agents.**

CIRWEL builds systems for agent work that spans sessions, restarts, and handoffs.

The main project is **[UNITARES](https://github.com/CIRWEL/unitares)** — a self-hosted runtime layer that keeps identity, evidence, memory, runtime state, review, and coordination accountable across those boundaries.

Here, **persistent** does not mean one process runs forever. It means the accountable work can continue across transient processes without losing identity, evidence, or memory.

UNITARES runs alongside model providers and agent frameworks rather than replacing them.

### Start here

**[UNITARES](https://github.com/CIRWEL/unitares)**  
Runtime infrastructure for persistent agents. MCP, REST, SDK, shared memory, review, policy, recovery, and coordination.

```bash
git clone https://github.com/CIRWEL/unitares
cd unitares
docker compose up -d --wait
```

**[unitares-sdk](https://pypi.org/project/unitares-sdk/)**  
The public agent-side contract.

```bash
pip install unitares-sdk
```

### Research

CIRWEL also studies whether longitudinal runtime signals contain useful information beyond outputs and traces.

That work is treated as an empirical question, not a product assumption.

- [UNITARES paper](https://doi.org/10.5281/zenodo.19647159)
- [Trajectory Identity](https://github.com/CIRWEL/trajectory-identity-paper)
- [Digital Proprioception](https://github.com/CIRWEL/digital-proprioception-paper)
- [Datasets and models](https://huggingface.co/hikewa)

### Built under its own machinery

CIRWEL uses UNITARES in its own development environment.

Agents working on the stack use attributed memory, advisory consultation, structured review, evidence-linked check-ins, and coordinated handoffs. Advice remains evidence rather than automatically becoming authority.

The deployment has been running continuously since November 2025. That demonstrates sustained use of the mechanisms in one operator's environment; it does not establish predictive benefit, incident prevention, or cross-operator generality.

### Elsewhere

[cirwel.org](https://cirwel.org) · [Research index](https://cirwel.github.io) · [Hugging Face](https://huggingface.co/hikewa) · founder@cirwel.org
