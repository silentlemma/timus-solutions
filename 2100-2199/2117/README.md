# 2117. Sums of two square roots equal to a given root

[Timus 2117](https://acm.timus.ru/problem.aspx?space=1&num=2117) · difficulty 544 · number_theory

Original problem by Pavel Klimov, from the University Academic Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For an integer C count the pairs of non-negative integers A ≤ B with
√A + √B = √C. The limits are 1 second and 256 MB.

## Input

C, 0 ≤ C ≤ 10¹⁸.

## Output

The number of pairs.

## Examples

### Example 1

Input:

```
9
```

Output:

```
2
```

### Example 2

Input:

```
3
```

Output:

```
1
```

## Solution

Write C = s² q with q square-free. Squaring √A = √C − √B shows that √(BC)
is an integer, and from there that A and B are a² q and b² q with
a + b = s; conversely every such split works. So the answer is the
number of pairs a ≤ b with a + b = s, that is ⌊s/2⌋ + 1 (C = 0 has the
single pair 0, 0).

It remains to find s, the root of the largest square dividing C. Trial
division by d up to 10⁶ (the cube root of 10¹⁸) removes d² as long as it
divides and then one more d if present, multiplying s by d for every d²
removed. What is left is 1, a prime, or a product of two primes above 10⁶, since
three such factors exceed 10¹⁸. So it contains a square factor only when
it is itself the square of a prime; then s gains that prime. The time
complexity is O(min(10⁶, √C)).

In the first example 9 = 3² · 1, so s = 3 and the pairs are 0 + 9 and
1 + 4.

## Optimized solutions

The new C++/Go versions keep square-part factorization and the answer floor(s/2)+1 for C=s²q, q square-free. For C>0, squaring √A = √C − √B gives 2√(BC) = B + C − A. The right side is even, since its square is divisible by four. Thus BC is a square. For B>0 the prime exponents of B and C have the same parity, so B=b²q and A=(s−b)²q. This gives the integer splits of s, including A=0.

A perfect square, including zero, returns immediately with s=sqrt(C). Otherwise remove square pairs and an odd remaining occurrence of2 and3, then only test divisors6k±1. Stop when d³ exceeds the shrinking residual R: every remaining prime factor is at least d, so R has at most two factors counted with multiplicity. It contributes another square factor exactly if R itself is a square. All square roots start from floating-point estimates and are corrected with exact integer products; values≤10^18 and the first failing cube fit64-bit unsigned arithmetic. Compared with scanning every integer to a fixed10^6 bound, the wheel removes most trial divisions and the adaptive residual often finishes much earlier. Worst time O(C^(1/3)) and extra space O(1). Go reads through standard handles into a 64-byte buffer. The answer is at most 500,000,001, so nine digits and a newline fit in its ten-byte output buffer. All simpler trial-division sources remain; Java/Python/Rust reuse qualifying originals.

The accepted base implementations [2117_number_theory.java](2117_number_theory.java), [2117_number_theory.py](2117_number_theory.py), [2117_number_theory.rs](2117_number_theory.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.031 s | 136 KB | 11294802 |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.046 s | 1096 KB | 11294803 |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(min(10⁶, √C)) | AC | 0.140 s | 1604 KB | 11294808 |
| [2117_number_theory.py](2117_number_theory.py) \* | Python 3.12 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.500 s | 472 KB | 11294805 |
| [2117_number_theory.rs](2117_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.062 s | 232 KB | 11294811 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2117_number_theory_optimized.cpp](2117_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(C^(1/3)) | AC | 0.015 s | 112 KB | 11315748 |
| [2117_number_theory_optimized.go](2117_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(C^(1/3)) | AC | 0.046 s | 276 KB | 11315923 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
