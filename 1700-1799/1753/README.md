# 1753. Bookshelf

[Timus 1753](https://acm.timus.ru/problem.aspx?space=1&num=1753) · difficulty 335 · geometry

Original problem by Dmitry Ivankov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shelf of length L has rims of height h at both ends. A book of height
H stands upright at the left rim. Its lower edge is dragged to the
right along the shelf while its side keeps leaning on the top of the
left rim, until the book lies flat. Everything has zero thickness. Find
how far to the left of the left rim the middle of the book gets.

## Input

Integers h, H and L (1 ≤ h < H < L ≤ 1000).

## Output

The largest shift of the middle of the book to the left of the rim,
with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
7 120 200
```

Output:

```
39.850361
```

## Solution

Put the top of the left rim at (0, h) and the foot of the book at
(x, 0). The book lies along the line from the foot through the rim
top, which is r = √(x² + h²) long, so its middle at distance H/2 from
the foot is at horizontal position x(1 − H / 2r). The shift to the left
is f(x) = x(H / 2r − 1).

Its derivative is H·h² / 2r³ − 1, so f grows while r³ < H·h²/2 and
falls after, and the best moment is r = ∛(H·h²/2). That r is never
more than H, so the book still leans on the rim then. If this r is not
above h, which happens exactly when H ≤ 2h, the middle never passes
the rim and the answer is 0; otherwise x = √(r² − h²) and the answer is
f(x). L plays no part, since the book always fits on the shelf. `O(1)`.

In the example r = ∛2940 ≈ 14.33, x ≈ 12.50 and the shift is about
39.85.

Pitfalls:

- a book at most twice the rim gives 0, not a negative shift;
- the rim is on the left, so the foot moving right pushes the middle
  left only while the book is steep.

The formula agrees with a scan over 200001 foot positions on 100
random inputs and with an independent accepted implementation on 300
more.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1753_geometry.cpp](1753_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1753_geometry.go](1753_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1753_geometry.java](1753_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1816 KB |
| [1753_geometry.py](1753_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 400 KB |
| [1753_geometry.rs](1753_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 244 KB |
