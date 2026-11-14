# 2216. Fewest watched elevators that every route from bottom to top must use

[Timus 2216](https://acm.timus.ru/problem.aspx?space=1&num=2216) · difficulty 662 · prefix_sums

Original problem by Matvey Dmitriev, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A building has floors 1 … N and K elevators, elevator i moving between
any floors of [lᵢ, rᵢ]. Put cameras into as few elevators as possible
so that everyone who goes from floor 1 to floor N rides at least one
watched elevator, or print −1. Floors can only be reached using elevators,
and every floor is reachable from every other floor. The limits are
1 second and 256 MB.

## Input

N and K, 1 ≤ N, K ≤ 10⁵, then the K segments with 1 ≤ lᵢ ≤ rᵢ ≤ N.

## Output

The fewest cameras, or −1.

## Examples

### Example 1

Input:

```
1984 1
1 1984
```

Output:

```
1
```

### Example 2

Input:

```
2 2
1 2
1 2
```

Output:

```
2
```

## Solution

With N = 1 nobody needs an elevator, so no choice of cameras works and
the answer is −1.

Otherwise look at the gap between floors f and f + 1. Every route from
1 to N has to cross it, and only elevators with l ≤ f < r cross it, so
watching all of them catches everyone. Conversely, if some set of
cameras leaves at least one unwatched elevator over every gap, the
unwatched elevators' segments overlap all the way from 1 to N and form
an unwatched route. So the answer is the smallest number of elevators
over any single gap.

A difference array (+1 at l, −1 at r) gives the number of elevators
over each gap as a running sum, and the minimum over f = 1 … N − 1 is
the answer.

Connectivity guarantees a positive minimum when N > 1. A pitfall is to
require a shared gap for transfers: intervals meeting at just one floor
also allow a transfer (test 12).

In the second example both elevators cross the only gap, so both need
a camera.

This takes O(N + K).

## Optimized solutions

Read elevator intervals as a stream and accumulate their endpoint updates in a compact difference array. The minimum prefix sum over gaps between floors is the answer.

Python submission 11317733 took 0.156 s and used 1560 KB. The simple version took 0.14 s and used 14948 KB.

Go submission 11317737 took 0.031 s and used 1312 KB. The simple version took 0.015 s and used 5784 KB.

Rust submission 11317747 took 0.015 s and used 596 KB. The simple version took 0.062 s and used 3156 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321723 · Java 1.8 №11321729 · Go 1.14 x64 №11322089 · Python 3.12 x64 №11322090 · Rust 1.75 x64 №11322092.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2216_prefix_sums.cpp](2216_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + K) | AC | 0.046 s | 800 KB | 11321723 |
| [2216_prefix_sums.go](2216_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 5784 KB | 11322089 |
| [2216_prefix_sums.java](2216_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + K) | AC | 0.125 s | 960 KB | 11321729 |
| [2216_prefix_sums.py](2216_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.14 s | 14948 KB | 11322090 |
| [2216_prefix_sums.rs](2216_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.062 s | 3156 KB | 11322092 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2216_prefix_sums_optimized.py](2216_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.156 s | 1560 KB | 11317733 |
| [2216_prefix_sums_optimized.go](2216_prefix_sums_optimized.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 1312 KB | 11317737 |
| [2216_prefix_sums_optimized.rs](2216_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 596 KB | 11317747 |

\* The marked solutions can improve their target rankings.
