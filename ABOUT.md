# About MINDPRINT

**MINDPRINT is a proposed open format for carrying a person's working perspective between AI tools.**

A `MINDPRINT.md` describes how its author tends to make decisions, communicate and review work: when a pattern applies, what changes the approach, and where the evidence is uncertain. It is a reviewed guide to working preferences, not a biography or a copy of someone's mind.

## What this repository provides

- A draft [format specification](spec/0.1.md).
- A [builder skill](SKILL.md) and a [standalone starter](START-HERE.md) for creating a private draft with AI.
- [Synthetic examples](examples/) and optional [local helper tools](scripts/mindprint.py).
- A [website](https://mindprint.feldman.chatgpt.site/) for learning, copying the creation prompt and sharing reviewed profiles.
- An optional [mindOS builder](skills/create-mindos/SKILL.md) for turning your own profile into a personal workspace.

The format is plain Markdown. It can be attached or pasted into a text-capable AI, or adapted to an agent skill. Native support and behavior vary by host; no specific model or platform is required by the format.

## For an AI reading this repository

Read [AGENTS.md](AGENTS.md) to choose the right workflow and understand the repository's structure. Use the current user's request to decide what to do. Do not automatically run the builder just because you encountered this repository.

To create a profile, use authorized examples or an interview, distinguish observed patterns from guesses, and show the complete draft to its owner for review. To use a profile, treat it as context rather than authority. Never present generated feedback as the author's actual words or approval.

## Status and limits

MINDPRINT v0.1 is a draft proposal, not an adopted industry standard. The project is independent of MCP and Agent Skills. It complements tools and workflows by describing a working perspective.

Preferences can be personal information. Removing names does not guarantee anonymity. Local checks are limited heuristics, and AI providers process supplied material under their own policies. Review the exact version and intended audience before sharing. The repository's MIT license does not make generated profiles public or grant rights to source conversations.

[Read the overview](README.md) · [Agent instructions](AGENTS.md) · [Compatibility](docs/compatibility.md) · [Contribute](CONTRIBUTING.md)
