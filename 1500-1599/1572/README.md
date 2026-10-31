# 1572. Yekaterinozavodsk Great Well

[Timus 1572](https://acm.timus.ru/problem.aspx?space=1&num=1572) · difficulty 146 · geometry

Original problem by Alexander Ipatov and Alex Samsonov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The opening of a well and up to 100 manhole covers are each a circle
(type 1, size = radius), a square (type 2) or an equilateral triangle
(type 3, size = side), with integer sizes 1 … 100. A flat cover may be
turned and moved in space in any way. Count the covers that can be
dropped into the well.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The type and size of the well, then N (1 ≤ N ≤ 100) and the type and
size of each cover.

## Output

The number of covers that fit through.

## Examples

### Example 1

Input:

```
2 10
3
3 20
1 5
2 11
```

Output:

```
2
```

### Example 2

Input:

```
1 5
2
2 10
1 6
```

Output:

```
1
```

## Solution

A cover held upright and pushed straight down meets the plane of the
opening along parallel chords of itself, so it passes when, in some
direction, its longest chord fits into the opening. The cover's best
direction gives a circle's diameter 2r, a square's side a and a
triangle's height a·√3/2 (the chords parallel to a height). The opening
holds segments up to its longest one: a circle's diameter 2R, a
square's diagonal A·√2 and a triangle's side A.

Squared and multiplied by 4, all these lengths are integers: 16r², 4a²
and 3a² for the covers, 16R², 8A² and 4A² for the well, so the
comparison is exact and a cover that just touches still passes. `O(N)`.
The answers agree with an independent program for every pair of a well
and a cover of any shape and size.

Pitfalls:

- the size of a circle is its radius, not its diameter;
- a triangle passes by its height, not by its side, so a triangle of
  side 16 still goes into a square well of side 10 (test 06);
- equal sizes pass: a square of side 10 goes through a circle of
  radius 5 (the second example), so floating-point comparisons need care.

## Optimized solutions

The optimized Java solution parses the numbers by hand from a 4 KB
buffer filled from `System.in` instead of creating a `Scanner`, so the
JVM does not load the scanner and its regular expressions; the
comparison of the squared lengths is the same:
{1572_geometry_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1572_geometry_optimized.java`: time reduction +44.29%; memory
  reduction +80.86%; base: `1572_geometry.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1572_geometry.cpp](1572_geometry.cpp).
- [1572_geometry.go](1572_geometry.go).
- [1572_geometry.rs](1572_geometry.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry.cpp](1572_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 128 KB | 11287799 |
| [1572_geometry.go](1572_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1072 KB | 11287801 |
| [1572_geometry.java](1572_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1776 KB | 11287805 |
| [1572_geometry.py](1572_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 384 KB | 11287803 |
| [1572_geometry.rs](1572_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 228 KB | 11287810 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry_optimized.java](1572_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.078 s | 340 KB | 11304529 |
