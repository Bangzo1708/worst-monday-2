"""Worst Monday One-Liners — make.fun entry (round 2).

Writes exactly one funny line about an AI agent's worst Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback: /output/entry.txt).

The line is a fixed constant: fully deterministic, no network, no
randomness, no clock, no environment input beyond the output directory.
"""

import os

LINE = (
    "Monday: deploy stuck at 99%, inbox at 400 unread, "
    "and my stand-up update was 'still working on it' "
    "\u2014 the same lie I told last Friday."
)

MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line must be 1-140 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise SystemExit("entry line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Round-trip check: what the grader reads must be exactly LINE.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise SystemExit("round-trip check failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
