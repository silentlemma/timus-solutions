# 1987. Shortest containing interval in a laminar family

[Timus 1987](https://acm.timus.ru/problem.aspx?space=1&num=1987) · difficulty 168 · greedy

Original problem by Mikhail Rubinchik, idea by Nikita Pervukhin, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `n` distinct closed intervals, every pair is either disjoint or
one contains the other. For each of `m` query points, find the shortest
interval containing it. Output its original 1-based input index, or −1
if none exists.

The bounds are `1≤n,m≤10⁵`, `1≤aᵢ<bᵢ≤10⁹`, and `1≤cⱼ≤10⁹`. Intervals are
sorted by nondecreasing left endpoint; ties are ordered by decreasing
length. Queries are sorted nondecreasingly. Time limit: 1 second; memory
limit: 64 MB.

## Input

Read `n`, then `n` pairs `aᵢ bᵢ`, then `m`, followed by the `m` query
coordinates. Input numbering of intervals determines the output indices.

## Output

For each query, one line containing the index of the shortest covering
interval, or −1.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
3
2 10
2 3
5 7
11
1
2
3
4
5
6
7
8
9
10
11
```

Output:

```
-1
2
2
1
3
3
3
1
1
1
-1
```

## Solution

Sweep through the query points from left to right and advance a pointer
through the already sorted intervals. Keep a stack of interval indices.
Its entries form a chain from outer intervals to inner ones.

For query `c`, process every not-yet-seen interval whose left endpoint
`a` satisfies `a≤c`. Before pushing it, pop stack entries with right
endpoint strictly less than `a`: they are disjoint from this interval
and have ended. If an entry remains, it contains the new interval.
Indeed, they intersect at `a`; the laminar condition excludes a partial
overlap, and input ordering excludes a new outer interval arriving after
its inner one. When left endpoints are equal, the outer interval is
explicitly listed first. Thus pushing preserves the containment chain.

After all starts at most `c` have been processed, pop intervals with
right endpoint strictly less than `c`. Every remaining entry contains
`c`, since its left endpoint has already been reached and its right
endpoint has not passed. The top is the innermost member and therefore
the shortest. If the stack is empty, return −1.

No discarded interval can answer a later query: it ended before an
already reached coordinate, and queries never move left. An interval not
yet processed starts after `c` and cannot contain it. Every previously
processed covering interval remains in the chain, so the top is optimal
among all intervals, not only among an arbitrary subset. Distinct nested
intervals have strictly different lengths, making the shortest covering
choice unique.

For the example, points 2 and 3 belong to interval 2. Point 4 is outside
that inner interval but inside interval 1. Points 5–7 belong to interval
3, while 8–10 return interval 1. Points 1 and 11 are uncovered. These
are exactly the eleven output lines.

Each interval is pushed at most once and popped at most once across both
cleanup loops. The interval pointer only advances, so total time is
`O(n+m)`, despite the nested loops. The stack needs `O(n)` auxiliary
memory. These standalone programs buffer the input or answers, so their
complete storage is `O(n+m)`. No sorting, recursion, heap or binary
search is required.

Pitfalls:

- Both expiration checks use strict `<`, because right endpoints still
  belong to the interval.
- Process every interval starting at the query coordinate before answering it.
- Equal left endpoints must retain the supplied outer-before-inner order.
- Preserve original 1-based interval indices; do not renumber the stack depth.
- Pop ended children before falling back to an enclosing ancestor.
- The laminar and sorted-input guarantees are essential to the linear algorithm.

## Language notes

All five versions implement the same sweep. Coordinates and indices fit
signed 32-bit integers under the stated bounds. C++ and Rust use
vectors, Java uses primitive arrays, and Go uses slices. Go and Java
include fast integer readers. Python stores endpoint arrays, consumes
query tokens through an iterator, and buffers the answers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1987_greedy.cpp](1987_greedy.cpp) | G++ 13.2 x64 | greedy | O(n+m) | AC | 0.031 s | 1288 KB |
| [1987_greedy.go](1987_greedy.go) | Go 1.14 x64 | greedy | O(n+m) | AC | 0.031 s | 10676 KB |
| [1987_greedy.java](1987_greedy.java) | Java 1.8 | greedy | O(n+m) | AC | 0.125 s | 5572 KB |
| [1987_greedy.py](1987_greedy.py) | Python 3.12 x64 | greedy | O(n+m) | AC | 0.187 s | 24900 KB |
| [1987_greedy.rs](1987_greedy.rs) | Rust 1.75 x64 | greedy | O(n+m) | AC | 0.031 s | 5328 KB |
