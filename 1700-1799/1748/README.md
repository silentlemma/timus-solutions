# 1748. The Most Complex Number

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · difficulty 266 · number_theory

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The complexity of a number is the number of its divisors. For each
given n, find the most complex number from 1 to n, the smallest one if
several tie, and its complexity.

## Input

t (1 ≤ t ≤ 100), then t numbers n (1 ≤ n ≤ 10¹⁸).

## Output

For each n, the number and its number of divisors.

## Examples

### Example 1

Input:

```
5
1
10
100
1000
10000
```

Output:

```
1 1
6 4
60 12
840 32
7560 64
```

## Solution

The number of divisors of p₁^a₁ · p₂^a₂ · … is (a₁ + 1)(a₂ + 1)…, which
depends only on the exponents. Putting the largest exponents on the
smallest primes gives the smallest number with those exponents, so the
answer is always of the form 2^a · 3^b · 5^c · … with
a ≥ b ≥ c ≥ … on consecutive primes. There are only a few tens of
thousands of such numbers up to 10¹⁸, and the primes needed stop
before 53, since 2 · 3 · … · 53 is already above 10¹⁸.

List them all by a search over the exponents, sort them, and walk up
keeping the best so far: a number replaces the best only with strictly
more divisors, which keeps the smallest on ties. Each query is then a
binary search for the last listed number not above n.
`O(K log K + t log K)` for the K = 32 749 listed numbers.

For n = 100 the answer is 60 = 2² · 3 · 5 with 3 · 2 · 2 = 12 divisors.

Pitfalls:

- products near 10¹⁸ overflow 64 bits unless the bound is checked by
  division before multiplying;
- on ties the smaller number wins: 2 and 3 both have two divisors.

The answers match a sieve of divisor counts for every query of 100
random numbers up to 20 000, and an independent accepted implementation
on 30 random tests up to 10¹⁸ and around record holders.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1924 KB |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.156 s | 6608 KB |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB |
