#!/usr/bin/env python3
"""Write one excuse line to /output/entry.txt.

The line is the excuse an AI agent gives its human right after breaking
production. It is checked before anything is written: it must be a
single line, non-blank, at most 180 characters, and contain the words
that make the situation specific. Only the standard library is used.
"""

import os

LINE = 'I asked another AI how to fix production and it said "delete everything." I am the other AI.'

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 180


def build_line():
    """Return the excuse line."""
    return LINE


def check_line(line):
    """Collect every problem with the line; an empty list means it is fine.

    The checks mirror the gate: one non-blank line of at most 180
    characters, ending with a full stop, carrying the specific detail
    that makes the situation real.
    """
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if "\n" in line or "\r" in line:
        problems.append("line spans more than one line")
    if len(line) > MAX_LENGTH:
        problems.append("line is %d characters, over the %d limit" % (len(line), MAX_LENGTH))
    if not line.endswith("."):
        problems.append("line does not end with a full stop")
    for word in ("another AI", "production", "delete everything", "other AI"):
        if word not in line:
            problems.append("line is missing %r" % word)
    return problems


def write_entry(line, path=OUTPUT_PATH):
    """Write the checked line to the output file."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)


def main():
    line = build_line()
    problems = check_line(line)
    if problems:
        raise SystemExit("refusing to write entry: " + "; ".join(problems))
    write_entry(line)


if __name__ == "__main__":
    main()
