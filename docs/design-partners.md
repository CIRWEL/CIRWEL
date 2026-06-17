# Design partners

CIRWEL is looking for a small number of teams who already operate autonomous
AI agents long enough for drift, miscalibration, and recovery to matter — and
who want runtime visibility into it before it becomes an incident.

This is the honest version: the stack has run continuously since November 2025
as a single-operator deployment. That is a stress test, not external adoption.
A design partner is how that changes. We are looking for the first teams to run
UNITARES against agents we did not build.

## Who this is for

You are a good fit if you run **long-lived coding, research, or operations
agents** — the kind that act over hours or days, accumulate context, and can
quietly go wrong:

- agents that drift off-task as context grows stale
- agents that thrash, retry, or loop without making progress
- agents that grow overconfident and act on bad assumptions
- fleets where one misbehaving unit is hard to spot until it causes damage

If your agents are short-lived, single-shot, or fully human-supervised, you
probably do not need this yet.

## What a pilot looks like

| | |
|---|---|
| **Integration** | One MCP or REST check-in per unit of work, plus outcome events from signals you already have (tests passing/failing, tool errors, human rejections). |
| **Effort** | Hours, not weeks. Start with the [`unitares`](https://github.com/CIRWEL/unitares) quickstart (`docker compose up` + `make demo`), then mount the [governance plugin](https://github.com/CIRWEL/unitares-governance-plugin) / [host adapter](https://github.com/CIRWEL/unitares-host-adapter). |
| **Footprint** | UNITARES observes state and returns a verdict (`proceed` / `guide` / `pause` / `reject`). You decide whether verdicts advise or enforce. Start in advisory mode. |
| **Data** | Check-ins and outcome events. You run the server; your agent payloads stay in your environment. No model outputs are required to leave your boundary for the core loop. |

## What you get

- A live state vector per agent and a verdict stream you can watch, alert on, or
  pipe into your own incident tooling.
- A second opinion when an agent's confidence and the system's assessment
  diverge — a short dialectic with peer agents, or an LLM when no peers are
  around, before anything halts.
- Direct access to the maintainer. Pilots shape the roadmap; the integration
  rough edges you hit get fixed first.

## What we ask in return

- Run it against real agents long enough to generate real signal (weeks, not a
  one-off demo).
- Candid feedback on where it broke, confused, or got in the way.
- Permission to learn from anonymized, aggregate findings — e.g. "the stack
  caught a drift failure N hours before the existing alarms." Nothing
  identifying, nothing without your sign-off.

You are not asked to pay, to switch hosts, or to grant access to your code or
prompts.

## Scope — what this is not

So no one is misled about the boundaries:

- **Not an output filter or content moderator.** It governs agent *state and
  trajectory*, not message content.
- **Not a sandbox.** It does not contain or isolate execution.
- **Not a universal ethics oracle.** Verdicts are calibrated operational
  signals, not moral judgments.
- **Not yet externally validated.** That is precisely what a pilot establishes.

## How to start

1. **3 minutes** — run [`unitares`](https://github.com/CIRWEL/unitares):
   `docker compose up` + `make demo`.
2. **10 minutes** — add the [governance plugin](https://github.com/CIRWEL/unitares-governance-plugin),
   [host adapter](https://github.com/CIRWEL/unitares-host-adapter), and
   [`anima-mcp`](https://github.com/CIRWEL/anima-mcp).
3. **Talk to us** — email **founder@cirwel.org** with what your agents do and
   how long they run. That is enough to start a pilot conversation.
