# 1672. Droid Flies

[Timus 1672](https://acm.timus.ru/problem.aspx?space=1&num=1672) · difficulty 10739 · geometry

Original problem by Dmitry Ivankov, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N flies hang at distinct integer points in space. Find a cube that holds
them all with at least one fly on every face, and print three unit
vectors along its edges. Such a cube always exists.

## Input

N (2 ≤ N ≤ 100), then the coordinates of the flies, integers of absolute
value at most 100.

## Output

Three unit vectors along the edges of the cube, as precisely as
possible.

## Examples

### Example 1

Input:

```
6
0 1 1
1 0 1
1 1 0
1 1 2
1 2 1
2 1 1
```

Output:

```
1 0 0
0 1 0
0 0 1
```

### Example 2

Input:

```
2
1 0 0
-1 0 0
```

Output:

```
0.577350269 0.211324865 -0.788675135
0.577350269 0.577350269 0.577350269
0.577350269 -0.788675135 0.211324865
```

Any valid cube is accepted; this solution prints different vectors for
the first example.

## Solution

For a unit vector u, the width w(u) is the largest minus the smallest
projection of a fly on u. The smallest box with edges along a right-angled
frame e₁, e₂, e₃ touches the flies on every face, and it is a cube
exactly when w(e₁) = w(e₂) = w(e₃).

Flies on one line (this covers N = 2) have w(u) = L·|cos|, so three axes
at angle arccos(1/√3) to the line each give a cube; they are written down
directly. Otherwise:

1. n_max is the direction between the two farthest flies, where no width
   is larger. n_min is the direction of the smallest width: the normal of
   a flat swarm, else the best of 1500 directions spread over the sphere,
   polished by small turns.
2. The frames considered have the third axis n(t) on the great circle
   from n_min (t = 0) to n_max (t = 1) and the first two turned by φ
   around it. Turning by a quarter turn swaps the first two axes, so
   w(e₁) − w(e₂) changes sign on [0, π/2] and a bisection finds φ(t)
   with equal first two widths.
3. At t = 0 the third width is the smallest of all, at t = 1 the
   largest, so a bisection on t for w(e₃) = w(e₁) gives the cube.

The root φ(t) is not always unique, and the bisection may then land on a
jump. The result is checked, and on failure the whole (t, φ) square is
searched: the curve of equal first two widths crosses it from t = 0 to
t = 1, and along it the third width goes from the smallest to the
largest, so a cube lies inside. An 80 × 80 grid of the squared width
differences is refined around its four best cells by fourteen rounds of
5 × finer local grids. Last, small turns of the frame about its own axes
polish the widths to rounding error. `O(N · (S + G²))` for S sphere
directions and a G × G grid.

Pitfalls:

- flies on a line or in a plane make the narrowest direction exact, and
  the line needs its own frame (tests 02, 05, 06);
- the local searches stop after a fixed number of passes, since tiny
  improvements could keep them going for very long;
- the checker accepts any right-angled unit vectors with widths equal
  within 10⁻⁶.

On 474 generated swarms (random, flat, on a line, near a sphere, long
and thin) every answer passes the checker; about one in twenty needed the
square search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1672_geometry.cpp](1672_geometry.cpp) | G++ 13.2 x64 | geometry | O(N (S + G^2)) | AC | 0.015 s | 408 KB |
| [1672_geometry.go](1672_geometry.go) | Go 1.14 x64 | geometry | O(N (S + G^2)) | AC | 0.078 s | 1828 KB |
| [1672_geometry.java](1672_geometry.java) | Java 1.8 | geometry | O(N (S + G^2)) | AC | 0.234 s | 6628 KB |
| [1672_geometry.py](1672_geometry.py) | Python 3.12 x64 | geometry | O(N (S + G^2)) | AC | 0.968 s | 2488 KB |
| [1672_geometry.rs](1672_geometry.rs) | Rust 1.75 x64 | geometry | O(N (S + G^2)) | AC | 0.031 s | 628 KB |
