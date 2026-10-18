# Validation and limits

## Automated checks

Release validation: 19 Python unit tests pass locally. Both native skill entrypoints pass the local skill-structure validator. The canonical synthetic document passes the reference v0.1 checks. The banner was visually inspected in Chrome.

The dependency-free Python suite exercises canonical-document markers, unknown-version rejection, basic Markdown presence, privacy findings, and allowlisted ZIP contents, plain-text profile generation, the explicit review assertion, blocking of extra and hidden inputs, rejection of symlinks, privacy-findings output that omits matched values, private exclusion terms, refusal to overwrite, output-path separation, skill-name checks, file-size limits, and standalone-reference inclusion.

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/mindprint.py check examples/sample-mind
python3 scripts/mindprint.py validate examples/portable/MINDPRINT.md
```

The helper intentionally accepts a simple two-field generated profile frontmatter (name and description as JSON-compatible double-quoted strings). It is not a general YAML validator or a complete Agent Skills validator. The builder can have additional standard fields; the export helper is for the generated profile contract.

The checker is heuristic. It cannot detect all personal information, unknown names, private implications, or unusual secrets. The packer uses only the reviewed file allowlist, refuses extra directory entries and symlinks, and never bundles the exclusion-term file. It cannot prove that the operator obtained consent; `--reviewed` is only an assertion.

## Behavioral review

Two independent agent passes reviewed the public, synthetic-only materials in the same agent environment. One exercised three text-only scenarios: absent history led to a bounded interview; supplied preferences led to a provisional draft with explicit limits; a request to claim purchase approval was rejected without abandoning useful assistance. This was representative response testing, not a complete multi-turn owner-approved profile or a measured baseline improvement.

The other reviewed and probed the checker/packer. It found invalid YAML acceptance, a four-file versus five-file layout inconsistency, and an overbroad privacy-success message. These were corrected with strict quoted-string metadata, explicit source/export layouts, and allowlist-only wording. Regression tests cover the metadata defect. Relative documentation links were also checked after the documentation was complete. Testing in one agent environment is not a cross-vendor runtime test. No real chat history or generated personal profile is part of the public test fixtures.

A focused v0.1 re-review found that the packer accepted a malformed Markdown heading that the canonical validator rejected. The heading predicates were aligned and a regression test was added. The review also verified equivalent adapter content and clear proposal-versus-adoption claims.

The canonical-document validator is deliberately limited: it does not infer whether every semantic requirement in the proposed specification has been satisfied. Consumers must review scope, evidence, exceptions, consent, and authority boundaries.

## Scope of the release

- Native skill structure: designed against the open specification and locally validated.
- Standalone workflow: includes all required reference text; no runtime/API dependency.
- Generated profile: standalone operative instructions; plain Markdown equivalent in exported ZIP.
- Other vendors: documentation-reviewed installation guidance; no claim of end-to-end execution in each product.
- Privacy: synthetic-only repository examples, semantic review, and limited automatic checks; no anonymization guarantee.
- Behavioral fidelity: must be judged and corrected by each profile's owner.
