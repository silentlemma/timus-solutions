# 2025. Maximize pairs across groups

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · difficulty 60 · math

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Partition `n` distinct objects into between two and `k` nonempty groups.
Every object must belong to exactly one group. An unordered pair
contributes one if its two objects are in different groups, and zero
otherwise. Find the largest possible total number of contributing pairs.
Only the maximum count is required, not a partition.

There are `1 ≤ T ≤ 10` independent test cases. Each satisfies `2 ≤ k ≤ n
≤ 10000`. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `T`. Each of the next `T` lines contains `n` and `k`.

## Output

For each case, print one integer on a separate line, in the input order.

## Checking

Outputs are compared token by token.

## Examples

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solution

Using all k groups is best: with fewer groups some group has at least
two objects, and splitting it adds pairs. With group sizes s₁, …, s_k
the number of pairs from different groups is (n² − Σ sᵢ²) / 2, so the
sum of squares should be as small as possible. That happens when the
sizes differ by at most one, since moving an object from a group of
size a to a group of size b ≤ a − 2 lowers the sum of squares. So
r = n mod k groups get q + 1 objects and the other k − r get
q = n div k, and the answer is (n² − (k − r)·q² − r·(q + 1)²) / 2.
`O(1)` per test.

For n = 6, k = 3 the groups are 2, 2, 2 and the answer is 12.

Pitfalls:

- every pair counts once, hence the division by two;
- integer arithmetic only, no average in floating point.

## Optimized solutions

The optimized C++ solution uses the same formula, but reads and writes
with `scanf` and `printf` instead of `iostream`: 128 KB instead of
444 KB, with the same time.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB | 11292869 |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB | 11292876 |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1628 KB | 11303364 |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11292879 |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11292891 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2025_math_optimized.cpp](2025_math_optimized.cpp) \* | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB | 11303661 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
