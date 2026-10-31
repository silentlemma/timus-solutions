# 1044. Counting balanced tickets of N digits

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · difficulty 123 · bruteforce

Original problem by Stanislav Vasiliev, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket number has `N` digits (`N` is even, `2 ≤ N ≤ 8`; leading zeros
are allowed). It is balanced when the first half of the digits and the
second half have equal sums. Count the balanced tickets.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of balanced tickets.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
```

Output:

```
670
```

### Example 2

Input:

```
2
```

Output:

```
10
```

## Solution

The halves are independent. Count, for every sum `s`, how many numbers
below `10^(N/2)` have digit sum `s`: at most 10000 numbers to look at.
A balanced ticket is a pair of halves with the same sum, so the answer is
the sum of `ways[s]^2` over all `s`. `O(10^(N/2) · N)`.

For `N = 8` the answer is 4816030, which fits in 32 bits, but outside
Python the squares are summed in 64-bit integers anyway.

Pitfalls:

- leading zeros count: `0000` is a ticket;
- the halves have `N / 2` digits each, not `N`.

[Problem 1036](../1036/README.md) asks the same for up to 100 digits and
a fixed total sum; there the counts come from a DP and need big integers.

## Optimized solutions

The optimized C++ solution keeps the counts in a fixed array of
37 entries on the stack instead of a `std::vector`: since `N ≤ 8`, a
half has at most four digits and a digit sum of at most 36. The program
then needs no container library at all: {1044_bruteforce_optimized.cpp}.

The optimized Java solution reads `N` byte by byte from `System.in`
instead of creating a `Scanner`, whose regular expressions and locale
data cost more than the count itself; the count is the same:
{1044_bruteforce_optimized.java}.

The fast Go version uses digit-sum DP instead of enumerating all halves. Appending a digit convolves the current counts with ten ones; a sliding sum computes each new count in constant time. After `N/2` steps, summing the squared counts gives the same answer. Time is `O(N²)`, auxiliary memory `O(N)`. The enumeration remains the base implementation.

{1044_dp.go}.

Source-matched Accepted runs: base 0.046 s / 1080 KB; this version 0.015 s / 804 KB (submission 11307438). The rating target is met in the 2026-10-31 snapshot.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1044_bruteforce_optimized.cpp`: time reduction +0.00%; memory
  reduction +36.73%; base: `1044_bruteforce.cpp`.

- `1044_dp.go`: time reduction +67.39%; memory reduction +25.56%; base:
  `1044_bruteforce.go`.

- `1044_bruteforce_optimized.java`: time reduction +16.13%; memory
  reduction +79.64%; base: `1044_bruteforce.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1044_bruteforce.rs](1044_bruteforce.rs).

- All languages run the same count; Python takes digit sums of
  `str(x)`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB | 11278614 |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB | 11278618 |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB | 11278622 |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB | 11278621 |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB | 11278623 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1044_bruteforce_optimized.cpp](1044_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.001 s | 124 KB | 11304375 |
| [1044_dp.go](1044_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.015 s | 804 KB | 11307438 |
| [1044_bruteforce_optimized.java](1044_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 316 KB | 11304376 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
