# 2067. Pairs that no third point can join

[Timus 2067](https://acm.timus.ru/problem.aspx?space=1&num=2067) · difficulty 326 · geometry

Original problem by Alexey Danilyuk, prepared by Alexey Danilyuk and Alexander Borzunov, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n distinct points (sᵢ, rᵢ) are given. For two points v, u let p(v, u)
be the distance between them, and for three points let p(v, u, w) be
half the sum of the three pairwise distances. Two different points v, u
form a best pair when p(v, u) ≥ p(v, u, w) for every point w. Find all
best pairs. The limits are 2 seconds and 64 MB.

## Input

The number of points n, 2 ≤ n ≤ 2·10⁵, then n lines with the integers
sᵢ and rᵢ, −10⁸ ≤ sᵢ, rᵢ ≤ 10⁸. No two points coincide.

## Output

The number of best pairs, then the pairs, one per line, as the numbers
of their points in the input order. The pairs and the two numbers of a
pair may come in any order.

## Checking

A checker compares the number of pairs and the set of pairs, with the
two numbers of each pair in any order.

## Examples

### Example 1

Input:

```
2
2 3
7 6
```

Output:

```
1
1 2
```

### Example 2

Input:

```
3
5 5
2 -4
-4 2
```

Output:

```
0
```

## Solution

Multiply the condition by 2: p(v, u) ≥ p(v, u, w) means
p(v, u) ≥ p(v, w) + p(w, u). The triangle inequality says the opposite,
so equality must hold, and that happens exactly when w lies on the
segment vu (for w = v or w = u it holds trivially). So v and u are a
best pair exactly when every point lies on the segment between them.

If the points are not all on one line, there is no best pair. If they
are, the only candidates are the two extreme points of the line, and
they do work: every other point lies between them. Two points are always
collinear, so n = 2 gives the single pair 1 2.

Collinearity is checked exactly with the cross product
(p₂ − p₁) × (pᵢ − p₁) = 0, whose terms reach 4·10¹⁶ and fit 64-bit
integers. The extremes are the smallest and the largest point in the
order by s and then by r. Everything takes O(n), except Python's sort: O(n log n).

In the second example the three points form a triangle, so the answer
is 0.

## Language notes

Products need 64-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2067_geometry.cpp](2067_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.296 s | 2888 KB |
| [2067_geometry.go](2067_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.281 s | 8768 KB |
| [2067_geometry.java](2067_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 3708 KB |
| [2067_geometry.py](2067_geometry.py) | Python 3.12 x64 | geometry | O(n log n) | AC | 0.531 s | 62832 KB |
| [2067_geometry.rs](2067_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 10476 KB |
