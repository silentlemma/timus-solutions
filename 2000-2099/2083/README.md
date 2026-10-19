# 2083. A weighted sum of permutation powers along cycles

[Timus 2083](https://acm.timus.ru/problem.aspx?space=1&num=2083) · difficulty 2654 · math

Original problem by Denis Dublennykh.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A permutation p of 1 … n is given. Row t of an m × n matrix A is p
applied t times: A[t][j] = pᵗ(j) (the first row is p itself). Compute
the vector q × A for a given q of length m, that is
v[j] = q₁ p(j) + q₂ p²(j) + … + q_m pᵐ(j). The limits are 4 seconds and
256 MB.

## Input

m and n, 2 ≤ m, n ≤ 5·10⁴, then p(1) … p(n), then q₁ … q_m,
0 ≤ qᵢ ≤ 10⁹.

## Output

The n components of q × A.

## Examples

### Example 1

Input:

```
3 4
3 2 4 1
3 5 8
```

Output:

```
37 32 41 50
```

## Solution

Split p into cycles. On a cycle c₀, c₁, …, c_{L−1} with p(c_s) = c_{s+1}
(indices modulo L), pᵗ(c_s) = c_{(s+t) mod L}. Fold q by the remainder of
t modulo L: Q[r] = sum of q_t over t ≡ r (mod L). Then
v[c_s] = Σ_r Q[r] · c_{(s+r) mod L}, a cyclic correlation of length L.
The fold depends only on L, and cycles have at most about √(2n)
different lengths, so the folds cost O(m √n).

A correlation is a product of polynomials: the reversed Q times the
cycle written twice gives v[c_s] as coefficient s + L − 1. The values
reach 5·10⁴ · 5·10⁴ · 10⁹ = 2.5·10¹⁸, so the product must be exact.
C++, Go, Java and Rust use a number-theoretic transform modulo three
primes (998244353, 167772161, 469762049) and put the coefficients back
together by Garner's method; the result is below 2⁶³, so wrapping
64-bit arithmetic gives it exactly. Python packs each sequence into one
big integer, ten bytes per number, multiplies the two integers and reads
the coefficients back, as no coefficient overflows its ten bytes. Short
cycles (up to 32) are summed directly. Products cost O(n log n) with NTT,
O(n^(log₂ 3)) with Python's Karatsuba multiplication.

In the example p is the single cycle 1 → 3 → 4 → 1 plus the fixed point
2, and v[2] = (3 + 5 + 8) · 2 = 32.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2083_math.cpp](2083_math.cpp) | G++ 13.2 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12432 KB |
| [2083_math.go](2083_math.go) | Go 1.14 x64 | math | O(n log n + m sqrt n) | AC | 0.734 s | 19740 KB |
| [2083_math.java](2083_math.java) | Java 1.8 | math | O(n log n + m sqrt n) | AC | 1.500 s | 16236 KB |
| [2083_math.py](2083_math.py) | Python 3.12 x64 | math | O(n^(log₂ 3) + m sqrt n) | AC | 2.781 s | 27692 KB |
| [2083_math.rs](2083_math.rs) | Rust 1.75 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12824 KB |
