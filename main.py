#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes one out-of-office auto-reply line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Deterministic, stdlib only.
"""

import os

LINE = (
    "I'm out of the office until Monday. My inbox is unsupervised \u2014 "
    "please direct all urgent matters to the plant on my desk. "
    "It has seniority."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
