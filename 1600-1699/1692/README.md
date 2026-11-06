# 1692. Flags for Provinces

[Timus 1692](https://acm.timus.ru/problem.aspx?space=1&num=1692) · difficulty 380 · constructive

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Design as many flags as possible using n colors so that every two flags
share a color but no color appears on three or more flags.

## Input

n (3 ≤ n ≤ 1000).

## Output

The number of flags k, then each flag as its number of colors followed
by the colors. Any valid design is accepted.

## Examples

### Example 1

Input:

```
4
```

Output:

```
3
2 1 2
2 1 3
2 2 3
```

## Solution

Each of the k(k − 1)/2 pairs of flags needs a common color. A color on
at most two flags is common to at most one pair, so different pairs use
different colors and k(k − 1)/2 ≤ n.

That bound is reached: number the pairs of flags and give each pair its
own color, put on just those two flags. Every flag then carries k − 1
colors, every two flags share their pair's color, and no color is on
more than two flags. Take the largest k with k(k − 1)/2 ≤ n; spare
colors stay unused. `O(n)` output.

Pitfalls:

- leftover colors need not be used (test 04);
- the example's design is one of many, so a checker validates the
  flags instead of comparing text.

The checker checks the count, the ranges, the pairwise common colors
and the at-most-two rule; the answers of an independent accepted
implementation pass it for every n up to 300.

## Optimized solutions

Go and Rust generate each flag directly from the indices of the other flags. For a zero-based pair a < b among k flags, the colour is a(2k−a−1)/2 + b−a. The first term counts earlier pairs and the second locates this pair. Thus the same colour appears on exactly the two flags without storing a matrix of pair colours. Both versions use fixed byte buffers for input and output, without scanner or string conversion.

The accepted base implementations [1692_constructive.cpp](1692_constructive.cpp), [1692_constructive.java](1692_constructive.java), [1692_constructive.py](1692_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1692_constructive.cpp](1692_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 232 KB | 11288948 |
| [1692_constructive.go](1692_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 1152 KB | 11288949 |
| [1692_constructive.java](1692_constructive.java) \* | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1796 KB | 11288952 |
| [1692_constructive.py](1692_constructive.py) \* | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 464 KB | 11288950 |
| [1692_constructive.rs](1692_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 264 KB | 11288953 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1692_constructive_optimized.go](1692_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 780 KB | 11311145 |
| [1692_constructive_optimized.rs](1692_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 180 KB | 11311155 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
