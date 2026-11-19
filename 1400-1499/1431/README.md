# 1431. Diplomas

[Timus 1431](https://acm.timus.ru/problem.aspx?space=1&num=1431) · difficulty 362 · greedy

Original problem by Stanislav Vasiliev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N types of diplomas (N ≤ 18), from 1 to 30 of each. All
diplomas of a type hang in one row. A row holds one type, or two types
that strictly alternate, and every row must be symmetric about the
centre of the wall. Find the smallest number of rows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the number of diplomas of each type.

## Output

The smallest number of rows.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
6
8 15 13 8 14 8
```

Output:

```
5
```

## Solution

A row of one type is always fine. Two types that strictly alternate
form ABAB…, and such a row reads the same backwards only when it starts
and ends with the same type, A B A … B A, so the counts differ by
exactly one. The answer is N minus the largest number of disjoint pairs
of types whose counts differ by one.

The pairs join neighbouring values of a chain 1, 2, …, 30. Going up the
chain, the types of count c not yet paired can only pair with count
c + 1 now, so pairing as many of them as possible right away is never
worse. `O(N + 30)`.

Pitfalls:

- equal counts cannot share a row: an alternating row of even length is
  not symmetric (test 06);
- in 1, 2, 3, 4 the pairs are 1–2 and 3–4, not 2–3 (test 07);
- several types may have the same count (tests 08, 12).

## Optimized solutions

`1431_greedy_optimized.py`. Keep the frequency-chain greedy matching of leftover count c with count c+1. Parse integers in 4096-byte chunks and retain only the 31 frequencies, not the entire input line or token list. For V=30 the time is O(n+V), and storage is O(V+B) with bounded-size integer tokens and chunk size B. Matching and the final n-pairs formula are unchanged. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1431_greedy.py`: time 0.078 s → 0.156 s; memory 420 KB → 256 KB.

Go and Rust store the frequencies of counts one through 30 in byte arrays. At each count, match as many types as possible with the unmatched types at the preceding count. Each match removes one required row. Carry only the unmatched remainder forward, so no sorted list or matching graph is needed. Both use fixed byte buffers for input and decimal output. Go accesses the standard input and output handles directly, and Rust uses the C runtime.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 56 KB versus 220 KB.

The accepted base implementations [1431_greedy.cpp](1431_greedy.cpp), [1431_greedy.java](1431_greedy.java), [1431_greedy.py](1431_greedy.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1431_greedy_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1431_greedy.java`: time 0.156 s → 0.109 s; memory 1644 KB → 440 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1431_greedy_optimized.java`: time place 8/13, memory place 2/13 in this comparable sample.

`1431_greedy_optimized.py`: time place 32/36, memory place 1/36 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1431_greedy.cpp](1431_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + 30) | AC | 0.015 s | 128 KB | 11286206 |
| [1431_greedy.go](1431_greedy.go) | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 1076 KB | 11286207 |
| [1431_greedy.java](1431_greedy.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.156 s | 1644 KB | 11286209 |
| [1431_greedy.py](1431_greedy.py) \* | Python 3.12 x64 | greedy | O(N + 30) | AC | 0.078 s | 420 KB | 11286208 |
| [1431_greedy.rs](1431_greedy.rs) | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.015 s | 220 KB | 11286210 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1431_greedy_optimized.go](1431_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 348 KB | 11311231 |
| [1431_greedy_optimized.rs](1431_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.031 s | 56 KB | 11311246 |
| [1431_greedy_optimized.java](1431_greedy_optimized.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.109 s | 440 KB | 11324802 |
| [1431_greedy_optimized.py](1431_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n+V) time; O(V+B) space | AC | 0.156 s | 256 KB | 11325486 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
