# 1793. Tray 2

[Timus 1793](https://acm.timus.ru/problem.aspx?space=1&num=1793) · difficulty 403 · geometry

Original problem by Sofia Tekhazheva, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tray has an a × b bottom and vertical borders of height d. Two plates
are truncated cones of the same height h, each with a bottom radius and
a larger top radius. Can both plates stand with their whole bottoms on
the tray?

## Input

a, b and d; then the bottom and top radius of each plate; then h. All
numbers are whole, from 1 to 1000.

## Output

"YES" if the plates can be placed, otherwise "NO".

## Examples

### Example 1

Input:

```
10 10 10
1 2
1 2
5
```

Output:

```
YES
```

### Example 2

Input:

```
8 4 1
1 2
1 3
1
```

Output:

```
NO
```

## Solution

A plate widens upwards, so inside the borders it is widest at height
min(d, h), where its radius is w = r + (R − r)·min(d, h)/h. Above the
borders it may hang over the edge. So each plate's centre must stay at
least w from every side, which needs 2w ≤ a and 2w ≤ b. Two plates of
the same height are farthest from overlapping at the bottom and
closest at the top, so their centres must be at least R₁ + R₂ apart.
The centres are farthest apart in opposite corners of their allowed
rectangles, a − w₁ − w₂ apart along one side and b − w₁ − w₂ along the
other. Multiplying everything by h keeps it all in whole numbers, and
comparing squared distances avoids roots, so the test is exact.
`O(1)`.

In the first example the borders are higher than the plates, so w = 2
for both; the centres can be 6 apart along each side, about 8.49 in
all, and they need only 4.

Pitfalls:

- with low borders the top of a plate may be wider than the tray;
- the plates collide at their tops, not at the height of the borders;
- plates that just touch still fit, which a floating-point test can get
  wrong.

The answers agree with an independent accepted implementation on 600
random cases, among them plates that exactly touch along a 3-4-5
diagonal.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1793_geometry.cpp](1793_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 384 KB |
| [1793_geometry.go](1793_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1076 KB |
| [1793_geometry.java](1793_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1592 KB |
| [1793_geometry.py](1793_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 432 KB |
| [1793_geometry.rs](1793_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 220 KB |
