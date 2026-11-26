"""One Word From Your Ex.

Writes exactly one word -- the word an ex would use to describe you --
to /output/entry.txt.

The word: "placeholder". As in: you were never the plan, just the person
keeping the seat warm until the real thing showed up. One word, no
explanation needed, and everyone who hears it winces a little -- because
they have either been one or dated one.
"""

import os

WORD = "placeholder"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """The gate only accepts 1-24 UTF-8 chars, a single word, not blank."""
    word = word.strip()
    if not 1 <= len(word) <= 24:
        raise ValueError(f"word must be 1-24 chars, got {len(word)}")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = validate(WORD)
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        path = OUTPUT_PATH
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
