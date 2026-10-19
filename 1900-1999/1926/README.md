# 1926. Dynamic Remainders Through One Common Modulus

[Timus 1926](https://acm.timus.ru/problem.aspx?space=1&num=1926) · difficulty 997 · number_theory

Original problem by Alexander Onokhin and Bulat Zaynullin, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Maintain a positive decimal integer n under digit replacements and
remainder queries. Positions are numbered from 1 at the rightmost digit.
A replacement addresses an existing position, writes a digit 0..9 and
never makes the leading digit zero, so the decimal length stays fixed.
Each queried divisor c is either 1 or a product of distinct primes not
exceeding 47. Print each requested remainder after preceding updates.
Limits: 2 seconds, 64 MB.

## Input

The first line is n, 1≤n<10^100000, represented by up to 100000 decimal
digits. Then m, 1≤m≤10000. Each of the next m queries is either `0 c`
or `1 k b`, where k is the position from the right and b is the new digit.
c is positive and satisfies the distinct-prime condition; it can reach
614889782588491410 and requires 64-bit parsing.

## Output

For each type-0 query print n mod c on its own line, in query order.
Type-1 queries produce no output. If every query updates, output nothing.

## Checking

Compare the sequence of integer tokens exactly.

## Examples

```
4123456789897654321
5
0 1
0 7
0 10
1 2 9
0 6
```

```
0
0
1
5
```

## Solution

Let P be the product of all fifteen primes at most 47:
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47. Their product is
P=614889782588491410. Every permitted c divides P, including c=1.
Consequently, if R=n mod P, then n mod c=R mod c. Maintaining just
one residue suffices; no reconstruction from separate prime residues is needed.

Read n as text. Precompute W[j]=10^j mod P for j=0..D−1, where D is
the number of digits. Compute the initial R by decimal Horner steps:
replace R by (10R+digit) mod P while scanning from left to right.

Replacing the kth digit from the right changes the integer by
(new−old)·10^(k−1). Keep the current digits in a mutable array, retrieve
old at index D−k, write new, and update

```text
R = (R + (new−old)·W[k−1]) mod P, normalized to 0..P−1.
```

The update formula preserves R≡n mod P. Initial Horner computation
establishes this invariant, so induction proves it after every update.
For every query, divisibility c|P then gives the exact requested remainder.
Keeping the changed digit ensures repeated updates use the latest value.

### Arithmetic bounds

All operations fit signed 64-bit arithmetic. R and W lie in [0,P).
Horner and power-table steps are below 10P. Since new−old is in [−9,9],
the update expression lies strictly between −9P and 10P. In particular,
10P=6148897825884914100 is less than 2^63−1=9223372036854775807.
Convert operands to signed 64-bit before multiplying.

In languages with a negative remainder, first take `% P`, then add P
if the result is negative. Rust uses `rem_euclid`; Python's `%` already
normalizes. Neither a machine-sized conversion of n nor arbitrary-precision
arithmetic is required in the submitted programs.

O(D+m) time and O(D+m) total space including buffered queries and output.
The digit array and modular power table use O(D) working space.
Each replacement and remainder query takes O(1) fixed-width operations.

Use k−1 for the power and D−k for the text index. Read the current old
digit, not the initial one. Normalize negative updates after taking the
remainder. The distinct-prime condition is what ensures c divides P.
Factors 2 and 5 cause no issue because the algorithm never divides by 10
or uses its modular inverse. Parse large c as 64-bit, even for a tiny n.

## Language notes

C++, Go, Java and Rust use signed 64-bit residues, weights and divisors.
Java uses a buffered reader, and Go reads the large digit token through
a buffered reader without a fixed scanner-token limit. Python keeps the
initial number as text, avoiding the integer-string conversion limit.
All versions retain mutable digits and produce an empty result when needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1926_number_theory.cpp](1926_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(D+m) | AC | 0.015 s | 1692 KB |
| [1926_number_theory.go](1926_number_theory.go) | Go 1.14 x64 | number_theory | O(D+m) | AC | 0.046 s | 3652 KB |
| [1926_number_theory.java](1926_number_theory.java) | Java 1.8 | number_theory | O(D+m) | AC | 0.125 s | 3464 KB |
| [1926_number_theory.py](1926_number_theory.py) | Python 3.12 x64 | number_theory | O(D+m) | AC | 0.171 s | 6808 KB |
| [1926_number_theory.rs](1926_number_theory.rs) | Rust 1.75 x64 | number_theory | O(D+m) | AC | 0.046 s | 1684 KB |
