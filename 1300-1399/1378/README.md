# 1378. Artificial Intelligence

[Timus 1378](https://acm.timus.ru/problem.aspx?space=1&num=1378) · difficulty 1491 · geometry

Original problem: idea by Alexander Klepinin, prepared by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A black-and-white picture of W × H pixels, 32 ≤ W, H ≤ 1000, shows one
filled figure drawn in a graphics editor: a circle, a square or a
triangle, at least 30 pixels across, with no triangle angle under 10°.
It may be turned any way. Print `circle`, `square` or `triangle`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W and H, then H lines of W digits 0 or 1.

## Output

`circle`, `square` or `triangle`.

## Examples

### Example 1

Input:

```
32 32
00000000000000000000000000000000
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
00000000000000000000000000000000
```

Output:

```
square
```

## Solution

Two numbers that do not depend on size or turn tell the figures apart.
Take the centre of the figure, the distance r₁ to its farthest pixel,
and the reach r₂ across that direction; each is grown by half a pixel,
since a pixel reaches beyond its centre. With A the number of pixels:

- A / (π r₁ r₂) is 1 for any circle or oval, because r₁ and r₂ are its
  half-axes, but 2/π ≈ 0.64 for a square, whose r₁ and r₂ are its two
  half-diagonals. Above 0.8 the figure is a circle;
- A / (π r₁²) is 2/π for a square and at most about 0.41 for any
  triangle, the equilateral one included. Above 0.5 it is a square,
  below a triangle.

A convex figure fills one run of pixels in every row, so only the ends
of the runs matter for r₁ and r₂. `O(W · H)`.

Pitfalls:

- the first number is the width, the second the height;
- squares can be turned by any angle (test 03);
- some circles in the judge's tests are slightly oval, so a test of
  roundness alone that ignores r₂ can call them squares (test 06);
- thin triangles have an angle down to 10°.

On random rasterised figures of 30 to 150 pixels, the first measure
was at least 0.92 for ovals whose short axis is 0.6 to 1 times the long
one and at most 0.70 for turned squares, and the second at least 0.60
for squares and at most 0.38 for triangles with every angle at least
10°. Another 600 such figures were all recognised.

## Language notes

- Python joins all digits into one string and cuts it into rows, so
  rows written with or without spaces both work.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1378_geometry.cpp](1378_geometry.cpp) | G++ 13.2 x64 | geometry | O(W·H) | AC | 0.031 s | 224 KB |
| [1378_geometry.go](1378_geometry.go) | Go 1.14 x64 | geometry | O(W·H) | AC | 0.031 s | 1260 KB |
| [1378_geometry.java](1378_geometry.java) | Java 1.8 | geometry | O(W·H) | AC | 0.109 s | 640 KB |
| [1378_geometry.py](1378_geometry.py) | Python 3.12 x64 | geometry | O(W·H) | AC | 0.093 s | 3384 KB |
| [1378_geometry.rs](1378_geometry.rs) | Rust 1.75 x64 | geometry | O(W·H) | AC | 0.015 s | 3112 KB |
