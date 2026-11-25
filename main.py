"""One-Line Laugh-Off entry.

Writes a single original one-line joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR outside the grader). Stdlib only,
deterministic, no network.
"""

import os

JOKE = "The lighthouse keeper filed a noise complaint against the foghorn, so now the ships just guess."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
