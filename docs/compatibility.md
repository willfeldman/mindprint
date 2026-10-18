# Compatibility

MINDPRINT is a proposed document standard, with no assumed native adoption. The canonical `MINDPRINT.md` starts with a `mindprint-spec: 0.1` HTML comment; see the [specification](../spec/0.1.md).

The reference project has two layers: a builder workflow and the personal profile it produces. Both can be used as plain text. Native skill discovery is a convenience, not a requirement.

## Choose a route

| Environment | Builder | Generated profile | Dependency |
|---|---|---|---|
| Agent with Agent Skills support | Install the `mindprint/` folder containing SKILL.md and references | Install the reviewed profile folder, whose name matches its frontmatter | Host's skill loader |
| Chat assistant with file attachments | Attach START-HERE.md | Attach MINDPRINT.md | Text attachment support and adequate context |
| Text-only chat | Paste START-HERE.md; if too long, send its sections before asking the agent to begin | Paste MINDPRINT.md | Instruction following and adequate context |
| Agent with history tools | Authorize the available history scope | No history access needed to use the profile | Optional host tools |
| Agent without history tools | Adaptive interview or selected pasted examples | No special access needed | None beyond chat |
| Agent without filesystem/shell | Full labeled file blocks in chat | Paste the complete profile | No code execution |

No prompt can make an assistant read history it cannot access or bypass a host's permissions. Smaller models or short context windows may lose instructions. Different models may interpret the same profile differently. This repository does not claim every vendor has been runtime-tested.

## Native installation

Clone the repository into a fresh folder, then copy the core files to a skill directory the host supports. Do not overwrite an existing skill blindly. Example commands for a local shell:

```bash
git clone https://github.com/willfeldman/mindprint.git
cd mindprint

# Choose ONE target supported by your host:
# Claude Code: ~/.claude/skills/mindprint
# Codex: ~/.codex/skills/mindprint (supported in the creation environment)
# Cursor: ~/.cursor/skills/mindprint

# Example for Claude Code, only if the destination does not already exist:
mkdir -p ~/.claude/skills
mkdir ~/.claude/skills/mindprint
cp SKILL.md ~/.claude/skills/mindprint/
cp -R references scripts ~/.claude/skills/mindprint/
```

Invoke through the host's skill picker or command. Claude Code and Cursor document slash-command discovery; Codex in the creation environment supports `$mindprint`. Host versions and managed policies can affect availability. If native discovery fails, attach START-HERE.md instead; the workflow does not rely on a particular command syntax.

For another person's generated profile, use its own folder name and follow the same host installation process. Ask for a perspective on a task, not an assertion that its author approved something.

## Source review

The portability design follows the open [Agent Skills specification](https://agentskills.io/specification): a directory with SKILL.md and name/description frontmatter, plus relative supporting files. The core uses no vendor-only frontmatter or tool names.

Native locations and loading behavior were checked against [Claude Code skills documentation](https://code.claude.com/docs/en/skills), [Cursor skills documentation](https://cursor.com/help/customization/skills), and the local Codex skill-creator/installed-skill conventions. [OpenAI's skill-building documentation](https://learn.chatgpt.com/docs/build-skills) provides the broader OpenAI authoring reference.

The single-file starter embeds every workflow reference, so it needs no relative-file resolver. The generated profile contract keeps every operative rule inside SKILL.md; MINDPRINT.md removes the native frontmatter and adds the format marker for ordinary chats. Native skill support means the SKILL.md adapter can load; it does not imply that the host implements MINDPRINT consumer conformance.

See [validation.md](validation.md) for what was actually tested. Documentation review and native installation do not establish behavioral parity across vendors.
