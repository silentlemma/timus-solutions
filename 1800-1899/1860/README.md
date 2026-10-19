# 1860. Fiborial

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · difficulty 469 · number_theory

Original problem by Denis Dublennykh (idea by Grigoriy Nazarov), from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let F₀ = F₁ = 1 and Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂. Find the number of divisors of
Fₙ modulo 10⁹ + 7.

## Input

n (1 ≤ n ≤ 10⁶).

## Output

The number of divisors of Fₙ modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
3
```

Output:

```
4
```

## Solution

Each step multiplies in i once and repeats the two previous products, so
the factor k enters Fₙ exactly fib(n − k + 1) times, with fib(1) =
fib(2) = 1: it appears once in F_k, once in F_{k+1}, twice in F_{k+2},
and so on by the Fibonacci rule. Hence Fₙ = Π k^fib(n−k+1) over
k = 1 … n.

The number of divisors is Π (e_p + 1) over the primes p, where e_p is
the exponent of p in Fₙ. A number k contributes v_p(k) times its weight
fib(n − k + 1), and v_p(k) counts how many of p, p², p³, … divide k, so
e_p is the sum of the weights of all multiples of p, of p², and so on.
Only e_p modulo 10⁹ + 7 matters, so the weights are kept reduced too.
Going over the multiples of every prime power takes about
n·ln ln n steps; the Python solution sums every progression with one
slice. `O(n log log n)`.

In the example F₃ = 3·F₂·F₁ = 3·2·1 = 6, which has the divisors 1, 2, 3
and 6.

Pitfalls:

- the exponents are huge, but the answer only needs them modulo
  10⁹ + 7;
- a prime power past n must stop the loop before it overflows;
- the Python solution runs on PyPy.

The answers agree with a direct factorisation of Fₙ for n up to 14 and
with an independent accepted implementation up to 10⁶.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15508 KB |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB |
| [1860_number_theory.java](1860_number_theory.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.140 s | 18448 KB |
| [1860_number_theory.py](1860_number_theory.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.187 s | 34144 KB |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.062 s | 16688 KB |
