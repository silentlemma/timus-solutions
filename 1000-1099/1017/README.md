# 1017. Counting staircases: partitions into distinct parts

[Timus 1017](https://acm.timus.ru/problem.aspx?space=1&num=1017) · difficulty 158 · dp

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

`O(N^2)` time, at most 125 250 updates. The numbers grow fast: for
`N = 500` the answer is about `7.3 · 10^14`, so 64-bit integers are
needed.

Alternatively, `f(n, k)` — partitions of `n` into distinct parts not smaller
than `k` — satisfies `f(n, k) = f(n, k + 1) + f(n - k, k + 1)`, which gives
the same numbers with memoization.

Pitfalls:

- going over `s` upwards counts partitions with repeated parts;
- forgetting to subtract the one-step partition;
- signed 32-bit integers overflow from `N = 226` on.

## Optimized solutions

The optimized C++ solution keeps the table in a fixed array of 501
`long long` values on the stack instead of a `vector`, since `N ≤ 500`,
and so needs no heap allocation: {1017_dp_optimized.cpp}.

The optimized Java solution reads the single number with
`StreamTokenizer` over a `BufferedReader` instead of `Scanner`, whose
regular-expression machinery costs time and memory to load:
{1017_dp_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1017_dp_optimized.cpp`: time reduction +0.00%; memory reduction
  +46.94%; base: `1017_dp.cpp`.

- `1017_dp_optimized.java`: time reduction +14.68%; memory reduction
  +71.65%; base: `1017_dp.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1017_dp.rs](1017_dp.rs).

The same DP in every language with 64-bit integers; Python's integers are
unbounded.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1017_dp.cpp](1017_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 196 KB | 11278180 |
| [1017_dp.go](1017_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 1088 KB | 11278186 |
| [1017_dp.java](1017_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 1580 KB | 11278192 |
| [1017_dp.py](1017_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 420 KB | 11278189 |
| [1017_dp.rs](1017_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.015 s | 236 KB | 11278195 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1017_dp_optimized.cpp](1017_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 104 KB | 11305919 |
| [1017_dp_optimized.java](1017_dp_optimized.java) | Java 1.8 | dp | O(N^2) | AC | 0.093 s | 448 KB | 11305922 |
