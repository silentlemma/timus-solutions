# 2065. Few distinct segment sums

[Timus 2065](https://acm.timus.ru/problem.aspx?space=1&num=2065) · difficulty 318 · constructive

Original problem by Nikita Sivukhin, prepared by Alexey Danilyuk and Nikita Sivukhin, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Build an array of n integers with at least k distinct values such that
the sums of its contiguous segments take as few distinct values as
possible. Every value must be at most 10⁶ in absolute value. The limits
are 1 second and 64 MB.

## Input

Two integers n and k, 1 ≤ k ≤ n ≤ 500.

## Output

The n integers on one line. Any optimal array is accepted.

## Checking

A checker verifies the values and the number of distinct values and
counts the distinct segment sums, which must equal k.

## Examples

### Example 1

Input:

```
1 1
```

Output:

```
-987654
```

### Example 2

Input:

```
3 2
```

Output:

```
0 7 0
```

## Solution

Every single element is a segment, so an array with k distinct values
has at least k distinct segment sums. This bound can always be reached:
take n − k + 1 zeros followed by 1, −1, 2, −2, 3, … until there are n
numbers. The zeros and the k − 1 other numbers give exactly k distinct
values.

A segment sum is the difference of two prefix sums. The prefix sums of
this array are 0, …, 0, 1, 0, 2, 0, 3, …: zeros alternating with 1, 2,
…, m, where m is the largest number used. If the array ends with −m,
the differences of an earlier prefix and a later one cover exactly
−m, …, m, which is 2m + 1 = k values. If it ends with m, the prefix m
comes last, so −m never appears and the sums are −(m − 1), …, m, again
2m = k values. Thus the array is optimal, and the answer is O(n).

In the second example the array 0 0 1 has the values 0 and 1 and the
segment sums 0 and 1, two of each, just like the sample answer 0 7 0.

## Optimized solutions

`2065_constructive_optimized.java`. Java keeps n-k+1 zeros followed by 1,-1,2,-2,... . The array has exactly k distinct entries and its nonempty segment sums also have exactly k values, attaining the lower bound from one-element segments. Compute each entry directly from its index, without an intermediate array. A 1024-byte input buffer and bounded 1024-byte raw output replace general parsing and the whole-line StringBuilder; the output helper flushes when full. Time O(N), fixed auxiliary storage. The readable teaching construction and all other languages are preserved.

Exact-source Java 1.8 Accepted #11327446: 0.093 s / 364 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/45, memory 1/45. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11324791 was 0.109 s / 476 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2065_constructive_optimized.java`: 0.093 s / 364 KB; retained teaching base `2065_constructive.java`: 0.109 s / 1648 KB.

Go and Rust emit the same construction as a zero prefix of length n−k+1 followed by 1, −1, 2, −2 and so on until there are n values. Go formats the result into a fixed buffer for n ≤ 500 and accesses standard input and output handles directly. Rust writes through a bounded output buffer. Neither version builds an intermediate array of integers or a list of formatted strings.

The accepted base implementations [2065_constructive.cpp](2065_constructive.cpp), [2065_constructive.java](2065_constructive.java), [2065_constructive.py](2065_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2065_constructive.cpp](2065_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 112 KB | 11325631 |
| [2065_constructive.go](2065_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1056 KB | 11294350 |
| [2065_constructive.java](2065_constructive.java) \* | Java 1.8 | constructive | O(n) | AC | 0.109 s | 1648 KB | 11325630 |
| [2065_constructive.py](2065_constructive.py) \* | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 456 KB | 11294354 |
| [2065_constructive.rs](2065_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.015 s | 260 KB | 11325632 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2065_constructive_optimized.go](2065_constructive_optimized.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 316 KB | 11311234 |
| [2065_constructive_optimized.rs](2065_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 176 KB | 11311148 |
| [2065_constructive_optimized.java](2065_constructive_optimized.java) | Java 1.8 | constructive | O(N) time; O(1) auxiliary space | AC | 0.093 s | 364 KB | 11327446 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
