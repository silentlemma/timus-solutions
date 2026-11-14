# 2220. Average of 1 / gcd over all pairs up to N

[Timus 2220](https://acm.timus.ru/problem.aspx?space=1&num=2220) · difficulty 685 · number_theory

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

## Optimized solutions

Go groups four consecutive factorial and harmonic updates. It uses the product rule to obtain the block product and its derivative, then applies one update to the weighted sum. Submission 11317204 took 0.046 s and used 1504 KB, versus 0.078 s and 1908 KB for the base.

PyPy pairs the first and last factors in each block of eight, then evaluates the block product and its derivative using the four paired factors. The totient sums for large quotient arguments are computed in increasing order and stored in an array. Submission 11317253 took 0.343 s and used 4016 KB, versus 1.328 s and 5096 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321803 · Go 1.14 x64 №11322081 · Java 1.8 №11318205 · Rust 1.75 x64 №11321807 · PyPy 3.10 x64 №11322169.

Rust groups four harmonic updates and stores the small totient sums as 32-bit residues. Rust 1.75 x64, submission 11322387. Time 0.062 → 0.046 s, memory 1000 → 612 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2220_number_theory.cpp](2220_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 1196 KB | 11321803 |
| [2220_number_theory.go](2220_number_theory.go) | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.078 s | 1908 KB | 11322081 |
| [2220_number_theory.java](2220_number_theory.java) | Java 1.8 | number_theory | O(N + N^(3/4)) | AC | 0.421 s | 1252 KB | 11318205 |
| [2220_number_theory.py](2220_number_theory.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 1.328 s | 5096 KB | 11322169 |
| [2220_number_theory.rs](2220_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.062 s | 1000 KB | 11321807 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2220_number_theory_optimized.go](2220_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 1504 KB | 11317204 |
| [2220_number_theory_optimized.py](2220_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | O(N + N^(3/4)) | AC | 0.343 s | 4016 KB | 11317253 |
| [2220_number_theory_optimized.rs](2220_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(N + N^(3/4)) | AC | 0.046 s | 612 KB | 11322387 |

\* The saved rating has no comparable Go submissions from other authors.
