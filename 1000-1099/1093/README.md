# 1093. Does a falling dart pass through a round target in space

[Timus 1093](https://acm.timus.ru/problem.aspx?space=1&num=1093) · difficulty 1996 · geometry

Original problem by Alexander Klepinin, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The target is a disk with centre `C`, radius `R` and normal vector `N`.
A dart starts at `S` with velocity `V` (with a nonzero horizontal part)
and moves as `S + V·t − (g/2)·t²·ẑ` with `g = 10`. It starts outside the
target. Print `HIT` if the dart ever passes strictly inside the disk,
from either side, and `MISSED` otherwise. All 13 numbers are at most 500
in absolute value with at most four decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`Cx Cy Cz Nx Ny Nz R`, then `Sx Sy Sz Vx Vy Vz`.

## Output

`HIT` or `MISSED`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
47 0 -72 1 0 1 4.25
0 0 0 10 0 10
```

Output:

```
HIT
```

## Solution

Let `D = S − C`. The dart's distance to the plane, times `|N|`, is
`N·(D + V t) − 5 Nz t²`, a quadratic `a t² + 2h t + c` with `a = −5 Nz`,
`h = N·V / 2` and `c = N·D`. The dart can only touch the disk at a root
`t ≥ 0` of it, and there the test is whether the squared distance to the
centre, `Q(t) = |D + V t − 5t² ẑ|² − R²`, is negative.

- `a ≠ 0`: up to two roots `t = (−h ± √(h² − ac)) / a`; the parabola can
  cross the plane twice, and either crossing may be the hit.
- `a = 0`, `h ≠ 0` (a vertical plane): one root `t = −c / 2h`.
- `a = h = 0`: the path is parallel to the plane or lies in it. Either
  way the dart never comes through the disk from one side, so it misses:
  sliding inside the plane of the target is not a hit.

`O(1)`.

Pitfalls:

- strictly inside: a dart exactly on the rim misses, so the comparison
  uses a small negative tolerance;
- only roots with `t ≥ 0` count, and both roots must be tried, since the
  first crossing can pass beside the disk and the second through it;
- the discriminant can be slightly negative from rounding when the top of
  the flight just touches the plane, so it is compared with a small
  tolerance, and a root a hair below zero still counts as `t = 0`;
- `N` is not normalised, which does not matter because only the sign and
  the roots of the plane equation are used.

The answers were checked against an exact computation with fractions: at
a root of the quadratic, `Q` reduces to a linear form in `t`, and its sign
at `(−h ± √d) / a` is decided without rounding. Hundreds of random throws
aimed within a ten-thousandth of the rim were compared this way. An
earlier version counted a path lying in the plane and crossing the disk
as a hit; Timus rejected it on test 56, so such a path is now a miss.

## Language notes

- Rust destructures the thirteen numbers with a slice pattern.
- Java reads the numbers with `Locale.US`, so the decimal point is
  accepted whatever the system locale is.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1093_geometry.cpp](1093_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 448 KB |
| [1093_geometry.go](1093_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1093_geometry.java](1093_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1844 KB |
| [1093_geometry.py](1093_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 548 KB |
| [1093_geometry.rs](1093_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 228 KB |
