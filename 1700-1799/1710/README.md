# 1710. Boris, You Are Wrong!

[Timus 1710](https://acm.timus.ru/problem.aspx?space=1&num=1710) · difficulty 654 · geometry

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1710_geometry.cpp](1710_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 140 KB |
| [1710_geometry.go](1710_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1104 KB |
| [1710_geometry.java](1710_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.171 s | 1800 KB |
| [1710_geometry.py](1710_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 428 KB |
| [1710_geometry.rs](1710_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB |
