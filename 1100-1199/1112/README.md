# 1112. Keeping the most segments with no common inner point

[Timus 1112](https://acm.timus.ru/problem.aspx?space=1&num=1112) · difficulty 165 · greedy

Original problem from the Bulgarian National Olympiad in Informatics, Day 2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` segments on a line (`1 ≤ N ≤ 99`), segment `i` from `A_i`
to `B_i` with integers `−999 ≤ A_i < B_i ≤ 999`. Remove as few segments as
possible so that no two of the remaining ones share an inner point; ends
may touch. Print the remaining segments.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines `A_i B_i`.

## Output

The number `P` of segments kept, then `P` lines `A B` in increasing order
of the left ends. Any optimal answer is accepted.

## Checking

Any optimal answer is accepted. The checker computes the largest possible
number of segments by a quadratic DP and verifies that the output keeps
that many, takes them from the input, lists them by left end and has no
two of them overlapping.

## Examples

### Example 1

Input:

```
3
3 6
1 3
2 5
```

Output:

```
2
1 3
3 6
```

## Solution

This is interval scheduling. Sort the segments by their right ends and
take each one that starts no earlier than the right end of the last taken
segment. The segment that ends first is always part of some optimal
answer: in any optimal set, the segment with the leftmost right end can be
swapped for it without creating an overlap. Repeating the argument on the
rest proves the greedy choice. The kept segments are disjoint, so their
order by right end is also their order by left end. `O(N log N)`.

Pitfalls:

- touching segments (one ends where the next starts) share no inner point
  and may both stay;
- sorting by left end, or by length, and taking greedily gives wrong
  answers: a long segment that starts first can block several short ones;
- segments may repeat; each copy is a separate segment, but at most one of
  them can stay.

The answers were checked by the checker on every test and on 150 random
sets, including touching chains, repeated segments and nested ones.

## Optimized solutions

The optimized C++ solution keeps the segments in one global array of 99
pairs, since `N ≤ 99`, instead of two `vector`s, and writes the kept
segments over the front of the same array: a kept segment only takes the
place of one already scanned. No heap memory is allocated:
{1112_greedy_optimized.cpp}.

The optimized Java solution reads the input in 4 KB blocks and parses
the signed numbers by hand instead of `Scanner`, keeps the ends in two
`int` arrays instead of an array object per segment, and sorts them by
insertion, which for `N ≤ 99` is cheap and needs no comparator; the kept
segments are written over the front of the same arrays:
{1112_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1112_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +41.67%; base: `1112_greedy.cpp`.

- `1112_greedy_optimized.java`: time reduction +40.38%; memory reduction
  +89.45%; base: `1112_greedy.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1112_greedy.go](1112_greedy.go).
- [1112_greedy.rs](1112_greedy.rs).

- All languages run the same sort and scan.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy.cpp](1112_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB | 11279212 |
| [1112_greedy.go](1112_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.015 s | 1156 KB | 11279213 |
| [1112_greedy.java](1112_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.156 s | 3944 KB | 11279215 |
| [1112_greedy.py](1112_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 460 KB | 11279214 |
| [1112_greedy.rs](1112_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 232 KB | 11279216 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy_optimized.cpp](1112_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 112 KB | 11307228 |
| [1112_greedy_optimized.java](1112_greedy_optimized.java) | Java 1.8 | greedy | O(N²) | AC | 0.093 s | 416 KB | 11307227 |
