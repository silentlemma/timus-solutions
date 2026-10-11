# 1265. Mirror

[Timus 1265](https://acm.timus.ru/problem.aspx?space=1&num=1265) · difficulty 1514 · geometry

Original problem by Alexander Klepinin (prepared by Ivan Dashkevich), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given the eye (x1, y1), the target (x2, y2) and a flat mirror, the
segment between (xm1, ym1) and (xm2, ym2), decide whether the target is
seen in the mirror from the eye. The mirror reflects on both sides, with
the angle of incidence equal to the angle of reflection. All eight
numbers lie in [−1000, 1000] with at most six digits after the point;
neither point lies on the mirror's line, and the mirror's ends differ.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The eight numbers, separated by spaces and line breaks.

## Output

`VISIBLE` or `INVISIBLE`.

## Examples

### Example 1

Input:

```
1 0 0 -1 0 0 1 1
```

Output:

```
VISIBLE
```

### Example 2

Input:

```
0.000001   0
0   0.000001
-0.000001   -0.000001
0.000001   0.000001
```

Output:

```
INVISIBLE
```

## Solution

The target is seen when both points are on the same side of the
mirror's line and the line of sight from the eye to the target's mirror
image crosses the mirror segment, its ends included.

Put the origin at end A of mirror AB, let s = B − A,
and let e and t be the eye and the target relative to A. The cross
products he = s × e and ht = s × t are the heights of the two points
above the line, times |s|; they must have the same sign. The dot
products pe = s · e and pt = s · t are their positions along the line,
times |s|. The line of sight meets the mirror's line where it divides
the way between the two feet in the ratio of the heights, so at

```text
u = (pe · ht + pt · he) / ((he + ht) · |s|²)
```

of the mirror's length from A, and the target is seen exactly when
0 ≤ u ≤ 1.

Floating point is not enough here: a crossing can lie a few millionths
from an end of a mirror two thousand long and decide the answer. So every
number is read as an exact integer in millionths, up to 10⁹ in absolute value.
Cross and dot products are bounded by 4 · 10¹⁸ and 8 · 10¹⁸
in absolute value; final products by 6.4 · 10³⁷, within signed 128-bit range. `O(1)`.

Pitfalls:

- a target in front of the mirror is not always seen: the reflected
  line of sight may miss the segment (tests 03, 04);
- a line of sight through an end of the mirror counts as seen (test 05),
  and moving the eye by 10⁻⁶ changes the answer (tests 06, 07);
- points on opposite sides are never seen, even with a two-sided mirror
  (test 02);
- the final products need more than 64 bits.

The answers were compared on 1500 random cases (small integers and
six-decimal points) with an exact reflection of the target in
fractions and a segment intersection test.

## Language notes

- C++ and Rust compute in `__int128` and `i128`; Go and Java take the
  heights and positions in 64 bits and the final products in `big.Int`
  and `BigInteger`; Python uses its own integers.
- Every language parses the numbers by hand, padding the fraction to
  six digits, so no value passes through a double.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1265_geometry.cpp](1265_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 368 KB |
| [1265_geometry.go](1265_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [1265_geometry.java](1265_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 564 KB |
| [1265_geometry.py](1265_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 516 KB |
| [1265_geometry.rs](1265_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 228 KB |
