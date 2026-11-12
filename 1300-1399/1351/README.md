# 1351. Good Gnusmas – Dead Gnusmas

[Timus 1351](https://acm.timus.ru/problem.aspx?space=1&num=1351) · difficulty 518 · geometry

Original problem by Denis Musin, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A machine gun at the origin covers a sector between two rays: the right
border through (X1, Y1) and the left border through (X2, Y2); the sector
is narrower than a half turn. It reaches up to distance D ≤ 30 000. For
each of N ≤ 30 000 points print `YES` if the point is in the sector and
no farther than D, and `NO` otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

D, X1, Y1, X2, Y2, then N, then N lines with the points. All numbers are
integers of absolute value at most 30 000, and no point is the origin.

## Output

N lines with `YES` or `NO`.

## Examples

### Example 1

Input:

```
5 1 0 0 1
6
1 1
5 6
3 0
-1 2
0 5
-3 0
```

Output:

```
YES
NO
YES
NO
YES
NO
```

## Solution

The sector runs counterclockwise from the right border R to the left
border L. A point P is in it when it is not clockwise of R and not
counterclockwise of L:

- cross(R, P) = X1·y − Y1·x ≥ 0;
- cross(P, L) = x·Y2 − y·X2 ≥ 0.

Each test cuts a half-plane, and because the sector is narrower than a
half turn the two half-planes meet exactly in the sector, with one
exception: when both borders lie on the same ray (a sector of zero
width), the backward extension of that ray passes both tests too. So a
point on a border's line but behind the gun, with a zero cross product
and a negative dot product, is rejected explicitly. The range test
is x² + y² ≤ D², all in integers with no square roots. `O(N)`.

Pitfalls:

- points on the borders and on the circle count: `3 0` and `0 5` in the
  example;
- a point on the ray opposite to a border has a zero cross product with
  that border; the other test rejects it, except in a sector of zero
  width, where only the explicit check does (tests 02 and 06);
- the products reach 1.8·10⁹, within signed 32-bit integers;
- with D = 30 000 the point (30 000, 1) is just out of range (test 04).

The answers were compared with an angle check through `atan2` on 18
generated tests and with an independent solution on 300 random
sectors, zero-width ones included.

## Optimized solutions

C++, Go and Rust retain the two cross-product tests and the squared-distance test. For a nonzero sector narrower than 180°, the two closed half-planes intersect in exactly the sector. With coincident border rays the tests accept their entire line, so a negative dot product on that line excludes points behind the origin. Each coordinate has magnitude at most 30,000. A sum or difference of two coordinate products is bounded by 2·30,000² = 1.8·10⁹ and fits a signed 32-bit integer. Points and answers stream through fixed buffers of 4096 and 8192 bytes, respectively. This removes growing input/output strings in Rust, growing output in C++, and Scanner/token conversion in Go. Time O(N), constant extra storage; no floating angles or geometric approximation. All simple sources remain; Java and Python reuse their admitted bases.

The accepted base implementations [1351_geometry.java](1351_geometry.java), [1351_geometry.py](1351_geometry.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Cross products and squares use 64-bit integers in C++, Go, Java and
  Rust, and arbitrary-precision integers in Python.
- Java reads with `StreamTokenizer`; its double values hold these
  integers exactly.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1351_geometry.cpp](1351_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 320 KB | 11285165 |
| [1351_geometry.go](1351_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1392 KB | 11285171 |
| [1351_geometry.java](1351_geometry.java) \* | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1328 KB | 11285176 |
| [1351_geometry.py](1351_geometry.py) \* | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 6832 KB | 11285173 |
| [1351_geometry.rs](1351_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1236 KB | 11285179 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1351_geometry_optimized.cpp](1351_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 76 KB | 11315502 |
| [1351_geometry_optimized.go](1351_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 904 KB | 11315507 |
| [1351_geometry_optimized.rs](1351_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 188 KB | 11315506 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
