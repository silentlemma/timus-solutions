# 1348. Goat in the Garden 2

[Timus 1348](https://acm.timus.ru/problem.aspx?space=1&num=1348) · difficulty 179 · geometry

Original problem by Pavel Egorov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goat is tied to the point C with a rope of length L, so it can reach
everything within L of C. A bed of pineapples is the segment AB. Find
how much longer the rope must be for the goat to reach at least one
pineapple, and how much longer to reach all of them, with two digits
after the point. All numbers are integers, L ≥ 0, and the coordinates
are at most 10 000 in absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The coordinates of A, B and C and the length L.

## Output

The two extra lengths, one per line.

## Examples

### Example 1

Input:

```
8 -6 8 6
0 0 7
```

Output:

```
1.00
3.00
```

## Solution

The nearest point of the bed is the projection of C onto the line AB,
moved to A or B if it falls outside the segment. The farthest point of a
segment from any point is one of its ends. So the answers are
max(0, d_near − L) and max(0, max(|CA|, |CB|) − L). The projection uses
t = (C − A) · (B − A) / |B − A|², kept between 0 and 1, and a bed of a
single point, A = B, takes t = 0. `O(1)`.

Pitfalls:

- the bed can be a single point (tests 02 and 08);
- with C on the line of the bed beyond an end, the nearest point is that
  end, not the projection (test 04);
- a rope that is already long enough needs 0, not a negative number
  (test 05).

## Language notes

- All five solutions use the same formulas.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1348_geometry.cpp](1348_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 144 KB |
| [1348_geometry.go](1348_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1132 KB |
| [1348_geometry.java](1348_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1812 KB |
| [1348_geometry.py](1348_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 504 KB |
| [1348_geometry.rs](1348_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB |
