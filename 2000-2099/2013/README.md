# 2013. Route-Independent Values Before and After a Vertex

[Timus 2013](https://acm.timus.ru/problem.aspx?space=1&num=2013) · difficulty 940 · graphs

Original problem by Alex Samsonov, prepared by Egor Shchelkonogov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A walk starts at vertex 1 of a directed graph, carrying value 0. On
entering a vertex, record the incoming value. Its parameter `k` then
replaces that value if `k>0`; when `k=0`, the value stays unchanged.
Record the outgoing value and follow any outgoing edge. Vertices may be
revisited. For every vertex, determine whether its incoming value and
its outgoing value are each the same for all possible walks reaching
that visit. Every vertex is reachable from 1.

## Input

First `n`, `1 ≤ n ≤ 100,000`. For each vertex in order, a row gives `k
m` and `m` distinct outgoing target IDs in increasing order. Values
satisfy `0 ≤ k ≤ 100,000`, `0 ≤ m ≤ n`; targets are in `1..n`, including
possibly the vertex itself. The total number of edges is at most
100,000. Time limit 1 second, memory 64 MB.

## Output

Print one line per vertex in ID order: the answer before entry's
replacement and the answer after it. Use `sober` for an always-zero
value, the positive integer for an always-equal positive value, or
`unknown` if different walks can give different values. Spelling is
lowercase. The unique tokens are compared token by token.

## Checking

Outputs are compared token by token.

## Examples

```
5
0 2 2 3
6 1 4
5 2 4 5
5 1 5
0 0
```

```
sober sober
sober 6
sober 5
unknown 5
5 5
```

```
2
0 2 1 2
0 2 1 2
```

```
sober sober
sober sober
```

In the first example, vertex 4 can be entered with 6 or 5, so its entry
is unknown; its own replacement makes its exit 5. Both ways of reaching
vertex 5 then carry 5. In the second example no vertex changes the
initial value, so every entry and exit remains zero despite the cycles.

## Solution

For each entry keep one of: unreached, one known value (including zero),
or unknown. Use different negative codes for unreached and unknown. Seed
entry 1 with zero and put it in a work queue. That initial zero remains
a possible entry even if the walk later returns to vertex 1.

When a vertex is removed from the queue, its outgoing state is its fixed
positive `k`, or its current entry state when `k=0`. Offer this state to
every successor. An unreached successor takes the offered state. Equal
known values stay equal; different states merge to unknown. Unknown
absorbs every later offer. Enqueue a successor only when its stored
entry changes. After the queue empties, compute each exit by the same
replacement rule.

The summary is sufficient: a replacement discards the entire previous
history, while a zero vertex preserves it. Merging two different
feasible values, or a state already known to have two values, correctly
certifies ambiguity. Equal values from different vertices are still
equal; vertex identity is irrelevant. Every propagated possibility comes
from a real walk, so ambiguity is never invented. At termination every
edge has transferred its predecessor's final exit state; induction over
walk length shows that every possible finite walk is represented. Thus a
remaining single value is shared by all walks, and unknown means at
least two possibilities. Cycles require no special ordering.

A vertex changes at most twice: unreached to a known value, then to
unknown (or directly to unknown). Each change causes at most one queue
insertion. Each adjacency list is scanned at most twice, proving time
`O(n+m)` and space `O(n+m)`. Store adjacency in flat arrays with offsets
and use an iterative queue; no recursion or per-path enumeration is
needed.

## Language notes

A first visit does not finalize a value. A later conflicting route must
propagate through zero vertices. Positive vertices reset even unknown
inputs, and revisiting vertex 1 can make its entry unknown. A zero-only
cycle stays zero; equal positive labels do not conflict. All vertices
are reachable, so unreached is never printed. Java's queue has `2n`
slots from the change bound; Go, C++ and Rust use growing arrays. Python
uses compact signed integer arrays for the graph and states, a deque,
and releases parsed tokens before constructing output; it runs in
CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2013_graphs.cpp](2013_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.078 s | 2752 KB |
| [2013_graphs.go](2013_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.234 s | 11180 KB |
| [2013_graphs.java](2013_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.140 s | 14336 KB |
| [2013_graphs.py](2013_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.453 s | 15644 KB |
| [2013_graphs.rs](2013_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.031 s | 6608 KB |
