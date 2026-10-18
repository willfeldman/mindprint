# MINDPRINT website design system

## Page families

- `website/index.html`: marketing homepage. The owner's supplied Apple Product Page / Showcase reference governs the visual language. Centered product names and short promises; white, light gray and black sections; pill CTAs; rounded promo tiles separated by 24px; 28px corners for content objects; system typography; 56px navigation; 980px content measure.
- `website/docs.html`: documentation, creation, profile sharing and mindOS handoff. Uses the owner's Apple Guide reference: 817px desktop / 692px tablet measure, 17px/26px prose, unfilled reading sections, 4px controls, blue links and a light neutral hero.
- Shared profile viewer remains part of the documentation application. Old root hash URLs redirect without decoding or transmitting profile data.

## Art direction

On this page, the portable Markdown document becomes the product on display. The useful object is the hero, rather than an abstract AI illustration.

Audience: people who use AI for work and want continuity in judgment and communication. Main claim: a reviewed Markdown file can carry working preferences between tools. Evidence: an actual sample document, an explicitly scripted response comparison, the specification, and functional creation/share/build handoffs.

Subject inventory: plain Markdown; conditional decision rules; exceptions; human review; conversation-based creation; no on-site questionnaire; portable AI context; shareable snapshots; owner-only mindOS input; original upstream skills; draft standard; no authority delegation.

Argument: understand the file → see a preference change an approach → share a reviewed snapshot → build a personal workspace → understand portability/privacy → start with AI.

## Tokens and components

Marketing semantic colors and fonts live in `website/tokens.css`. Keep exact values there. Blue is reserved for actions and links. System fonts use installed faces; no Apple fonts, logos, product images or proprietary components are distributed. The reference's low-contrast secondary text and hover colors are adjusted for readability.

Primary navigation: 56px sticky bar. Footer: compact inline project information and real links. Components: document specimen, two-state illustrative response, promo tile, native details accordion, pill action. Essential content is never hidden behind animation. One document entrance, targeted control transitions and reduced-motion support.

The guide retains its existing stylesheet and application logic. Marketing does not import `app.js`; `home.js` handles the example and backward-compatible hash routing.

## Skill sources and deliberate adaptations

- [Hallmark](https://github.com/nutlope/hallmark): Narrative Workflow macrostructure adapted to the supplied Showcase reference: centered hero, full-width demonstration, four rounded promo tiles, final CTA and FAQ. No fabricated customers, statistics, testimonials or pricing. Marketing token discipline, mobile review and copy hierarchy applied.
- [Taste Skill](https://github.com/Leonxlnx/taste-skill): `borrowed-category` direction, seed 1862558839. A Markdown standard presented like a consumer product. Subject inventory, copy-first argument, functional example and rendered critique applied.

The owner's two design references take precedence over random direction slots. We intentionally retain system typography, 96px desktop headline, blue actions, light/dark section bands and restrained motion. No generic water photographs, unrelated stock imagery or video added to satisfy an image/motion quota. Real text-based product specimens carry the visuals. Scripted examples are labeled. Inspector allowances: `eyebrow` (announcement/product labels), `few-pictures`, `focal-point` (reference type scale), `still-page` (restrained motion). Documentation is a reference-driven reading surface, not a marketing-page Taste audit target.

These upstream skills are linked, not vendored. Private Claude share tokens and task identifiers are excluded from published source.

## Collaboration

`website/collaborate.html` is a marketing subpage in the Showcase family. It explains multi-profile collaboration through a contrasting-preferences example, four use cases, and a three-step handoff. The homepage links to it in navigation and a dedicated feature section. A reviewable, copyable Markdown team prompt helps people use their existing AI tool. It does not imply a hosted multiplayer chat, synchronized profiles, access to teammates' histories, impersonation, or delegated approval.

## Latest refinement

The supplied Showcase artifact was inspected directly. Its dark opening, oversized type, neutral feature chapters, sticky local navigation and restrained blue actions govern marketing only. Impeccable (https://github.com/pbakaus/impeccable) informed contrast, spacing, heading wraps, focus and copy states. Its two detector findings were corrected: promo paragraph line height and collaboration button hover contrast.

Developer ecosystem references: agentskills.io, skills.sh, anthropics/skills and openai/plugins. The page borrows their concrete file examples, immediate primary action and clear ecosystem explanation, without copying logos or claiming adoption. The creation prompt is reviewable and downloadable, and its copy state has been checked in browser. Desktop, tablet and mobile inspection found no failed checks; remaining warnings concern intentional type scale and the absence of decorative video.
