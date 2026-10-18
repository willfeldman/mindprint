# Evolving the MINDPRINT proposal

MINDPRINT is currently a draft open-format proposal maintained by Will Feldman in this repository. It has no standards-body status, formal ecosystem adoption, or affiliation with MCP or Agent Skills. The specification and reference implementation are MIT licensed.

## Propose a change

Open an issue or PR with:

1. The user or interoperability problem.
2. A minimal synthetic example.
3. Proposed normative wording or implementation change.
4. Backward-compatibility impact.
5. Privacy, consent, and portability implications.
6. A test or review method that could demonstrate the behavior.

Never attach private chats or real personal profiles. Use invented fixtures. Discussion and decisions remain public. The maintainer reviews proposals and records accepted changes through pull requests or commits; no consensus process beyond this maintainer-led review is implied.

## Compatibility principles

- Readable without a dedicated application.
- Useful without access to the source conversations.
- No vendor-specific tool dependency in the canonical profile.
- Personalization never implies authority or identity verification.
- Clear separation between structural checks, semantic review, and actual model behavior.
- Evidence of adoption or integrations must be real and linked; planned integrations are labeled as planned.

Breaking format changes require a new spec version. Release notes identify the corresponding specification revision and reference-tool behavior. Other implementations are encouraged; compliance should be described precisely, not inferred from a logo or filename.
