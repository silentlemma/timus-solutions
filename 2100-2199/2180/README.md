# 2180. Adding to a subtree down to a depth and reading one vertex

[Timus 2180](https://acm.timus.ru/problem.aspx?space=1&num=2180) · difficulty 1297 · fenwick

Original problem by Vladimir Cherepanov, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rooted tree has N vertices with root 1. An update "+ v k x" adds x to
v and to every descendant at most k levels below it, and a query "? v"
asks for the total added to v so far. The limits are 2 seconds and
256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then the parents p₂ … p_N with pᵢ < i, then Q,
1 ≤ Q ≤ 10⁵, and Q lines "+ v k x" with 0 ≤ k ≤ N, 1 ≤ x ≤ 10⁹, or
"? v".

## Output

The answer to each query.

## Examples

### Example 1

Input:

```
4
1 1 2
6
? 3
+ 1 1 5
? 2
+ 2 1 9
? 4
? 2
```

Output:

```
0
5
9
14
```

## Solution

With an Euler tour, the subtree of v is an interval of entry times, and
the update reaches exactly the vertices u in that interval with
depth(u) ≤ depth(v) + k. A query at u therefore sums the updates whose
interval contains entry(u) and whose depth limit is at least depth(u),
a two-dimensional question answered online.

The outer Fenwick tree runs over entry times and stores each update as
+x at the start of the interval and −x after its end, so a prefix sum
up to entry(u) keeps exactly the intervals containing u. Each outer node
holds an inner Fenwick tree for the depth condition. C++, Go, Java and
Rust retain all vertices and compress the partial updates' depth limits
in each outer node reached by an endpoint update. An update adds at its
limit; a query sums all limits at or above depth(u), using reversed ranks.

Python instead keeps only vertices that are ever queried, mapping each
subtree to an interval of these retained entry times. Its inner trees
compress the query depths in each outer node visited by a prefix query.
An update adds to all stored depths at or below its limit, and a query
reads its own depth, using a Fenwick tree with reversed traversal.
Both variants read all operations to prepare the coordinates, then
process them in input order. Total memory is O(N + Q log N).

Two cases skip the inner trees in every implementation: k = 0 only
touches v and goes to a plain array; a limit that reaches the deepest
vertex of the subtree needs no depth test and goes to an ordinary outer
Fenwick tree.

A pitfall is treating vertex labels as subtree intervals: labels can be
interleaved (test 06), so Euler entry times are required. The depth bound
is inclusive, including vertices exactly k levels below v (test 09).

In the example the first update reaches 1, 2 and 3 with 5, and the
second reaches 2 and 4 with 9, so vertex 2 has 14.

Each operation costs O(log² N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2180_fenwick.cpp](2180_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + Q) log² N) | AC | 0.609 s | 35640 KB |
| [2180_fenwick.go](2180_fenwick.go) | Go 1.14 x64 | fenwick | O((N + Q) log² N) | AC | 1.250 s | 60432 KB |
| [2180_fenwick.java](2180_fenwick.java) | Java 1.8 | fenwick | O((N + Q) log² N) | AC | 1.015 s | 53608 KB |
| [2180_fenwick.py](2180_fenwick.py) | PyPy 3.10 x64 | fenwick | O((N + Q) log² N) | AC | 0.843 s | 65728 KB |
| [2180_fenwick.rs](2180_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + Q) log² N) | AC | 0.687 s | 54696 KB |
