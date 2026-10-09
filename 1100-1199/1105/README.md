# 1105. Choosing intervals so that exactly one covers two thirds of the time

[Timus 1105](https://acm.timus.ru/problem.aspx?space=1&num=1105) · difficulty 824 · greedy

Original problem by Dmitry Filimonenkov with Igor Goldberg, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A time span `[T0, T1]` is covered by `N < 10 000` intervals
`[a_i, b_i]` with `T0 ≤ a_i < b_i ≤ T1`: every moment of the span lies in
at least one of them. Choose a set of intervals such that the total time
covered by exactly one chosen interval is at least `2/3 · (T1 − T0)`.
Print `0` if no such set exists. All times are real numbers.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`T0 T1`, then `N`, then `N` lines `a_i b_i`.

## Output

The number of chosen intervals, then their numbers (1-based), one per
line, in any order; or a single `0`.

## Checking

Any valid set is accepted. The checker sweeps over the ends of the chosen
intervals, measures the time covered by exactly one of them and compares
it with `2/3 · (T1 − T0)` with a tolerance of `10^-6`.

## Examples

### Example 1

Input:

```
0.0 20.0
7
1.0 1.5
0.0 10.0
9.0 10.0
18.0 20.0
9.0 18.0
2.72 3.14
19.0 20.0
```

Output:

```
2
2
5
```

## Solution

The answer always exists, so `0` is never printed. First reduce the
intervals to a chain with the classic greedy cover: sort by start and,
from the current point, always take the interval that starts no later and
reaches furthest. In the resulting chain `I_1, …, I_m` only neighbours
overlap: if `I_{k+2}` started before `I_k` ends, the greedy would have
taken it instead of `I_{k+1}`.

Each moment of the span is then either in one chain interval or in the
overlap of two neighbours. Remove every third interval of the chain,
starting at shift 0, 1 or 2. A moment covered by one interval stays
covered once in the two shifts that keep that interval; a moment in the
overlap of `I_k` and `I_{k+1}` is covered once in the two shifts that
remove one of them, as they are never both removed. Summed over the three
shifts, every moment is counted twice, so the best shift keeps at least
`2/3` of the span. Its time alone is `Σ |I_k| − 2 Σ overlaps` over the
kept intervals and kept neighbour pairs. `O(N log N)`.

Pitfalls:

- choosing every interval can give nothing at all: two identical
  intervals covering the span are never alone;
- neighbours of the chain can merely touch, with an overlap of zero
  length, which the formula handles with `max(0, ·)`.

The answers were checked against a brute force over all subsets with
exact fractions on hundreds of small random covers, which also confirmed
that 2/3 is always reachable, and with the checker on every test.

## Language notes

- All five solutions read the times as doubles; equal input strings give
  equal values, so touching ends compare as equal everywhere.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1105_greedy.cpp](1105_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.031 s | 424 KB |
| [1105_greedy.go](1105_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1636 KB |
| [1105_greedy.java](1105_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.187 s | 6656 KB |
| [1105_greedy.py](1105_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 3296 KB |
| [1105_greedy.rs](1105_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.031 s | 628 KB |
