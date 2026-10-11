# 1294. Mars Satellites

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · difficulty 317 · geometry

Original problem by Vladimir Yakovlev, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four satellites A, B, C and D lie on one circular orbit in this order.
The distances AD, AC, BD and BC are known, in thousands of kilometres
(whole numbers from 1 to 10 000); the radius of the orbit is not. Find
the distance CD in kilometres, rounded to an integer, or report that it
cannot be determined uniquely.

Time limit: 1 second. Memory limit: 64 MB.

## Input

AD, AC, BD and BC.

## Output

`Distance is X km.` or `Impossible.`

## Examples

### Example 1

Input:

```
4 7 5 7
```

Output:

```
Distance is 5385 km.
```

## Solution

Write a = AD, b = AC, c = BD, d = BC and x = CD. The points A and B lie
on the same arc cut off by the chord CD, so they see it at the same
inscribed angle t. The law of cosines in triangles ACD and BCD gives

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t,

two equations in x² and cos t. Hence

cos t = (a² + b² − c² − d²) / (2 (ab − cd)),

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd).

- If ab = cd, the equations either contradict each other or say
  nothing about t. In the second case, for example a symmetric
  trapezoid, CD really can take many values (test 02). Either way the
  answer is `Impossible.` (tests 02 and 03).
- If |a² + b² − c² − d²| ≥ 2 |ab − cd|, no nondegenerate triangle
  exists: equality also fails because three distinct points on a circle
  cannot be collinear (tests 04 and 07).
- Ptolemy’s theorem requires AB · CD = bc − ad > 0 for the stated cyclic
  order. Reject bc ≤ ad as `Impossible.` (tests 05 and 07). With a strict
  cosine bound, this check also ensures the reconstructed points have
  the required order.
- Otherwise x = 1000 · √x² kilometres, rounded.

All feasibility checks use exact 64-bit integers (the original products
stay below 2 · 10¹⁶). Normalize the numerator and denominator to positive
values. Use a floating-point square root to estimate the integer part m
of the distance in kilometres, then round up exactly when
(2m + 1)² ≤ floor(4 · 1000² · num / den). Compute this bound as
s · (num div den) + (s · (num mod den)) div den, where s = 4 · 1000²,
to avoid overflow. All new intermediates are below 2 · 10¹⁵.
Time and auxiliary space are both `O(1)`.

The corrected feasibility checks and rounded answers are verified
against an independent exact oracle using Ptolemy’s theorem, opposite
angles and strict triangle inequalities.

Pitfalls:

- the inputs are in thousands of kilometres, the answer in kilometres
  (test 01);
- AD · AC = BD · BC does not always mean the data contradict each
  other: sometimes it means many answers (tests 02 and 03);
- a cosine in [−1, 1] alone does not ensure a valid orbit: exclude
  degenerate triangles and enforce the cyclic order (test 07).

## Language notes

- Python's `round` sends halves to the even neighbour. All five
  solutions instead compare the squared half-kilometre boundary with
  exact integers, so ties round up identically.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1648 KB |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 448 KB |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
