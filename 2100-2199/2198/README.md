# 2198. Total height of all ordered rooted trees with N vertices

[Timus 2198](https://acm.timus.ru/problem.aspx?space=1&num=2198) · difficulty 1241 · math, combinatorics

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sum the heights of all ordered rooted trees with N vertices, modulo
10⁹ + 7. The limits are 1 second and 256 MB.

## Input

N, 1 ≤ N ≤ 400.

## Output

The sum modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
3
```

Output:

```
3
```

## Solution

Walking around an ordered tree with e = N − 1 edges, going down and up
every edge once, gives a Dyck path of 2e steps, and this is a bijection
in which the height of the tree is the highest level of the path. The
total height is the sum over h ≥ 1 of the number of paths that reach
level h.

Paths that stay inside the strip from level 0 to level h − 1 are counted
by reflecting across the two lines −1 and h, which gives an alternating
sum of binomial coefficients with period w = h + 1. Subtracting from all
paths and regrouping, the number of Dyck paths that reach level h is

Σ over k ≥ 1 of C(2e, e + kw − 1) − 2 C(2e, e + kw) + C(2e, e + kw + 1),

and only terms with kw ≤ e + 1 are non-zero. So the answer is a double
sum over the widths w = 2 … e + 1 and their multiples, about e ln e
terms, with the binomials C(2e, j) built once from modular inverses.

In the example the two trees with 3 vertices are a path of height 2 and
a root with two leaves of height 1, so the answer is 3.

This takes O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2198_math_combinatorics.cpp](2198_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.015 s | 188 KB |
| [2198_math_combinatorics.go](2198_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 880 KB |
| [2198_math_combinatorics.java](2198_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.140 s | 216 KB |
| [2198_math_combinatorics.py](2198_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.078 s | 272 KB |
| [2198_math_combinatorics.rs](2198_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.031 s | 24 KB |
