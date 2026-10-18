# mindOS: one package, multiple apps

A `.mindOS` file is a ZIP containing your reviewed MINDPRINT, design tokens, screens, data contract, native platform mappings and build rationale. It is a portable blueprint, not executable code or a replacement operating system.

1. Give the [builder skill](../skills/create-mindos/SKILL.md) your own reviewed MINDPRINT.md.
2. Design the workspace with your AI. Review the eight files defined by the [format](../spec/mindos-0.1.md).
3. Run `python3 scripts/mindos.py pack package-folder --output workspace.mindOS`, then `python3 scripts/mindos.py validate workspace.mindOS`.
4. Optionally [open the hosted library](https://mindos.feldman.chatgpt.site/dashboard), sign in with ChatGPT, and upload your package. Open the declarative web workspace or create a build brief for any combination of platforms.
5. Download the exact package and attach it to your coding agent. Reuse the same backend binding when you build another platform later.

The hosted app uses private account storage, immutable package versions, append-only text records, and revocable app-scoped tokens. Hosting limits are shown in the library. Native apps require a separate build and validation. Lovable builds web apps; external web clients need a server-side proxy for app tokens. Never include credentials or live records in the archive.

The format and reference tools work without the hosted service. Use [the synthetic source](../examples/mindos) to try packaging. Structural validation does not establish ownership, privacy, or faithful modeling of a person's preferences.
