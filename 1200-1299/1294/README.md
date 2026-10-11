# 1294. Mars Satellites

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · difficulty 316 · geometry

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
- If |a² + b² − c² − d²| > 2 |ab − cd|, the cosine would leave
  [−1, 1] and no such orbit exists, so the answer is again
  `Impossible.` (test 04).
- Otherwise x = 1000 · √x² kilometres, rounded.

Both checks use exact 64-bit integers (all products stay below
2 · 10¹⁶). Only the last square root is taken in floating point. `O(1)`.

The formula was checked on 100 000 random cyclic quadrilaterals, in
both orientations: it reproduced CD to a relative error of 10⁻¹⁰.

Pitfalls:

- the inputs are in thousands of kilometres, the answer in kilometres
  (test 01);
- AD · AC = BD · BC does not always mean the data contradict each
  other: sometimes it means many answers (tests 02 and 03).

## Language notes

- Python's `round` sends halves to the even neighbour, so the Python
  solution takes floor(x + 0.5) instead, which rounds halves up like
  the other four languages do for positive numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 148 KB |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1088 KB |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1632 KB |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 472 KB |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
