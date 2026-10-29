# 1991. Count unused supplies and unmatched targets

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · difficulty 48 · implementation

Original problem by Denis Dublennykh, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` independent groups, each with exactly `k` targets. Group
`i` receives `a_i` supplies, each usable once to remove one target in
that same group. Every use succeeds. Supplies cannot be transferred
between groups. After every group removes as many targets as possible,
count the supplies left unused and the targets left unmatched.

The bounds are `1≤n,k≤10000` and `0≤a_i≤100000`. Time limit: 1 second;
memory limit: 64 MB.

## Input

The first line contains `n k`. The next line contains the `n` supply counts.

## Output

Two integers: total unused supplies, followed by total remaining targets.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
4 5
2 7 5 0
```

Output:

```
2 8
```

The groups leave `(unused,targets)` equal to `(0,3)`, `(2,0)`, `(0,0)`,
`(0,5)`. Their sum is `(2,8)`.

## Solution

Each group uses min(aᵢ, k) supplies on min(aᵢ, k) targets. So it leaves
aᵢ − k unused supplies when aᵢ > k, and k − aᵢ remaining targets
otherwise. Add these up over the groups. `O(n)`.

Pitfalls:

- supplies do not move between groups, so one group can have spare
  supplies while another still has targets: comparing only the totals
  is wrong;
- the unused total reaches 10 000 · 99 999 ≈ 10⁹, which still fits a
  32-bit signed integer.

## Optimized solutions

The optimized C++ solution reads and writes with `scanf` and `printf`
instead of `iostream`: 132 KB instead of 448 KB. The totals are the
same.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB | 11292383 |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB | 11292384 |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 472 KB | 11303526 |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB | 11292385 |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB | 11292387 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1991_implementation_optimized.cpp](1991_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 132 KB | 11303652 |
