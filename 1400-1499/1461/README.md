# 1461. Christmas Garland

[Timus 1461](https://acm.timus.ru/problem.aspx?space=1&num=1461) · difficulty 988 · greedy

Original problem by Alexander Toropov, with special thanks to Dmitry Ivankov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A garland of length N (2 ≤ N ≤ 100000) is a broken line from (0, 0) to
(N, 0) whose links go one unit to the right and up (u), down (d) or
straight (h). No vertex may lie below the x-axis, and no two consecutive
vertices may both lie on it. All garlands are listed as strings in
lexicographic order. Given one garland, print the next one in the list,
or "No solution" if it is the last.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the garland as a string of u, d and h.

## Output

The next garland, or "No solution".

## Examples

### Example 1

Input:

```
6
uhduhd
```

Output:

```
uhhdud
```

## Solution

A horizontal link on the axis would put two vertices on it in a row, so
the rule is: never below the axis, and no h on it. The order of the
letters is d < h < u. Whether a garland can still be finished from
height y with r links left has a simple answer: from the axis the next
link must rise, so r is 0 or at least 2; above the axis horizontal links
can pad any spare length, so r ≥ y is enough.

As usual for the next string in lexicographic order, find the last
position whose letter can be raised, to h or u, so that the prefix stays
valid and the garland can still be finished; keep everything before it,
and fill the rest with the smallest letters that keep a finish
possible, trying d, then h, then u at every step. If no position can be
raised, the garland is the last one. `O(N)`.

Pitfalls:

- h is never allowed on the axis, so from the axis the only way on is
  up, and the rest after a raised letter cannot always start low
  (tests 03, 05);
- the last garland, rising as long as it can, has no successor (tests
  02, 04, 06, gen2, gen3);
- odd lengths need a horizontal link somewhere above the axis (tests
  05, 07, 09).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1461_greedy.cpp](1461_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 916 KB |
| [1461_greedy.go](1461_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 3260 KB |
| [1461_greedy.java](1461_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.093 s | 4648 KB |
| [1461_greedy.py](1461_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.218 s | 6648 KB |
| [1461_greedy.rs](1461_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 1244 KB |
