# Contributing

Small improvements with a clear behavioral effect are welcome. Explain the problem, show a synthetic reproduction, and describe how the change affects the output.

Do not upload personal profiles, private chats, exclusion-term files, or examples about identifiable people. Use invented subjects and data. Remove private information from screenshots and logs too.

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/mindprint.py check examples/sample-mind` before submitting a change. If you change SKILL.md or the references, regenerate START-HERE.md with `python3 scripts/mindprint.py prompt --output /tmp/mindprint-starter.md`, inspect it, and replace the committed starter with that generated file.

Keep the core workflow usable with no proprietary tool and no code execution. New dependencies or integrations must remain optional. Do not market heuristic scans as anonymization guarantees. Add a regression case for packaging, privacy-scanner, or portability defects.

Do not commit generated real profiles to this repository. The builder's MIT license does not grant rights to anyone's conversation data or generated profile.
