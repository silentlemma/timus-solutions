# 1387. Vasya's Dad

[Timus 1387](https://acm.timus.ru/problem.aspx?space=1&num=1387) · difficulty 1360 · math

Original problem by Alexander Ipatov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A directed graph is nice if it has N vertices and N − 1 arcs, exactly
one vertex without incoming arcs and no directed cycles. Count the nice
graphs with N vertices, 1 ≤ N ≤ 50, up to renumbering the vertices.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

The number of different nice graphs.

## Examples

### Example 1

Input:

```
3
```

Output:

```
2
```

### Example 2

Input:

```
5
```

Output:

```
9
```

## Solution

Every vertex except the source has at least one incoming arc, and there
are only N − 1 arcs, so each of them has exactly one. Without cycles,
following those arcs back always ends at the source: a nice graph is a
rooted tree with arcs pointing away from the root. So the answer is the
number a(N) of unlabeled rooted trees.

Removing the root leaves a multiset of smaller rooted trees, and
counting such multisets gives the classic recurrence

a(1) = 1, a(m + 1) = (s(1)·a(m) + s(2)·a(m − 1) + … + s(m)·a(1)) / m,

where s(k) is the sum of d·a(d) over the divisors d of k. The division
is always exact. `O(N²)` operations on numbers.

Pitfalls:

- a(50) = 425 976 989 835 141 038 353 does not fit in 64 bits, and the
  sum before the division overflows them from N = 44 (tests 10 and
  11), so the solutions use 128-bit or big integers;
- a(8) is 115; summing over shapes by hand easily gives a little more
  (test 06).

The first nine answers were checked by building every tree from smaller
ones and keeping distinct canonical strings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1387_math.cpp](1387_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.015 s | 196 KB |
| [1387_math.go](1387_math.go) | Go 1.14 x64 | math | O(N^2) | AC | 0.031 s | 1228 KB |
| [1387_math.java](1387_math.java) | Java 1.8 | math | O(N^2) | AC | 0.125 s | 1848 KB |
| [1387_math.py](1387_math.py) | Python 3.12 x64 | math | O(N^2) | AC | 0.078 s | 424 KB |
| [1387_math.rs](1387_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.015 s | 224 KB |
