# 2066. The smallest value of three numbers

[Timus 2066](https://acm.timus.ru/problem.aspx?space=1&num=2066) · difficulty 28 · bruteforce

Original problem by Kirill Borozdin, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three non-negative integers may be written in any order with one of the
signs +, − or × between each two neighbours; multiplication goes first,
and there are no brackets or unary minus. Find the smallest value such
an expression can have. The limits are 1 second and 64 MB.

## Input

The numbers a ≤ b ≤ c, 0 ≤ a, each on its own line, c ≤ 100.

## Output

The smallest value.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
1
2
3
```

Output:

```
-5
```

## Solution

There are at most 6 orders and 9 pairs of signs, so the programs try up to
54 expressions. Evaluate x op₁ y op₂ z with the usual precedence: if
only the second sign is ×, compute y × z first; otherwise go from left
to right.

The search always ends with the same shape: the smallest number minus
the larger of b + c and b × c, that is a − max(b + c, b × c). Subtracting
as much as possible from the smallest number is clearly best, and b + c
beats b × c only when one of them is 0 or 1. Checking all 176 851
inputs confirms the formula, but the plain search needs no argument.

In the example 1 − 2 × 3 = −5.

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.140 s and
400 KB instead of 1584 KB.

`2066_math.py`. Replace enumeration of permutations and operator pairs by two expressions. For sorted nonnegative a<=b<=c, the minimum among additive expressions is a-b-c. If a product is subtracted, put the two larger operands in it to get a-b*c; positive products and other mixed placements cannot improve both candidates. Return their minimum. The math filename distinguishes this argument from the preserved brute-force teaching version. Time and storage O(1). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `2066_bruteforce.py`: time 0.078 s → 0.14 s; memory 532 KB → 208 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2066_math.py`: time place 330/341, memory place 3/341 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2066_bruteforce.cpp](2066_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 176 KB | 11303806 |
| [2066_bruteforce.go](2066_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1080 KB | 11294375 |
| [2066_bruteforce.java](2066_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.140 s | 1584 KB | 11303807 |
| [2066_bruteforce.py](2066_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 532 KB | 11294380 |
| [2066_bruteforce.rs](2066_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 224 KB | 11303808 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2066_bruteforce_optimized.java](2066_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(1) | AC | 0.093 s | 400 KB | 11303798 |
| [2066_math.py](2066_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 208 KB | 11324830 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
