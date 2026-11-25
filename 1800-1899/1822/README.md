# 1822. Hugo II's War

[Timus 1822](https://acm.timus.ru/problem.aspx?space=1&num=1822) · difficulty 686 · binary_search

Original problem by Kirill Butin, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The nobles of a kingdom form a tree under the king, noble 1. An order
with a number x travels down from the king. A noble without vassals
gathers troops at once, taking tᵢ days. A noble with vassals waits until
at least x% of the direct vassals are ready, then gathers troops
in tᵢ days. The king sets out once at least x% of the direct vassals
are ready. Find the largest x for which the king sets out within t days.

## Input

n and t (1 ≤ n ≤ 10⁴, 0 ≤ t ≤ 10⁶), then for nobles 2, …, n the
suzerain pᵢ and the days tᵢ (0 ≤ tᵢ ≤ 100).

## Output

The largest x, with absolute error at most 10⁻⁴.

## Examples

### Example 1

Input:

```
6 3
1 2
2 2
2 1
1 2
1 4
```

Output:

```
50.00000000
```

## Solution

For a fixed x, a noble with c vassals waits for ⌈x·c/100⌉ of them,
that is, for the ⌈x·c/100⌉-th smallest of their ready days, and is
ready that many days plus tᵢ later; one pass from the leaves up gives
the king's day. A larger x never makes anyone faster, so the feasible x
form an interval [0, X].

Inside that interval only the values ⌈x·c/100⌉ matter, and they change
only at fractions m/c, with c a number of direct vassals. So X itself
is 100·m/c for some such fraction. Collect the fractions for every
distinct c, sort them and binary search for the last one the king can
afford, checking each with exact integers. C++, Go, Java and Rust sort
by cross-multiplication; Python sorts by floating-point m/c. Distinct
fractions differ by at least 1/9999², so floating-point sorting is safe
under these constraints. Round 100·m/c to eight decimal places using
integer arithmetic, rounding halfway values up, and print the integer
and padded fractional parts separated by a decimal point. All five
languages then produce identical output with error at most 5·10⁻⁹.
With at most 2n fractions this is `O(n log² n)`.

For the example at x = 50, noble 2 waits for one of the vassals 3
and 4, ready on day 1, and is ready on day 3. The king's vassals are
ready on days 3, 2 and 4, so the second of them comes on day 3, in
time. Any x above 50 makes noble 2 wait for both; the king then waits
for two of 4, 2, 4 when x ≤ 200/3, and all three otherwise (for example,
at 75%). Either way the king leaves on day 4, too late.

Pitfalls:

- x is a share of direct vassals, rounded up: with 3 vassals, 34%
  already needs two of them;
- a suzerain can have a larger number than its vassals, so the order
  of processing comes from a traversal from the king;
- the king spends no days on gathering;
- output must use a decimal point regardless of the locale: test 10
  exposes Java's default decimal comma under a Russian locale, so its
  formatter explicitly uses `Locale.US`;
- with no vassals at all the king leaves at once and the answer is 100.

## Optimized solutions

The tree DP first accumulates the time along each path from the king. It then works from the leaves up, sorting the limits of the direct vassals. At rank r, the supported share is bounded by both the r-th limit and r divided by the number of vassals.

Python 3.12 x64, submission 11318642. Time 0.125 → 0.109 s, memory 4116 → 3356 KB.

Rust 1.75 x64, submission 11318846. Time 0.015 → 0.062 s, memory 1368 → 552 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321968 · Java 1.8 №11321961 · Rust 1.75 x64 №11321962 · Go 1.14 x64 №11322431 · Python 3.12 x64 №11322432.

Go 1.14 x64, submission 11321995. Time 0.031 → 0.031 s, memory 3820 → 1608 KB.

Java 1.8, submission 11321996. Time 0.156 → 0.093 s, memory 6636 → 808 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1822_binary_search.cpp](1822_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 552 KB | 11321968 |
| [1822_binary_search.go](1822_binary_search.go) | Go 1.14 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 3820 KB | 11322431 |
| [1822_binary_search.java](1822_binary_search.java) | Java 1.8 | binary_search | O(n log^2 n) | AC | 0.156 s | 6636 KB | 11321961 |
| [1822_binary_search.py](1822_binary_search.py) | Python 3.12 x64 | binary_search | O(n log^2 n) | AC | 0.125 s | 4116 KB | 11322432 |
| [1822_binary_search.rs](1822_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log^2 n) | AC | 0.015 s | 1368 KB | 11321962 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1822_trees_dp.py](1822_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n) | AC | 0.109 s | 3356 KB | 11318642 |
| [1822_trees_dp.rs](1822_trees_dp.rs) | Rust 1.75 x64 | trees, dp | O(n log n) | AC | 0.062 s | 552 KB | 11318846 |
| [1822_trees_dp.go](1822_trees_dp.go) \* | Go 1.14 x64 | trees, dp | O(n log n) | AC | 0.031 s | 1608 KB | 11321995 |
| [1822_trees_dp.java](1822_trees_dp.java) | Java 1.8 | trees, dp | O(n log n) | AC | 0.093 s | 808 KB | 11321996 |

\* The marked versions have room to improve in the ratings.
