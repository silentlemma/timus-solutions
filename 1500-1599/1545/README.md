# 1545. Hieroglyphs

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · difficulty 50 · implementation

Original problem by Evgeny Krokhalev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dictionary holds N ≤ 1000 hieroglyphs, each written as two lowercase
letters. Given a typed letter, print the hieroglyphs that start with it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, the N two-letter entries, then the letter.

## Output

The matching entries, one per line, in any order; nothing if there are
none.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The repository checker splits output into tokens and compares sorted token lists, preserving multiplicities. Matching entries may appear in any order; duplicates must be retained.

## Examples

### Example 1

Input:

```
6
na
no
ni
ki
ka
ku
k
```

Output:

```
ka
ki
ku
```

## Solution

Compare the first letter of every entry with the typed one and print
the matches in input order. `O(N)`.

Pitfalls:

- with no match the output is empty (tests 02, 05);
- an entry that appears twice is printed twice (test 03);
- the letter must be first: a match in the second place does not count
  (test 05).

## Optimized solutions

The optimized C++ solution keeps the two-letter entries in a local array
of three-byte C strings instead of `std::string`, reads them with
`scanf("%2s")` and prints them with `puts`: 120 KB instead of 392 KB,
with the same time.

Every hieroglyph is two letters. The optimized Java solution keeps them
in byte arrays filled from 256-byte blocks and writes the answer from
one byte array, with no `Scanner` and no strings: 392 KB instead of
1804 KB, with the same time. The optimized Rust solution keeps each
hieroglyph as a pair of bytes and writes through a `BufWriter` with a
small buffer: 0.015 s instead of 0.046 s and 196 KB instead of 236 KB.

`1545_implementation_optimized.py`. Keep the dictionary filter and preserve its order and duplicate entries. Split raw bytes, match the one-letter prefix with startswith and join matching entries as bytes. No decoded dictionary or separate list of matched text strings is retained, but the token list, sliced references and joined answer still use O(N) storage because entries have length two. Time O(N). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1545_implementation.py`: time 0.062 s → 0.14 s; memory 460 KB → 216 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1545_implementation_optimized.py`: time place 168/175, memory place 2/175 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
| [1545_implementation_optimized.py](1545_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N) | AC | 0.14 s | 216 KB | 11324837 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
