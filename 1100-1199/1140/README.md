# 1140. The shortest way back to the centre of a hexagonal grid after a walk

[Timus 1140](https://acm.timus.ru/problem.aspx?space=1&num=1140) · difficulty 381 · geometry

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bog is split into hexagonal cells, and three of the six directions
between neighbouring cells are named `X`, `Y` and `Z`, with `Y` lying
between `X` and `Z`. A student starts in the central cell and walks along
up to 32000 straight segments, each given as a direction and a nonzero
signed length; a negative length goes the opposite way. The student never
gets more than 100 cells away from the centre. Describe a route back to
the centre through the fewest cells, in the same format.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n`, then `n` lines with a direction letter and a signed length.

## Output

The number of segments `m ≥ 0` of the way back, then the segments.

## Checking

Any shortest route is accepted. The checker verifies the format, that the
route ends at the centre, and that its total length equals the hexagonal
distance from the last cell.

## Examples

### Example 1

Input:

```
4
Z -2
Y 3
Z 3
X -1
```

Output:

```
2
Y -2
Z -2
```

## Solution

On a hexagonal grid the middle direction is the sum of the other two: one
step along `Y` lands on the same cell as one step along `X` followed by
one along `Z`. So add up the lengths per direction and write the end of
the walk as `a·X + b·Z` with `a = X + Y` and `b = Z + Y`. A way back that
uses `m` steps along `Y` needs `a − m` along `X` and `b − m` along `Z`,
backwards, and has `|a − m| + |m| + |b − m|` steps. A sum of distances
from `m` to the points `a`, `0` and `b` is smallest at their median, so
take `m` as the median of `a`, `0` and `b` and print the nonzero parts of
`X −(a − m)`, `Y −m`, `Z −(b − m)`. `O(n)`.

Pitfalls:

- when `a` and `b` have the same sign, part of the way goes along `Y`;
  when their signs differ, `m = 0` and `Y` is not used;
- segments of length zero are not allowed, so they are dropped, and the
  answer can be `0` segments;
- several shortest routes may exist, any one is accepted.

The answers were checked by the checker on every test and on 200 random
walks; the distance formula in the checker was compared with a
breadth-first search over all cells within 100 of the centre.

## Language notes

- All languages add up the lengths and take the same median.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1140_geometry.cpp](1140_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 188 KB |
| [1140_geometry.go](1140_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1348 KB |
| [1140_geometry.java](1140_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 828 KB |
| [1140_geometry.py](1140_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.125 s | 776 KB |
| [1140_geometry.rs](1140_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 344 KB |
