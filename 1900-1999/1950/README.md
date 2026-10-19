# 1950. Area Crossed by a Finite Channel

[Timus 1950](https://acm.timus.ru/problem.aspx?space=1&num=1950) · difficulty 2085 · geometry

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Start with triangle A=(0,0), B=(10,0), C=(10,10) and the finite channel
segment AF, where F=(x,y) is strictly inside. Cut the triangle by its
altitude to the hypotenuse into two congruent right isosceles triangles.
Leave the child not containing F as a final plot and repeat in the child
containing F. If F lies on the new altitude, stop and leave both children
as final plots. Otherwise the process may continue to arbitrarily small sizes.

A final plot is usable exactly when its boundary has two distinct points
in common with AF. Sum the usable areas, approximating an indefinitely small
remaining plot if necessary. Limits: 1 second, 64 MB.

## Input

Two decimal real coordinates x,y with at most three fractional digits,
0<y<x<10. These inequalities are strict.

## Output

One total area, with absolute or relative error at most 10⁻³.

## Checking

The answer is compared with absolute or relative error 10⁻³.

## Examples

```
8.125 4.375
```

```
29.6875
```

## Solution

Represent a current triangle by right-angle vertex R and hypotenuse endpoints
P,Q. Initially R=B, P=A, Q=C, area=50. The altitude ends at H=(P+Q)/2.
Every edge and cut is horizontal, vertical or has slope ±1, while AF has
slope strictly between 0 and 1. Thus the channel never lies along an edge.
A discarded child contains neither endpoint of AF in its interior, so
crossing its interior means exactly two boundary intersections. Touching
only a vertex does not qualify.

Let n=(sign(H_y−R_y),−sign(H_x−R_x)), a normal to RH, and define
v(T)=n·(T−R), w(T)=x·T_y−y·T_x. The discarded half is usable precisely when
w(R),w(H) have strict opposite signs, and either v(A),v(F) have opposite
signs or v(F)=0. The first condition puts the crossing inside cut segment
RH, excluding its endpoints. The second puts it on finite AF, allowing F;
using the infinite ray would incorrectly include plots beyond F.

Add half the current area when those tests hold. If v(F)=0, stop. F was
inside the parent, so it is inside the cut segment, one new child contains
the incoming channel and the other only touches F; exactly one half counts.
Otherwise, compare v(F) with v(P). Equal signs retain triangle (H,P,R),
opposite signs retain (H,R,Q), with the first listed vertex the new right
angle. Halve the current area and repeat.

Correctness follows by induction. A convex current triangle contains the
final part of AF ending at F. Its discarded child contains channel interior
exactly when this part crosses the cut internally, which the two sign tests
express. Only that discarded child becomes final at this iteration; the
retained child's contributions are handled later. The exact-stop rule
handles both final children, so every usable plot is counted once.

Parse coordinates into integer thousandths fx,fy. Multiply every geometric
coordinate by S=2³⁰. Start with R=(10000S,0), P=(0,0), Q=(10000S,10000S),
F=(fxS,fyS), and perform at most 30 cuts. After d midpoint operations,
vertex coordinates remain multiples of 10000·2^(30−d), so all midpoint and
side calculations are exact integers. For w, use raw fx,fy, not scaled F.

Native coordinates are at most 10737418240000; normal components are −1,0,1.
The ray-side expressions have absolute value below 2.15·10¹⁷, safely within
signed 64 bits. Compare signs directly; multiplying two side values or
using a general cross product of scaled coordinates could overflow.

Partial areas are exact binary fractions. The unresolved area after 30 cuts
is at most 50/2³⁰≈4.657·10⁻⁸, bounding all omitted usable plots. Ten output
decimal places add at most 5·10⁻¹¹ error. Time and space are O(1) for 30 cuts;
parameterized by target precision ε, time is O(log(1/ε)) and space O(1).

The channel is a segment, not an infinite line. A cut-endpoint touch gives
no usable discarded area; F on the cut does count as a boundary endpoint.
Keep the new right angle at H. Do not use epsilon tests for exact sides,
multiply sign values, or claim the truncated infinite process is exact.

## Language notes

C++, Go, Java and Rust use signed 64-bit point coordinates and products;
Python uses integers. Only area accumulation and printing use floating point.
Decimal parsing pads the fractional part to three digits, avoiding binary
input-rounding decisions. Use a 64-bit left operand for the grid shift.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1950_geometry.cpp](1950_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 432 KB |
| [1950_geometry.go](1950_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1164 KB |
| [1950_geometry.java](1950_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1080 KB |
| [1950_geometry.py](1950_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 728 KB |
| [1950_geometry.rs](1950_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 268 KB |
