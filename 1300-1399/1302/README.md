# 1302. Delta-wave

[Timus 1302](https://acm.timus.ru/problem.aspx?space=1&num=1302) · difficulty 347 · math

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An infinite triangle is cut into unit triangles and numbered row by
row: row 1 holds cell 1, row 2 holds cells 2 to 4, row k holds the
2k − 1 cells from (k − 1)² + 1 to k², alternating triangles pointing
up and down. A step crosses an edge into a neighbouring cell (crossing
a corner does not count). Find the fewest steps from cell m to cell n,
1 ≤ m, n ≤ 10⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

m and n.

## Output

The length of the shortest route.

## Examples

### Example 1

Input:

```
6 12
```

Output:

```
3
```

## Solution

The edges of the grid lie on three families of parallel lines:
horizontal ones and two families of slanted ones. Number the strips
between the lines of each family. Every cell then has three numbers:
its row r, its strip counted from the left edge and its strip counted
from the right edge. For cell n with r = ⌈√n⌉ and place
p = n − (r − 1)² in its row (1 to 2r − 1):

- left strip ⌊(p + 1) / 2⌋, right strip ⌊(2r − p + 1) / 2⌋.

Crossing an edge crosses exactly one line, so it changes exactly one
of the three numbers by 1. Hence every route is at least as long as the
sum of the three differences, and on this grid that sum can always be
reached, so

answer = |Δrow| + |Δleft| + |Δright|.

For the example, cell 6 is (3, 1, 2) and cell 12 is (4, 2, 3), so the
answer is 1 + 1 + 1 = 3. The row comes from an exact integer square
root. `O(1)`.

Pitfalls:

- consecutive numbers can be far apart: k² ends one row and k² + 1
  starts the next at the other edge (tests 06 and 07);
- cells 1 and 2 touch only at a corner, so they are 2 steps apart
  (test 03);
- the row must come from an exact integer square root: the row ends
  exactly at k², and a root that is one off puts a cell in the wrong
  row.

The formula was compared with a breadth-first search over a board of
30 rows, for every pair of a start below 120 and a target below 625.

## Language notes

- Python uses `math.isqrt`; the other languages adjust a
  floating-point root up or down until it is exact.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1302_math.cpp](1302_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB |
| [1302_math.go](1302_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1302_math.java](1302_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1576 KB |
| [1302_math.py](1302_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 504 KB |
| [1302_math.rs](1302_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
