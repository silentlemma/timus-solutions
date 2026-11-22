# 2081. Decreasing times behind a faulty dial

[Timus 2081](https://acm.timus.ru/problem.aspx?space=1&num=2081) · difficulty 721 · greedy

Original problem by Pavel Egorov, prepared by Ivan Burmistrov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A timer shows MM:SS on a seven-segment dial drawn with `_`, `|` and `.`,
but some lit segments may fail to show (a shown segment is always
right). Given n readings, restore times from 00:00 to 59:59, strictly
decreasing, each consistent with its reading. Any valid answer is
accepted. The limits are 2 seconds and 256 MB.

## Input

n ≤ 100, then three lines of 17 characters per reading: the four digits
take columns 1–3, 5–7, 11–13 and 15–17.

## Output

n lines MM:SS.

## Checking

A checker verifies the format, the strict decrease and that every
shown segment belongs to the chosen digit.

## Examples

### Example 1

Input:

```
2
._..._........._.
|...._|.*...|.._|
|_|.._..*...|.|..
....._....._..._.
|.|...|.*.|.|.._.
|.|.|_..*.|_|.._.
```

Output:

```
03:12
00:05
```

## Solution

A digit fits a cell when every shown character equals the character of
the digit at that place. For each reading the four cells give a table
of fitting digits. Going through the readings in order, take the
largest time that fits and is below the previous answer, scanning down
from it.

This never fails when some answer exists: by induction the greedy value
of each reading is at least the value in that answer, because the
answer's value fits and is below the previous answer value, which is at
most the greedy previous value. The scan takes at most 3600 steps per
reading.

In the example the first reading fits 09:48 as well as 03:12, so the
output may differ from the sample.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321978 · Java 1.8 №11321972 · Python 3.12 x64 №11321979 · Rust 1.75 x64 №11321974 · Go 1.14 x64 №11322308.

## Optimized solutions

`2081_bitmask_optimized.java`. Keep the exact 60-bit masks of feasible minutes and seconds and greedy greatest-time-below-bound choice. Read the fixed-width dot/lit-cell displays directly as bytes, without reader, decoded strings or encoding conversions; format each result into six output bytes. All bitset feasibility and descending-time rules are unchanged. O(R) time for R bounded-size displays, O(R) output storage plus constant masks/input buffer. Retain the older bitmask implementation and the teaching solution.

Exact-source Java 1.8 Accepted #11326954: 0.125 s / 464 KB. Saved current-Java comparison, 2026-11-20: time rank 10/17, memory rank 1/17. With memory below 1024 KB, strict admission uses time only.

- `2081_bitmask_optimized.java`: 0.125 s / 464 KB; retained teaching base `2081_greedy.java`: 0.14 s / 2372 KB; time change -10.7%; memory change -80.4%.

Bit masks represent feasible minute and second values separately. The highest set bit gives the largest value under the current bound. If the current minute has no feasible second, the algorithm takes the preceding feasible minute and its largest second.

Go 1.14 x64, submission 11322015. Time 0.031 → 0.031 s, memory 1128 → 928 KB.

Java 1.8, submission 11322017. Time 0.14 → 0.156 s, memory 2372 → 536 KB.

Rust maps each lit-cell pattern to a digit mask and selects the greatest time below the previous reading. Rust 1.75 x64, submission 11323256. Time 0.062 → 0.046 s, memory 252 → 64 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2081_greedy.cpp](2081_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 372 KB | 11321978 |
| [2081_greedy.go](2081_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1128 KB | 11322308 |
| [2081_greedy.java](2081_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.14 s | 2372 KB | 11321972 |
| [2081_greedy.py](2081_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 596 KB | 11321979 |
| [2081_greedy.rs](2081_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.062 s | 252 KB | 11321974 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2081_bitmask.go](2081_bitmask.go) | Go 1.14 x64 | bitmask | O(n) | AC | 0.031 s | 928 KB | 11322015 |
| [2081_bitmask_optimized.java](2081_bitmask_optimized.java) \* | Java 1.8 | bitmask | O(R) time; O(R) output space | AC | 0.125 s | 464 KB | 11326954 |
| [2081_bitmask.java](2081_bitmask.java) \* | Java 1.8 | bitmask | O(n) | AC | 0.156 s | 536 KB | 11322017 |
| [2081_bitmask.rs](2081_bitmask.rs) \* | Rust 1.75 x64 | bitmask | O(N) | AC | 0.046 s | 64 KB | 11323256 |

\* The marked versions have room to improve in the ratings.
