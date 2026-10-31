# 1206. Pairs of numbers whose digit sums add up

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · difficulty 124 · combinatorics

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let `S(N)` be the digit sum of `N`. For `2 ≤ K ≤ 50`, count the ordered
pairs of `K`-digit numbers `A` and `B`, without leading zeros, with
`S(A + B) = S(A) + S(B)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`.

## Output

The number of pairs.

## Examples

### Example 1

Input:

```
2
```

Output:

```
1980
```

## Solution

Every carry in the addition turns a 10 in one position into a 1 in the
next, lowering the digit sum by 9. So the equality holds exactly when no
position carries, that is when the digits in each position add up to at
most 9. The positions are then independent. In the leading position both
digits are from 1 to 9, which allows `8 + 7 + … + 1 = 36` pairs; in each
of the other `K − 1` positions the digits are from 0 to 9, which allows
`10 + 9 + … + 1 = 55` pairs. The answer is `36 · 55^(K−1)`, a number of
up to 87 digits. `O(K²)` with schoolbook multiplication.

Pitfalls:

- the answer outgrows 64 bits already at `K = 12`;
- the leading digits cannot be 0, so their count differs from the
  others.

The formula was checked by brute force over all pairs for `K = 2` and
`K = 3`, and every `K` was compared with a separately written solution.

## Optimized solutions

The optimized C++ solution multiplies the same decimal digits by 55, but
in a fixed array of 100 entries on the stack instead of a growing
`std::vector`: since `K ≤ 50`, the answer `36 · 55^(K−1)` is below
`100^K` and has at most 100 digits (in fact at most 87). Without
`<vector>` the program carries no container code at all:
{1206_combinatorics_optimized.cpp}.

The optimized Java solution reads `K` byte by byte from `System.in`
instead of creating a `Scanner`, whose regular expressions and locale
data cost more than the power itself; the answer is still computed with
`BigInteger`: {1206_combinatorics_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1206_combinatorics_optimized.cpp`: time reduction +0.00%; memory
  reduction +46.81%; base: `1206_combinatorics.cpp`.

- `1206_combinatorics_optimized.java`: time reduction +10.71%; memory
  reduction +74.37%; base: `1206_combinatorics.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1206_combinatorics.rs](1206_combinatorics.rs).

- Python uses its own integers, Go `math/big` and Java `BigInteger`;
  C++ and Rust multiply a decimal digit array by 55 `K − 1` times.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(K²) | AC | 0.125 s | 448 KB | 11304422 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
