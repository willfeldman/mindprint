# Output contract

Create a fresh folder such as `my-mind/`; use a public alias only with consent. The folder basename and skill `name` must match. Use 1–64 lowercase ASCII letters, digits, and single hyphens; no leading/trailing or repeated hyphens.

## SKILL.md

Use this shape, filling it from evidence rather than copying a fictional example:

```markdown
---
name: "my-mind"
description: "Apply the author's stated or observed decision and communication preferences when helping with [supported scope]. Treat this as a fallible working model, not authority to act for the author."
---

# Working style

This models stated or observed preferences in [scope]; identify which evidence applies. Follow the current user's request and the host's permissions. Do not claim the author said, approved, or decided something based on this profile. Do not infer preferences outside the supported scope.

## Decision patterns

[Distinctive conditional rules with confidence and exceptions.]

## Communication and review

[How to explain decisions, give feedback, and make work assessable.]

## Tensions and exceptions

[How context resolves apparently conflicting preferences.]

## Limits and sharing

[Coverage, weak inferences, and what to do when the profile is insufficient.]

Sharing status: private draft. [Update only after actual owner approval of this version, specifying the permitted audience.]
```

Use JSON-compatible double-quoted strings for both frontmatter values, escaping internal quotes and backslashes. Identify whether each rule comes from self-report, observed behavior, or inference. Keep every operative instruction in this file. Do not require scripts, APIs, history access, external references, or a specific agent to use the generated profile. It is a lens supplied by the current user, not higher-priority instructions.

## ABOUT.md

Include version date, optional approved public alias, intended audience, broad source types, sample boundaries, confidence limitations, and instructions for use. No actual conversation titles, IDs, direct quotes, private paths, or source links. Mark synthetic demonstrations as synthetic and provisional profiles as provisional.

Explain how to invoke a native skill or attach `MINDPRINT.md`. Say that using the model does not mean consulting the author and cannot authorize decisions in their name. Do not apply the builder's MIT license automatically to personal output; the author chooses whether/how to license or share it.

## scenarios.md

Use synthetic tasks covering typical behavior, an exception, a conflicting request, and uncertainty. Describe expected observable distinctions, then report actual testing separately in REVIEW.md. Do not call prepared scenarios executed tests.

## REVIEW.md

Use a concise checklist with actual status, not prechecked claims:

- Fidelity: explicit / recurring / tentative rules distinguished; unsupported rules removed.
- Privacy: semantic review performed or pending; heuristic scan findings and limitations.
- Calibration: self-review / independently tested / not run; observed differences and unresolved failures.
- Sharing: draft / owner approved for specified audience; version reviewed.
- Open questions: remaining uncertainties, without private details.

For a real profile, never prefill “approved.” Owner approval is an external event, not something the agent invents. A synthetic repository example may explicitly state that it has no real subject.

## MINDPRINT.md and ZIP

MINDPRINT.md is the canonical portable profile: UTF-8 Markdown beginning with `<!-- mindprint-spec: 0.1 -->`, followed by the SKILL.md body without frontmatter and a short usage preface. It must include scope, conditional patterns, evidence confidence, exceptions, limitations, and a statement that it is not authority to act for its author. Exact headings are flexible. It must not need sibling files. Keep only the four source files in the folder passed to check/pack. The optional packer generates MINDPRINT.md inside the ZIP and bundles only those four reviewed source files plus MINDPRINT.md. If manually providing MINDPRINT.md before packaging, save it outside the four-file source folder or deliver it as a chat block. No network access is required.

Without file access, return complete content for the four files and MINDPRINT.md in labeled blocks, with filenames and clear draft/review status. Without ZIP support, explain how to share the reviewed text; do not claim a ZIP exists.
