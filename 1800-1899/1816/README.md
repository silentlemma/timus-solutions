# 1816. Troubles with Pollard

[Timus 1816](https://acm.timus.ru/problem.aspx?space=1&num=1816) · difficulty 2272 · number_theory

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

To split n, a program stops if n is prime. Otherwise it takes a random
r from 1 to 10¹⁸ and g = gcd(n, r), repeats while g is 1 or n, and then
splits g and n/g the same way. Find the expected number of gcd
computations, with error at most 10⁻⁶.

## Input

n (2 ≤ n ≤ 10⁹).

## Output

The expected number of gcd computations.

## Examples

### Example 1

Input:

```
12
```

Output:

```
4.8571428571
```

### Example 2

Input:

```
8
```

Output:

```
6.6666666667
```

## Solution

Since 10¹⁸ is far larger than n, r mod n is uniform up to a negligible
error, and the gcd splits over the prime powers of n. If p
appears in m with exponent e, the exponent of p in gcd(m, r) is c < e
with chance (1 − 1/p)/pᶜ and e with chance 1/pᵉ, independently for
every prime. For a composite m, the step is repeated until the gcd is
proper, so E(m) = (1 + Σ P(g)·(E(g) + E(m/g))) / (1 − P(1) − P(m)),
with the sum over the proper divisors g, and E is 0 on primes.

Every number met is a divisor of n, at most 1344 of them below 10⁹.
Writing a divisor as its exponent vector in mixed radix, every proper
divisor of a divisor gets a smaller number, so E can be filled in
increasing order. The pair g and m/g are numbers d and index − d. The
sum runs over all divisors of all divisors of n, about 1.4·10⁵ terms in
the worst case. `O(Σ d(m))` over the divisors m of n.

In the second example 8 = 2³: the gcd is 1, 2, 4 or 8 with chances 1/2,
1/4, 1/8 and 1/8. E(4) = 4, and
E(8) = (1 + 1/4·4 + 1/8·4) / (3/8) = 20/3.

Pitfalls:

- E(m) appears on both sides, since a useless gcd repeats the step;
- the chances depend on the primes, not only on the shape of the
  exponents;
- primes need no gcd at all, so E(p) = 0.

The answers agree with an independent accepted implementation on the
examples, primes, prime powers, the number with the most divisors and
random values.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1816_number_theory.cpp](1816_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.015 s | 248 KB |
| [1816_number_theory.go](1816_number_theory.go) | Go 1.14 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.015 s | 2372 KB |
| [1816_number_theory.java](1816_number_theory.java) | Java 1.8 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.125 s | 2280 KB |
| [1816_number_theory.py](1816_number_theory.py) | Python 3.12 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.093 s | 708 KB |
| [1816_number_theory.rs](1816_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sum of d(m) over divisors m of n) | AC | 0.031 s | 324 KB |
