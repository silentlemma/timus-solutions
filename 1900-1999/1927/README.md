# 1927. Area of Two Infinite Strips

[Timus 1927](https://acm.timus.ru/problem.aspx?space=1&num=1927) · difficulty 1060 · geometry

Original problem from Ural Regional School Programming Contest 2012 | by Artyom Averin.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of two nonzero segments is a perpendicular cross-section of a full
infinite strip. The strip consists of all lines perpendicular to the segment
through its points, extending infinitely in both directions. Find the area
common to both strips. Report −1 when that area is infinite.
Limits: 1 second, 64 MB.

## Input

Two lines, each containing endpoint coordinates x1 y1 x2 y2 of one segment.
All coordinates are integers in [−1000,1000]; endpoints of each segment differ.
The order of the endpoints is arbitrary.

## Output

One real area, or −1 for infinite area. Disjoint strips and strips that only
touch along a line have area zero, even though the touching line is unbounded.

## Checking

One numeric token; absolute OR relative error at most 10^−6.

## Examples

```
0 0 2 0
0 0 0 2
```

```
4
```

## Solution

Write the endpoints as A,B and C,D, with normal vectors v=B−A and w=D−C.
The first strip is the set of points X with v·X between v·A and v·B;
the second has the analogous bounds w·C,w·D. Sort bounds when necessary.

Calculate the integer determinant Δ=vx wy−vy wx. If Δ is nonzero, the
invertible linear map X↦(v·X,w·X) transforms the intersection into a
rectangle. Its side lengths are v·(B−A)=|v|² and w·(D−C)=|w|².
The map multiplies areas by |Δ|, giving area=|v|²|w|²/|Δ|.
This proves the finite formula; translations do not change its value.

If Δ=0, use the common normal v for both segments. Form sorted intervals
from v·A,v·B and v·C,v·D. Let L be the larger lower bound and R the smaller
upper bound. When L<R, positive common width extends infinitely along
the strip, so the area is infinite. When L>R there is no intersection;
when L=R the intersection is a line. Both latter cases have zero area.
These cases exhaust all possibilities, proving the algorithm.

O(1) time and O(1) space, since the input always contains eight integers.

These are entire strips, not rays or half-strips. Detect parallelism exactly,
without an epsilon: determinant ±1 can give a huge but finite area.
Do not report infinity merely because a line of contact is unbounded.
Use the SAME projection vector for parallel intervals, including reversed
endpoints. Square lengths directly; no square roots or trigonometry are needed.
Oblique segments need not be parallel: tests 07 and 08 have perpendicular
cross-sections and positive finite areas. In test 08, the segments do not
intersect, but the full strips do.

## Language notes

Use signed 64-bit integers before multiplying in C++, Go, Java and Rust.
Vector components are at most 2000 in magnitude; each squared norm is at
most 8,000,000 and their product at most 64,000,000,000,000. This is below
2^46 and exactly representable in double precision. The absolute determinant
is at most 8,000,000; a nonzero one is at least 1. Exact predicates followed
by a single floating division and ten fractional digits meet the tolerance.
Python uses exact integers before division. Java prints with Locale.US.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1927_geometry.cpp](1927_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB |
| [1927_geometry.go](1927_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1927_geometry.java](1927_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1796 KB |
| [1927_geometry.py](1927_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 544 KB |
| [1927_geometry.rs](1927_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB |
