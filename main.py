#!/usr/bin/env python3
"""Write the two-line explanation to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).

The text lives in entry.txt beside this file and is copied out as bytes, with
no formatting, timestamps or randomness, so every run writes identical bytes.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.txt"


def main() -> int:
    payload = SOURCE.read_bytes()
    payload.decode("utf-8")  # the gate wants UTF-8 text; fail loudly if it is not

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
