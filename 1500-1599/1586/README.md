# 1586. Threeprime Numbers

[Timus 1586](https://acm.timus.ru/problem.aspx?space=1&num=1586) · difficulty 144 · dp

Original problem by Denis Musin, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number is threeprime when every three neighbouring digits form a
three-digit prime. Count the n-digit threeprime numbers
(3 ≤ n ≤ 10000) modulo 10⁹ + 9.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n.

## Output

The count modulo 10⁹ + 9.

## Examples

### Example 1

Input:

```
4
```

Output:

```
204
```

## Solution

Whether a digit can follow depends only on the last two digits, so
count the numbers by them. For n = 3 every three-digit prime counts
once, under its last two digits. Each further digit c appends to a
number ending in ab exactly when abc is a three-digit prime, and the
new number ends in bc. The 143 three-digit primes give 143 transitions
per digit: `O(143·n)`. The results were checked against testing every
number of up to six digits.

Pitfalls:

- a three-digit prime cannot start with 0, so no window may start with a
  zero digit either; counting by the primes themselves takes care of it;
- the count overflows quickly and is taken modulo 10⁹ + 9, not
  10⁹ + 7.

## Optimized solutions

The optimized C++ solution stores the two-digit start and end of every
prime transition once, in fixed arrays, instead of taking `p / 10` and
`p % 100` again at every digit, and reuses two fixed arrays of counts
instead of a new `vector` for every digit. The counts are `int` instead
of `long long`, and each addition is reduced by one conditional
subtraction instead of `%`: two residues below 10⁹ + 9 add up to less
than 2³¹: {1586_dp_optimized.cpp}.

The optimized Go solution stores the two-digit start and end of every
prime transition once, in fixed arrays, and reuses two fixed arrays of
counts instead of a new slice for every digit; each addition is reduced
by one conditional subtraction instead of `%`: {1586_dp_optimized.go}.

The optimized Java solution reads `n` byte by byte with `System.in.read`
instead of a `Scanner`, stores the two-digit start and end of every
prime transition in `int` arrays instead of iterating over a list of
boxed `Integer` primes, and swaps two count arrays instead of allocating
a new one for every digit. The counts are `int` instead of `long`, and
each addition is reduced by one conditional subtraction instead of `%`:
two residues below 10⁹ + 9 add up to less than 2³¹:
{1586_dp_optimized.java}.

For `n = 3` the optimized Python solution prints the number of
three-digit primes, 143. For `n ≥ 4` it raises a transition matrix to a
power instead of stepping through all `n` digits. From the fourth digit
on, both of the last two digits end a three-digit prime, so each is 1,
3, 7 or 9 and only 16 pairs remain; a 16 × 16 matrix counts the primes
leading from one pair to another. The counts for four digits times this
matrix to the power `n − 4`, computed by repeated squaring with at most
14 squarings for `n ≤ 10000`, give the answer, `O(16³ log n)` in all:
{1586_dp_matrix.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1586_dp_optimized.cpp`: time reduction +0.00%; memory reduction
  +47.06%; base: `1586_dp.cpp`.

- `1586_dp_optimized.go`: time reduction +0.00%; memory reduction
  +83.27%; base: `1586_dp.go`.

- `1586_dp_optimized.java`: time reduction +36.26%; memory reduction
  +93.08%; base: `1586_dp.java`.

- `1586_dp_matrix.py`: time reduction +76.15%; memory reduction -44.26%;
  base: `1586_dp.py`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1586_dp.rs](1586_dp.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1586_dp.cpp](1586_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 204 KB | 11287946 |
| [1586_dp.go](1586_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 6456 KB | 11287947 |
| [1586_dp.java](1586_dp.java) | Java 1.8 | dp | O(n) | AC | 0.171 s | 6072 KB | 11287950 |
| [1586_dp.py](1586_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.390 s | 488 KB | 11287948 |
| [1586_dp.rs](1586_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.015 s | 240 KB | 11287953 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1586_dp_optimized.cpp](1586_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 108 KB | 11304491 |
| [1586_dp_optimized.go](1586_dp_optimized.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 1080 KB | 11304492 |
| [1586_dp_optimized.java](1586_dp_optimized.java) | Java 1.8 | dp | O(n) | AC | 0.109 s | 420 KB | 11304525 |
| [1586_dp_matrix.py](1586_dp_matrix.py) \* | Python 3.12 x64 | dp, matrix | O(16³ log n) | AC | 0.093 s | 704 KB | 11304526 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
