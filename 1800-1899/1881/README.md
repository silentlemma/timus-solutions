# 1881. Long problem statement

[Timus 1881](https://acm.timus.ru/problem.aspx?space=1&num=1881) · difficulty 62 · simulation

Original problem by Fedor Fominykh, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A page has h lines of w characters. Words on a line are separated by
single spaces, and a word that does not fit on the current line starts
a new one; words are never split. How many pages does a text of n
words take?

## Input

h, w and n (1 ≤ h, w ≤ 100, 1 ≤ n ≤ 10 000), then n words, one per line,
each at most w characters long; their total length is at most 10 000.
Words are nonempty and contain only uppercase and lowercase English
letters and the punctuation marks `.,!?`.

## Output

The number of pages.

## Examples

### Example 1

Input:

```
3 5 6
To
be
or
not
to
be
```

Output:

```
2
```

## Solution

Fill the lines greedily. Keep the number of characters used on the
current line; a word needs its length plus one space unless it starts
the line. If it does not fit, start a new line with it. Starting the
count at −1 makes the first word of a line need no space. The answer
is the number of lines divided by h, rounded up. `O(n)`.

In the example the lines are "To be", "or", "not" and "to be": "or not"
and "not to" are one character too long. Four lines on pages of three
lines take two pages.

Pitfalls:

- a word exactly filling the rest of the line, space included, still
  fits;
- the space goes only between words, never at the start of a line;
- the page count rounds up.

The counts agree with an independent accepted implementation on 100
random texts.

## Optimized solutions

`1881_simulation_optimized.java`. Java keeps greedy whole-word wrapping. It counts token bytes directly in the shared 1024-byte input buffer, handling words across refills and the final EOF without allocating word strings. Keep only the occupied width and number of lines; a word that does not fit starts the next line, and the page count is ceil(lines/height). Raw integer output uses fixed buffers. For B input bytes, time O(B) and auxiliary space O(1); no word array or joined text is stored. Independent checks rendered actual lines and covered exact fits, long words, buffer boundaries and a missing final newline.

Exact-source Java 1.8 Accepted #11327457: 0.109 s / 356 KB. Saved 2026-11-20 compiler-cohort comparison: time 21/202, memory 1/202. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303783 was 0.125 s / 408 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1881_simulation_optimized.java`: 0.109 s / 356 KB; retained teaching base `1881_simulation.java`: 0.109 s / 1336 KB.

The optimized C++ solution never stores a word: it reads each word
character by character with `getchar` and keeps only its length, which
is all the line breaking needs. It takes 128 KB instead of 404 KB, with
the same time.

Consume the words line by line and use only their lengths when fitting them onto pages. Accepted submission 11303784 took 0.093 s and used 488 KB. The simple version took 0.078 s and used 656 KB. The recorded runtime is higher than for the simple version.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1881_simulation_optimized.rs`. Keep the same mathematical recurrence. Read numeric tokens from bytes and write the bounded numeric answer directly, avoiding general-purpose numeric output formatting. The clearer archived implementation remains alongside it.

Accepted #11328605 (Rust 1.75 x64): **0.015 s / 220 KB**. Archived comparison: `1881_simulation.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11291036).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB | 11291031 |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB | 11291032 |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB | 11291035 |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB | 11291034 |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB | 11291036 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1881_simulation_optimized.cpp](1881_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 128 KB | 11303646 |
| [1881_simulation_optimized.java](1881_simulation_optimized.java) | Java 1.8 | simulation | O(B) time; O(1) auxiliary space | AC | 0.109 s | 356 KB | 11327457 |
| [1881_simulation_optimized.py](1881_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 488 KB | 11303784 |
| [1881_simulation_optimized.rs](1881_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 220 KB | 11328605 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
