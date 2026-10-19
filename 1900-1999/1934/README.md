# 1934. Black Spot

[Timus 1934](https://acm.timus.ru/problem.aspx?space=1&num=1934) · difficulty 360 · shortest_paths, probability

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find a route from s to t in a simple undirected graph. An edge with
integer percentage p has independent failure probability p/100.
First minimize the number of visited vertices, counting both endpoints.
Among those routes, minimize the probability of at least one failure.
A shortest route whose risk differs from the optimum by at most 10⁻⁶
is also permitted. Limits: 1 second, 64 MB.

## Input

First n,m, with 2≤n≤100000 and 1≤m≤100000. Next come distinct endpoints
s,t in 1..n. The following m records contain a,b,p, where 1≤a,b≤n,
a≠b and 0≤p≤99. There is at most one edge per unordered pair.
The requested output describes an existing s–t route.

## Output

First print k and the route's failure probability as a fraction in 0..1,
with absolute error at most 10⁻⁶. Then print the k vertex identifiers
in route order. The path must minimize k; its true risk may exceed the
best risk for that length by at most 10⁻⁶. Any qualifying path is valid.

## Checking

A checker verifies that the route exists and has the least number of
vertices. Its true failure probability must be within 10⁻⁶ of the optimum,
and the printed probability must be within 10⁻⁶ of that route's true risk.
Any such route is accepted.

## Examples

```
4 4
1 3
1 2 50
2 3 50
1 4 10
4 3 10
```

```
3 0.19
1 4 3
```

## Solution

For an edge, let q=1−p/100. Survival along a path is the product of q;
failure risk is one minus that product. Since q>0, define the additive
edge cost c=−log(q). Minimizing total c maximizes survival.

Run ordinary FIFO BFS from s. Store distance, minimum log cost among
paths of that distance, and the corresponding predecessor. On an edge
u→v, discover v at distance[u]+1 if necessary. Relax its cost only when
distance[v]=distance[u]+1. Thus backward and same-layer edges cannot
introduce longer routes. Every preceding-layer vertex is processed
before a vertex is removed from the queue. By induction on layers,
all shortest predecessors have already offered their candidates, so
the stored cost is optimal when that vertex is removed. It is safe to
stop when t is removed, but not when t is first discovered.

Follow predecessor pointers back from t and reverse the result.
If C is the selected total log cost, compute risk as −expm1(−C).
The log1p and expm1 functions retain accuracy near zero. Logs remain
finite even when multiplying many survival factors would underflow.
Double precision and twelve printed decimal places comfortably meet
the 10⁻⁶ probability tolerance. The edge cost table has only 100 entries.

O(n+m) time and O(n+m) space, including adjacency, BFS state, path and
input/output buffers. No priority queue or recursive traversal is needed.

Read s,t before the edges. Minimize vertex count before probability:
a longer zero-risk route cannot beat a shorter risky route. Summing
percentages is wrong; multiply survival, or add negative logarithms.
Do not stop at the first encounter with t, and do not compare paths
byte for byte. Zero-risk edges and output risk rounded to 1 are legal.
Test 06 illustrates the permitted route-risk tolerance. Apply the two
tolerances separately: the printed value describes the selected route,
so it can differ from the optimum by more than 10⁻⁶.

## Language notes

Adjacency packs a neighbor and its percentage as 100·neighbor+p using
zero-based identifiers; the largest value is 9,999,999, safe in 32 bits.
C++, Go and Rust use vectors/slices of packed edges. Java uses primitive
head/next/edge arrays and a buffered integer reader. Python releases the
input token iterator before BFS and uses typed arrays for distances,
parents and costs. All versions reconstruct iteratively and buffer output.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1934_shortest_paths.cpp](1934_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 7288 KB |
| [1934_shortest_paths.go](1934_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 15636 KB |
| [1934_shortest_paths.java](1934_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 9180 KB |
| [1934_shortest_paths.py](1934_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.406 s | 33792 KB |
| [1934_shortest_paths.rs](1934_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 14136 KB |
