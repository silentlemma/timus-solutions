# 1874. Football Goal

[Timus 1874](https://acm.timus.ru/problem.aspx?space=1&num=1874) · difficulty 199 · geometry

Original problem by Fedor Fominykh, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goal is built from a vertical birch, the ground and two sticks of
lengths a and b: the birch is one post, and the sticks make the other
post and the crossbar. The goal may be any quadrilateral. Find its
largest area. The birch is taller than a + b.

## Input

a and b (1 ≤ a, b ≤ 10 000).

## Output

The largest area, with at least six digits after the decimal point.

## Checking

Compare numerical output with the stated tolerance, including the rounding bounds proved below.

- `1874_geometry_optimized.go` (Go 1.14 x64): 13 repository cases; 13 additional source-bound comparisons.

- `1874_geometry_optimized.java` (Java 1.8). 13 repository cases and 30 additional cases ran in separate Java processes. Another 40,292 calls checked the six decimal places and compared the area against a high-precision reference, including fragmented input.

- `1874_geometry_optimized.py` (PyPy 3.10 x64): 13 repository cases; 204 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
2 2
```

Output:

```
4.828427125
```

## Solution

The quadrilateral has a right angle where the birch meets the ground.
Its diagonal c from the top of the birch side to the far end on the
ground splits it in two. One part is a right triangle with hypotenuse
c, whose area is at most c²/4, reached when its legs are equal. The
other part is the triangle of the two sticks with angle t between
them. Then c² = a² + b² − 2ab·cos t, and the total is
(a² + b² − 2ab·cos t)/4 + ab·sin t/2. Its derivative vanishes when
sin t + cos t = 0, so t = 135°, and the area is
(a² + b² + 2√2·ab)/4. `O(1)`.

For a = b = 2 this gives (4 + 4 + 8√2)/4 = 2 + 2√2 ≈ 4.828427125.

Pitfalls:

- the goal need not be a rectangle; the right angle at the foot of the
  birch is the only fixed part;
- the angle between the sticks is 135°, not 90°: a right angle there
  gives only (a + b)²/4;
- the birch is tall enough by the statement, so its height never
  limits the answer.

The formula agrees with a direct search over the angle between the
sticks, and with an independent accepted implementation on all tests.

## Optimized solutions

Keep the same geometric optimum (a*a+b*b+2*sqrt(2)*a*b)/4 and the readable sources. Java reads both positive integers in blocks, then reuses the 32-byte input buffer for six-decimal output. It computes the square term exactly in millionths and rounds the scaled cross term once. The absolute error is below 0.000000522 throughout the allowed range. Go and Python compute the formula at runtime, then round once to six decimals using an integer scaled by 10^6; there is no answer table. For a,b<=10000 the scaled result is below 2^47, so floating-point roundoff plus at most half a micro-unit of decimal rounding stays below 10^-6 absolute error. Emit the fractional part with six positions including leading zeros. Only input/output and representation change; time and space remain O(1).

- `1874_geometry_optimized.go`: 0.031 s / 304 KB; base `1874_geometry.go`: 0.031 s / 1136 KB; relative change: time -0.0%, memory -73.2%.
- `1874_geometry_optimized.java`. The simple Java run #11290975 used 0.140 s and 1832 KB. The earlier optimized run #11308337 used 0.109 s and 544 KB. The new run #11328166 used 0.093 s and 344 KB.
- `1874_geometry_optimized.py`: 0.140 s / 316 KB; base `1874_geometry.py`: 0.078 s / 452 KB; relative change: time +79.5%, memory -30.1%.

`1874_geometry_optimized.rs`. Keep the same closed-form area calculation in f64 and print nine fractional digits directly with printf. The optimization changes input/output representation, not the geometric formula or its precision class. Time and auxiliary space remain O(1). Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1874_geometry.rs`: time 0.031 s → 0.046 s; memory 236 KB → 112 KB.

## Language notes

The Java 1.8 snapshot of 1 November 2026 places this run 2/61 by time and 1/61 by memory. With less than 1 MiB, the time rank qualifies it under the strict rule.

The Rust results are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1874_geometry_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1874_geometry.cpp](1874_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 132 KB | 11309209 |
| [1874_geometry.go](1874_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB | 11290968 |
| [1874_geometry.java](1874_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1832 KB | 11290975 |
| [1874_geometry.py](1874_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 452 KB | 11290970 |
| [1874_geometry.rs](1874_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 236 KB | 11309210 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1874_geometry_optimized.go](1874_geometry_optimized.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 304 KB | 11309758 |
| [1874_geometry_optimized.java](1874_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.093 s | 344 KB | 11328166 |
| [1874_geometry_optimized.py](1874_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(1) | AC | 0.140 s | 316 KB | 11309748 |
| [1874_geometry_optimized.rs](1874_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 112 KB | 11325114 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
