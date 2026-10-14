# 1550. Dean's Pyramid 3

[Timus 1550](https://acm.timus.ru/problem.aspx?space=1&num=1550) · difficulty 594 · geometry

Original problem by Evgeny Krokhalev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A regular square pyramid of height H and base side W (both below 10⁴)
has a vertical cylindrical hole of radius R through it, centred over the
point (X, Y) of the base, with the origin at the centre of the base and
the axes along its sides. The hole meets no edge of the pyramid. Find
the volume of the pyramid with the hole, within 10⁻³.

Time limit: 1 second. Memory limit: 64 MB.

## Input

H and W, then X and Y, then R.

## Output

The volume.

## Examples

### Example 1

Input:

```
3.0 3.0
-1.00 -0.70
0.1
```

Output:

```
8.96858
```

## Solution

The solid pyramid has volume H·W²/3. Over a point (x, y) of the base
its height is H·(1 − max(|x|, |y|)/(W/2)). Since the hole meets no edge,
its disc lies inside one triangle of the base under a single face, where
the height is a linear function of (x, y). The integral of a linear
function over a disc is its value at the centre times the area, so the
hole removes πR²·H·(1 − max(|X|, |Y|)/(W/2)). `O(1)`.

Pitfalls:

- the numbers may come without a decimal point (test 02);
- the volume reaches about 3·10¹¹, which double precision still holds
  to well under 10⁻³ (test 04);
- C++ has no standard M_PI, and the judge's compiler lacks it, so the
  C++ solution uses acos(−1).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1550_geometry.cpp](1550_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 456 KB |
| [1550_geometry.go](1550_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1550_geometry.java](1550_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1964 KB |
| [1550_geometry.py](1550_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 460 KB |
| [1550_geometry.rs](1550_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB |
