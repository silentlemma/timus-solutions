# 1625. Hankel Matrix

[Timus 1625](https://acm.timus.ru/problem.aspx?space=1&num=1625) · difficulty 1046 · math

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Hankel matrix of size n has the entry α(i + j − 1) in row i, column j,
so it is built from α1, …, α(2n−1). For 1 ≤ n ≤ 100, find non-negative
integers of at most 300 digits each such that every square submatrix
that contains the upper left cell has determinant 1. Any such numbers
are accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n.

## Output

α1, …, α(2n−1), one per line.

## Examples

### Example 1

Input:

```
1
```

Output:

```
1
```

### Example 2

Input:

```
2
```

Output:

```
1
6
37
```

### Example 3

Input:

```
3
```

Output:

```
1
3
10
7
630
```

## Solution

The Catalan numbers 1, 1, 2, 5, 14, … work: the Hankel matrix
[C(i + j)] has every leading square of determinant 1. By the
Lindström–Gessel–Viennot lemma such a determinant counts families of
non-crossing lattice paths, and C(i + j) counts the Dyck-type paths from
one starting point to one end point; for these points only one family
does not cross, so every determinant is 1.

C(198) has 116 digits, well within the limit. Each number follows from
the previous one: C(k + 1) = C(k) · 2(2k + 1) / (k + 2), and the
division is exact. Python, Go and Java use their big integers; C++ and
Rust keep the number as base-10⁹ digits with multiplication and division
by a small number. `O(n²)`.

Pitfalls:

- the example answers differ from these, so a checker verifies the
  determinants (modulo three large primes, by elimination whose pivots
  are the leading minors);
- n = 1 needs only the number 1.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1625_math.cpp](1625_math.cpp) | G++ 13.2 x64 | math | O(n²) | AC | 0.015 s | 228 KB |
| [1625_math.go](1625_math.go) | Go 1.14 x64 | math | O(n²) | AC | 0.015 s | 1164 KB |
| [1625_math.java](1625_math.java) | Java 1.8 | math | O(n²) | AC | 0.125 s | 2116 KB |
| [1625_math.py](1625_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.078 s | 416 KB |
| [1625_math.rs](1625_math.rs) | Rust 1.75 x64 | math | O(n²) | AC | 0.015 s | 288 KB |
