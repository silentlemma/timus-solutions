# 1157. The fewest tiles that make N rectangles, with M rectangles K tiles earlier

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · difficulty 200 · number_theory

Original problem from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A boy lays out all his square tiles as rectangles. Given `M`, `N` and
`K` (`1 ≤ M, N ≤ 50`, `1 ≤ K ≤ 9999`), find the smallest number of tiles `L` such
that `L` tiles can form exactly `N` different rectangles and `L − K` tiles
exactly `M` different rectangles. Print `0` if there is no such `L` up to
10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Integers M, N and K, with 1<=M,N<=50 and 1<=K<=9999.

## Output

The smallest `L`, or `0`.

## Checking

Compare the single integer answer token by token, ignoring whitespace,
as specified by tests.json. The reference is the simple C++ sieve.

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

This pair-sieve section applies to optimized C++, Java, Python and
Rust. Optimized Go retains the full divisor sieve of its base, using
int counters and computing shapes from divisor counts; its change
is the token reader and reused output buffer, not byte storage or
pair enumeration. Both algorithms use O(B log B) time and O(B) words
or bytes as appropriate; full-input readers additionally retain I
input bytes.

Measured against each language's original base, C++ memory drops
216 → 120 KB (44.4%), Python 712 → 428 KB (39.9%), and Java
1620 → 420 KB (74.1%). C++ and Python keep their recorded times;
Java also improves 0.125 → 0.078 s (37.6%). Rust improves in recorded time,
0.046 → 0.015 s (67.4%); its memory drops only 25.3%, 300 → 224 KB.
These measurements belong to the preceding Accepted revisions.

The earlier Go pair-sieve experiment (0.015 s / 1076 KB) was not
published as that source. The current distinct optimized Go file
exists: it uses the full divisor sieve with faster I/O and had
Accepted #11328509, 0.031 s / 1040 KB. Its base remains available.
A one-tick difference alone does not prove repeatable acceleration.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1157_number_theory_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328509 (Go 1.14 x64): **0.031 s / 1040 KB**. Archived comparison: `1157_number_theory.go` (Go 1.14 x64) — 0.031 s / 1172 KB (#11281331).

The current optimized Go revision moves the limit comment beside
its constant and names the unchanged 64-bit strconv width. The algorithm and all simple sources remain unchanged.

## Language notes

Current admission follows the shared [rating criteria](../../RATING_CRITERIA.md),
not an obsolete first-place or 30% gain rule. The source-bound cached
audit confirms time-only admission below 1 MiB for both C++ sources,
both Python sources, both Rust sources and optimized Java. Rust uses
the recorded fallback to all compiler versions, with one eligible
Rust 1.58 rival; this is not an empty cohort or a small exact-version
reference. The preceding optimized Go receipt passes both small-
cohort metrics (two Go 1.14 rivals). Java/Go bases remain teaching
versions even though they miss their applicable metrics. No current
row has a star; these conclusions concern the cached evidence.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

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
| [1157_number_theory_optimized.java](1157_number_theory_optimized.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.078 s | 420 KB | 11308317 |
| [1157_number_theory_optimized.py](1157_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 428 KB | 11308301 |
| [1157_number_theory_optimized.rs](1157_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.015 s | 224 KB | 11308320 |
| [1157_number_theory_optimized.go](1157_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.015 s | 1024 KB | 11331013 |
