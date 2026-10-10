# 1118. The number with the smallest sum of proper divisors per unit

[Timus 1118](https://acm.timus.ru/problem.aspx?space=1&num=1118) · difficulty 103 · number_theory

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The ratio of a positive integer `N` is the sum of its proper divisors
(those below `N`) divided by `N`. For `1 ≤ I ≤ J ≤ 10^6`, print a number
in `[I, J]` with the smallest ratio.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`I J` on one line.

## Output

The number with the smallest ratio.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
24 28
```

Output:

```
25
```

## Solution

The number 1 has no proper divisors, ratio 0, and wins whenever `I = 1`.
A prime `p` has ratio `1/p`, so among primes the largest is best. It also
beats every composite `n ≤ J` in the range: a composite has a divisor
`d ≥ √n` besides 1, so its ratio is at least `(1 + √n)/n`, and the largest
prime below `J` is above `J/2` (Bertrand's postulate), which makes `1/p`
smaller. So scan down from `J` and stop at the first prime.

Only when the range holds no prime at all must the ratios be compared; such
a range lies inside a prime gap, at most 113 numbers below `10^6`. Each
divisor sum takes `O(√n)` by trial division, and two ratios are compared
exactly as `σ(a)·b < σ(b)·a`, the smaller number winning a tie. In all,
`O(g · √J)` for the longest gap `g`.

Pitfalls:

- `I = 1` must answer 1, not the largest prime;
- in a range without primes the best number need not be the largest, nor a
  square: `[24, 28]` gives 25, `[8, 10]` gives 9;
- comparing ratios in floating point is unnecessary, the cross product
  fits in 64 bits.

The answers were checked against a sieve of the divisor sums of every
number up to `10^6` with an exact comparison over the whole range, on
every test, on 200 random ranges below 3000 and on the longest prime gap
below a million.

## Language notes

- All languages use the same trial division.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1118_number_theory.cpp](1118_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.015 s | 128 KB |
| [1118_number_theory.go](1118_number_theory.go) | Go 1.14 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 1060 KB |
| [1118_number_theory.java](1118_number_theory.java) | Java 1.8 | number_theory | O(g · √J), g ≤ 114 | AC | 0.109 s | 1552 KB |
| [1118_number_theory.py](1118_number_theory.py) | Python 3.12 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.093 s | 440 KB |
| [1118_number_theory.rs](1118_number_theory.rs) | Rust 1.75 x64 | number_theory | O(g · √J), g ≤ 114 | AC | 0.031 s | 212 KB |
