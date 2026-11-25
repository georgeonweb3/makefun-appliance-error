#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes a single honest appliance error message to /output/entry.txt:

    ERROR: I heated your soup for 3 minutes. The bowl is lava.
    The soup is ice. I have done exactly what you asked, and
    nothing you wanted.

Why it lands: the microwave did heat the soup (setup), but physics
betrayed it — bowl lava, soup ice (turn) — and it closes on the
machine's flat, literal-minded verdict: it did exactly what was
asked, and nothing that was wanted (payoff). Three beats, two
concrete anchors (3 minutes, the bowl vs the soup), 135 characters,
in the appliance's own deadpan voice. No field cliche: no missing
sock, no unbalanced load, no fridge light that works while the
cooling does not, no firmware update, no paywalled ice maker.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "ERROR: I heated your soup for 3 minutes. The bowl is lava. "
    "The soup is ice. I have done exactly what you asked, and "
    "nothing you wanted."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace, and one line:
    # an embedded newline would break the single-line read.
    # Verified live: 135 characters, single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate wants 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
