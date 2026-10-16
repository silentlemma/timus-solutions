# 1822. Hugo II's War

[Timus 1822](https://acm.timus.ru/problem.aspx?space=1&num=1822) · difficulty 687 · binary_search

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
distinct c, sort them by cross-multiplication and binary search for the
last one the king can afford, checking each with exact integers. No
precision issues remain, and the printed value is exact. With at most
2n fractions this is `O(n log² n)`.

For the example at x = 50, noble 2 waits for one of the vassals 3
and 4, ready on day 1, and is ready on day 3. The king's vassals are
ready on days 3, 2 and 4, so the second of them comes on day 3, in
time. Any x above 50 makes noble 2 wait for both and the king for two
of 4, 2, 4.

Pitfalls:

- x is a share of direct vassals, rounded up: with 3 vassals, 34%
  already needs two of them;
- a suzerain can have a larger number than its vassals, so the order
  of processing comes from a traversal from the king;
- the king spends no days on gathering;
- with no vassals at all the king leaves at once and the answer is 100.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1822_binary_search.cpp](1822_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 564 KB |
| [1822_binary_search.go](1822_binary_search.go) | Go 1.14 x64 | binary_search | O(n log^2 n) | AC | 0.062 s | 3844 KB |
| [1822_binary_search.java](1822_binary_search.java) | Java 1.8 | binary_search | O(n log^2 n) | AC | 0.187 s | 6708 KB |
| [1822_binary_search.py](1822_binary_search.py) | Python 3.12 x64 | binary_search | O(n log^2 n) | AC | 0.140 s | 4136 KB |
| [1822_binary_search.rs](1822_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log^2 n) | AC | 0.031 s | 1364 KB |
