"""make.fun bounty: Sum up 23 November's world news in one image.

Deterministic entry program (Python 3.13, standard library only).
It copies the bundled image entry.png to /output/entry.png.
No network, no randomness, no timestamps: two runs write identical bytes.
"""

import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
