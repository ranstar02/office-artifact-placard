#!/usr/bin/env python3
"""Write a one-line museum placard for an office artifact.

The placard treats an ordinary whiteboard marker as an ancient
artifact: an oracle of the brainstorming rite whose final prophecy
went unfulfilled. The line is composed from named catalogue parts
(object, date, material, conceit, donor) and written to
/output/entry.txt (or $MAKEFUN_OUTPUT when set, for local testing).

Deterministic, standard library only, no network, no randomness,
and it reads nothing outside this repository.
"""

import os
import sys
from pathlib import Path

# Catalogue parts of the placard.
OBJECT = "Whiteboard Marker"
DATE = "c. 2019"
MATERIAL = "dried pigment on felt"
CONCEIT = (
    "oracle of the brainstorming rite; "
    "its final prophecy \u2014 \u2018SYNERGY\u2019 \u2014 went unfulfilled"
)
DONOR = "Gift of Facilities"


def build_placard() -> str:
    """Compose the single placard line from its catalogue parts."""
    return f"{OBJECT}, {DATE}, {MATERIAL}: {CONCEIT}. {DONOR}."


def main() -> None:
    text = build_placard()
    assert 1 <= len(text) <= 180, f"placard must be 1-180 chars, got {len(text)}"
    assert text.strip(), "placard must not be only whitespace"
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    # Self-verification: read the file back and confirm it is exactly
    # the composed placard, byte for byte, within the 1-180 char gate.
    read_back = output.read_bytes()
    assert read_back == text.encode("utf-8"), "entry.txt differs from placard"
    assert 1 <= len(text) <= 180, f"placard must be 1-180 chars, got {len(text)}"
    print(
        f"wrote {output}: {len(text)} chars, {len(read_back)} bytes",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
