# 1554. Multiplicative Functions

[Timus 1554](https://acm.timus.ru/problem.aspx?space=1&num=1554) · difficulty 639 · number_theory

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given the first N values (N ≤ 10⁴) of a multiplicative function F with
values modulo 2007, find the first N values of its inverse G under
Dirichlet convolution, (F * G)(n) = Σ F(n/d)·G(d) over the divisors d of
n, which must be 1 at n = 1 and 0 elsewhere.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then F(1), …, F(N).

## Output

G(1), …, G(N) on one line.

## Examples

### Example 1

Input:

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

Output:

```
1 2006 2006 0 2006 1 2006 0 0 1 2006 0 2006 1 1 0
```

## Solution

At n = 1 the condition reads F(1)·G(1) = 1. For n > 1 it gives
F(1)·G(n) = −Σ F(n/d)·G(d) over the proper divisors d of n, all smaller
than n. A multiplicative F has F(1) = 1; the solutions still divide by
F(1), through its inverse modulo 2007, which costs nothing.

So G is filled in increasing order like a sieve: once G(d) is known,
add F(k)·G(d) to an accumulator at every multiple d·k ≤ N with k ≥ 2;
when the loop reaches n, its accumulator holds the whole sum over the
proper divisors. This takes O(N log N) steps, about 10⁵.
The results were checked against the definition directly.

Pitfalls:

- 2007 = 9·223 is not prime, so −1 is 2006 and inverses need the
  extended Euclidean algorithm or a library call;
- the inverse of 1 everywhere is the Möbius function (test 01), of the
  identity n·μ(n) (test 03), of Liouville's function |μ| (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1554_number_theory.cpp](1554_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.015 s | 280 KB |
| [1554_number_theory.go](1554_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 1680 KB |
| [1554_number_theory.java](1554_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 1156 KB |
| [1554_number_theory.py](1554_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.093 s | 2632 KB |
| [1554_number_theory.rs](1554_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 936 KB |
