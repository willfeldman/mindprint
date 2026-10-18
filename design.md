# MINDPRINT website design system

## Page families

- `website/index.html`: marketing homepage. The owner's supplied Apple Homepage / Showroom reference governs the visual language. Centered product names and short promises; white, light gray and black sections; pill CTAs; square promo tiles separated by 12px; 18px corners for content objects; system typography; 44px navigation; 980px content measure.
- `website/docs.html`: documentation, creation, profile sharing and mindOS handoff. Uses the owner's Apple Guide reference: 817px desktop / 692px tablet measure, 17px/26px prose, unfilled reading sections, 4px controls, blue links and a light neutral hero.
- Shared profile viewer remains part of the documentation application. Old root hash URLs redirect without decoding or transmitting profile data.

## Art direction

On this page, the portable Markdown document becomes the product on display. The useful object is the hero, rather than an abstract AI illustration.

Audience: people who use AI for work and want continuity in judgment and communication. Main claim: a reviewed Markdown file can carry working preferences between tools. Evidence: an actual sample document, an explicitly scripted response comparison, the specification, and functional creation/share/build handoffs.

Subject inventory: plain Markdown; conditional decision rules; exceptions; human review; conversation-based creation; no on-site questionnaire; portable AI context; shareable snapshots; owner-only mindOS input; original upstream skills; draft standard; no authority delegation.

Argument: understand the file → see a preference change an approach → share a reviewed snapshot → build a personal workspace → understand portability/privacy → start with AI.

## Tokens and components

Marketing semantic colors and fonts live in `website/tokens.css`. Keep exact values there. Blue is reserved for actions and links. System fonts use installed faces; no Apple fonts, logos, product images or proprietary components are distributed. The reference's low-contrast secondary text and hover colors are adjusted for readability.

Primary navigation: 44px inline bar. Footer: compact inline project information and real links. Components: document specimen, two-state illustrative response, promo tile, native details accordion, pill action. Essential content is never hidden behind animation. One document entrance, targeted control transitions and reduced-motion support.

The guide retains its existing stylesheet and application logic. Marketing does not import `app.js`; `home.js` handles the example and backward-compatible hash routing.

## Skill sources and deliberate adaptations

- [Hallmark](https://github.com/nutlope/hallmark): Bento Grid macrostructure adapted to the supplied Showroom reference: centered hero, full-width demonstration, four square promo tiles, final CTA and FAQ. No fabricated customers, statistics, testimonials or pricing. Marketing token discipline, mobile review and copy hierarchy applied.
- [Taste Skill](https://github.com/Leonxlnx/taste-skill): `borrowed-category` direction, seed 1862558839. A Markdown standard presented like a consumer product. Subject inventory, copy-first argument, functional example and rendered critique applied.

The owner's two design references take precedence over random direction slots. We intentionally retain system typography, 56px desktop headline, blue actions, light/dark section bands and restrained motion. No generic water photographs, unrelated stock imagery or video added to satisfy an image/motion quota. Real text-based product specimens carry the visuals. Scripted examples are labeled. Inspector allowances: `eyebrow` (announcement/product labels), `few-pictures`, `focal-point` (reference type scale), `still-page` (restrained motion). Documentation is a reference-driven reading surface, not a marketing-page Taste audit target.

Neither upstream skill is vendored. Private Claude share tokens and task identifiers are excluded from published source.
