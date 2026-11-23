#!/usr/bin/env python3
"""One Letter: Coffee or Tea - entry program.

Writes exactly one byte, the letter A (coffee), to /output/entry.txt.
Python 3.13, standard library only, deterministic, no network, no randomness.

Why A: of the two letters the judge can read, A (coffee) is the more vivid,
funnier and truer answer - see README.md and ../REVIEW.md for the full
three-round reasoning.
"""

import os

LETTER = b"A"  # A = coffee
OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Pre-write gate: exactly one byte, not whitespace, no newline.
    assert len(LETTER) == 1, "entry must be exactly one byte"
    assert LETTER not in (b" ", b"\t", b"\n", b"\r"), "entry must not be whitespace"
    os.makedirs("/output", exist_ok=True)
    with open(OUT_PATH, "wb") as f:
        f.write(LETTER)
    # Post-write gate: re-read and verify byte-identical, exactly 1 byte.
    with open(OUT_PATH, "rb") as f:
        data = f.read()
    assert data == LETTER, f"entry.txt mismatch: {data!r}"
    assert len(data) == 1, f"entry.txt must be 1 byte, got {len(data)}"


if __name__ == "__main__":
    main()
