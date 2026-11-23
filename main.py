#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke (1-199 characters) to
/output/entry.txt. Standard library only; fully deterministic:
the same joke every run, so the two grading runs agree byte for
byte.

The joke:
  My performance review said I need to be more visible, so I
  started replying-all to everything -- including the fire alarm.

Why this line: it is a genuine one-line office joke (performance
review + reply-all), it turns at the end (the fire alarm is not
an email thread, and that is exactly the point), it rings true
about office life, every word earns its place, and the punchline
is not the obvious Monday-morning or photocopier line.
"""

import os

JOKE = (
    "My performance review said I need to be more visible, "
    "so I started replying-all to everything \u2014 including "
    "the fire alarm."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 199:
        raise SystemExit(f"joke is {len(text)} characters, must be 1-199")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
