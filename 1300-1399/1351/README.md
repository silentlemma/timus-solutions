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

Integers D, X1, Y1, X2, Y2, then N and N coordinate pairs, with
1 ≤ D, N ≤ 30000 and coordinate magnitudes at most 30000. Target
points are not the origin; both border rays must be nonzero vectors.
The cached statement prints 1 ≤ absolute value for each border
coordinate, but its own example has zero components. Following that
example, these implementations allow axis-aligned nonzero rays.
The counterclockwise sector from right to left is narrower than 180°.

## Output

N lines with `YES` or `NO`.

## Checking

Token comparison (`judging: tokens`): exactly N case-sensitive `YES`
or `NO` tokens in point order. Boundary rays and the range circle
are included; whitespace separators are ignored.

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

C++, Go and Rust retain the two cross-product tests and the squared-distance test. For a nonzero sector narrower than 180°, the two closed half-planes intersect in exactly the sector. With coincident border rays the tests accept their entire line, so a negative dot product on that line excludes points behind the origin. Each coordinate has magnitude at most 30,000. A sum or difference of two coordinate products is bounded by 2·30,000² = 1.8·10⁹ and fits a signed 32-bit integer. Points and answers stream through fixed buffers of 4096 and 8192 bytes, respectively. This removes growing input/output strings in Rust, growing output in C++, and Scanner/token conversion in Go. Time O(N), constant extra storage; no floating angles or geometric approximation. All simple sources remain; Java reuses its admitted base; Python uses its separate streaming variant.

Java reuses its base: both required ranks, time 8/17 and memory 5/17,
pass top ten. Python uses [1351_geometry_optimized.py](1351_geometry_optimized.py),
Accepted #11328774 `0.093 s / 1172 KB`, not the 6832 KB teaching base.
Five exact CPython rivals select the third reference with limits
`0.109 s / 5170.40 KB`; both metrics are required at 1172 KB and pass.
The base fails memory. See the shared [criteria](../../RATING_CRITERIA.md);
meaningful simple files remain, without identical optimized copies.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1351_geometry_optimized.py`. Stream point coordinates through a bounded token reader and write answers in chunks of at most 1024 lines. The geometric tests are unchanged; points and all answers are no longer stored together. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328774 (Python 3.12 x64): **0.093 s / 1172 KB**. Archived comparison: `1351_geometry.py` (Python 3.12 x64) — 0.093 s / 6832 KB (#11285173).

## Language notes

The O(N) geometric pass does not mean constant space for all simple
files. C++/Java retain O(N) output; Go streams answers with O(B) storage.
Python retains input/tokens/integers and output: O(I+N+B), with I input
bytes. Simple Rust retains a full input String and output String:
O(I+N+B). B denotes bounded parser/I/O buffers; C++/Java use O(N+B).
Fast C++/Go/Rust stream through fixed buffers, O(B). Fast Python uses
bounded input blocks and 1024-answer batches, plus any partial token.
Including byte input, total time is O(I+N); geometric state is O(1).

These notes describe the simple implementations.

- Cross products and squares use 64-bit integers in C++, Go, Java and
  Rust, and arbitrary-precision integers in Python.
- Java reads with `StreamTokenizer`; its double values hold these
  integers exactly.

Only lint-required constants in `1351_geometry_optimized.py` were given names; their values, algorithm and comments are unchanged. Accepted #11328774 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1351_geometry.cpp](1351_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 320 KB | 11285165 |
| [1351_geometry.go](1351_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1392 KB | 11285171 |
| [1351_geometry.java](1351_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.14 s | 1328 KB | 11285176 |
| [1351_geometry.py](1351_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 6832 KB | 11285173 |
| [1351_geometry.rs](1351_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1236 KB | 11285179 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1351_geometry_optimized.cpp](1351_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 76 KB | 11315502 |
| [1351_geometry_optimized.go](1351_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 904 KB | 11315507 |
| [1351_geometry_optimized.rs](1351_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 188 KB | 11315506 |
| [1351_geometry_optimized.py](1351_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 1280 KB | 11331087 |
