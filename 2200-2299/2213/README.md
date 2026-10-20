# 2213. Moving one command of a robot program to minimize the collected sum

[Timus 2213](https://acm.timus.ru/problem.aspx?space=1&num=2213) · difficulty 1278 · prefix_sums

Original problem by Ignat Nigmatullin, from the University Academic School Olympiad in Informatics 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot starts at cell (1, 1) of an infinite grid where only an N × M
rectangle holds nonzero values, follows a program of R, D, L and U
moves, and adds the value of every cell it visits, the start included.
Move exactly one command to any position of the program, possibly its
own, so that the sum is as small as possible, and print the new
program. The limits are 1.5 seconds and 256 MB.

## Input

N and M with N · M ≤ 10⁵, the grid with values up to 10⁹ in absolute
value, then the program of length 2 … 10⁵.

## Output

An optimal program.

## Examples

### Example 1

Input:

```
2 3
1 2 3
1 -1 2
DRULL
```

Output:

```
DRLLU
```

### Example 2

Input:

```
2 2
-1 1
1 -1
RDULD
```

Output:

```
DULRD
```

### Example 3

Input:

```
2 3
1 1 1
1 1 1
RRD
```

Output:

```
RRD
```

## Solution

Number commands from zero, let p[k] be the position after k commands,
and let f(p) be its cell value (zero outside the rectangle). Remove the
command with direction d at index i and insert it at index j in the
remaining program. The change of the sum, including the interval
boundaries, is:

- if j ≤ i: sum over k = j … i of f(p[k] + d) − f(p[k + 1]);
- if j ≥ i: sum over k = i … j of f(p[k + 1] − d) − f(p[k]).

Visits outside these intervals stay unchanged. The term at k = i is
zero because p[i + 1] = p[i] + d.

For each of the four directions both cases become best-interval
problems on a prefix sum along the path:

- moving a command earlier needs, for every position i holding that
  command, the best start of the interval ending at i, found from the
  running maximum of the prefix sums of f(p[k] + d) − f(p[k + 1]);
- moving a command later needs, for every end of the interval, the best
  position of a command with that direction before it, found from the
  running maximum of the prefix sums of f(p[k + 1] − d) − f(p[k]),
  considering only starts holding that command.

The best of the eight scans gives the command to move and its new
position. Leaving the program unchanged is always allowed, so the
change is never positive.

In the first example moving U at index 2 to the end replaces the visits
to (1, 2) and (1, 1) with (2, 1) and (2, 0), lowering the sum from 4 to 2.

Pitfall ([test 05](tests/05.in)): summing only f(p[k] ± d) − f(p[k])
misses a boundary term. On its single cell of value 7, RL and LR both
score 14; shifting the original intermediate cell alone predicts a
change of +7 instead of zero. Use the adjacent path indices above.

This takes O(NM + |S|).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2213_prefix_sums.cpp](2213_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(NM + L) | AC | 0.031 s | 2792 KB |
| [2213_prefix_sums.go](2213_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(NM + L) | AC | 0.062 s | 8332 KB |
| [2213_prefix_sums.java](2213_prefix_sums.java) | Java 1.8 | prefix_sums | O(NM + L) | AC | 0.171 s | 6292 KB |
| [2213_prefix_sums.py](2213_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(NM + L) | AC | 0.671 s | 21304 KB |
| [2213_prefix_sums.rs](2213_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(NM + L) | AC | 0.046 s | 4512 KB |
