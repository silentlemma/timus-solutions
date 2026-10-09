# 1043. The integer bounding box of a circular arc

[Timus 1043](https://acm.timus.ru/problem.aspx?space=1&num=1043) · difficulty 1626 · geometry

Original problem by Alexander Mironenko, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An arc of a circle is given by its two ends `A`, `B` and one more point
`C` of the arc; all three have integer coordinates of absolute value at
most 1000 and are not collinear. The center of the circle and the whole
arc lie in the square `[-1000, 1000]^2`. Find the smallest area of an
axis-parallel rectangle with integer corners that covers the arc.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Three lines with the coordinates of `A`, `B` and `C`.

## Output

The smallest area.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
476 612
487 615
478 616
```

Output:

```
66
```

### Example 2

Input:

```
-5 0
5 0
0 5
```

Output:

```
50
```

## Solution

The bounding box of the arc is spanned by its ends and by those of the
four extreme points of the circle (`center ± r` along each axis) that lie
on the arc. The rectangle then extends the box down to the floor of the
lower bounds and up to the ceiling of the upper ones.

A point of the circle is on the arc exactly when it is `A`, `B`, or lies
on the same side of the line `AB` as `C`. So the test is a sign of a
cross product.

The difficulty is precision. An extreme like `center_x + r` can be an
integer exactly, or miss one by `10^-8`; then `ceil` in floating point
easily gives the wrong answer. The solutions work exactly with integers:

- the center is `(ux / d, uy / d)` with integers `ux`, `uy`, `d > 0`
  (Cramer's rule), and `r · d = sqrt(rho2)` with an integer `rho2`;
- `ceil(center_x + r)` is the smallest integer `k` with `k·d − ux ≥ 0`
  and `(k·d − ux)^2 ≥ rho2`; a floating-point estimate gives a start, and
  exact comparisons move it by a step or two; `floor` is symmetric;
- the side of an extreme point times `d` has the form
  `alpha − gamma · sqrt(rho2)` with integers `alpha`, `gamma`, and its
  sign is found by comparing `alpha^2` with `gamma^2 · rho2` (after
  checking the signs of `alpha` and `gamma`).

The numbers reach about `10^28`, which needs 128-bit integers. `O(1)`.

Pitfalls:

- an extreme exactly on a grid line must not push the border one unit
  further, and one just past a grid line must;
- an extreme that coincides with an end of the arc gives side 0: it is
  already counted as an end;
- the center can be at a half-integer, so integer extremes do not need
  an integer center (tests 13 and 14).

## Language notes

- **C++**: `__int128`; **Rust**: `i128`.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: built-in
  integers, with `math.isqrt` for the starting point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1043_geometry.cpp](1043_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 400 KB |
| [1043_geometry.go](1043_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1216 KB |
| [1043_geometry.java](1043_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1724 KB |
| [1043_geometry.py](1043_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 828 KB |
| [1043_geometry.rs](1043_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 220 KB |
