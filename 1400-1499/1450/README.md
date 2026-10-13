# 1450. Russian Pipelines

[Timus 1450](https://acm.timus.ru/problem.aspx?space=1&num=1450) · difficulty 149 · dp

Original problem by Dmitry Kovalioff, Ilya Grebnov and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A gas network has N stations (2 ≤ N ≤ 500) and M one-way pipelines
(0 ≤ M ≤ 124750), each from A to B with profit C (1 ≤ C ≤ 10000); a pair
of stations has at most one pipeline, and the network has no cycles: if
gas can flow from X to Y, it cannot flow back. Find the most profitable
route from station S to station F, the profit of a route being the sum
over its pipelines, or print "No solution" if F cannot be reached.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M, then M lines A, B, C, then S and F.

## Output

The largest profit, or "No solution".

## Examples

### Example 1

Input:

```
6 7
6 5 10
1 4 11
1 2 4
3 1 5
2 4 5
6 3 1
6 1 3
6 4
```

Output:

```
17
```

The best route in the example is 6, 3, 1, 4.

## Solution

Without cycles the longest path is a simple dynamic programme. Order the
stations topologically with Kahn's method: start from the stations with
no incoming pipelines and release a station once all pipelines into it
have been taken. In that order every station is final before any of its
pipelines is used, so best[w] = max(best[v] + C) over the pipelines
v → w, with best[S] = 0 and stations unreachable from S left empty. The
answer is best[F]. `O(N + M)`.

Pitfalls:

- an unreachable F, including when the pipelines lead from F to S
  (tests 02, 03, 06);
- the longest route may take more pipelines than the direct one (tests
  05, 07);
- stations unreachable from S must not pass on a profit, even though
  they still have to be ordered.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1450_dp.cpp](1450_dp.cpp) | G++ 13.2 x64 | dp | O(N + M) | AC | 0.187 s | 1668 KB |
| [1450_dp.go](1450_dp.go) | Go 1.14 x64 | dp | O(N + M) | AC | 0.203 s | 6332 KB |
| [1450_dp.java](1450_dp.java) | Java 1.8 | dp | O(N + M) | AC | 0.140 s | 2460 KB |
| [1450_dp.py](1450_dp.py) | Python 3.12 x64 | dp | O(N + M) | AC | 0.406 s | 35968 KB |
| [1450_dp.rs](1450_dp.rs) | Rust 1.75 x64 | dp | O(N + M) | AC | 0.046 s | 5760 KB |
