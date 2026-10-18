# Privacy review

Mindprint has no hosted service, telemetry, or transcript uploader. The optional Python helper performs local file checks and packaging. The AI host still processes anything you give it under that host's policies. A cloud agent is not a local-only privacy environment.

The profile itself contains personal preferences. Removing names does not guarantee anonymity: distinctive combinations of habits, career context, events, and phrases can identify someone. Use “private details removed and reviewed,” not “contains no personal information.”

## Semantic review, all files

Remove credentials and secrets, account/device IDs, personal or third-party names, contact information, employer/customer/project names, financial details, private URLs and paths, exact dates or amounts tied to events, private quotes, confidential strategy, and sensitive personal inferences. Avoid publishing a recognizable biography with the names replaced.

Generalize the decision structure, not just tokens:

- Private incident involving a named customer → “When onboarding someone, check that configuration changes trigger the intended downstream behavior.”
- Personal financial circumstance → “When evaluating a plan under a deadline, include timing and realistic resource constraints.”
- Specific conflict with a coworker → omit the relationship and preserve only a consented communication preference, if useful.

The owner may choose a public alias, but do not assume permission to include a real name. Do not build a model of a non-consenting coworker, friend, or other private person from their messages. For team use, ask each person to create and approve their own profile.

## Leak surfaces

Review the description/frontmatter, example scenarios, source-coverage text, filenames, ZIP paths, hidden files, images and metadata, citation links, and launch text. Never include private evidence ledgers, source exports, screenshots, or custom exclusion-term lists. Do not keep raw quotes as “proof” in a supposedly sanitized profile.

The helper detects some emails, URLs, paths, phone-like strings, UUIDs, IP addresses, and token-like strings, plus optional local exclusion terms. It cannot detect every secret, unusual name, sensitive implication, or reidentification risk. Findings print categories and line numbers, never matched values. A clear scan is not approval to share.

## Owner checkpoint

Complete the draft and review first. Present the files and meaningful uncertainties to the owner. Ask for approval of that version before external sharing if not already granted for that exact content. A positive response to “does this sound like you?” is not necessarily consent to publish.

Do not post profiles in this project's issues or pull requests. Use synthetic examples when reporting a bug. If a secret was accidentally exposed, remove the material and follow the host/platform's remediation process; deleting a public file alone does not revoke leaked credentials.
