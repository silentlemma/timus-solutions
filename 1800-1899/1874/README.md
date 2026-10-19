# 1874. Football Goal

[Timus 1874](https://acm.timus.ru/problem.aspx?space=1&num=1874) · difficulty 199 · geometry

Original problem by Fedor Fominykh, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goal is built from a vertical birch, the ground and two sticks of
lengths a and b: the birch is one post, and the sticks make the other
post and the crossbar. The goal may be any quadrilateral. Find its
largest area. The birch is taller than a + b.

## Input

a and b (1 ≤ a, b ≤ 10 000).

## Output

The largest area, with at least six digits after the decimal point.

## Examples

### Example 1

Input:

```
2 2
```

Output:

```
4.828427125
```

## Solution

The quadrilateral has a right angle where the birch meets the ground.
Its diagonal c from the top of the birch side to the far end on the
ground splits it in two. One part is a right triangle with hypotenuse
c, whose area is at most c²/4, reached when its legs are equal. The
other part is the triangle of the two sticks with angle t between
them. Then c² = a² + b² − 2ab·cos t, and the total is
(a² + b² − 2ab·cos t)/4 + ab·sin t/2. Its derivative vanishes when
sin t + cos t = 0, so t = 135°, and the area is
(a² + b² + 2√2·ab)/4. `O(1)`.

For a = b = 2 this gives (4 + 4 + 8√2)/4 = 2 + 2√2 ≈ 4.828427125.

Pitfalls:

- the goal need not be a rectangle; the right angle at the foot of the
  birch is the only fixed part;
- the angle between the sticks is 135°, not 90°: a right angle there
  gives only (a + b)²/4;
- the birch is tall enough by the statement, so its height never
  limits the answer.

The formula agrees with a direct search over the angle between the
sticks, and with an independent accepted implementation on all tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1874_geometry.cpp](1874_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1874_geometry.go](1874_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1874_geometry.java](1874_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1832 KB |
| [1874_geometry.py](1874_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 452 KB |
| [1874_geometry.rs](1874_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 248 KB |
