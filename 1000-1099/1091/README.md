# 1091. Counting sets of numbers with a common divisor

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · difficulty 526 · number_theory

Original problem by Stanislav Vasiliev, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the sets of `K` different positive integers, none larger than `S`
(`2 ≤ K ≤ S ≤ 50`), whose greatest common divisor is larger than 1. Print
the count, or 10000 if it is larger than that.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K` and `S`.

## Output

The number of sets, at most 10000.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 10
```

Output:

```
11
```

## Solution

The sets whose numbers are all multiples of `d` number `C(⌊S/d⌋, K)`. A
set with a common divisor larger than 1 has a common prime divisor, so
the answer is the size of the union of these families over the primes.
Inclusion–exclusion over the square-free `d > 1` gives

`answer = Σ −μ(d) · C(⌊S/d⌋, K)`,

where the Möbius function `μ(d)` is `(−1)^(number of prime factors)` for
square-free `d` and 0 otherwise: products of an odd number of primes are
added and of an even number subtracted. A small sieve computes `μ` up to
`S`, and the binomials come from Pascal's triangle. `O(S²)`.

Pitfalls:

- the true count can be far above 10000, for example `C(25, 5)` sets of
  even numbers alone for `K = 5`, so only the final value is capped and
  the sums are kept in 64 bits;
- a set counted for `d = 2` and for `d = 3` is also counted for `d = 6`,
  which is why the signs alternate;
- the numbers must be different, so `C(m, K)` is 0 when `m < K`.

The answers were checked for every pair `K ≤ S ≤ 50` against counts of
sets with gcd exactly `g`, found from the largest `g` down by subtracting
the counts for multiples of `g`, and for `S ≤ 20` by listing all sets.

## Language notes

- Python uses `math.comb`; the other languages fill a table of binomial
  coefficients.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB |
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB |
| [1091_number_theory.py](1091_number_theory.py) | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB |
