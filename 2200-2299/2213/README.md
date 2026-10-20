# 2213. Moving one command of a robot program to minimize the collected sum

[Timus 2213](https://acm.timus.ru/problem.aspx?space=1&num=2213) · difficulty 2005 · prefix_sums

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

Take a command c with direction d at position i and reinsert it at
position j. The cells visited before both positions and after both
positions do not change. If j > i, the cells visited between them are
the original ones shifted by −d, since the step d now comes later; if
j < i, the cells in between are shifted by +d. So the change of the sum
is a sum over a contiguous interval of the path of
cell(p + shift) − cell(p).

For each of the four directions both cases become best-interval
problems on a prefix sum along the path:

- moving a command earlier needs, for every position i holding that
  command, the best start of the interval ending at i, found from the
  running maximum of the prefix sums with shift +d;
- moving a command later needs, for every end of the interval, the best
  position of a command with that direction before it, found from the
  running maximum of the prefix sums with shift −d.

The best of the eight scans gives the command to move and its new
position. Leaving the program unchanged is always allowed, so the
change is never positive.

In the first example moving the U at position 3 to the end shifts the
last two cells of the path down by one row and lowers the sum from 4
to 2.

This takes O(NM + |S|).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2213_prefix_sums.cpp](2213_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(NM + L) | AC | 0.031 s | 2792 KB |
| [2213_prefix_sums.go](2213_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(NM + L) | AC | 0.062 s | 8332 KB |
| [2213_prefix_sums.java](2213_prefix_sums.java) | Java 1.8 | prefix_sums | O(NM + L) | AC | 0.171 s | 6292 KB |
| [2213_prefix_sums.py](2213_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(NM + L) | AC | 0.671 s | 21304 KB |
| [2213_prefix_sums.rs](2213_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(NM + L) | AC | 0.046 s | 4512 KB |
