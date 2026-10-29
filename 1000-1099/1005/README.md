# 1005. Splitting weights into two piles

[Timus 1005](https://acm.timus.ru/problem.aspx?space=1&num=1005) · difficulty 78 · dp, bitmask, bruteforce, meet_in_middle

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `n` positive integers `w1, ..., wn` (`1 ≤ n ≤ 20`,
`1 ≤ wi ≤ 100 000`), split them into two groups so that the difference
between the sums of the groups is as small as possible. Output that
difference. A group may be empty.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number `n` and then the `n` weights, separated by whitespace.

## Output

One integer: the minimal possible difference.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
5 8 13 27 14
```

Output:

```
3
```

### Example 2

Input:

```
1
100000
```

Output:

```
100000
```

## Solution

If one group weighs `s`, the other weighs `total - s` and the difference is
`|total - 2s|`. So the task is to find the subset sum `s ≤ total / 2` closest
to `total / 2`.

**Subset sums (dp).** `reach[s]` tells whether some weights sum to exactly
`s`; start with `reach[0]` and add the weights one by one, going over `s`
downwards so that each weight is used at most once. Only sums up to
`total / 2 ≤ 1 000 000` matter, so this is at most `20 · 10^6` steps and
`O(total)` memory. The answer comes from the largest reachable `s ≤ total / 2`.

**Bitset (dp, bitmask).** The same table fits in one integer whose bit `s` is
`reach[s]`: adding a weight `x` is `reach |= reach << x`. In Python, with its
arbitrary-precision integers, this runs on whole machine words at a time and is
much faster than a loop over `s`.

Pitfalls:

- the total is up to `2 · 10^6`: `int` is enough, but a table over all sums up
  to `total` wastes memory; `total / 2` is enough;
- `n = 1`: the answer is the only weight.

## Optimized solutions

**All subsets** (C++). With `n ≤ 20` all `2^20` subsets can be listed. In
Gray code order every next subset differs from the previous one in one
weight, so the sum is updated in `O(1)`; the last weight can stay in the
second group, which halves the work. `O(2^(n-1))` time and no table at
all, so it needs much less memory than the DP: 200 KB instead of
1124 KB, with the same time.

**Meet in the middle** (Go, Java, Rust). Split the weights into two halves
of at most 10 and list the subset sums of each half, at most 1024, sorted.
A pile is a subset of one half plus a subset of the other, so walk the sums
of the left half upwards and those of the right half downwards, moving the
side that brings the pile closer to `total / 2`; every pair skipped this way
is no better than one already seen. The walk stops early when the
difference reaches `total mod 2`, which no split can beat. `O(n·2^(n/2))`
time and a few kilobytes of memory instead of a table of `total / 2`
entries. Go and Java also parse the input by hand from a small buffer.
With the same time, Go needs 920 KB instead of 2000 KB, Java 472 KB
instead of 1388 KB and Rust 244 KB instead of 1144 KB.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: the simple solutions fill the
  boolean subset-sum table, about `2 · 10^7` simple steps.
- **Python**: the big-integer bitset; a plain double loop over the weights and
  sums would be far too slow.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1005_dp.cpp](1005_dp.cpp) | G++ 13.2 x64 | dp | O(n·S) | AC | 0.015 s | 1124 KB | 11277610 |
| [1005_dp.go](1005_dp.go) | Go 1.14 x64 | dp | O(n·S) | AC | 0.062 s | 2000 KB | 11277623 |
| [1005_dp.java](1005_dp.java) | Java 1.8 | dp | O(n·S) | AC | 0.109 s | 1388 KB | 11303450 |
| [1005_dp.rs](1005_dp.rs) | Rust 1.75 x64 | dp | O(n·S) | AC | 0.031 s | 1144 KB | 11277646 |
| [1005_dp_bitmask.py](1005_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(n·S/64) | AC | 0.093 s | 920 KB | 11277630 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1005_bruteforce_bitmask.cpp](1005_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^(n-1)) | AC | 0.015 s | 200 KB | 11277615 |
| [1005_meet_in_middle.go](1005_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(n·2^(n/2)) | AC | 0.046 s | 920 KB | 11303539 |
| [1005_meet_in_middle.java](1005_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(n·2^(n/2)) | AC | 0.109 s | 472 KB | 11303540 |
| [1005_meet_in_middle.rs](1005_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(n·2^(n/2)) | AC | 0.031 s | 244 KB | 11303541 |
