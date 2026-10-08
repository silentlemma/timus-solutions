# 1017. Counting staircases: partitions into distinct parts

[Timus 1017](https://acm.timus.ru/problem.aspx?space=1&num=1017) · difficulty 157 · dp

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A staircase built from `N` equal cubes (`5 ≤ N ≤ 500`) is a sequence of at
least two columns (steps) of strictly increasing heights, each at least 1,
using all `N` cubes. Count the different staircases.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of staircases.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
```

Output:

```
3
```

### Example 2

Input:

```
11
```

Output:

```
11
```

## Solution

A staircase is determined by the set of its step heights: they are distinct
and their order is fixed (increasing). So the answer is the number of ways
to write `N` as a sum of **distinct** positive integers, minus one — the
"staircase" of a single step of `N` cubes is not allowed.

**0/1 knapsack counting.** `ways[s]` is the number of sets of distinct sizes
with sum `s`. Start with `ways[0] = 1` and add the sizes `1, 2, ..., N` one
by one: for a size `k`, `ways[s] += ways[s - k]` for `s` going **down** from
`N` to `k`, so that every size is used at most once (going up would allow
repeats). After all sizes, the answer is `ways[N] - 1`.

`O(N^2) = 250 000` steps. The numbers grow fast: for `N = 500` the answer is
about `7.3 · 10^14`, so 64-bit integers are needed.

Alternatively, `f(n, k)` — partitions of `n` into distinct parts not smaller
than `k` — satisfies `f(n, k) = f(n, k + 1) + f(n - k, k + 1)`, which gives
the same numbers with memoization.

Pitfalls:

- going over `s` upwards counts partitions with repeated parts;
- forgetting to subtract the one-step partition;
- signed 32-bit integers overflow from `N = 226` on.

## Language notes

The same DP in every language with 64-bit integers; Python's integers are
unbounded.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1017_dp.cpp](1017_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 196 KB |
| [1017_dp.go](1017_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 1088 KB |
| [1017_dp.java](1017_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 1580 KB |
| [1017_dp.py](1017_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 420 KB |
| [1017_dp.rs](1017_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.015 s | 236 KB |
