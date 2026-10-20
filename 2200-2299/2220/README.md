# 2220. Average of 1 / gcd over all pairs up to N

[Timus 2220](https://acm.timus.ru/problem.aspx?space=1&num=2220) · difficulty 1465 · number_theory

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the average of 1 / gcd(i, j) over all pairs 1 ≤ i ≤ j ≤ N, modulo
10⁹ + 7. The limits are 1.5 seconds and 512 MB.

## Input

N, 1 ≤ N ≤ 10⁷.

## Output

The average as p · q⁻¹ modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
2
```

Output:

```
833333340
```

### Example 2

Input:

```
3
```

Output:

```
805555562
```

### Example 3

Input:

```
1
```

Output:

```
1
```

## Solution

Group the pairs by their gcd d. Writing i = da and j = db, the pairs
with gcd d are the coprime pairs a ≤ b ≤ ⌊N / d⌋, and there are
Φ(⌊N / d⌋) of them, where Φ(m) = φ(1) + … + φ(m). So the sum is

Σ over d of Φ(⌊N / d⌋) / d,

which is divided by the N(N + 1) / 2 pairs at the end.

⌊N / d⌋ takes O(√N) distinct values, and on each block of d with the
same quotient the sum needs Φ of that quotient times the difference of
harmonic numbers H(right) − H(left − 1) modulo the prime.

- Φ at all quotients comes from a sieve of φ up to a bound and, above
  it, the identity Φ(x) = x(x + 1) / 2 − Σ over d ≥ 2 of Φ(⌊x / d⌋),
  again grouped by quotients, smaller arguments first.
- The harmonic numbers would need an inverse for every d up to 10⁷. The
  solution instead keeps F = d! and W = d! · H(d), updated by
  W ← W · d + F and F ← F · d, and takes one inverse of F per block.
  The Python version folds eight consecutive steps into one using the
  product of the eight factors and its derivative.

In the first example the pairs (1, 1), (1, 2) and (2, 2) give
1 + 1 + 1/2 = 5/2, and the average is 5/6.

This takes O(N) multiplications for the harmonic numbers plus about
O(N^(3/4)) for the totient sums.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2220_number_theory.cpp](2220_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 1000 KB |
| [2220_number_theory.go](2220_number_theory.go) | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.093 s | 1704 KB |
| [2220_number_theory.java](2220_number_theory.java) | Java 1.8 | number_theory | O(N + N^(3/4)) | AC | 0.437 s | 1064 KB |
| [2220_number_theory.py](2220_number_theory.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 1.265 s | 4892 KB |
| [2220_number_theory.rs](2220_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 800 KB |
