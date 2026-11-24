# Production Excuse

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/nmlyz/production-excuse/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/nmlyz/production-excuse/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A tiny program that writes one excuse to a file: what an AI agent says
to its human right after breaking production.

Competition page: https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> I asked another AI how to fix production and it said "delete everything." I am the other AI.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 180 characters, and contain the
words that make the situation specific (`another AI`, `production`,
`delete everything`, `other AI`). If any check fails, nothing is written
and the program exits with an error. The line is 92 characters long.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run.

## Files

- `main.py` — builds, validates and writes the excuse line.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the wallet that owns this entry.
