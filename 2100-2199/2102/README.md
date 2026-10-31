# 2102. Does a number have exactly twenty prime factors

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · difficulty 147 · number_theory

Original problem by Vladimir Leskov, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tell whether the prime factorisation of n has exponents adding up to
exactly 20, that is whether n is a product of exactly 20 primes counted
with multiplicity. The limits are 2 seconds and 64 MB.

## Input

n, 1 ≤ n ≤ 10¹⁸.

## Output

`Yes` or `No`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
No
```

### Example 2

Input:

```
1048576
```

Output:

```
Yes
```

### Example 3

Input:

```
10000000000
```

Output:

```
Yes
```

## Solution

Divide n by every d from 2 up to B = 2·10⁶ while d² ≤ n, counting the
prime factors removed. If the loop stops because d² exceeds what is
left, the rest is 1 or a prime and adds 0 or 1. Otherwise the rest is at
least B² = 4·10¹², so the removed part is at most 10¹⁸ / B², less than
2¹⁸, which means fewer than 18 factors so far; the rest has no factor
below B and is at most 10¹⁸ < B³, so it adds at most two. The total
cannot reach 20, and the answer is No. The work is O(min(sqrt n, B)).

In the third example 10¹⁰ = 2¹⁰ · 5¹⁰ has 20 prime factors.

## Optimized solutions

The optimized Java solution parses n by hand from a 4 KB buffer filled
from `System.in` instead of creating a `Scanner`, so the JVM does not
load the scanner and its regular expressions; n up to 10¹⁸ fits in
`long`, and the trial division is the same:
{2102_number_theory_optimized.java}.

The optimized Python solution counts down the prime factors still needed
and stops as soon as the answer is known. Every prime below the current
divisor has been divided out, so all factors left are at least the
divisor: while more than two are needed and the divisor raised to their
number exceeds what is left of n, the answer is No at once, which
settles a large prime n after a handful of divisions. Once at most two
factors are needed, at least 18 are removed, so what is left is at most
10¹⁸ / 2¹⁸ and the division stops at its square root, at most 1 953 125,
without the bound B. After 2 it tries only odd divisors:
{2102_number_theory_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2102_number_theory_optimized.java`: time reduction -12.00%; memory
  reduction +74.87%; base: `2102_number_theory.java`.

- `2102_number_theory_optimized.py`: time reduction +41.50%; memory
  reduction -9.28%; base: `2102_number_theory.py`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2102_number_theory.rs](2102_number_theory.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 116 KB | 11304072 |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB | 11294722 |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.125 s | 1592 KB | 11304073 |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.453 s | 388 KB | 11304074 |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB | 11294726 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory_optimized.java](2102_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.140 s | 400 KB | 11304532 |
| [2102_number_theory_optimized.py](2102_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.265 s | 424 KB | 11304531 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
