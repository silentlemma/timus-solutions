# 1103. A circle through three pencils that splits the rest in half

[Timus 1103](https://acm.timus.ru/problem.aspx?space=1&num=1103) · difficulty 504 · geometry

Original problem by Katya Ovechkina, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` pencils stand at integer points (`N` odd, `3 ≤ N ≤ 5000`, coordinates
at most `10^8` in absolute value). No three of them are on a line and no
four on a circle. Pick three pencils so that the circle through them has
exactly `(N − 3) / 2` of the other pencils inside and the same number
outside. If there is no such circle, print `No solution`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines `x y`.

## Output

The coordinates of the three pencils, one pencil per line.

## Checking

Any valid circle is accepted. The checker verifies that the three points
are distinct pencils and counts the pencils inside and outside the circle
with an exact integer determinant.

## Examples

### Example 1

Input:

```
7
0 0
1 0
2 -1
2 1
1 1
0 2
-3 -1
```

Output:

```
-3 -1
2 -1
1 1
```

## Solution

A solution always exists. Take `A`, the lowest pencil (the leftmost of
the lowest), and `B`, its neighbour on the convex hull, chosen so that
every other pencil lies on the left of the line `AB`. Every circle
through `A` and `B` then cuts that half-plane the same way: a pencil `P`
is inside the circle through `A`, `B` and `C` exactly when it sees the
segment `AB` under a larger angle than `C` does. All the angles `APB` are
below 180° and, since no four pencils are concyclic, all different. Sort
the other `N − 2` pencils by this angle and take the middle one as `C`:
`(N − 3) / 2` pencils see `AB` under a larger angle and lie inside, the
same number see it under a smaller one and lie outside. `O(N log N)`.

The angle is compared without floating point. Its cotangent is
`dot / cross`, where `dot = (A − P)·(B − P)` and `cross` is twice the oriented
area of `P`, `A`, `B`, positive for every `P`. A larger angle has a
smaller cotangent, so `P` comes before `Q` when
`dot_P · cross_Q > dot_Q · cross_P`.

Pitfalls:

- the coordinates reach `10^8`, so `dot` and `cross` are bounded by
  `8 · 10^16` and `4 · 10^16`, and their products by `3.2 · 10^33`, well past 64 bits;
- comparing angles with `atan2` is risky: two distant pencils can see
  `AB` under angles that differ by less than the rounding error;
- `B` must be a hull neighbour of `A`; for an arbitrary second point the
  pencils on both sides of `AB` are not ordered by one angle.

The answers were checked with an exact in-circle determinant on every
test, including random sets of thousands of pencils over the full
coordinate range.

## Optimized solutions

`1103_geometry_optimized.java`. Keep the supporting hull edge and median-angle circle construction. Store coordinates, dot products, positive cross products and sort indices in primitive arrays. Replace allocating BigInteger products in the comparator by exact signed-product comparison: handle signs first, then compare unsigned high and low halves of each 64-by 64 product, assembling the high half from 32-bit limbs. Coordinate bounds 10^8 keep dots and crosses below 2^63, so absolute values are safe and the full products fit 128 bits. No floating-point angles or epsilon are introduced. Bottom-up primitive merge sort is O(N log N), with O(N) storage, and preserves the same median criterion; no three collinear/no four cocircular guarantee the required split.

Compared with `1103_geometry.java`: time 0.140 s → 0.078 s; memory 7336 KB → 688 KB.

Go keeps the hull edge AB and orders the other points by increasing angle, so the larger cotangent comes first. The cross products are positive. Compare the dot product signs first, treating zero as nonnegative. For equal signs, math/bits.Mul64 gives the high and low words of the exact product magnitudes. Compare the high word first and reverse the order when both signs are negative. Coordinates, dot products and cross products share one flat array. Each partition uses the median of three samples. Geometric shrinkage of the remaining interval gives O(N) work. After at most 2·bit_length(N−2) partitions the remaining interval is sorted, bounding worst-case time by O(N log N). Space is O(N). The other four families use their admitted bases.

The accepted base implementations [1103_geometry.cpp](1103_geometry.cpp), [1103_geometry.java](1103_geometry.java), [1103_geometry.py](1103_geometry.py), [1103_geometry.rs](1103_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1103_geometry_implementation_optimized.rs`. Keep one point vector: move the two chosen hull points to its front and select the angular median in the remaining slice in place. Exact i128 comparisons replace copied point/key collections. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328975 (Rust 1.75 x64): **0.015 s / 236 KB**. Archived comparison: `1103_geometry.rs` (Rust 1.75 x64) — 0.015 s / 1160 KB (#11279171).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1103_geometry_optimized.java`: time place 1/16, memory place 1/16 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 444 KB | 11279167 |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB | 11279168 |
| [1103_geometry.java](1103_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 7336 KB | 11279170 |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB | 11279169 |
| [1103_geometry.rs](1103_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB | 11279171 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1103_geometry_optimized.go](1103_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) worst case | AC | 0.015 s | 980 KB | 11328264 |
| [1103_geometry_optimized.java](1103_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.078 s | 688 KB | 11325008 |
| [1103_geometry_implementation_optimized.rs](1103_geometry_implementation_optimized.rs) | Rust 1.75 x64 | geometry, implementation | O(n) expected time; O(n) space | AC | 0.015 s | 236 KB | 11328975 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
