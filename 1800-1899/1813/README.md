# 1813. Random Shuffler

[Timus 1813](https://acm.timus.ru/problem.aspx?space=1&num=1813) · difficulty 1570 · number_theory

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The sequence x₀ = 0, xᵢ = (a·xᵢ₋₁ + b) mod m must pass through every
number from 0 to m − 1 once in its first m terms and come back to 0.
Over all pairs (a, b) with 0 ≤ a, b < m that do so, find the average of
a, rounded down.

## Input

Up to 100 lines, each with m (1 < m < 10⁹).

## Output

For each m, the average rounded down.

## Examples

### Example 1

Input:

```
2
36
100
123
```

Output:

```
1
13
41
1
```

## Solution

The sequence must be a single cycle of length m, the full period of a
linear congruential generator. By the Hull–Dobell theorem that happens
exactly when b is coprime to m, a − 1 is divisible by every prime
factor of m, and a − 1 is divisible by 4 if m is. So with c the product
of the distinct primes of m, doubled when 4 divides m, the good values
of a are 1, 1 + c, 1 + 2c, …, below m: m/c of them, since c divides m.
The number of good b does not depend on a, so the average over pairs
is the average of this progression, (m − c + 2)/2. Factoring m by trial
division up to √m takes `O(√m)` per value.

For m = 36 = 2²·3², c = 2·3·2 = 12 and a is 1, 13 or 25, with the
average 13. For m = 123 = 3·41, c = 123 and only a = 1 works.

Pitfalls:

- the extra factor 2 for multiples of 4: for m = 4 the value a = 3
  fails;
- the average over pairs equals the average over a only because every
  good a has the same number of good b;
- a = 0 never works, since then the sequence repeats b.

The answers agree with a full simulation of every pair (a, b) for all m
from 2 to 60, and with an independent accepted implementation on random
values, products of small primes, large primes and their squares.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1813_number_theory.cpp](1813_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(m)) per value | AC | 0.015 s | 128 KB |
| [1813_number_theory.go](1813_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 1104 KB |
| [1813_number_theory.java](1813_number_theory.java) | Java 1.8 | number_theory | O(sqrt(m)) per value | AC | 0.078 s | 528 KB |
| [1813_number_theory.py](1813_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(m)) per value | AC | 0.093 s | 704 KB |
| [1813_number_theory.rs](1813_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(m)) per value | AC | 0.031 s | 232 KB |
