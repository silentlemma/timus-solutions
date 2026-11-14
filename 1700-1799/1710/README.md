# 1710. Boris, You Are Wrong!

[Timus 1710](https://acm.timus.ru/problem.aspx?space=1&num=1710) · difficulty 649 · geometry

Original problem by Alexander Ipatov (prepared by Vladimir Yakovlev), from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Boris claims that two triangles are congruent when AB, BC and the
angle at A agree, that is two sides and the angle opposite one of
them. Given a triangle ABC, print YES if every triangle that agrees
with it in this way is congruent to it. Otherwise print NO and such a
triangle A₂B₂C₂ that is not congruent.

## Input

The points A, B and C, one per line: integer coordinates up to 100 in
absolute value, not on one line.

## Output

YES, or NO and the three points of a counterexample with the greatest
precision. Its coordinates must stay within 1000, and it must not be
degenerate. Any counterexample is accepted.

## Examples

### Example 1

Input:

```
0 0
-1 4
4 0
```

Output:

```
YES
```

### Example 2

Input:

```
0 0
4 3
6 0
```

Output:

```
NO
0.0000000000 0.0000000000
-3.0000000000 4.0000000000
0.0000000000 2.0000000000
```

## Solution

Keep A and B and the direction of the ray from A towards C. Any
agreeing triangle can be moved to this position, with C₂ on that ray
at the distance |BC| from B. A point at distance t along the ray is
there when t² − 2t·(AB·u) + |AB|² − |BC|² = 0, with u the unit vector
along AC. One root is |AC|. The other is t′ = 2(AB·AC)/|AC| − |AC|,
since the roots add up to 2(AB·u).

A different triangle exists exactly when t′ > 0 and t′ ≠ |AC|. In
integers, 2(AB·AC) > |AC|² and AB·AC ≠ |AC|². Then
C₂ = A + (C − A)·(2(AB·AC) − |AC|²)/|AC|². It lies on the ray at less
than 2|AB| from A, well within 1000, and the triangle ABC₂ has the
same AB, BC and angle A but a different side AC. `O(1)`.

Pitfalls:

- when AB·AC = |AC|² the circle around B touches the ray, so the
  other root is C itself and the answer is YES (test 07). A
  floating-point test easily prints C again as a "different" point;
- an obtuse or right angle at A gives t′ ≤ 0: YES (example 1 and test
  04);
- Java must print with a fixed locale, as some locales print a
  decimal comma.

A checker accepts any counterexample. It checks the two sides and the
angle at A, a different third side, a nonzero area and the bound
of 1000. The verdicts match an independent accepted implementation on
900 random triangles, except for the touching ones, where it prints C
again.

## Optimized solutions

The optimized versions read integer coordinates and print A and B directly as integers. Only the reflected point needs decimal output.

Python 3.12 x64, submission 11319471. Time 0.078 → 0.109 s, memory 456 → 436 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322295 · Go 1.14 x64 №11321873 · Java 1.8 №11321949 · Rust 1.75 x64 №11321952 · Python 3.12 x64 №11322296.

Java 1.8, submission 11321999. Time 0.125 → 0.093 s, memory 1780 → 480 KB.

G++ 13.2 x64, submission 11322000. Time 0.031 → 0.015 s, memory 124 → 124 KB.

Rust computes coordinates from integer numerators and denominators and formats the results into a fixed buffer. Rust 1.75 x64, submission 11323313. Time 0.046 → 0.046 s, memory 260 → 60 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1710_geometry.cpp](1710_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 124 KB | 11322295 |
| [1710_geometry.go](1710_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB | 11321873 |
| [1710_geometry.java](1710_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1780 KB | 11321949 |
| [1710_geometry.py](1710_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 456 KB | 11322296 |
| [1710_geometry.rs](1710_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB | 11321952 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1710_geometry_optimized.py](1710_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 436 KB | 11319471 |
| [1710_geometry_optimized.java](1710_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 480 KB | 11321999 |
| [1710_geometry_optimized.cpp](1710_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB | 11322000 |
| [1710_geometry_optimized.rs](1710_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 60 KB | 11323313 |

\* The marked versions have room to improve in the ratings.
