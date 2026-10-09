# 1046. Restoring a polygon from the apexes of its side triangles

[Timus 1046](https://acm.timus.ru/problem.aspx?space=1&num=1046) · difficulty 1887 · geometry

Original problem by Dmitry Filimonenkov, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A polygon `A1 A2 … AN` (`3 ≤ N ≤ 50`) has its vertices in clockwise
order. On every side `Ai Ai+1` (with `AN+1 = A1`) an isosceles triangle
`Ai Mi Ai+1` is built outside the polygon, with `Mi Ai = Mi Ai+1` and the
angle `αi` at `Mi`. No nonempty subset of the angles sums to a multiple of
360°. Given the apexes `Mi` and the angles, restore the vertices.

All input numbers are reals with at most two decimals, `|xi|, |yi| ≤ 100`.
Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the coordinates of `M1 … MN`, then `N` lines with
the angles `α1 … αN` in degrees.

## Output

`N` lines with the coordinates of `A1 … AN`, accurate to two decimals.

## Checking

Numbers are compared with an absolute error of 0.011: the answers are
printed with two decimals, so the last digit may differ by one.

## Examples

### Example 1

Input:

```
3
0 2
3 3
2 0
90
90
90
```

Output:

```
1.00 1.00
1.00 3.00
3.00 1.00
```

### Example 2

Input:

```
4
-1.73 1.00
1.00 3.00
2.58 1.00
1.00 -2.41
60
90
120
45
```

Output:

```
0.00 -0.01
0.01 2.00
2.00 2.01
2.00 -0.01
```

## Solution

Treat points as complex numbers. `Mi Ai = Mi Ai+1` with the angle `αi`
at `Mi` means that `Ai+1` is `Ai` turned around `Mi` by `αi`
(counterclockwise for a clockwise polygon with outer triangles):

```text
A[i+1] = M[i] + w[i] · (A[i] − M[i]),     w[i] = e^(i·α[i])
```

Each step is a map `z → w·z + (1 − w)·M`. Composing all `N` of them in
order gives `z → a·z + b` with `a = w1 · … · wN = e^(i·Σα)`, and `A1`
must be its fixed point because the walk returns to `A1`:

```text
A1 = a·A1 + b   →   A1 = b / (1 − a)
```

The angles never add up to a multiple of 360°, so `a ≠ 1` and the
answer is unique. The other vertices follow by applying the steps one by
one. `O(N)`.

Pitfalls:

- the turn direction: with clockwise vertices and triangles outside, the
  turn from `Ai` to `Ai+1` about `Mi` is counterclockwise;
- angles are in degrees;
- the input apexes are rounded, so the restored polygon is close to, not
  exactly, the original one; print two decimals and avoid `-0.00`.

## Language notes

- **C++**: `std::complex`; **Go**: `complex128`; **Python**: built-in
  complex numbers.
- **Java**: real and imaginary parts kept in separate variables;
  `String.format` with `Locale.US` for the decimal point.
- **Rust**: a small complex type with the four operators.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1046_geometry.cpp](1046_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 212 KB |
| [1046_geometry.go](1046_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1160 KB |
| [1046_geometry.java](1046_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 1116 KB |
| [1046_geometry.py](1046_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.062 s | 576 KB |
| [1046_geometry.rs](1046_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 280 KB |
