#!/usr/bin/env python3
"""news-image-20261122 candidate 6: ship the pre-rendered entry image.

The picture is rendered at build time because the grader runs bare-stdlib
Python (no fonts, no network). This file copies entry.png into the output
directory named by MAKEFUN_OUTPUT_DIR, default /output, byte for byte.
"""
import os
import shutil
import sys

IMAGE = "entry.png"


def main() -> int:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE)
    try:
        size = os.path.getsize(src)
    except OSError:
        sys.stderr.write(IMAGE + " is missing next to main.py\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE)
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != size:
        sys.stderr.write(IMAGE + " copy is incomplete\n")
        return 1
    # Deterministic by construction: the shipped PNG is never modified.
    return 0


if __name__ == "__main__":
    sys.exit(main())
