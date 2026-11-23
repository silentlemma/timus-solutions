# 1185. The shortest wall that keeps a set distance from a polygonal castle

[Timus 1185](https://acm.timus.ru/problem.aspx?space=1&num=1185) · difficulty 301 · geometry

Original problem by Sergey Volchenkov and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A castle is a simple polygon with `3 ≤ N ≤ 1000` integer vertices given
clockwise. Find the length of the shortest closed wall around it that
never comes closer than `L` feet to the castle, rounded to a whole number
of feet.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `L`, then the vertices.

## Output

The length in feet, accurate to 8 inches.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
9 100
200 400
300 400
300 300
400 300
400 400
500 400
500 200
350 200
200 200
```

Output:

```
1628
```

## Solution

The shortest wall is convex, so it encloses the castle's convex hull,
and is the set of points at distance exactly `L` from the
hull. Along each hull side it runs parallel at distance `L`, adding the
side length. At each hull vertex it turns along a circular arc of radius
`L` by the exterior angle there, and the exterior angles of a convex
polygon add up to a full turn. So the length is the hull perimeter plus
`2πL`.

The hull comes from Andrew's monotone chain: sort the points, build the
lower and the upper chains, and drop points that do not turn left,
including collinear ones. Rounding to the nearest foot leaves an error of
at most 6 inches. `O(N log N)`.

Pitfalls:

- the castle need not be convex, so its own perimeter is too long; dents
  are bridged by hull sides, as in the example;
- vertices in the middle of a straight side must not break the hull,
  hence dropping collinear points;
- the answer is rounded, not truncated.

The answers were compared with a separately written solution on 200
random castles and on every test.

## Optimized solutions

`1185_geometry_optimized.java`. Keep the monotone-chain convex hull and its perimeter plus 2πL, rounded once at the end. Pack each integer point in one long: signed x occupies the high 32 bits, while flipping the sign bit of y preserves its signed order in the low half. Primitive sorting then gives the same lexicographic order. Store the hull as indices in one int array instead of coordinate objects and temporary lists. Cross products remain exact long values; only edge lengths use hypot. Storage O(N). With S(N) the primitive-sort cost, the hull scan costs O(N) beyond sorting; Java 8 typically takes O(N log N), with a conservative quadratic sort allowance rather than a strict worst-case guarantee.

Compared with `1185_geometry.java`: time 0.140 s → 0.109 s; memory 3144 KB → 556 KB.

The Go version shifts both coordinates by 10,000 and packs each point into one 32-bit integer, with x in the high bits. Sorting those integers gives lexicographic order. Scan the order in both directions and reuse one stack for the two monotone chains. The perimeter still includes the offset term 2πL.

The accepted base implementations [1185_geometry.cpp](1185_geometry.cpp), [1185_geometry.java](1185_geometry.java), [1185_geometry.py](1185_geometry.py), [1185_geometry.rs](1185_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1185_geometry_parsing_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11328893 (Go 1.14 x64): **0.015 s / 1072 KB**. Archived comparison: `1185_geometry.go` (Go 1.14 x64) — 0.031 s / 1204 KB (#11283369).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1185_geometry_implementation_parsing_optimized.rs`. Use native bounded input and complete native output writes, with binary Windows descriptors and a C entry. Numeric-only input is converted directly from bytes into signed integers without token allocation; line-sensitive input retains complete lines. Sort points with the unstable in-place sorter; equal points are interchangeable in the unchanged convex hull.

Accepted #11329170 (Rust 1.75 x64): **0.015 s / 124 KB**. Archived comparison: `1185_geometry.rs` (Rust 1.75 x64) — 0.031 s / 264 KB (#11283379).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1185_geometry_optimized.java`: time place 5/27, memory place 1/27 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB | 11283368 |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB | 11283369 |
| [1185_geometry.java](1185_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB | 11283377 |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB | 11283372 |
| [1185_geometry.rs](1185_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB | 11283379 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1185_geometry_optimized.go](1185_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 824 KB | 11310857 |
| [1185_geometry_optimized.java](1185_geometry_optimized.java) | Java 1.8 | geometry | O(N+S(N)) | AC | 0.109 s | 556 KB | 11325011 |
| [1185_geometry_parsing_optimized.go](1185_geometry_parsing_optimized.go) | Go 1.14 x64 | geometry, parsing | O(N log N) | AC | 0.015 s | 1072 KB | 11328893 |
| [1185_geometry_implementation_parsing_optimized.rs](1185_geometry_implementation_parsing_optimized.rs) | Rust 1.75 x64 | geometry, implementation, parsing | O(N log N) | AC | 0.015 s | 124 KB | 11329170 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
