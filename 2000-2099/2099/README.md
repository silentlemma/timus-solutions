# 2099. One right-angle turn through four points

[Timus 2099](https://acm.timus.ru/problem.aspx?space=1&num=2099) · difficulty 574 · geometry

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Can a point flying in a straight line pass A and then B, turn by 90°,
and then fly in a straight line through C and then D? The turning point
may be B or C. The limits are 1 second and 64 MB.

## Input

The integer coordinates of A, B, C, D in space, up to 10⁶ in absolute
value; the points are pairwise different.

## Output

`Valid` or `Invalid`.

## Examples

### Example 1

Input:

```
-2 0 0
-1 0 0
0 1 0
0 2 0
```

Output:

```
Valid
```

## Solution

The first line is A + t·AB and the second goes through C with direction
CD, both travelled forwards. The flight works exactly when:

- AB · CD = 0, the turn is a right angle;
- AC · (AB × CD) = 0, the two lines lie in one plane, so being
  perpendicular they meet in a point P;
- P = A + t·AB with t = (AC · AB) / |AB|² (the foot of the second line on
  the first, since CD ⊥ AB) is not before B: AC · AB ≥ |AB|²;
- C is not before P on the second line: (C − P) · CD = AC · CD ≥ 0,
  because the AB part of C − P is orthogonal to CD.

All checks are exact in integers. The mixed product reaches about
5·10¹⁹, beyond 64 bits, so C++ and Rust use 128-bit integers and Go and
Java big integers for it.

In the example the first line is the x axis, the second the y axis, the
turn happens at the origin after B = (−1, 0, 0), and C = (0, 1, 0) comes
after it: Valid.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 128 KB |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1160 KB |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1720 KB |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 548 KB |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 240 KB |
