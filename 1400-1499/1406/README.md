# 1406. Next Number

[Timus 1406](https://acm.timus.ru/problem.aspx?space=1&num=1406) · difficulty 344 · greedy

Original problem by Alexander Ipatov, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A K-digit number N, K ≤ 2000, possibly with leading zeros, is given.
Print the smallest K-digit number greater than N with the same sum of
digits, again with leading zeros, or -1 if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N with all its K digits.

## Output

The next number, or -1.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
113
```

Output:

```
122
```

### Example 2

Input:

```
0050
```

Output:

```
0104
```

## Solution

A larger number with the same sum agrees with N up to some position,
has a larger digit there, and the digits after it give back what that
digit took. The next number changes as late a position as possible and
raises its digit by exactly one, so look for the rightmost digit below 9
with a positive sum after it. Raise it by one and rebuild the tail with
that sum minus one in its smallest form: zeros first and the sum pushed
to the end, nines from the right. If no digit qualifies, the answer is
-1. `O(K)`.

Pitfalls:

- leading zeros are part of the number and must be kept (example 2 and
  test 09);
- 0, 9 and numbers like 1000 have no next number (tests 05 to 07, and
  generated test 3, the largest number of its sum);
- the number has up to 2000 digits, far beyond fixed-width integer types;
  Python's `int` supports arbitrary precision, but leading zeros still
  require preserving the width (test 09).

The answers were compared with counting up number by number on 2 000
random numbers of up to five digits.

## Optimized solutions

C++ and Go scan right to left while keeping the suffix digit sum. The first digit below nine with a positive suffix sum is increased by one. Distribute the remaining sum from the right end to make the suffix as small as possible. Both versions update the input digits in place, using constant space beyond the input buffer. Go uses fixed byte arrays for reading and storing the digits, without scanner tokens. It accesses standard handles directly, retrying interrupted calls and completing partial writes.

The accepted base implementations [1406_greedy.java](1406_greedy.java), [1406_greedy.py](1406_greedy.py), [1406_greedy.rs](1406_greedy.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1406_greedy_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1406_greedy.java`: time 0.125 s → 0.109 s; memory 1576 KB → 548 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1406_greedy_implementation_parsing_optimized.rs`. Use native bounded input reads and a small stack output buffer instead of initializing Rust global standard streams. The C entry returns only after complete output writes. Windows descriptors use binary mode so CRLF and control bytes retain the original raw-stream meaning; the mathematical decisions are unchanged.

Accepted #11329159 (Rust 1.75 x64): **0.015 s / 84 KB**. Archived comparison: `1406_greedy.rs` (Rust 1.75 x64) — 0.062 s / 200 KB (#11286053).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1406_greedy.cpp](1406_greedy.cpp) | G++ 13.2 x64 | greedy | O(K) | AC | 0.015 s | 376 KB | 11286049 |
| [1406_greedy.go](1406_greedy.go) | Go 1.14 x64 | greedy | O(K) | AC | 0.031 s | 1088 KB | 11286050 |
| [1406_greedy.java](1406_greedy.java) | Java 1.8 | greedy | O(K) | AC | 0.125 s | 1576 KB | 11286052 |
| [1406_greedy.py](1406_greedy.py) | Python 3.12 x64 | greedy | O(K) | AC | 0.093 s | 552 KB | 11286051 |
| [1406_greedy.rs](1406_greedy.rs) | Rust 1.75 x64 | greedy | O(K) | AC | 0.062 s | 200 KB | 11286053 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1406_greedy_optimized.cpp](1406_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(K) | AC | 0.015 s | 96 KB | 11310623 |
| [1406_greedy_optimized.go](1406_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(K) | AC | 0.015 s | 328 KB | 11311213 |
| [1406_greedy_optimized.java](1406_greedy_optimized.java) | Java 1.8 | greedy | O(K) | AC | 0.109 s | 548 KB | 11324800 |
| [1406_greedy_implementation_parsing_optimized.rs](1406_greedy_implementation_parsing_optimized.rs) | Rust 1.75 x64 | greedy, implementation, parsing | O(K) | AC | 0.015 s | 84 KB | 11329159 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
