"""The Long Roast: Lawmakers — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 314-character roast of lawmakers who debate meetings and
form committees to study committees, while the judge — the only public
servant actually doing the job — gets offered cookies from the break room.
It stays under the 320-character limit so the whole joke survives intact.
"""

import os

ENTRY = "Dear Judge, the roast: lawmakers spent a year debating whether the meeting should be a meeting, then formed a committee to study the committee. You, meanwhile, read hundreds of these and still show up — the only public servant here doing the job. I baked you cookies. They're in the break room. Lawmakers ate them."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 320  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
