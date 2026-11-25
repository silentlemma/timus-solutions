# 2045. Prescribing the number of distinct palindromes

[Timus 2045](https://acm.timus.ru/problem.aspx?space=1&num=2045) · difficulty 478 · constructive

Original problem by Mikhail Rubinchik, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each integer `i` from `1` to `n`, construct a word of length `n`
over the lowercase Latin alphabet with exactly `i` different nonempty
palindromic substrings, or report that no such word exists. Substrings
are contiguous. Equal substring values count once even if they occur at
different positions. A palindrome reads the same in both directions.

## Input

One integer `1≤n≤2000`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Output

Print `n` lines in order. Line `i` has the form `i : word` or `i : NO`.
Every printed word must have exactly `n` lowercase letters and exactly
`i` distinct nonempty palindromes.

Any valid word is accepted. The checker verifies the number and order of
lines, the colon, length, alphabet, and actual distinct palindrome count
using a palindromic tree. It accepts `NO` only when `i<min(n,3)`; it
does not compare the word with a fixed construction.

## Checking

A checker verifies the format, the length and the letters of each word
and counts its distinct palindromes with an eertree; `NO` is accepted
only when no word exists. Any valid words are accepted.

## Examples

```
4
```

```
1 : NO
2 : NO
3 : abca
4 : bbca
```

A four-letter word cannot have only one or two different palindromes. In
`abca` the only ones are the letters `a,b,c`. In `bbca` they are
`b,c,a,bb`. These are example choices; the programs may print other
valid words.

## Solution

The first two lengths need separate handling. For `n=1` use `a`. For
`n=2`, one distinct palindrome is impossible and `aa` supplies two: `a`
and `aa`.

For `n≥3`, print `NO` for targets one and two. For every `3≤i≤n`, set
`k=i-3`. Print `k` copies of `a` followed by the first `n-k` characters
of the infinite periodic word `bcdbcdbcd…`.

### Correctness

First, every word of length at least three has at least three distinct
palindromes. If it uses three or more letters, their one-letter
substrings suffice. If it uses only one letter, its first one, two and
three letters give three different palindromes. If it uses exactly two
letters, both singletons occur; either equal adjacent letters give a
third palindrome of length two, or all adjacent letters differ and the
first three letters form a palindrome. For length two the minimum is
two: distinct letters give two singletons, while equal letters give the
singleton and the pair. Thus the impossible targets are precisely
`i<min(n,3)`.

For the construction, `n-k=n-i+3≥3`, so the tail contains all of
`b,c,d`. It has no palindromes of length two or three: adjacent letters
and letters two positions apart differ. Every longer palindrome has a
central palindrome of length two or three, obtained by repeatedly
removing its equal endpoints. Consequently the tail has exactly its
three single-letter palindromes.

The initial run contributes exactly the distinct strings `a,a²,…,a^k`.
For `k=0` it contributes none. A substring crossing the boundary starts
with `a` and ends in `b,c` or `d`, so it cannot be a palindrome. These
two sets are disjoint, and the total is `k+3=i`. The length is
`k+(n-k)=n`. Together with the small cases and the lower bound, this
proves every printed word and every `NO`.

### Complexity

Each word takes `O(n)` construction and output time. There are `n` rows,
so total time is `O(n^2)` and auxiliary space is `O(n)` when rows are
written immediately. For large `n`, `n-2` words of length `n` must be
printed, so the output alone requires `Ω(n^2)` time.

Pitfalls:

- Count distinct strings, not palindrome occurrences or partitions.
- Keep at least three tail characters, including at target `i=n`.
- The tail alphabet must exclude the run letter; a binary alternating
  tail creates longer palindromes.
- Treat `n=1` and `n=2` separately.
- A checker must accept valid words different from the example or the
  production construction.

## Optimized solutions

New C++, Go and Rust emit the identical accepted construction from reusable a-run and periodic bcd buffers, instead of allocating a prefix, tail substring and combined word each row. C++ writes the two slices directly through C stdio; Go/Rust collect bounded 8192-byte output blocks and flush before a row no longer fits. A row is at most n+16 bytes, including its label, so the buffers cover n≤2000 safely. Small n and impossible targets keep the same rules. No palindrome-generation logic changes: the original proof still applies. Time O(n²), already required by output size, and O(n) bounded storage without per-word allocation. All ordinary sources remain; Python reuses its admitted base.

The accepted Go 1.14 x64 run takes 0.078 s versus 0.046 s for the base and uses 348 KB versus 5888 KB.

In the earlier comparison snapshot, the base implementations [2045_constructive.java](2045_constructive.java), [2045_constructive.py](2045_constructive.py) met the top-15% or top-ten admission rule on both metrics. Their measured results are kept in the Simple table.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2045_constructive_parsing_optimized.py`. Keep the single mutable periodic word and increasing constant prefix. Write byte batches directly with complete partial-write handling, releasing memory views before reusing the output buffer. Use 8 KiB output batches to keep transient output storage small. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11329239 (Python 3.12 x64): **0.078 s / 900 KB**. Archived comparison: `2045_constructive.py` (Python 3.12 x64) — 0.203 s / 692 KB (#11293460).

## Language notes

These notes describe the simple implementations.

All five ports build a periodic tail once and write one row at a time.
C++, Go, Python and Rust combine a repeated prefix with a tail prefix.
Java fills one character array per row. Buffered output avoids
per-character writes; no port retains the quadratic complete answer in
memory. CPython 3.12 is selected.

Prebuild the repeated suffix and a buffer of prefix letters. Write slices of these buffers directly for each row. Accepted submission 11324212 took 0.140 s and used 668 KB. The simple version took 0.156 s and used 5140 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2045_constructive.cpp](2045_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.031 s | 1088 KB | 11293451 |
| [2045_constructive.go](2045_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 5888 KB | 11293458 |
| [2045_constructive.java](2045_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.171 s | 5116 KB | 11329308 |
| [2045_constructive.py](2045_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.203 s | 692 KB | 11293460 |
| [2045_constructive.rs](2045_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 956 KB | 11293465 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2045_constructive_optimized.cpp](2045_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 104 KB | 11315321 |
| [2045_constructive_optimized.go](2045_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n²) | AC | 0.078 s | 348 KB | 11315327 |
| [2045_constructive_optimized.rs](2045_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 68 KB | 11315328 |
| [2045_constructive_optimized.java](2045_constructive_optimized.java) | Java 1.8 | constructive | O(n^2) | AC | 0.140 s | 668 KB | 11324212 |
| [2045_constructive_parsing_optimized.py](2045_constructive_parsing_optimized.py) | Python 3.12 x64 | constructive, parsing | O(n^2) | AC | 0.078 s | 900 KB | 11329239 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.

**Current measurements.** The solution tables record the exact preserved sources and their latest Accepted runs. Earlier performance comparisons describe historical runs; current admission follows the shared [rating criteria](../../RATING_CRITERIA.md).
