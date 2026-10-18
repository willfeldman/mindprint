# From MINDPRINT to mindOS

mindOS is a personal workspace application built around the requesting person's own working patterns. Choose web, macOS, or iOS. It is not a device operating system or a claim to recreate a mind.

Use [the create-mindos skill](../skills/create-mindos/SKILL.md) with a coding agent, or use the website's guided builder. If you have no profile, copy or download the creation prompt and send it to your AI. The AI conducts the interview/evidence workflow; review and correct its output, then bring the finished MINDPRINT.md back to the website. The website does not collect questionnaire answers or generate profiles.

## The method

The originating design session demonstrated an explicit method: turn decision rules into interface rules, derive components from recurring jobs, define semantic tokens, document the choices, and test rendered examples. This workflow generalizes that observable artifact structure. It does not extract hidden reasoning or claim the originating agent's private thought process. The originating profile and private session are not included.

Each design should trace:

**Owner's pattern → need → interaction → component → visual/content rule → scenario check.**

Someone who likes comparing alternatives might need a comparison workspace. Someone who protects attention might prefer a focused queue. Neither should inherit a reference person's fonts, palette or component names simply because that reference worked well.

## Original upstream projects

- [OpenAI Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps): the official OpenAI web app building plugin.
- [OpenAI Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps).
- [OpenAI Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps).
- [Emil Kowalski's apple-design](https://github.com/emilkowalski/skills/tree/main/skills/apple-design): independently authored, not an Apple product.

Links were verified October 17, 2026. These skills are not copied into MINDPRINT. Their own licenses and installation requirements apply. An agent without these integrations can use equivalent tools or return a clearly labeled implementation brief.

## Website behavior and privacy

The static site reads imported profiles and prepares mindOS handoff prompts in browser memory. It has no profile database, model API, analytics script or account system. Reloading may discard work; download files to keep them. Hosting providers may log normal page requests. The user reviews and attests that the profile is their own before generating a build prompt. This is self-attestation, not identity verification.

Copy exports the exact previewed prompt to the clipboard. Open in Lovable puts that prompt, including the profile, in a URL fragment passed to Lovable; it can also remain in browser history. Lovable prefills the prompt and requires the user to click Send. Longer prompts get a copy/download fallback. Native targets offer copy/download to a capable coding agent, not a misleading Lovable native-app button. Provider policies apply after handoff.

A MINDPRINT contains personal preferences even after private source details have been removed. Review it before sharing. This workflow is only for the owner's own profile; it does not authorize building another person's simulation.
