# 1157. The fewest tiles that make N rectangles, with M rectangles K tiles earlier

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · difficulty 200 · number_theory

Original problem from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A boy lays out all his square tiles as rectangles. Given `M`, `N` and
`K` (`M, N ≤ 50`, `K ≤ 9999`), find the smallest number of tiles `L` such
that `L` tiles can form exactly `N` different rectangles and `L − K` tiles
exactly `M` different rectangles. Print `0` if there is no such `L` up to
10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M`, `N` and `K`.

## Output

The smallest `L`, or `0`.

## Checking

Independently factor all tile counts `1..10000` and compute divisor
counts from prime exponents. This supplies the expected shape-count
table; it has maximum 32 rectangles. The actual Python candidate was
checked on 125 queries, including the sample, no-solution counts and
`K = 9999`, using the first matching entry of that independent table.
Each of the five actual candidates also passed 13 repository inputs in
Docker. These checks do not claim exhaustive testing of every input
triple. All five candidates subsequently received their own Accepted.

## Examples

### Example 1

Input:

```
2 3 1
```

Output:

```
16
```

## Solution

For `x` tiles, each unordered divisor pair `a × b = x`, `a ≤ b`,
gives one rectangle; rotating it does not give another shape. Let `d[x]`
be the number of divisors. Pairing each divisor with its quotient gives
`shapes[x] = (d[x] + 1) // 2`: a square's middle divisor pairs with itself.

The simple sieve increments `d[x]` for every multiple of each divisor
`1..B`, where `B = 10000`. It counts every divisor once. Search `L` in
increasing order from `K + 1` through `B`, checking both required shape
counts. The first match is minimal; if none matches, output `0`.
Starting at `K + 1` ensures `L − K ≥ 1`. This proves both the count and
the answer selection. Time is `O(B log B)` and auxiliary space `O(B)`.
The five original Accepted sources remain unchanged; Python materializes
a second list of shape counts, while the native bases compute them from
the divisor table when needed.

## Optimized solutions

Count unordered divisor pairs directly. For every smaller side
`a = 1..floor(sqrt(B))`, increment the entries `a², a² + a, …, B`.
These are precisely the products `a × b` with `b ≥ a`. Every rectangle
has exactly one smaller side, so it is visited once; a square is also
visited once. The same increasing search then gives the same answer.

Use one byte per count: at most `floor(sqrt(x)) ≤ 100` smaller sides can
belong to any `x ≤ B`. Thus even Java's signed byte cannot overflow.
The table has `10001` bytes, excluding its object header, I/O and runtime.
The sieve and search still take `O(B log B)` time and `O(B)` space, with
fewer increments and compact storage. Java also replaces `Scanner` with
`StreamTokenizer`; Rust parses the three input values without collecting
a numeric vector. These are distinct implementations of the same
divisor-pair sieve approach, hence the `_optimized` suffix.

Measured against each language's original base, C++ memory drops
216 → 120 KB (44.4%), Python 712 → 428 KB (39.9%), and Java
1620 → 420 KB (74.1%). C++ and Python keep their recorded times;
Java also improves 0.125 → 0.078 s (37.6%). Rust qualifies by time,
0.046 → 0.015 s (67.4%); its memory drops only 25.3%, 300 → 224 KB.
Each published version has its own exact-source Accepted.

The Go candidate was also Accepted, but memory improves only 8.2%,
1172 → 1076 KB, and its 0.031 → 0.015 s change is one timer tick.
That tick is not reliable speedup evidence, so this candidate is not
added as an optimized source. The original Go base is retained.

## Language notes

The rating snapshot is from 2 November 2026. Optimized C++ has time
place 1 and memory place 2 against 73 filtered other-author entries and
meets the target. Python has places 2 and 2 against 16 entries; Java has
places 1 and 2 against five. Under the established stricter non-C++
comparison profile, which requires first place in both metrics, these
two retain stars despite their admitted gains. The Go and Rust filtered
samples are empty: their formal coverage provides no competitive claim.
Ranking and the measured 30% admission criterion are separate.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 216 KB | 11281313 |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.031 s | 1172 KB | 11281331 |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.125 s | 1620 KB | 11281380 |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 712 KB | 11281359 |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.046 s | 300 KB | 11281448 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1157_number_theory_optimized.cpp](1157_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 120 KB | 11308304 |
| [1157_number_theory_optimized.java](1157_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(B log B) | AC | 0.078 s | 420 KB | 11308317 |
| [1157_number_theory_optimized.py](1157_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 428 KB | 11308301 |
| [1157_number_theory_optimized.rs](1157_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.015 s | 224 KB | 11308320 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
