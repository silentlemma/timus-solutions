# 2148. Bouncing a shot off a round tank between two equidistant players

[Timus 2148](https://acm.timus.ru/problem.aspx?space=1&num=2148) · difficulty 491 · geometry

Original problem by Kirill Meshcheryakov, from the Ural Team Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A round tank has centre C and radius r. Two players A and B stand
outside it at the same distance from C. Find a point of the tank's
border at which a shot from A bounces to B, with the angle of incidence
equal to the angle of reflection and no part of the path inside the
tank; a grazing shot along a tangent does not count. Print "No way" if
there is none. The limits are 0.5 seconds and 256 MB.

## Input

The centre and the radius, then A, then B, all integers with absolute
values at most 3000.

## Output

The point, or "No way".

## Checking

A checker verifies the distance to the centre and the two angles within
10⁻⁶ and that both shots stay outside the tank.

## Examples

### Example 1

Input:

```
4 7 3
0 0
8 0
```

Output:

```
4.000000 4.000000
```

### Example 2

Input:

```
0 0 2
-5 0
-3 4
```

Output:

```
-1.788854 0.894427
```

## Solution

Since |A − C| = |B − C|, the picture is symmetric about the bisector of
the angle ACB, and the point on that bisector, P = C + r · w / |w| with
w = A + B − 2C, reflects A to B: the normal at P is the bisector
itself. The path A → P stays outside without grazing exactly when A is strictly
beyond the tangent line at P, that is, (A − C) · w > r · |w|; by
symmetry the same then holds for B. With equality the shot grazes the
tangent, and w = 0 means A and B are opposite each other, which makes
the left side 0.

If the condition fails there is no other point either: the border
points visible from A form an arc around A's direction, those visible
from B an arc around B's, and when the bisector point is not strictly
inside both arcs, their interiors do not overlap.

The test uses integers only, squaring both sides once the left side is
positive; the values stay far below 64 bits. The coordinates of P are
printed with nine decimals.

In the first example w = (0, −14) points straight down from C = (4, 7),
so P = (4, 4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2148_geometry.cpp](2148_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 144 KB |
| [2148_geometry.go](2148_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [2148_geometry.java](2148_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1800 KB |
| [2148_geometry.py](2148_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 524 KB |
| [2148_geometry.rs](2148_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 260 KB |
