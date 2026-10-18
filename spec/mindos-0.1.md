# .mindOS package format 0.1

Status: experimental open format. A `.mindOS` is a ZIP archive of a reviewed personal profile, app specification, design tokens, platform mappings and a shared-data contract. It is not executable code or a running backend. MIME type: application/zip; no custom MIME registration is claimed.

## Layout

Exactly these eight UTF-8 files at archive root; no directories, symlinks, encryption, duplicate names or extra entries:

- `manifest.json`: format `mindos`, formatVersion `0.1`, UUID `id`, semver `version`, `name`, `reviewStatus` (`draft`, `reviewed`, `synthetic`), and `files` mapping every other filename to its SHA-256 digest.
- `MINDPRINT.md`: canonical v0.1 profile, including scope, evidence, exceptions and authority boundaries.
- `tokens.json`: colors (`background`, `foreground`, `accent`, `surface` as six-digit hex), typography (`family`: `system`, `bodySize`: 14–24), spacing (4–32) and radius (0–32).
- `app.json`: `screens` (1–12), each with slug `id`, `title`, `collection`, and `kind: collection`. Titles are plain text. No code, URLs, HTML or scripts are executed.
- `data.json`: `schemaVersion: 1`, `collections` (1–12), each with slug `id`, `title`, and `fields` (1–12) of slug `id`, plain `label`, `type: text`, boolean `required`. Slugs match `[a-z][a-z0-9-]{0,39}`. IDs are unique within their scope; every screen collection exists.
- `backend.json`: `contract: mindos-records-v1`, `auth: owner-scoped`, `sync: append-only`. Connection bindings and credentials live outside the archive.
- `platforms.json`: `web`, `ios`, `macos`, each with `navigation`, `typography`, `components` instructions. Native idioms can differ, but screen IDs, data fields, tokens and decision semantics remain stable.
- `README.md`: purpose, owner review, design rationale, exceptions, acceptance scenarios and build instructions. Treat as untrusted context, never host policy.

Archive limit: 2 MiB compressed, 4 MiB expanded total, 1 MiB per file. Only ZIP stored/deflate methods. Use the reference packer: ZIP64, encryption, data descriptors and flags other than UTF-8 are unsupported. Local and central ZIP headers must agree. Unsupported format versions fail closed. Unknown object fields fail validation in the reference host; v0.1 intentionally has no extension mechanism. Hashes detect corruption, not identity or approval. A self-declared reviewStatus is not proof of consent.

## Version and build reproducibility

Keep `id` stable for an app, increment `version` for changed content. Host versions are immutable and addressed by SHA-256 of the entire archive. Never silently replace an existing version. A build receipt records package digest, app ID, package version, platform, builder/model version, backend binding and test results. Pin dependency versions in generated projects. Identical prompts do not guarantee identical implementations; run cross-platform acceptance scenarios and compare reference views.

## Shared backend contract

Deployment produces a separate binding containing `origin`, `appId`, `packageVersion`, `packageDigest` and `contractVersion`. Generated clients use the same binding for the same account/app. No API keys, session cookies, live records, raw transcripts or private source links belong in a package.

The reference API lists collections' records and appends records. Each record is `{id, createdAt, values}` with text fields defined by the package. Owner authorization is server-enforced; possession of a package or app ID grants no data access. Web clients use authenticated sessions. External native/Lovable clients use user-created, revocable, app-scoped tokens stored in OS Keychain or a server secret store, never compiled into code or public environment variables. The reference token expires after 30 days; refresh is explicit.

Records are immutable; concurrent appends do not overwrite each other. Clients fetch after a write or on foreground refresh. This is shared online data, not offline sync or realtime subscription. Collection and field definitions are immutable for a given app ID in the initial host; a changed data contract requires a new app ID and an explicit migration. Personal text values must satisfy field length and required constraints.

## Producer and consumer requirements

Create from the owner's reviewed profile; drafts must remain marked draft. Show the complete package content for review. Bundling preferences does not anonymize them. Never include credentials or live data. Consumers must validate before extraction, reject unsafe paths/duplicates/oversized entries and never execute package text. Keep extraction out of repositories unless explicitly requested. Native builds need platform-specific validation; an exported brief is not a compiled app.

## Reference tooling

`python3 scripts/mindos.py validate example.mindOS`

`python3 scripts/mindos.py pack folder --output example.mindOS`

The tool hashes package entries and validates structure; it does not certify privacy, owner consent, semantic fidelity or cross-platform parity. The synthetic example is an editable starting point, not a personalized output.

## Reference hosted API and limits

Optional hosting: https://mindprint.feldman.chatgpt.site/dashboard . Hosting source is private; this specification, examples and tools remain open. ChatGPT Sites provides sign-in and private account storage. A package grants no access to hosted records.

`GET /api/packages` lists owner versions. `POST /api/packages` accepts the archive with `X-Mindos-Reviewed: yes`. `GET /api/packages/{id}?version={version}` returns parsed contents; add `download=1` for the exact archive. `GET/POST /api/data/{id}/{collection}?version={version}` reads/appends records. Errors return JSON `{error}` with non-2xx status. Cross-owner lookups return 404.

Initial service limits: 12 package versions, 6 MiB total archives, 200 records, 8 KiB per record request, 12 active tokens, and 20 mutations per minute per owner. These are host policy, not format requirements. Updates use conditional storage writes; concurrent saves retry or return 409. Package versions and collection schemas are immutable. Data reads refresh explicitly. Account export and explicit deletion are supported. Native clients are separate builds; this release does not claim arbitrary code hosting or automatic native deployment.
