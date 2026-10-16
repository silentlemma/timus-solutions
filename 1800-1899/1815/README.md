# 1815. Farm in San Andreas

[Timus 1815](https://acm.timus.ru/problem.aspx?space=1&num=1815) · difficulty 4112 · geometry

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three cities and the price per kilometre of a road from each of them
are given. Place a farm anywhere in the plane so that the total price
of the three straight roads to it, the weighted sum of distances, is
as small as possible, and print that price with absolute or relative
error at most 10⁻⁹. There are up to 10⁴ cases.

## Input

t (1 ≤ t ≤ 10⁴), then for each case three lines with city coordinates
(integers up to 1000 in absolute value) and a line with the three
prices (from 1 to 1000).

## Output

The least total price for each case.

## Examples

### Example 1

Input:

```
2
0 0
1 0
0 1
1 1 1
-3 0
3 5
0 -1
7 9 8
```

Output:

```
1.9318516526
81.1600672826
```

## Solution

This is the weighted Fermat–Torricelli problem. Iterative searches
can crawl near a city at the precision asked for. It has an exact
answer.

The cost is convex. A city v is the best place when the pull of the
others, the sum of their weights times the unit vectors from v towards
them, is no longer than the total weight standing at v; cities in the
same spot add their weights there.

If no city qualifies, the best point M is inside, where the three
weighted unit vectors cancel, and its cost has a closed form. Build the
point Q on the far side of BC from A with |BQ| : |CQ| : |BC| =
w₃ : w₂ : w₁. Ptolemy's inequality for M, B, Q, C gives
w₂|MB| + w₃|MC| ≥ w₁|MQ| for every M, so the cost is at least
w₁(|MA| + |MQ|) ≥ w₁|AQ|. Since the optimum is inside, equality holds,
and the answer is w₁|AQ|. A tiny tolerance in the city test handles
roundoff at the exact border, where both formulas agree.
`O(1)` per case.

In the first case of the example all prices are 1 and every angle is below 120°,
so the answer is the classic Fermat point, at total distance
(1 + √3)/√2 ≈ 1.93185.

Pitfalls:

- Weiszfeld's iteration can stop at a city whenever it steps exactly
  onto it, for instance when the cities lie on a line and their centre
  is one of them;
- two or three cities may share a spot;
- the weights need not form a triangle; then the city with the largest
  weight wins outright.

The answers agree with a fine local search from the centre on 3000
random cases with coinciding, collinear and general cities. They also
agree with an independent accepted implementation everywhere, except
on collinear cases where its iteration starts on a city and stays
there.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1815_geometry.cpp](1815_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per case | AC | 0.156 s | 168 KB |
| [1815_geometry.go](1815_geometry.go) | Go 1.14 x64 | geometry | O(1) per case | AC | 0.062 s | 1588 KB |
| [1815_geometry.java](1815_geometry.java) | Java 1.8 | geometry | O(1) per case | AC | 0.234 s | 6304 KB |
| [1815_geometry.py](1815_geometry.py) | Python 3.12 x64 | geometry | O(1) per case | AC | 0.265 s | 10052 KB |
| [1815_geometry.rs](1815_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per case | AC | 0.015 s | 1304 KB |
