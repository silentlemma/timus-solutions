# 1062. Who can win a triathlon with suitable stage lengths

[Timus 1062](https://acm.timus.ru/problem.aspx?space=1&num=1062) · difficulty 1830 · geometry

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A race has three stages. `N` athletes (`1 ≤ N ≤ 100`) have speeds
`Vi, Ui, Wi` (integers from 1 to 10000) on the three stages. The organisers
may choose any positive lengths of the stages. For every athlete, decide
whether some lengths make that athlete the only one with the smallest
total time.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines with `Vi Ui Wi`.

## Output

For every athlete `Yes` or `No`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
9
10 2 6
10 7 3
5 6 7
3 2 7
6 2 6
3 5 7
8 4 6
10 4 2
1 8 7
```

Output:

```
Yes
Yes
Yes
No
No
No
Yes
No
Yes
```

### Example 2

Input:

```
3
5 5 5
5 5 5
1 1 10
```

Output:

```
No
No
Yes
```

## Solution

With lengths `(a, b, c)` the time of athlete `j` is `a/Vj + b/Uj + c/Wj`.
Athlete `i` beats `j` when

```text
(1/Vi − 1/Vj)·a + (1/Ui − 1/Uj)·b + (1/Wi − 1/Wj)·c < 0
```

Rescale the lengths for athlete `i`: `u = (a/Vi, b/Ui, c/Wi)` is still any
positive triple, and after multiplying by `Vj·Uj·Wj` the condition reads
`Σ (Sj − Si) · (the other two speeds of j) · u < 0` over the three stages,
with integer coefficients below `10^12`. Only the ratios matter, so `u`
runs over the triangle `x > 0, y > 0, x + y < 1` (the third part is
`1 − x − y`), and every rival cuts it by an open half-plane. Athlete `i`
can win when the open region left is not empty.

Deciding that in floating point is fragile: the region can be a strip of
tiny but positive area, or a segment of zero area, and no tolerance
separates the two reliably. The solutions decide it exactly. Every
constraint is tightened by the same tiny `ε > 0`; the open region is not
empty exactly when the closed, tightened polygon is not empty for all
small `ε`. The polygon is kept as its list of lines in boundary order, a
corner is the meeting point of two consecutive lines, and the side of a
corner against a new line is the sign of an integer value, then of its
`ε` coefficient. These values stay below `3 · 10^37`, inside 128 bits.
Clipping keeps every edge with a part strictly inside and puts the new
line where the boundary leaves the half-plane. `O(N)` per rival,
`O(N^3)` in total, at most a million steps.

Pitfalls:

- identical athletes: neither can finish alone first;
- an athlete who is equal on two stages and slower on the third is never
  first;
- the region of good lengths can be a segment or a point, which is not
  enough: a strict win needs an open region;
- a floating-point area test with a fixed tolerance (a first version used
  `10^-12`) failed on the judge; the exact test needs no tolerance.

The answers were checked against an exact implementation with fractions
(clipping by closed half-planes, then a positive area) on several hundred
random inputs, many of them full of ties or nearly equal speeds, and on a
thin strip of wins built just below the midpoint of two rivals.

## Language notes

- C++ and Rust use 128-bit integers, Java `BigInteger`, Go `math/big`,
  Python its own integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1062_geometry.cpp](1062_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.015 s | 212 KB |
| [1062_geometry.go](1062_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.046 s | 6444 KB |
| [1062_geometry.java](1062_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.109 s | 5156 KB |
| [1062_geometry.py](1062_geometry.py) | Python 3.12 x64 | geometry | O(N^3) | AC | 0.093 s | 756 KB |
| [1062_geometry.rs](1062_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.046 s | 244 KB |
