# 1802. Cube Puzzle

[Timus 1802](https://acm.timus.ru/problem.aspx?space=1&num=1802) · difficulty 2070 · backtracking

Original problem by Stanislav Vasilyev, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Six flat n × n squares are lacquered on one side; on the other side
each cell carries a column of unit cubes of height 0 to n. The heights
add up to n³. Turning the parts freely, assemble an n × n × n cube with
lacquer all around, or report that it cannot be done.

## Input

n (2 ≤ n ≤ 20), then the six parts, each as n rows of n heights.

## Output

"No", or "Yes" and then n layers from the bottom up, each n rows from
back to front of n part numbers from 1 to 6, left to right.

## Examples

### Example 1

Input:

```
3
0 0 0
1 0 1
1 2 0
1 0 0
1 1 1
0 0 0
0 2 1
1 0 0
0 0 0
0 1 0
0 0 0
0 2 1
1 0 0
0 0 1
0 2 1
0 0 1
0 2 1
1 0 0
```

Output:

```
Yes
3 4 4
1 4 1
1 1 5
3 3 2
5 6 2
5 1 2
6 4 2
3 6 6
5 5 6
```

### Example 2

Input:

```
3
0 0 0
0 3 0
0 0 0
2 0 0
0 0 0
0 0 0
0 0 2
0 0 0
0 0 0
2 0 0
0 0 0
0 0 0
0 0 2
0 0 0
0 0 0
2 1 2
2 1 2
2 2 2
```

Output:

```
No
```

## Solution

With the lacquer outside, a part lies on one face of the cube with its
columns pointing inwards, turned in one of four ways. Mirrored
placements are impossible, so the six faces are fixed as the bottom
face moved by rotations of the cube. A part on a face and a turn fills
a known set of cells, kept as a bit mask, and equal masks from a
symmetric part are counted once. Since the whole cube may be turned,
the largest part goes on the bottom without a turn. Then a backtracking
search fills the remaining faces, always taking next the face with the
fewest parts and turns that do not overlap the cells already taken,
and giving up at once when a face has none. As the volumes add up to
n³, six non-overlapping parts fill the cube. There are at most 5! · 4⁵
assignments, and the pruning keeps the search tiny. `O(n³)` per step.

In the first example every cell of the 3 × 3 × 3 cube gets the number
of its part; the second example has no way to fit the parts.

Pitfalls:

- a part may not be flipped: turning it over would put the lacquer
  inside;
- symmetric parts give equal placements, which only slow the search;
- parts of height zero still need a face of their own.

The checker requires the cells of each part to be that part on some
face in one of its four turns, with a different face for every part,
and the given answer of the first example passes it. The answers
agree with an independent accepted implementation on cubes cut at
random into six parts, with and without one cell moved between parts.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1802_backtracking.cpp](1802_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(n^3) per search step | AC | 0.031 s | 696 KB |
| [1802_backtracking.go](1802_backtracking.go) | Go 1.14 x64 | backtracking | O(n^3) per search step | AC | 0.062 s | 1484 KB |
| [1802_backtracking.java](1802_backtracking.java) | Java 1.8 | backtracking | O(n^3) per search step | AC | 0.140 s | 5416 KB |
| [1802_backtracking.py](1802_backtracking.py) | Python 3.12 x64 | backtracking | O(n^3) per search step | AC | 0.234 s | 1152 KB |
| [1802_backtracking.rs](1802_backtracking.rs) | Rust 1.75 x64 | backtracking | O(n^3) per search step | AC | 0.031 s | 404 KB |
