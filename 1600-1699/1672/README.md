# 1672. Droid Flies

[Timus 1672](https://acm.timus.ru/problem.aspx?space=1&num=1672) · difficulty 8499 · geometry

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

Any valid cube is accepted.

## Solution

For a unit vector u, the width w(u) is the largest minus the smallest
projection of a fly on u. The smallest box along an orthonormal frame
e₁, e₂, e₃ touches flies on all six faces. It is a cube exactly when
w(e₁) = w(e₂) = w(e₃).

First test the coordinate axes: their integer widths are exact, and if
all three match, this frame already gives the cube.

Flies on one line, including N = 2, have w(u) = L·|cos|. Three axes at
angle arccos(1/√3) to the line give equal widths and are written directly.
Otherwise:

1. Find the diameter direction n_max. For n_min use the plane normal for
   a flat swarm, or the best of S = 1500 sphere directions followed by
   small turns. This search only supplies a starting direction.
2. Move the third axis along a great circle from n_min to n_max. At each
   position, bisect a quarter turn of the first two axes to equalize
   their widths. An outer bisection tries to equalize the third width.
   Check the resulting widths: the selected inner root can jump.
3. If this candidate fails, use a quaternion disk with boundary vertices
   (1,0,0,0), (−1/2,1/2,1/2,1/2), (−1/2,−1/2,−1/2,−1/2), and center
   (0,1/√2,−1/√2,0). Normalize interpolated quaternions and measure the
   residual F = (w(e₁) − w(e₃), w(e₂) − w(e₃)). Along the boundary the
   axes cycle, so F has nonzero winding about the origin unless a valid
   frame has already been found.
4. Split the disk into three triangles, retain one with nonzero winding,
   and repeatedly split it into four using normalized edge midpoints.
   Winding is additive, so a child still encloses a zero. To measure an
   edge safely, subdivide until one residual coordinate cannot change
   sign: its variation is at most 4D times the quaternion chord length,
   where D is the diameter. Then the endpoint angle change is valid.
   A zero on an edge is found by this subdivision as well. Stop only
   when the measured width spread is at most 10⁻¹⁰D.

With fixed bisection and local-search limits, the time is
`O(N² + N(S + K))`, where K counts the adaptive winding samples. The
search keeps only the current triangle and recursive edge stack; it
stores no growing mesh. Every search result is checked, and quaternion
normalization preserves orthogonality.

Pitfalls:

- collinear points need their direct frame, and planar points give an
  exact normal (tests 02, 05, 06);
- equal-width roots can jump, and refining the best grid cells or making
  small local turns can stall at a positive residual (test 17); retain
  nonzero winding instead of trusting a numerical minimum;
- winding needs certified edge subdivision; endpoint angles alone can
  miss a complete turn or a zero on the edge;
- the checker uses a relative width tolerance of 10⁻⁶ and accepts any
  orthonormal frame satisfying it.

All 16 stored inputs and 9 generator cases pass the checker. Another
1000 small random inputs pass independent checks against the constructive
oracle.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1672_geometry.cpp](1672_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.015 s | 244 KB |
| [1672_geometry.go](1672_geometry.go) | Go 1.14 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.046 s | 1204 KB |
| [1672_geometry.java](1672_geometry.java) | Java 1.8 | geometry | O(N^2 + N(S + K)) | AC | 0.156 s | 4976 KB |
| [1672_geometry.py](1672_geometry.py) | Python 3.12 x64 | geometry | O(N^2 + N(S + K)) | AC | 1.125 s | 1816 KB |
| [1672_geometry.rs](1672_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.046 s | 280 KB |
