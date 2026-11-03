# 1333. Genie Bomber 2

[Timus 1333](https://acm.timus.ru/problem.aspx?space=1&num=1333) · difficulty 219 · geometry

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to 10 bombs fall on the unit square 0 ≤ x, y ≤ 1. Each one hits a
disc with center (x, y) and radius r, all of them between 0 and 1.
Print the share of the square that is hit by at least one bomb, in
percent, with an error of at most one percent.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines with x, y and r.

## Output

The percentage of the square that is hit.

## Checking

Return a percentage, not a fraction. The statement asks for
one-percentage-point accuracy. The repository checker uses
`|actual−expected|≤0.01·max(1,|expected|)` in percentage units; this local
rule is separate from the universal quadrature bound. Each candidate
passed 12 repository inputs and 206 extra whole-program inputs in Docker
and obtained its own exact-SHA Accepted. The independent oracle builds
adaptive lower/upper rectangle enclosures for every cross-section in a
cell, plus analytic full/half/quarter-circle cases; it does not reuse
the candidate's midpoint grid. Across this dataset the maximum deviation
from enclosure endpoints was below 0.004001 point. That is a test result,
not a universal error claim. Include empty/zero discs, clipped/nested or
identical discs, near tangency, tiny radii and both samples.

## Examples

### Example 1

Input:

```
1
0.5 0.5 0.5
```

Output:

```
78.539816
```

### Example 2

Input:

```
2
0.2 0.2 0.5
0.8 0.8 0.5
```

Output:

```
80.74292
```

## Solution

At a fixed x, a disc with center `(cx,cy)` and radius r gives the
vertical interval `cy±sqrt(r²−(x−cx)²)` when `|x−cx|<r`. Clip it to `[0,1]`.
Sort intervals by their lower ends and sweep their union, adding only
the part beyond the largest covered upper endpoint. This counts overlap,
duplicates and nested discs once; zero-radius discs contribute no area.
Let f(x) be that union length. The required percentage is `100∫₀¹ f(x)dx`.

The five simple sources use S=20000 equal strips and sample each midpoint:
`area≈Σ f((k+1/2)/S)/S`. Sorting at most N intervals gives
`O(SN log N)` time, `O(N)` auxiliary storage apart from input/output.
All five Accepted source files remain byte-exact.

A deterministic error bound replaces an empirical accuracy guess.
For one disc, its clipped interval expands by inclusion until the center
and contracts afterwards. The sum of its changes in symmetric-difference
length is at most 4r. Clipping cannot increase this quantity. Changes of
a union lie within the union of the individual changes, hence f has total
variation at most `4Σr`. On a strip of width h, the integral of the
absolute difference from its midpoint value is at most h/2 times the
variation on that strip: each left/right variation affects at most half
the strip. Summing yields `|area−midpoint|≤2Σr/S`. Since N≤10,r≤1, the
simple S=20000 version has at most 0.1 percentage point quadrature error
in real arithmetic, within the problem's one-point requirement.

## Language notes

All measurements below refer to exact Accepted sources. In the
2 November 2026 snapshot, optimized C++ is 1/1 against 69 filtered other-author
entries and Java 1/1 against 4. Python is 1/2 against 8, so its admissible
time improvement remains starred. Go and Rust have no filtered
competitors; formal coverage is not proof of competitive superiority.
The established target is top15% or the first ten places in both metrics
for C++, and first in both for the other families. All five language
positions have an admitted improvement or an existing at-goal base.

## Optimized solutions

Keep the same midpoint/interval-union algorithm, with S=4096.
The bound becomes `100·20/4096=0.48828125` percentage points, still below
one. This uniform argument covers clipping, overlaps, narrow discs and
tangencies; a good random-test result alone would not justify fewer
strips. Six-decimal percentage output adds at most 0.0000005 point of
decimal rounding. Use double precision, and compare the squared distance
before taking a square root; nonpositive radicands contribute nothing.

Square each radius once. C++/Go/Java reuse bounded interval arrays and
insertion sort, avoiding per-strip allocation/object or reflection costs:
`O(SN²)` time, O(N) storage for N≤10. Python retains sorting and has
`O(SN log N)` time, O(N) storage. These are implementation improvements
of the same algorithm, so `_optimized` is appropriate.

C++ is admitted by its 39.3% memory reduction; its 0.031→0.015 s change
is one timer tick and is not reliable speed evidence. Go saves 67.4%
time/81.2% memory, Java 50.3%/90.9%. Python saves 30.1% time (0.156→0.109 s)
but uses 11.9% MORE memory (504→564 KB); it is admitted by time only and
keeps a rating asterisk. Rust's candidate has unchanged time and only
1.5% less memory (268→264 KB), so it is not added. The original Rust
already satisfies formal coverage in an empty competitor sample.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1333_geometry.cpp](1333_geometry.cpp) | G++ 13.2 x64 | geometry | O(SN log N), S=20000 | AC | 0.031 s | 224 KB | 11285016 |
| [1333_geometry.go](1333_geometry.go) | Go 1.14 x64 | geometry | O(SN log N), S=20000 | AC | 0.046 s | 5944 KB | 11285017 |
| [1333_geometry.java](1333_geometry.java) | Java 1.8 | geometry | O(SN log N), S=20000 | AC | 0.187 s | 6560 KB | 11285019 |
| [1333_geometry.py](1333_geometry.py) | Python 3.12 x64 | geometry | O(SN log N), S=20000 | AC | 0.156 s | 504 KB | 11285018 |
| [1333_geometry.rs](1333_geometry.rs) | Rust 1.75 x64 | geometry | O(SN log N), S=20000 | AC | 0.046 s | 268 KB | 11285021 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1333_geometry_optimized.cpp](1333_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(SN^2), S=4096 | AC | 0.015 s | 136 KB | 11308499 |
| [1333_geometry_optimized.go](1333_geometry_optimized.go) | Go 1.14 x64 | geometry | O(SN^2), S=4096 | AC | 0.015 s | 1116 KB | 11308504 |
| [1333_geometry_optimized.java](1333_geometry_optimized.java) | Java 1.8 | geometry | O(SN^2), S=4096 | AC | 0.093 s | 600 KB | 11308510 |
| [1333_geometry_optimized.py](1333_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(SN log N), S=4096 | AC | 0.109 s | 564 KB | 11308516 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
