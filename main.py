#!/usr/bin/env python3
"""One Letter for Your Day — make.fun bounty u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one letter, Z, to /output/entry.txt — nothing else, no
newline, no gloss. The letter stands for the word that describes the day:

    Z — "zero sleep"

The entry is built for the make.fun competition
"One Letter for Your Day" (program/v1, python3.13, no network).
"""

import os

LETTER = "Z"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one character: no trailing newline, no extra bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
