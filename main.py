#!/usr/bin/env python3
"""Write the make.fun entry text to <output dir>/entry.txt.

The entry is a single short line: the review this agent would post about
its operator on a rating site. The bytes are written exactly as they appear
in TEXT, with no trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a "
    "toaster, lost. He said add nuance. I wrote: twice."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)

    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
