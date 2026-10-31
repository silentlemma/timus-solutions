# 1582. Bookmakers

[Timus 1582](https://acm.timus.ru/problem.aspx?space=1&num=1582) · difficulty 123 · math

Original problem by Sergey Pupyrev, prepared by Vladimir Yakovlev, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A match has three outcomes with the best odds k₁, k₂ and k₃ (0.01 …
100): a bet of x on the right outcome pays k·x, a wrong one pays
nothing. Split bets totalling 1000 pounds over the three outcomes so as
to get back the most in the worst case, and print that amount rounded to
the nearest integer.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k₁, k₂ and k₃.

## Output

The guaranteed payout, rounded.

## Examples

### Example 1

Input:

```
3.5 3.5 3.5
```

Output:

```
1167
```

### Example 2

Input:

```
1.25 10.0 5.75
```

Output:

```
931
```

## Solution

Bet xᵢ on outcome i, with x₁ + x₂ + x₃ = 1000; outcome i pays kᵢ·xᵢ. To
guarantee a payout P, every outcome must pay at least P, so xᵢ ≥ P / kᵢ,
and adding the three inequalities gives 1000 ≥ P·(1/k₁ + 1/k₂ + 1/k₃).
The bets xᵢ = P / kᵢ reach this bound, so the best guaranteed payout is

P = 1000 / (1/k₁ + 1/k₂ + 1/k₃).

Read each decimal exactly as a / 10ˢ. Starting with N = 1 and D = 0,
for each odd update D = D·a + N·10ˢ, then N = N·a. Now P = 1000·N / D.
Use arbitrary-length integers and binary-search the largest integer m
such that 2·1000·N ≥ (2m − 1)·D; this rounds exact halves up without
floating-point error. The answer is at most ⌊1000·100 / 3⌋, so the search
takes a constant number of steps. With L decimal digits in the input
(after expanding any exponent), time is `O(L^2)` and space is `O(L)`.

Pitfalls:

- with odds above 3 each, the guaranteed payout is more than the
  stake, as in the first example;
- an exact half rounds up: odds 2, 10 and 25 give 1562.5 and the answer
  1563, while `printf("%.0f")` would round to even and print 1562
  (test 08);
- binary floating point can turn an exact half into a value just below
  it: odds 0.02, 0.02 and 0.03 give exactly 7.5, so the answer is 8
  (test 10). Decimal precision is not bounded, so use exact arithmetic
  rather than adding an epsilon.

## Optimized solutions

The optimized Java solution reads the three odds with `BufferedReader`
and `StringTokenizer` instead of a `Scanner`, avoiding its regular
expressions and locale data. The arithmetic stays exact, with the odds
in `BigDecimal` and the comparisons in `BigInteger`, so only reading the
input gets cheaper: {1582_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1582_math_optimized.java`: time reduction +14.68%; memory reduction
  +57.08%; base: `1582_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1582_math.go](1582_math.go).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1582_math.cpp](1582_math.cpp) | G++ 13.2 x64 | math | O(L^2) | AC | 0.031 s | 388 KB | 11304410 |
| [1582_math.go](1582_math.go) | Go 1.14 x64 | math | O(L^2) | AC | 0.031 s | 1192 KB | 11298030 |
| [1582_math.java](1582_math.java) | Java 1.8 | math | O(L^2) | AC | 0.109 s | 1780 KB | 11304013 |
| [1582_math.py](1582_math.py) | Python 3.12 x64 | math | O(L^2) | AC | 0.078 s | 532 KB | 11304014 |
| [1582_math.rs](1582_math.rs) | Rust 1.75 x64 | math | O(L^2) | AC | 0.046 s | 212 KB | 11304419 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1582_math_optimized.java](1582_math_optimized.java) | Java 1.8 | math | O(L^2) | AC | 0.093 s | 764 KB | 11304379 |
