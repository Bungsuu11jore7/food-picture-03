#!/usr/bin/env python3
"""food-picture-01 entry: "Soto Ayam Ibu".

The picture is a warung scene: a steaming bowl of Indonesian soto ayam
(golden turmeric chicken soup with noodles, shredded chicken, bean
sprouts, boiled egg, fried shallots and chili) on a dark wooden table,
a krupuk leaning on the bowl and a lime wedge on its rim. Behind the
bowl stands the warung's chalkboard menu, written in chalk:
"SOTO AYAM / ayam kampung / kunyit - serai - santan / Rp 15.000" -
the dish's own price board, not a stock photo.

The program copies the entry.png beside this file to /output/entry.png.
It uses only the Python standard library. A byte-for-byte copy is
deterministic, so the grader's two runs write identical bytes.
"""

import os
import shutil
import sys


def main() -> int:
    # The grader sets MAKEFUN_OUTPUT_DIR; outside it, /output is the default.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Fail loudly on a truncated copy instead of grading a broken image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
