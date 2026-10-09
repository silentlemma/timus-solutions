# 1055. The number of prime divisors of a binomial coefficient

[Timus 1055](https://acm.timus.ru/problem.aspx?space=1&num=1055) · difficulty 422 · number_theory

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `1 ≤ M < N ≤ 50000`, find how many different primes divide the
binomial coefficient `C(N, M) = N! / (M! · (N − M)!)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`.

## Output

The number of different prime divisors of `C(N, M)`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
2
```

### Example 2

Input:

```
10 5
```

Output:

```
3
```

## Solution

`C(N, M)` has tens of thousands of digits, so it is never computed. Only
primes up to `N` can divide it, and the exponent of a prime `p` in `x!` is
given by Legendre's formula:

```text
e_p(x!) = ⌊x/p⌋ + ⌊x/p²⌋ + ⌊x/p³⌋ + …
```

so `p` divides `C(N, M)` exactly when
`e_p(N!) − e_p(M!) − e_p((N − M)!) > 0`. A sieve of Eratosthenes lists the
primes up to `N`, and each prime takes `O(log N)` divisions:
`O(N log log N)` in total.

Pitfalls:

- the factorials themselves overflow at once: work with exponents only;
- every prime up to `N` must be checked, also those above `N / 2`;
- `M = N − 1` gives `C = N`, whose prime divisors are just those of `N`.

An equivalent test is Kummer's theorem: `p` divides `C(N, M)` exactly
when adding `M` and `N − M` in base `p` produces a carry. The tests were
checked with it and, for `N ≤ 3000`, by factoring the exact coefficient.

## Language notes

- All languages use the same sieve; Python marks the multiples of a prime
  with one slice assignment on a `bytearray`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1055_number_theory.cpp](1055_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 184 KB |
| [1055_number_theory.go](1055_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.015 s | 1112 KB |
| [1055_number_theory.java](1055_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.093 s | 1680 KB |
| [1055_number_theory.py](1055_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.078 s | 580 KB |
| [1055_number_theory.rs](1055_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.031 s | 268 KB |
