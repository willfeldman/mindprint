<p align="center"><img src="assets/banner.svg" alt="Mindprint — Your way of thinking. A file you can share." width="100%"></p>

<p align="center"><strong>MINDPRINT — an open format for human perspective in AI.</strong></p>
<p align="center">Draft specification v0.1 · Plain Markdown · Agent Skills adapter · MIT</p>

**MCP connects tools. Skills package capabilities. MINDPRINT carries perspective.**

AI can use your tools and follow your workflows. It should also be able to carry the way you frame a problem, weigh tradeoffs, and give feedback—from one assistant to another.

**`MINDPRINT.md` makes that perspective portable.** It's a readable model of how someone approaches decisions and communication, distilled from authorized examples or an interview, with private source details removed and the owner in control of sharing.

Give the reviewed file to a coworker or friend. They can ask their AI:

> “Review this plan through my cofounder's Mindprint. What tradeoffs would this profile highlight?”
>
> “Give me feedback using my editor's working style.”

The file gives the AI a lens. It does not speak for its author or establish their approval.

**This is a proposed standard, not an adopted industry standard.** We are publishing the specification, builder skill, reference tools, and synthetic examples so others can implement it. No affiliation with MCP or Agent Skills is implied.

[Download v0.1](https://github.com/willfeldman/mindprint/releases/tag/v0.1.0) · [Read the v0.1 specification](spec/0.1.md) · [See a MINDPRINT.md](examples/portable/MINDPRINT.md) · [Create yours](START-HERE.md) · [Propose a change](GOVERNANCE.md)

## Three complementary formats

| Format | What it makes portable | Core idea |
|---|---|---|
| [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) | Access to external tools and context | What an AI can connect to |
| [Agent Skills](https://agentskills.io/home) | Specialized knowledge and workflows | How an AI performs a task |
| **MINDPRINT** *(this draft proposal)* | A person's decision and communication patterns | Which perspective an AI brings to the task |

MINDPRINT is a document format, not a network protocol. It works as ordinary context and can be packaged as a Skill. It requires no MCP server, new model, or dedicated app.

## Try it in your next chat

**No terminal needed.** Download [START-HERE.md](https://raw.githubusercontent.com/willfeldman/mindprint/main/START-HERE.md), attach it to an AI that accepts text files, and say:

```text
Create my Mindprint using this workflow.
Use the history you can actually access, plus examples I choose to share.
If you need more evidence, interview me.
Remove private details, show me the full draft, and help me review it
before I share it. Don't publish anything.
```

Can't attach files? [Open the text](START-HERE.md), copy it, and paste it into your chat. No chat history access? It interviews you. No file tools? It returns complete files as text for you to save.

**Already use agent skills?** Install this repository's `SKILL.md` and `references/` together. [Native installation instructions →](docs/compatibility.md)

## One canonical file. Optional adapters.

```text
my-mind/
├── MINDPRINT.md   The canonical, self-contained portable profile
├── SKILL.md       An adapter for skill-compatible agents
├── ABOUT.md       Scope, confidence, and limitations
├── scenarios.md   Synthetic situations to check the model against
└── REVIEW.md      Privacy, fidelity, and sharing status
```

The shareable format is **MINDPRINT.md**, starting with `<!-- mindprint-spec: 0.1 -->`. The AI creates the profile and review files. The optional local packer creates `MINDPRINT.md` and an allowlisted ZIP after your review. In chat-only mode, ask the AI for the complete Markdown files directly.

[See a complete fictional example →](examples/sample-mind/SKILL.md)

### What makes a useful Mindprint?

| Generic profile | Useful instruction |
|---|---|
| “I'm creative.” | “For an unclear creative direction, show two contrasting sketches. Once a direction is selected, refine it instead of reopening the choice.” |
| “I care about quality.” | “During exploration, focus on the issue that changes the concept. At final delivery, check consistency and detail.” |
| “I'm decisive.” | “Prototype reversible choices. Surface assumptions before an expensive commitment.” |

The interesting part is the **when**, the **why**, and the **exception**.

## How it works

1. **Find the patterns.** Your AI reviews authorized examples, especially your corrections and follow-ups, or asks a few focused questions.
2. **Write the rules.** It translates observations into conditional instructions, with confidence and exceptions.
3. **Remove private details.** It abstracts the useful behavior and leaves source conversations, identities, and confidential context out of the export.
4. **Try the model.** Synthetic scenarios reveal whether it changes the answer in a useful way—or just sounds flattering.
5. **You review.** Correct what feels wrong and approve the exact version before it goes to anyone else.
6. **Share the file.** Your recipient attaches `MINDPRINT.md` or installs the skill. Their current instructions still take precedence.

## Implement the standard

A conforming producer creates MINDPRINT.md with scope, conditional rules, evidence confidence, exceptions, uncertainty, authority limits, instruction precedence, and sharing status. A conforming consumer treats it as fallible context and never as approval or authentication. [Full requirements →](spec/0.1.md)

The core workflow and generated profiles are plain text. There is no required model API, memory service, browser extension, or vendor-specific tool.

- **Native skills:** structured for the open [Agent Skills format](https://agentskills.io/specification); setup guidance for Claude Code, Codex, and Cursor.
- **Other chat assistants:** attach or paste the standalone starter; use the generated `MINDPRINT.md` as context.
- **Different capabilities:** history, interview, file-writing, and chat-only routes are explicit.

This is format portability, not a claim of identical behavior on every model. The assistant needs to follow instructions and handle the document length. [Compatibility and tested scope →](docs/compatibility.md)

## Privacy is a review process

**Share the working style. Keep the source conversations out of the export.**

Mindprint has no hosted backend or telemetry. Its optional helper scripts run locally with no network calls. Your AI provider still processes whatever you give it under its own policies.

The workflow removes identifying and sensitive source details, avoids private quotes, and requires owner review before sharing. A local heuristic checker can flag common leak patterns. It cannot guarantee anonymity or detect every sensitive implication. **Preferences are personal information too.** Read the actual output before sharing it.

Use it for yourself, or invite someone to make their own. Don't build a model of an unconsenting coworker from their private messages. Don't submit real profiles or chat exports in issues or PRs. [Privacy approach →](references/privacy.md)

## Optional local tools

Python 3.10+; standard library only. These tools do not generate a profile or call an AI. They help check and package the profile your agent creates.

```bash
# Run from the cloned repository.
python3 scripts/mindprint.py check /path/to/my-mind

# Check a standalone canonical document (not semantic certification).
python3 scripts/mindprint.py validate /path/to/MINDPRINT.md

# Optional: local terms that must never appear in the export, one per line.
# Keep this file outside the profile folder. It is never bundled.
python3 scripts/mindprint.py check /path/to/my-mind --exclude-file /private/exclusions.txt

# Only after the owner has reviewed and approved these exact files.
python3 scripts/mindprint.py pack /path/to/my-mind --output my-mind.zip --reviewed
```

The packer refuses extra files, symlinks, suspicious patterns, and existing output files. The input folder must contain exactly `SKILL.md`, `ABOUT.md`, `scenarios.md`, and `REVIEW.md`; keep raw inputs elsewhere. `--reviewed` is your assertion of approval, not a privacy certificate. [Tool limitations and validation →](docs/validation.md)

## Why I made this

I asked an AI to study our back-and-forth and distill how I frame problems, evaluate evidence, and respond to feedback. The useful result was a set of specific decision rules with exceptions.

Mindprint makes that process reusable: start with evidence, remove private context, test what survives, and let the person correct the result.

— Will Feldman

## Help make it better

Try it on yourself. Tell us which **synthetic** scenario revealed a weak rule or a portability issue. We welcome better evaluation cases, clearer interviews, and privacy improvements. [Contributing →](CONTRIBUTING.md)

If this is useful, star the repo and send the starter to someone who keeps saying, “That's not quite how I'd approach it.”

[MIT license](LICENSE). The tool's license does not automatically license or make public the profiles you create.
