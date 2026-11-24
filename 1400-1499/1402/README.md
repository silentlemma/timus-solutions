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

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

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

`1402_combinatorics_optimized.py`. Keep the running falling factorial: ways starts at N, is multiplied by N-k+1 for k=2..N, and is added to total. It counts ordered choices without building factorial tables or recomputing each product. N=1 correctly yields zero. Time O(N) bounded-width arithmetic and O(1) integer slots under N<=21. Use the same exact Python integer recurrence with byte input; no combinatorial formula change is claimed. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1402_combinatorics.py`: time 0.078 s → 0.125 s; memory 388 KB → 244 KB.

`1402_combinatorics_optimized.rs`. Keep the running falling factorial: ways starts at N, is multiplied by N-k+1 for k=2..N, and is added to total. It counts ordered choices without building factorial tables or recomputing each product. N=1 correctly yields zero. Time O(N) bounded-width arithmetic and O(1) integer slots under N<=21. Retain u128 because the answer for 21 drinks exceeds 64 bits. A fixed 39-byte decimal buffer holds any u128; the conservative total bound 21*21! is far below its maximum. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1402_combinatorics.rs`: time 0.031 s → 0.062 s; memory 232 KB → 56 KB.

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

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1402_combinatorics_optimized.py`: time place 62/71, memory place 1/71 in this comparable sample.

`1402_combinatorics_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1402_combinatorics_optimized.py](1402_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(N) | AC | 0.125 s | 244 KB | 11324912 |
| [1402_combinatorics_optimized.rs](1402_combinatorics_optimized.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.062 s | 56 KB | 11325095 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
