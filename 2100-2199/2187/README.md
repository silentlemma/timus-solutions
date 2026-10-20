# 2187. Cutting a degree-increasing walk into paid journeys

[Timus 2187](https://acm.timus.ru/problem.aspx?space=1&num=2187) · difficulty 1357 · dp, graphs

Original problem by Artyom Abaturov, from the Ural School Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph has n islands with aᵢ coins and m edges. A journey is a
path along edges where each next island has a strictly larger degree;
a journey of length i costs bᵢ, and only the island where it ends gives
its coins. Starting on island 1 with a₁ coins, any number of journeys
may follow one another, each starting where the last one ended. Find
the most coins that can be kept. The limits are 1 second and 256 MB.

## Input

n and m, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, then a₁ … a_n and b₁ … b_{n−1},
all between 1 and 10⁹, then the m edges.

## Output

The largest total.

## Examples

### Example 1

Input:

```
6 10
5 6 8 2 5 7
3 5 2 4 6
1 2
1 3
1 4
2 3
2 4
2 5
3 4
3 6
4 5
4 6
```

Output:

```
10
```

## Solution

Degrees keep growing from one journey to the next, so all journeys
together form a single degree-increasing path from island 1, cut into
pieces at the islands where the coins are taken. Orienting every edge
toward the larger degree gives a DAG, and degrees along a path of
length L are distinct numbers whose sum is at most 2m, so L is
O(√m).

Let f(v) be the best total when the last journey ends at v. Going
through the islands in order of degree, each island v keeps a row
whose entry L is the best f(u) over islands u with a path of exactly L
edges to v; the row is built from the rows of its predecessors shifted
by one. Then

f(v) = aᵥ + max over L ≥ 1 of (row[L] − b_L),

f(1) = a₁, and the answer is the largest f. Only islands reachable from
1 take part.

The compiled solutions push each row along the outgoing edges. The
Python version saves time twice: each island starts from a copy of its
longest incoming row and only merges the others into it, and the same
DP can also run backward from the ends of paths with the edges
reversed, so it picks the direction whose rows add up to less work.

In the example one journey of length 1 to island 3 gives 5 + 8 − 3 = 10.

Each edge merges a row of length O(√m), so the DP takes O(m √m) time.
Reading and initializing the input takes O(n + m), and the compiled
solutions order vertices by counting sort, giving O(n + m √m) total
time. Python uses comparison sorting, giving O(n log n + m √m) total
time. A pitfall illustrated by test 03 is that isolated or unreachable
islands still need to be read and initialized; n need not be O(m).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2187_dp_graphs.cpp](2187_dp_graphs.cpp) | G++ 13.2 x64 | dp, graphs | O(n + m √m) | AC | 0.078 s | 6724 KB |
| [2187_dp_graphs.go](2187_dp_graphs.go) | Go 1.14 x64 | dp, graphs | O(n + m √m) | AC | 0.078 s | 17156 KB |
| [2187_dp_graphs.java](2187_dp_graphs.java) | Java 1.8 | dp, graphs | O(n + m √m) | AC | 0.234 s | 9912 KB |
| [2187_dp_graphs.py](2187_dp_graphs.py) | PyPy 3.10 x64 | dp, graphs | O(n log n + m √m) | AC | 0.343 s | 55364 KB |
| [2187_dp_graphs.rs](2187_dp_graphs.rs) | Rust 1.75 x64 | dp, graphs | O(n + m √m) | AC | 0.062 s | 15008 KB |
