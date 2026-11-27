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

Compare angles without floating point. For P, let
dot=(A-P)·(B-P) and cross=cross(P,A,B)>0. Their ratio is cot(angle APB).
On (0,180 degrees) cotangent decreases strictly. We order angles
increasingly, hence cotangents decreasingly: P precedes Q exactly when
dot_P*cross_Q > dot_Q*cross_P. The inequality is unchanged and correct;
reversing the whole order would also leave the same median.

The C++ source selects the median with std::nth_element rather than
sorting all points. Its table gives a conservative O(N log N) worst-case
bound for the pinned GCC 13.2 implementation: a logarithmic partition-depth
limit switches to heap selection. An unconditional worst-case O(N) claim
would be unjustified. All implementations retain O(N) point/key storage,
plus retained input and sorting/selection workspace where used.

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

Optimized Go keeps the supporting hull edge and increasing-angle order.
Positive cross products let it compare dot signs first (zero is nonnegative),
then exact magnitudes via math/bits.Mul64 high/low words, reversing the
comparison when both products are negative. Points and keys share one array.
The deterministic pivot is median-of-three: fixed-factor interval shrinkage
would give linear total partition work, but is not guaranteed. The explicit
2*bit_length(N-2) partition limit gives O(N log N) worst-case partition
work; sorting the remaining interval also costs at most O(N log N).
Space is O(N). This bound does not assume random pivots or geometric shrinkage.

The cached audit confirms C++ base by time rank only below 1 MiB and
Python base by both exact-compiler small-cohort reference metrics. Simple
Java/Rust do not qualify; separate optimized Java passes time rank, and
optimized Rust below 1 MiB passes its time reference. Optimized Go still
fails its time target and retains the marker. Shared
[rating criteria](../../RATING_CRITERIA.md) apply, with teaching versions
preserved and no identical copies or separate first-place language target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1103_geometry_implementation_optimized.rs`. Keep one point vector: move the two chosen hull points to its front and select the angular median in the remaining slice in place. Exact i128 comparisons replace copied point/key collections. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328975 (Rust 1.75 x64): **0.015 s / 236 KB**. Archived comparison: `1103_geometry.rs` (Rust 1.75 x64) — 0.015 s / 1160 KB (#11279171).

The current 1103_geometry_implementation_optimized.rs revision only names
the unchanged 32-byte inline token capacity. Accepted #11328975
(0.015 s / 236 KB) belongs to the preceding revision.

## Language notes

Teaching C++/Rust compare products in 128-bit integers and select with
nth_element/select_nth_unstable_by. Teaching Go/Java sort using arbitrary-
precision products; Python also uses exact unbounded integers. Distinct
optimized Go/Java instead compare exact two-word product magnitudes.
These implementation notes apply to the named versions, not every source.

The 18 November 2026 notes describe a historical snapshot. Current
comparisons discard rival times below 0.015 s before cohort selection,
while our own smaller times are floored only for comparison. Paired
Accepted measurements remain raw. Use the shared current policy.

`1103_geometry_optimized.java`: time place 1/16, memory place 1/16 in this comparable sample.

Current admission uses the shared [rating criteria](../../RATING_CRITERIA.md):
ordinary top-ten/top-15% comparisons or the exact-compiler small-cohort
reference when applicable, with time only below 1 MiB. A 30% gain and a
separate first-place language target are not admission criteria. Keep
meaningful teaching versions without optimization-target stars.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) worst case (GCC 13.2) | AC | 0.015 s | 444 KB | 11279167 |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB | 11279168 |
| [1103_geometry.java](1103_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.14 s | 7336 KB | 11279170 |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB | 11279169 |
| [1103_geometry.rs](1103_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB | 11279171 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1103_geometry_optimized.go](1103_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) worst case | AC | 0.015 s | 980 KB | 11328264 |
| [1103_geometry_optimized.java](1103_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.078 s | 688 KB | 11325008 |
| [1103_geometry_implementation_optimized.rs](1103_geometry_implementation_optimized.rs) | Rust 1.75 x64 | geometry, implementation | O(n) expected time; O(n) space | AC | 0.015 s | 224 KB | 11331130 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
