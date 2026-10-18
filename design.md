# MINDPRINT website design

## Page families

The marketing homepage and collaboration page explain the product through concrete Markdown examples, short promises and clear next actions. Documentation, profile sharing and mindOS handoffs use a focused reading layout.

## Visual language

Use system typography, neutral light and dark sections, blue actions, restrained motion and clear keyboard focus. Marketing tokens live in `website/tokens.css`; documentation styles live in `website/style.css`. Keep responsive headings legible and avoid horizontal overflow. Honor reduced-motion preferences.

Use actual file examples and explicitly labeled illustrative responses. Do not invent customers, adoption statistics, endorsements or live AI results. Brand assets and usage guidance live in `assets/brandkit/`.

## Interaction requirements

- Profile creation happens in the user's chosen AI through a reviewable, copyable prompt. Do not add an on-site questionnaire or imply the website generates profiles.
- Preserve legacy root-hash routing to documentation and existing profile import, sharing and mindOS handoffs.
- Shared profiles are read-only, unencrypted URL snapshots; they are not synchronized or revocable.
- Collaboration explains how participants can supply reviewed profiles to their existing AI. It does not provide a hosted shared chat or speak for participants.
- Keep copy feedback, download fallbacks, accessible controls and error states usable.

## Verification

For affected pages, check desktop and mobile layout, contrast, heading wraps, keyboard focus, reduced motion, copy feedback and internal links. Exercise affected handoffs using synthetic profiles only. Distinguish static examples from live functionality.
