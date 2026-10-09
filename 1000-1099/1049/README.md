# 1049. The last digit of the number of divisors of a product

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · difficulty 249 · number_theory

Original problem by Stanislav Vasiliev, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Ten integers `a1 … a10` are given, each from 1 to 10000. Find the last
digit of the number of positive divisors of the product `a1 · … · a10`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Ten integers, one per line.

## Output

One digit: the last digit of the number of divisors.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1
2
6
1
3
1
1
1
1
1
```

Output:

```
9
```

### Example 2

Input:

```
1
1
1
1
1
1
1
1
1
1
```

Output:

```
1
```

## Solution

If `P = p1^e1 · p2^e2 · … · pk^ek`, a divisor of `P` chooses each
exponent independently from `0` to `ei`, so `P` has
`(e1 + 1)(e2 + 1)…(ek + 1)` divisors.

The product itself can have 40 digits, but it is never needed: factor
each number by trial division up to its square root (at most 100 steps),
add the exponents of equal primes, and multiply the `(e + 1)` modulo 10.
`O(10 · √10000)`.

Pitfalls:

- the exponents must be added over all ten numbers before the `+ 1`:
  `2 · 2` has 3 divisors, not `2 · 2`;
- a prime factor larger than the square root remains after the trial
  division and still counts;
- the last digit may be 0 (48 = `2^4 · 3` has 10 divisors).

## Language notes

- All languages use the same trial division and a map from primes to
  exponents.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB |
