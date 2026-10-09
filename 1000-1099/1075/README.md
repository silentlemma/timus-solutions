# 1075. The shortest thread around a fixed ball

[Timus 1075](https://acm.timus.ru/problem.aspx?space=1&num=1075) · difficulty 1982 · geometry

Original problem by Alexander Mironenko, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Points `A`, `B` and `C` in space have integer coordinates up to 1000 in
absolute value. A solid ball of integer radius `R` is centred at `C`, and
both `A` and `B` are farther than `R` from `C`. Find the length of the
shortest thread from `A` to `B` that does not go inside the ball, rounded
to two decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The coordinates of `A`, `B` and `C`, one point per line, then `R`.

## Output

The length of the thread.

## Checking

Numbers are compared with an absolute error of 0.011: the answers are
printed with two decimals, so the last digit may differ by one.

## Examples

### Example 1

Input:

```
0 0 12
12 0 0
10 0 10
10
```

Output:

```
19.71
```

## Solution

The shortest thread lies in the plane through `A`, `B` and `C`, so it is
the shortest path around a disk of radius `R` in that plane. Let
`a = |CA|`, `b = |CB|` and `φ` be the angle `ACB`. Seen from `C`, the
tangent point from `A` is `α = arccos(R/a)` away from the direction of
`A`, and the one from `B` is `β = arccos(R/b)` away from `B`.

- If `φ ≤ α + β`, the segment `AB` does not enter the ball, and the
  answer is `|AB|`.
- Otherwise the thread goes along the tangent from `A`, around the arc of
  angle `φ − α − β` and along the tangent to `B`:
  `√(a² − R²) + √(b² − R²) + R·(φ − α − β)`.

`O(1)`.

Pitfalls:

- `φ` from `arccos` of the normalised dot product loses precision near 0
  and `π`; `atan2(|CA × CB|, CA · CB)` is accurate everywhere, and the
  dot and cross products are exact integers;
- when `A`, `C` and `B` lie on one line with `C` in the middle, the plane
  is not unique, but `φ = π` and the formula still holds;
- `A` may coincide with `B`; then `φ = 0` and the answer is 0.

The answers were checked another way: the plane is laid flat, the segment
is tested against the disk by its distance from `C`, and otherwise all
tangent–arc–tangent paths, over both tangent points of each end and both
arc directions, are compared.

## Language notes

- C++ keeps the vectors in `long long` so the products are exact before
  the square roots.
- Python uses `math.hypot` with three arguments for the lengths.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1075_geometry.cpp](1075_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1075_geometry.go](1075_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1075_geometry.java](1075_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1840 KB |
| [1075_geometry.py](1075_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 620 KB |
| [1075_geometry.rs](1075_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 248 KB |
