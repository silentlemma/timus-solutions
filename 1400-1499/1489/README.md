# 1489. Points on a Parallelepiped

[Timus 1489](https://acm.timus.ru/problem.aspx?space=1&num=1489) · difficulty 384 · geometry

Original problem by Vladislav Isenbaev and Alexander Toropov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A box A × B × C (1 ≤ A, B, C ≤ 1000) is cut out as a cross-shaped net:
a column of width A at x from C to C + A holding, from the bottom up,
faces of heights B, C, B and C, and two C × B flaps on either side of
the third face. Two different points of the net, with two decimals,
are marked. Find the distance between them once the box is folded,
within 10⁻⁶.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C, then the two points as x y.

## Output

The distance.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 0.000001·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
2 2 2
3.00 3.00
5.00 5.00
```

Output:

```
1.4142135623730950
```

## Solution

Put the third face of the column on the floor: its corner (C, B + C)
goes to the origin, and a point (x, y) of it to (x − C, y − B − C, 0).
The four side faces fold up from it along shared edges, so a point keeps
its distance from that edge as its height:

- the left flap gives (0, y − B − C, C − x), the right flap
  (A, y − B − C, x − C − A);
- the face below the floor gives (x − C, 0, B + C − y), the one above it
  (x − C, B, y − 2B − C);
- the bottom face of the column folds via the face below the floor to
  become the lid: (x − C, B − y, C).

Points on a shared edge get the same position from either face. The
answer is the straight-line distance between the two positions.
Reading the coordinates in hundredths keeps the faces exact. `O(1)`.

Pitfalls:

- the distance is straight through the box, not along its surface
  (tests 01, 03);
- two different points of the net can be glued into one point of the
  box, and the answer is then 0 (tests 02, 05);
- the far ends of the column and of the flaps all become edges of the
  lid or of the side faces (tests 04, 05).

## Optimized solutions

`1489_geometry_optimized.java`. Java keeps the same integer folding of the six net faces into three-dimensional coordinates. It parses signed coordinates directly into hundredths, padding zero or one fractional digit to two, without token strings, UTF-8 conversion or Long.parseLong. Dimensions and folded coordinates are scaled by 100; the squared distance is at most 3*10^10 and is exact in long. Only the final sqrt and division by 100 use double, then direct fixed-twelve-decimal output replaces general formatting. The extra output error is well below the 1e-6 tolerance. Input uses 1024 bytes and output 64 bytes; time and auxiliary space O(1). Teaching geometry and the original fold cases are preserved.

Exact-source Java 1.8 Accepted #11327529: 0.109 s / 384 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/22, memory 1/22. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324809 was 0.125 s / 1068 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1489_geometry_optimized.java`: 0.109 s / 384 KB; retained teaching base `1489_geometry.java`: 0.125 s / 1892 KB.

The Go version reads the coordinates directly as integer hundredths and applies the same face formulas. Face selection and the squared distance stay exact. Only the square root uses floating point. The result is rounded to eight decimal places in a fixed buffer. syscall.Read and syscall.Write use standard handles, retry interrupted calls and complete partial writes.

The accepted base implementations [1489_geometry.cpp](1489_geometry.cpp), [1489_geometry.java](1489_geometry.java), [1489_geometry.py](1489_geometry.py), [1489_geometry.rs](1489_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1489_geometry_optimized.py`. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328558 (Python 3.12 x64): **0.078 s / 896 KB**. Archived comparison: `1489_geometry.py` (Python 3.12 x64) — 0.093 s / 572 KB (#11287178).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1489_geometry.cpp](1489_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 208 KB | 11287173 |
| [1489_geometry.go](1489_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1120 KB | 11287175 |
| [1489_geometry.java](1489_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1892 KB | 11287179 |
| [1489_geometry.py](1489_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 572 KB | 11287178 |
| [1489_geometry.rs](1489_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB | 11287180 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1489_geometry_optimized.go](1489_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 284 KB | 11311209 |
| [1489_geometry_optimized.java](1489_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 384 KB | 11327529 |
| [1489_geometry_optimized.py](1489_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 896 KB | 11328558 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
