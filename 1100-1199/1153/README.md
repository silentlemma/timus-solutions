# 1153. Recovering N from the sum 1 + 2 + … + N with up to 600 digits

[Timus 1153](https://acm.timus.ru/problem.aspx?space=1&num=1153) · difficulty 332 · math

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A computer added up the integers from 1 to `N`, `0 < N < 10³⁰⁰`, and
printed the sum `S`, but `N` is lost. Given `S`, which is always such a
sum, find `N`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`S`.

## Output

`N`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
28
```

Output:

```
7
```

## Solution

`S = N(N + 1)/2`, so `8S + 1 = 4N² + 4N + 1 = (2N + 1)²` is a perfect
square, and `N = (√(8S + 1) − 1) / 2`. The only difficulty is size: `S`
has up to 600 digits, so the square root needs big integers.

The long-hand method from school works digit by digit and needs only
multiplication by small numbers, addition, comparison and subtraction.
Split `8S + 1` into pairs of digits from the right. Keep the root found
so far, `r`, and a remainder. For each next pair, append it to the
remainder (multiply by 100 and add), then find the largest digit `x` with
`(20r + x)·x` not above the remainder, subtract that product, and append
`x` to the root. After the last pair the root is `2N + 1`; subtract one
and halve it from the top digit down. With about 300 pairs and at most
nine tries each over numbers of 600 digits, this is a few million digit
operations.

Pitfalls:

- `S` does not fit in any machine integer, nor does `N`;
- `8S + 1` may have an odd number of digits; a leading zero makes the
  pairs line up;
- `N = 1` gives `S = 1`, and the root of `9` is `3`.

The answers were checked on every test by computing `N(N + 1)/2` back
with Python integers.

## Optimized solutions

Both versions invert the same identity 8S + 1 = (2N + 1)² with an exact integer square root. Go uses fixed decimal arrays and brings down pairs of digits. For the root prefix r, it chooses the largest digit x with (20r + x)x at most the remainder, subtracts that contribution and appends x. It then subtracts one and halves the root. This takes O(L²) time and O(L) space, without general-purpose big integers or temporary strings. Python starts above the root at a power of two and applies integer Newton steps until they stop decreasing. With L input digits, O(L² log(L+1)) is a conservative bound using quadratic division.

The accepted base implementations [1153_math.cpp](1153_math.cpp), [1153_math.java](1153_math.java), [1153_math.rs](1153_math.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1153_math_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer. For this Java implementation, use the same conservative bound as the existing Python Newton variant: O(L² log(L+1)) with quadratic big-integer division, where L is the decimal input length. Starting above the square root gives O(log(L+1)) Newton steps; each divides numbers of O(L) digits. This clarifies the complexity for both the unchanged simple Java code and the new input-only variant.

Compared with `1153_math.java`: time 0.140 s → 0.125 s; memory 1676 KB → 736 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1153_math_implementation_optimized.rs`. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328983 (Rust 1.75 x64): **0.031 s / 356 KB**. Archived comparison: `1153_math.rs` (Rust 1.75 x64) — 0.046 s / 456 KB (#11280829).

## Language notes

These notes describe the simple implementations.

- Python uses `math.isqrt` on its built-in integers and Go uses
  `big.Int.Sqrt`.
- Java 8 has no `BigInteger.sqrt`, so it runs Newton's method,
  `x ← (x + D/x)/2`, from a power of two above the root.
- C++ and Rust have no big integers in the standard library and run the
  long-hand square root on decimal digits.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1153_math.cpp](1153_math.cpp) | G++ 13.2 x64 | math | O(L²) | AC | 0.015 s | 504 KB | 11280703 |
| [1153_math.go](1153_math.go) | Go 1.14 x64 | math | O(L²) | AC | 0.031 s | 1212 KB | 11280739 |
| [1153_math.java](1153_math.java) | Java 1.8 | math | O(L² log(L+1)) | AC | 0.140 s | 1676 KB | 11280808 |
| [1153_math.py](1153_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.093 s | 480 KB | 11280773 |
| [1153_math.rs](1153_math.rs) | Rust 1.75 x64 | math | O(L²) | AC | 0.046 s | 456 KB | 11280829 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1153_math_greedy.go](1153_math_greedy.go) \* | Go 1.14 x64 | math, greedy | O(L²) | AC | 0.031 s | 800 KB | 11311117 |
| [1153_math_optimized.py](1153_math_optimized.py) | Python 3.12 x64 | math | O(L² log(L+1)) | AC | 0.093 s | 408 KB | 11311055 |
| [1153_math_optimized.java](1153_math_optimized.java) | Java 1.8 | math | O(L² log(L+1)) | AC | 0.125 s | 736 KB | 11324796 |
| [1153_math_implementation_optimized.rs](1153_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(L²) | AC | 0.031 s | 356 KB | 11328983 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
