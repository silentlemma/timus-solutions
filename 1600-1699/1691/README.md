# 1691. Algorithm Complexity

[Timus 1691](https://acm.timus.ru/problem.aspx?space=1&num=1691) · difficulty 2798 · graphs

Original problem by Ivan Burmistrov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In a directed graph without parallel arcs (loops allowed), let F(N) be
the number of paths of length N from s to t. Find the least k ≥ 0 such
that F(N) ≤ C · Nᵏ for some constant C and every N ≥ 1, or −1 if F
grows faster than any polynomial.

## Input

n, m, s, t (1 ≤ n, m ≤ 100000), then the m arcs.

## Output

k, or −1.

## Examples

### Example 1

Input:

```
2 3 1 2
1 1
1 2
2 2
```

Output:

```
1
```

### Example 2

Input:

```
3 6 1 2
1 2
2 1
1 3
3 1
2 3
3 2
```

Output:

```
-1
```

## Solution

Only vertices lying on some path from s to t matter: those reachable
from s that can also reach t. If t is unreachable, F is zero and k = 0.
These vertices form whole strongly connected components, since anything
on a cycle with such a vertex is also between s and t.

A component with more arcs than vertices contains two different cycles
through a common vertex. A path can then wind around them in
exponentially many orders, so the answer is −1. Otherwise every
component is a single vertex, possibly with a loop, or one simple
cycle, which has as many arcs as vertices. A path that passes through
c ≥ 1 simple cycles spends its spare length on them in about N^(c − 1)
ways. So F(N) is at most C · N^(c − 1), and along a suitable arithmetic
progression of N it reaches that order. Hence k = max(0, c − 1), where
c is the largest number of cyclic components on one path from s to t.

Kosaraju's algorithm numbers the components so that arcs between them
go from lower to higher numbers. One pass in that order computes c as
a longest path, weighting each cyclic component 1. Every step uses an
explicit stack. `O(n + m)`.

Pitfalls:

- a component that holds two cycles but cannot reach t (or cannot be
  reached from s) does not matter (test 07);
- one cycle on the way keeps F bounded, so k = 0, not 1 (test 08);
- a loop is a cycle of length 1, and s = t is allowed (test 04);
- recursion depth would reach 10⁵, so the searches use their own
  stacks.

The answers match an independent accepted implementation. On 121 tiny
graphs they also match the growth of F(N), computed exactly up to
N = 3000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1691_graphs.cpp](1691_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.171 s | 9792 KB |
| [1691_graphs.go](1691_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.187 s | 18576 KB |
| [1691_graphs.java](1691_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.296 s | 37820 KB |
| [1691_graphs.py](1691_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.515 s | 55192 KB |
| [1691_graphs.rs](1691_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.093 s | 20620 KB |
