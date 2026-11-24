# 1942. The Nearest Shift for the Largest Lattice Class

[Timus 1942](https://acm.timus.ru/problem.aspx?space=1&num=1942) · difficulty 646 · geometry

Original problem from Open Ural FU Personal Contest 2012 | by Vitaliy Belokobilskiy, Sergey Madzhuga.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n points in a Cartesian plane, translate the coordinate origin once,
without rotating either axis. A point is counted when both coordinates
relative to the new origin are integers. Maximize the number counted;
among shifts achieving that maximum, minimize Euclidean shift length.
Coincident points are distinct and each contributes one.
Limits: 1 second, 64 MB.

## Input

n, where 1≤n≤50000, followed by n pairs of real coordinates. Each has
absolute value at most 100 and at most three digits after the decimal
point. Signs and shorter fractional parts are allowed.

## Output

The maximum count as an integer, followed by the minimum distance.
The distance must have absolute error at most 10⁻⁵.

## Checking

A checker verifies the number of points exactly and the shift length
with absolute error 10⁻⁵.

## Examples

```
3
0.500 0.200
0.500 0.500
-0.500 0.200
```

```
2 0.53852
```

```
2
1.000 1.000
1.000 1.000
```

```
2 0.00000
```

## Solution

Let S=1000. Skip each coordinate's integer part and parse only its signed
fractional part into integer thousandths X,Y, padding with zeros. This
preserves its residue and avoids converting arbitrarily many leading zeros;
do not multiply a binary floating value and truncate.
Two points can be made integral together exactly when both coordinate
differences are integers. Hence their scaled coordinates must have the
same normalized residues rx=X mod S and ry=Y mod S in 0..999.

Count each residue pair in an array of S² cells, indexed rx·S+ry. Every
possible useful shift belongs to one of these classes, and makes exactly
that class integral. Thus the largest frequency is the maximum count.

For a class, possible new origins are (rx/S+i,ry/S+j), i,j integers.
Minimize each squared coordinate independently: choose its nearest integer
translate. The component magnitudes in thousandths are dx=min(rx,S−rx)
and dy=min(ry,S−ry). Define q=dx²+dy². Among classes of maximum frequency,
choose minimum q; only then compute sqrt(q)/S.

Counts increase monotonically as points are read. After incrementing a
class, compare its (count,q) with the current best: larger count wins,
then smaller q. Every newly eligible tied class is compared, so induction
preserves the best among all processed points. The class argument proves
the final count optimal; the independent nearest-coordinate choices prove
the final distance minimal. A half-integer may have two nearest translates,
but both give the same squared distance.

O(S²+L) time, with S=1000 and L the input length, and O(S²) auxiliary
frequency storage. Including retained points, input and tokens, total space
is O(S²+L). For bounded token lengths this becomes O(S²+n).
Counts≤50000, signed fractional thousandths are within ±999, and
q≤500000; signed 32-bit integers suffice. The table occupies about 4 MB.

Do not rotate, merge coincident input records, use absolute fractional
parts of negative values, or choose the closest class before maximizing
its count. Integer parts do not affect the class. A residue near 1 is
close to a negative translation, not nearly one unit from the origin.
No epsilon is needed for grouping or comparing squared distances.
Test 34 contains a zero written with 4301 digits: leading zeros are valid,
but converting the whole token with Python's default int limit fails.
Strip leading zeros before converting n as well.
Test 35 uses n=0008: n must be read in decimal, not inferred as octal.

## Language notes

Normalize negative remainders explicitly in C++, Go and Java; Python's
positive-modulus remainder and Rust rem_euclid already do this. All
parsers preserve coordinate residues exactly, including negative fractions
whose integer part is zero. Python and Go use packed signed 32-bit counts.
Java fixes the output locale. Each program prints nine fractional digits,
introducing at most 5·10⁻¹⁰ rounding error. Only the final square root uses
floating point; group membership and tie comparisons are exact.

## Optimized solutions

The C++ version packs each pair of residues into one integer. It sorts these keys and counts equal runs, comparing squared distances to break ties. Only the final distance uses a square root. Time is O(L + N log N) for input length L and N points, with O(N) extra space. The metrics come from submission 11316985.

Java 1.8 also packs each pair into an integer and counts runs after sorting. Submission 11317110 took 0.109 s and 804 KB; the base took 0.125 s and 6036 KB.

Python 3.12 x64 also packs each pair into an integer and counts runs after sorting. Submission 11317108 took 0.203 s and 3384 KB; the base took 0.281 s and 11584 KB.

Rust 1.75 x64 also packs each pair into an integer and counts runs after sorting. Submission 11317104 took 0.015 s and 412 KB; the base took 0.031 s and 6016 KB.

Go 1.14 x64 also packs each pair into an integer and counts runs after sorting. Submission 11317099 took 0.031 s and 1260 KB; the base took 0.078 s and 8908 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322162 · Go 1.14 x64 №11322163 · Java 1.8 №11322164 · Python 3.12 x64 №11322165 · Rust 1.75 x64 №11322166.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1942_geometry.cpp](1942_geometry.cpp) | G++ 13.2 x64 | geometry | O(S^2+L) | AC | 0.031 s | 4788 KB | 11322162 |
| [1942_geometry.go](1942_geometry.go) | Go 1.14 x64 | geometry | O(S^2+L) | AC | 0.078 s | 8908 KB | 11322163 |
| [1942_geometry.java](1942_geometry.java) | Java 1.8 | geometry | O(S^2+L) | AC | 0.125 s | 6036 KB | 11322164 |
| [1942_geometry.py](1942_geometry.py) | Python 3.12 x64 | geometry | O(S^2+L) | AC | 0.281 s | 11584 KB | 11322165 |
| [1942_geometry.rs](1942_geometry.rs) | Rust 1.75 x64 | geometry | O(S^2+L) | AC | 0.031 s | 6016 KB | 11322166 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1942_geometry_optimized.cpp](1942_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(L + N log N) | AC | 0.015 s | 344 KB | 11316985 |
| [1942_geometry_optimized.go](1942_geometry_optimized.go) | Go 1.14 x64 | geometry | O(L + N log N) | AC | 0.031 s | 1260 KB | 11317099 |
| [1942_geometry_optimized.rs](1942_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(L + N log N) | AC | 0.015 s | 412 KB | 11317104 |
| [1942_geometry_optimized.py](1942_geometry_optimized.py) | Python 3.12 x64 | geometry | O(L + N log N) | AC | 0.203 s | 3384 KB | 11317108 |
| [1942_geometry_optimized.java](1942_geometry_optimized.java) | Java 1.8 | geometry | O(L + N log N) | AC | 0.109 s | 804 KB | 11317110 |
