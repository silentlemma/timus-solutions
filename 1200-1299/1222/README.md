# 1222. The highest product of numbers with a given sum

[Timus 1222](https://acm.timus.ru/problem.aspx?space=1&num=1222) · difficulty 144 · math

Original problem: folklore, proposed by Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A group of eagles with `1 ≤ N ≤ 3000` heads in total has an IQ equal to
the product of the head counts of its eagles. Find the largest possible
IQ; in other words, the largest product of positive integers that add up
to `N`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The largest product.

## Examples

### Example 1

Input:

```
5
```

Output:

```
6
```

## Solution

A part of 4 or more can be split into 2 and the rest without lowering the
product, and a part of 5 or more raises it that way (`2(k − 2) > k` for
`k > 4`), while a part of 1 only wastes a head. So an optimal split uses
only 2s, 3s and 4s, and a 4 is the same as 2 + 2. Three 2s are worse than
two 3s (`8 < 9`), so there are at most two 2s. That leaves: all 3s when
`3` divides `N`, one 2 more when the remainder is 2, and two 2s (or one
4) instead of a 3 when the remainder is 1. For `N` up to 3 the eagle
alone is best. The product has up to 478 digits. `O(N²)` digit
operations for the repeated multiplication by 3.

Pitfalls:

- `N = 1` gives 1, and `N = 4` gives 4;
- a remainder of 1 must not be kept as a factor of 1;
- the answer is far beyond 64 bits.

The answers were checked against a brute force over all splits for every
`N` up to 59, and compared with a separately written solution on every
test.

## Optimized solutions

The optimized C++ solution multiplies a fixed global array of 1000
decimal digits instead of a `std::vector` that grows with the product,
so the program needs no dynamic memory; for `N ≤ 3000` the product has
at most 478 digits: {1222_math_optimized.cpp}.

The optimized Java solution reads the single number byte by byte with
`System.in.read` instead of creating a `Scanner`, so the JVM does not
load the scanner and its regular expressions; the `BigInteger` power is
the same: {1222_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1222_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +45.83%; base: `1222_math.cpp`.

- `1222_math_optimized.java`: time reduction -34.41%; memory reduction
  +71.66%; base: `1222_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1222_math.go](1222_math.go).
- [1222_math.rs](1222_math.rs).

- Python uses its own integers, Go `math/big` and Java `BigInteger`;
  C++ and Rust multiply a decimal digit array by 3 again and again.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 192 KB | 11283695 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1184 KB | 11283696 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.093 s | 1708 KB | 11283698 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 396 KB | 11283697 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 208 KB | 11283699 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 104 KB | 11304484 |
| [1222_math_optimized.java](1222_math_optimized.java) \* | Java 1.8 | math | O(N²) | AC | 0.125 s | 484 KB | 11304486 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
