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

The mixed product equals the signed determinant of AB, AC and AD.
The determinant is affine in each point, so the maximum absolute
value is attained at cube corners. The corner bound is 1.6·10¹⁹,
which exceeds signed 64 bits. The simple C++ and Rust versions
use 128-bit integers, while Go and Java use big integers.

In the example the first line is the x axis, the second the y axis, the
turn happens at the origin after B = (−1, 0, 0), and C = (0, 1, 0) comes
after it: Valid.

## Optimized solutions

Java splits each coordinate of AC into a quotient and a remainder
in base 65 536. Each component of AB × CD is at most 8·10¹² in
absolute value, so the two sums H and L fit in signed 64 bits.
The product vanishes exactly when L is divisible by 65 536 and
H + L / 65 536 is zero.

Python computes each test directly from the coordinate differences.

**Timus submissions**

- Simple · G++ 13.2 x64, №11318402 · Java 1.8, №11318403 · Python 3.12 x64, №11318407 · Rust 1.75 x64, №11318409.
- Optimized · Java 1.8, №11318393 · Python 3.12 x64, №11318399.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11318402 · Java 1.8 №11318403 · Python 3.12 x64 №11318407 · Rust 1.75 x64 №11318409 · Go 1.14 x64 №11322396.

Rust evaluates dot products in 64 bits and widens the scalar triple product to 128 bits. Rust 1.75 x64, submission 11323329. Time 0.015 → 0.046 s, memory 232 → 48 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2099_geometry.cpp](2099_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 108 KB | 11318402 |
| [2099_geometry.go](2099_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1168 KB | 11322396 |
| [2099_geometry.java](2099_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1672 KB | 11318403 |
| [2099_geometry.py](2099_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 520 KB | 11318407 |
| [2099_geometry.rs](2099_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 232 KB | 11318409 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2099_geometry_optimized.java](2099_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 360 KB | 11318393 |
| [2099_geometry_optimized.py](2099_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 472 KB | 11318399 |
| [2099_geometry_optimized.rs](2099_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 48 KB | 11323329 |

\* The marked solutions have room to improve in the ratings.
