# 1806. Mobile Telegraphs

[Timus 1806](https://acm.timus.ru/problem.aspx?space=1&num=1806) · difficulty 178 · graphs

Original problem by Pavel Atnashev, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n telegraphs has a distinct ten-digit number. A message can go
from a to b if b differs from a in exactly one digit or by swapping two
digits; it takes cost[l] time, where l is the length of their common
prefix. Find the fastest route from the first telegraph to the last
one, or report that there is none.

## Input

n (2 ≤ n ≤ 50000), then the ten costs from 1 to 10000 in non-increasing
order, then the n numbers; the first is Anka's, the last Chapaev's.

## Output

"-1", or the least time, the number of telegraphs on the route and
their numbers from the first to the last.

## Examples

### Example 1

Input:

```
5
100 10 10 10 1 1 1 1 1 1
9123493342
3123493942
9223433942
3223493942
9223433945
```

Output:

```
211
5
1 2 4 3 5
```

### Example 2

Input:

```
2
1 1 1 1 1 1 1 1 1 1
0123493342
0223433945
```

Output:

```
-1
```

## Solution

Run Dijkstra's algorithm from the first telegraph, building the edges
on the fly. A telegraph has at most 90 numbers one changed digit away
and 45 numbers one swap away, and a hash map from numbers to
telegraphs tells which of them exist. For a change at digit p, or a
swap of digits p < q, the common prefix is exactly p, so its cost is
cost[p]. With the numbers stored as integers, a neighbour is the
number plus a multiple of a power of ten. The search stops when the
last telegraph leaves the queue, and the route is read back along the
predecessors. `O(135·n log n)`.

In the first example the route swaps the first and seventh digits
(100), changes the second digit (10), swaps the first and sixth digits
(100) and changes the last one (1): 211.

Pitfalls:

- ten-digit numbers do not fit in 32 bits, and leading zeros only
  matter for the digit positions;
- a swap of two equal digits changes nothing and is not an edge;
- any fastest route is accepted.

The checker sums the costs along the printed route, requires every
step to be one changed digit or one swap, and compares the total with
the least time. All solutions pass it on small random cases and on
50000 telegraphs in dense, sparse, chain-like and unreachable layouts,
against an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1806_graphs.cpp](1806_graphs.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.312 s | 4760 KB |
| [1806_graphs.go](1806_graphs.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.328 s | 8788 KB |
| [1806_graphs.java](1806_graphs.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.531 s | 12700 KB |
| [1806_graphs.py](1806_graphs.py) | Python 3.12 x64 | graphs | O(135 n log n) | AC | 2.343 s | 16128 KB |
| [1806_graphs.rs](1806_graphs.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.218 s | 6672 KB |
