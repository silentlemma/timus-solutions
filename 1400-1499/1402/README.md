# 1402. Cocktails

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · difficulty 130 · combinatorics

Original problem by Sergey Pupyrev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cocktail mixes two or more of N ≤ 21 drinks, each at most once, and
the order of the drinks matters. Count the different cocktails.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N (1 ≤ N ≤ 21).

## Output

The number of cocktails.

## Examples

### Example 1

Input:

```
3
```

Output:

```
12
```

## Solution

A cocktail of k drinks is an ordered choice of k different drinks, and
there are N·(N − 1)·…·(N − k + 1) of them. Add these for k from 2 to N,
building each product from the previous one. `O(N)`.

Pitfalls:

- with one drink there is no cocktail at all (test 02);
- for N = 21 the answer is about 1.4·10²⁰, past 64 bits, so the
  solutions use 128-bit or big integers (test 07).

The tests are judged by exact comparison.

## Optimized solutions

The optimized C++ solution sums in the same 128-bit integer but writes
the digits backwards into a fixed array of 23 characters instead of
inserting each one at the front of an `std::string`: since `N ≤ 21`, the
answer is below 21·21! < 10²², so 22 digits and the terminating zero
always fit. Without `<string>` the program itself allocates nothing on
the heap: {1402_combinatorics_optimized.cpp}.

The optimized Java solution reads N byte by byte from `System.in`
instead of creating a `Scanner`, whose regular expressions and locale
data cost more than the at most twenty multiplications; the sum is still
a `BigInteger`: {1402_combinatorics_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1402_combinatorics_optimized.cpp`: time reduction +0.00%; memory
  reduction +48.94%; base: `1402_combinatorics.cpp`.

- `1402_combinatorics_optimized.java`: time reduction +0.00%; memory
  reduction +73.70%; base: `1402_combinatorics.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1402_combinatorics.go](1402_combinatorics.go).
- [1402_combinatorics.rs](1402_combinatorics.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB | 11286026 |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB | 11286027 |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB | 11286031 |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB | 11286029 |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB | 11286032 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1402_combinatorics_optimized.cpp](1402_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.001 s | 96 KB | 11304432 |
| [1402_combinatorics_optimized.java](1402_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 444 KB | 11304433 |
