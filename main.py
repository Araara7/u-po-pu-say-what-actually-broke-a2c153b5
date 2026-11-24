"""Say What Actually Broke — one line of error copy.

Entry shape: a single-line software error message (1-200 chars) that
names the real failure in plain words and is funny on a single read.
The twist: the deploy is innocent; the culprit is a stale config file
pointing at a database that retired in 2024, and the line tells the
reader what to do next (restore the current config). Freshness: the
"stale config from years ago" angle is a postmortem classic, not a
generic "server down" line, and the retired-database image is the
repeatable punch.
"""

import os

ENTRY = (
    "The deploy didn't break anything. The config file was from 2023 "
    "and pointed at a database that retired in 2024 \u2014 restore the "
    "current config and try again."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
