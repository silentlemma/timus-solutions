# 1984. An enclosing circle touched by every unit disk

[Timus 1984](https://acm.timus.ru/problem.aspx?space=1&num=1984) · difficulty 214 · geometry

Folklore problem, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place `n` disks of radius 1 inside a circle, with disjoint interiors, so
that every disk touches the enclosing boundary internally. Find the
smallest possible enclosing radius. The input is an integer with
`1≤n≤10`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One integer `n`.

## Output

The minimum radius, as a real number.

## Checking

Compare numerical output with the stated tolerance, including the rounding bounds proved below.

- `1984_geometry_optimized.cpp` (G++ 13.2 x64): 16 repository cases.

- `1984_geometry_optimized.py` (PyPy 3.10 x64): 16 repository cases; 10 additional source-bound comparisons.

## Examples

Input:

```
2
```

Output:

```
2
```

## Solution

With one disk the answer is 1. For `n≥2`, write the outer radius as `R`
and let `r=R−1>0`. Internal tangency forces every disk center to lie on
the circle of radius `r` around the enclosing center. Distinct disk
centers must be at least distance 2 apart.

Sort the centers by polar angle. The `n` cyclic angular gaps sum to
`2π`, so one gap `α` is at most `2π/n≤π`. That pair has distance `2r
sin(α/2)≤2r sin(π/n)`. Non-overlap requires this distance to be at least
2; therefore `R≥1+1/sin(π/n)`.

This lower bound is attainable: put the centers at the vertices of a
regular `n`-gon on the circle with radius `1/sin(π/n)`. Adjacent centers
are exactly distance 2 apart, and every other pair is at least that far
apart. Each unit disk reaches outer radius `R=r+1`, so all required
internal tangencies hold. Thus the minimum is `1+1/sin(π/n)` for `n≥2`.

For the example `n=2`, the centers are opposite on a radius-1 circle.
Two unit disks fit inside a radius-2 circle and touch each other, giving
output 2.

The formula uses a constant number of operations: `O(1)` time and `O(1)`
memory. Double precision and ten digits after the decimal point are
sufficient for the required tolerance over this input range.

Pitfalls:

- Every disk must touch the outer boundary; unrestricted disk packing is
  a different optimization problem.
- The centers lie at radius `R−1`, not at radius `R`.
- Handle one disk geometrically before evaluating the formula, which
  would divide by `sin(π)`.
- The angle is `π/n` in radians.
- Interior overlap is forbidden, but tangency between small disks is allowed.

## Optimized solutions

`1984_geometry_optimized.java`. Keep radius 1 for N=1 and 1+1/sin(π/N) otherwise, using the same Math.sin. Parse the bounded integer directly and print the round-trip double representation instead of initializing Formatter/Locale. This avoids decimal-format machinery without changing the geometry or replacing library sine by an approximation. O(1) numeric work/state; retain the simple formula source.

Exact-source Java 1.8 Accepted #11326960: 0.078 s / 460 KB. Saved current-Java comparison, 2026-11-20: time rank 1/53, memory rank 2/53. With memory below 1024 KB, strict admission uses time only.

- `1984_geometry_optimized.java`: 0.078 s / 460 KB; retained teaching base `1984_geometry.java`: 0.125 s / 1796 KB; time change -37.6%; memory change -74.4%.

The computed radius is 1 for N=1, otherwise 1 + 1/sin(pi/N). C++/Java reduce standard input/output overhead while retaining the library formula. Python evaluates the sine polynomial through x^13 in Horner form, using six fixed factorial-ratio denominators, not an answer table. For 2 <= N <= 10, 0 < x<=pi/2 and the next alternating term x^15/15! is below 7e-10; sin(pi/N)>=sin(pi/10)>0.3, so radius error is below 10^-8. Six-decimal integer output adds at most half a micro-unit, remaining within 10^-6 absolute tolerance. All ten legal N were checked against an independent library-sine oracle. Fixed bounds give O(1) time and storage; the N = 1 exception remains explicit.

- `1984_geometry_optimized.cpp`: 0.015 s / 120 KB; base `1984_geometry.cpp`: 0.015 s / 444 KB; relative change: time -0.0%, memory -73.0%.

- `1984_geometry_optimized.py`: 0.109 s / 276 KB; base `1984_geometry.py`: 0.078 s / 396 KB; relative change: time +39.7%, memory -30.3%.

`1984_geometry_optimized.rs`. Retain the circle-packing radius formula: one circle needs radius 1; otherwise use 1+1/sin(PI/N). Compute in f64 and print ten fractional digits directly, with constant numeric state. Time and auxiliary space are O(1). Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1984_geometry.rs`: time 0.015 s → 0.031 s; memory 256 KB → 88 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1984_geometry_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1984_geometry.cpp](1984_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB | 11292346 |
| [1984_geometry.go](1984_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1100 KB | 11292347 |
| [1984_geometry.java](1984_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1796 KB | 11309215 |
| [1984_geometry.py](1984_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 396 KB | 11292348 |
| [1984_geometry.rs](1984_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB | 11292350 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1984_geometry_optimized.cpp](1984_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 120 KB | 11308253 |
| [1984_geometry_optimized.java](1984_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.078 s | 460 KB | 11326960 |
| [1984_geometry_optimized.py](1984_geometry_optimized.py) | PyPy 3.10 x64 | geometry | O(1) | AC | 0.109 s | 276 KB | 11309752 |
| [1984_geometry_optimized.rs](1984_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 88 KB | 11325118 |
