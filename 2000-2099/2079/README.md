# 2079. The Fibonacci residues that can follow a given one

[Timus 2079](https://acm.timus.ru/problem.aspx?space=1&num=2079) · difficulty 4667 · number_theory

Original problem by Vladislav Isenbaev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The Fibonacci numbers are taken modulo a prime p: x₀ = 0, x₁ = 1,
xₙ = (xₙ₋₁ + xₙ₋₂) mod p. Given a value x, find every value that can
follow it, that is, all distinct x_{k+1} over the indices k with
x_k = x (the indices go far beyond the period). The limits are
0.5 seconds and 256 MB.

## Input

A prime p, 2 ≤ p < 10⁹, and x, 0 ≤ x < p.

## Output

The number of distinct following values and then the values in
increasing order, or just 0 if x never occurs.

## Examples

### Example 1

Input:

```
7 0
```

Output:

```
2
1 6
```

### Example 2

Input:

```
7 3
```

Output:

```
1
5
```

### Example 3

Input:

```
11 4
```

Output:

```
0
```

## Solution

Two facts do the work. Cassini's identity
F(k+1)² − F(k+1) F(k) − F(k)² = (−1)ᵏ holds modulo p too, so the value
y following x solves y² − x y − (x² + s) = 0 with s = 1 or −1. That gives
at most four candidates y = (x ± √(5x² + 4s)) / 2, with the square roots
taken by the Tonelli–Shanks algorithm.

A candidate need not occur, though: in the third example 4 never shows
up modulo 11 even though the equation has roots. To check one, work in
the ring F_p[t] / (t² − t − 1), where tᵏ = F(k) t + F(k − 1). The pair
(x, y) occurs exactly when x t + (y − x) is a power of t, a discrete
logarithm question. The period of the sequence divides p − 1 when
p mod 5 is 1 or 4 and 2(p + 1) otherwise, so baby-step giant-step with
m ≈ √(2p) baby steps tⁱ in a table and giant steps by t⁻ᵐ = (t − 1)ᵐ
answers it in O(√p). Primes up to 50 (including 2 and 5, which the
formulas do not cover) are handled by walking the whole period, which is
at most 4p + 4 long.

In the first example x = 0 gives y² = ±1 modulo 7; −1 is not a square,
and both 1 (k = 0) and 6 (k = 8, F(9) = 34) occur.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2079_number_theory.cpp](2079_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt p) | AC | 0.015 s | 1264 KB |
| [2079_number_theory.go](2079_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt p) | AC | 0.031 s | 2528 KB |
| [2079_number_theory.java](2079_number_theory.java) | Java 1.8 | number_theory | O(sqrt p) | AC | 0.156 s | 4712 KB |
| [2079_number_theory.py](2079_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt p) | AC | 0.140 s | 8656 KB |
| [2079_number_theory.rs](2079_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt p) | AC | 0.062 s | 2436 KB |
