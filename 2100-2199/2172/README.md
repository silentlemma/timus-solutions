# 2172. Fewest problems to place every sponsor's mentions

[Timus 2172](https://acm.timus.ru/problem.aspx?space=1&num=2172) · difficulty 761 · greedy, constructive

Original problem by Valentin Zuev, from the Ural Team Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sponsor i wants to appear in exactly sᵢ different problems, and no
problem may mention more than K different sponsors. Find the smallest
number of problems M and a plan that lists the sponsors of every
problem. Any valid plan is accepted. The limits are 1 second and 256 MB.

## Input

N and K, 1 ≤ N, K ≤ 1000, then s₁ … s_N, 1 ≤ sᵢ ≤ 1000, with a total of
at most 10⁵.

## Output

M, then for every problem the number of its sponsors and their numbers.

## Checking

A checker verifies M and that the plan meets every wish and limit.

## Examples

### Example 1

Input:

```
5 2
1 1 1 1 1
```

Output:

```
3
1 5
2 2 3
2 4 1
```

## Solution

Two lower bounds are clear: the sponsor with the largest wish needs that
many different problems, and the S = Σ sᵢ mentions need at least
⌈S / K⌉ problems. So M ≥ max(max sᵢ, ⌈S / K⌉), and this many is enough.

Write all mentions in a row, sponsor by sponsor, and hand them out to
the problems in turn: mention t goes to problem t mod M. The mentions of
one sponsor are consecutive and there are at most M of them, so they
fall into different problems. Every problem receives at most ⌈S / M⌉ ≤ K
mentions. The work is O(S).

In the example five sponsors with one wish each need ⌈5 / 2⌉ = 3
problems.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2172_greedy_constructive.cpp](2172_greedy_constructive.cpp) | G++ 13.2 x64 | greedy, constructive | O(S) | AC | 0.062 s | 3732 KB |
| [2172_greedy_constructive.go](2172_greedy_constructive.go) | Go 1.14 x64 | greedy, constructive | O(S) | AC | 0.031 s | 4724 KB |
| [2172_greedy_constructive.java](2172_greedy_constructive.java) | Java 1.8 | greedy, constructive | O(S) | AC | 0.156 s | 17408 KB |
| [2172_greedy_constructive.py](2172_greedy_constructive.py) | Python 3.12 x64 | greedy, constructive | O(S) | AC | 0.187 s | 18848 KB |
| [2172_greedy_constructive.rs](2172_greedy_constructive.rs) | Rust 1.75 x64 | greedy, constructive | O(S) | AC | 0.046 s | 8796 KB |
