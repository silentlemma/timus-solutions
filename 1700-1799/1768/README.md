# 1768. Circular Strings

[Timus 1768](https://acm.timus.ru/problem.aspx?space=1&num=1768) · difficulty 1156 · geometry

Original problem by Dmitry Ivankov, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n points, decide whether they are the vertices of a regular
n-gon, not degenerate, listed in order around it.

## Input

n (3 ≤ n ≤ 100), then n points with real coordinates from 0 to 1,
given to at least 10⁻¹⁰. Points may coincide, but some two points are
at least 0.3 apart. When the answer is no, no change of the points by
less than 10⁻⁵ makes it yes.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
4
0 0
1 0
1 1
0 1
```

Output:

```
YES
```

### Example 2

Input:

```
3
0 0
1 0
0.5 1
```

Output:

```
NO
```

## Solution

The centre of a regular polygon is the mean of its vertices, and
listed in order, each vertex is the previous one turned about the
centre by 2π/n, one way or the other. So with the points as complex
numbers zᵢ measured from their mean, the answer is yes when
zᵢ₊₁ = ω·zᵢ for every i, cyclically, with ω = e^(±2πi/n), and z₀ is not
the centre itself. `O(n)`.

The equalities are tested with a tolerance of 10⁻⁸. Points given to
10⁻¹⁰ miss by a few 10⁻¹⁰ at most. If every turn missed by at most ε,
the points would lie within n·ε of the regular polygon built from z₀,
so a set that needs a change of 10⁻⁵ misses by more than 10⁻⁵/n ≥
10⁻⁷ somewhere.

In the first example the mean is (0.5, 0.5), and a quarter turn takes
each corner of the square to the next. In the second the three points
are not at equal distances from their mean.

Pitfalls:

- the order may go either way round;
- the right points in another order, such as a star, are not enough;
- a smaller polygon walked round twice repeats points and fails.

The answers agree with an independent accepted implementation on 160
random cases: regular polygons in order, with one vertex moved by at
least 0.001, in a star order, and walked round more than once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1768_geometry.cpp](1768_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 212 KB |
| [1768_geometry.go](1768_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1132 KB |
| [1768_geometry.java](1768_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 660 KB |
| [1768_geometry.py](1768_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB |
| [1768_geometry.rs](1768_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 244 KB |
