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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2216_prefix_sums.cpp](2216_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 604 KB |
| [2216_prefix_sums.go](2216_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.046 s | 5596 KB |
| [2216_prefix_sums.java](2216_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + K) | AC | 0.093 s | 784 KB |
| [2216_prefix_sums.py](2216_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.140 s | 15108 KB |
| [2216_prefix_sums.rs](2216_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 2948 KB |
