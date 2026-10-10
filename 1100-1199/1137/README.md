# 1137. Joining cyclic bus routes into one route over every segment

[Timus 1137](https://acm.timus.ru/problem.aspx?space=1&num=1137) · difficulty 322 · graphs

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has `n ≤ 100` cyclic bus routes, each a closed sequence of up to
200 stops with ids from 1 to 1000; no two routes share a road segment, and
every stop can be reached from every other one. Build a single cyclic
route that drives along every old segment exactly once, in its old
direction, and uses no other segments. Print `0` if this is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n`, then `n` lines: the number of stops `m` of a route and its `m + 1`
stops, the last equal to the first.

## Output

The number of stops `k` of the new route and its `k + 1` stops in the
same format, or `0`.

## Checking

Any valid route is accepted. The checker verifies the count, that the
route ends where it starts, and that its segments are exactly the old
segments, counted with multiplicity.

## Examples

### Example 1

Input:

```
3
6 1 2 5 7 5 2 1
4 1 4 7 4 1
5 2 3 6 5 4 2
```

Output:

```
15 1 2 5 7 5 2 1 4 7 4 2 3 6 5 4 1
```

## Solution

The segments are the edges of a directed graph, and the new route is an
Euler circuit of it. Every old route is a cycle, so it leaves each stop
as often as it enters it; summed over all routes, every stop has equal
in-degree and out-degree. Together with the promise that all stops are
connected, that is exactly the condition for an Euler circuit, so the
answer is never `0`.

Hierholzer's algorithm finds the circuit. Keep a stack, starting from any
stop of the first route. Look at the top stop: if it still has an unused
outgoing segment, take the next one and push its end; otherwise pop the
stop and append it to the circuit. The circuit comes out reversed. A
pointer per stop to its next unused segment makes the whole walk
`O(E)` for `E ≤ 20000` segments.

Pitfalls:

- a simple walk that follows segments until it gets stuck may close a
  loop too early; the stack splices the missed loops in;
- the count printed is the number of segments, and the list has one more
  stop because the first one is repeated at the end;
- the walk uses an explicit stack, as it can be 20000 steps deep;
- a route may visit the same stop several times and use a road in both
  directions.

The answers were checked by the checker on every test and on 150 random
sets of routes.

## Language notes

- All languages run the same walk with the same order of segments, so
  their answers are identical.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1137_graphs.cpp](1137_graphs.cpp) | G++ 13.2 x64 | graphs | O(E) | AC | 0.015 s | 468 KB |
| [1137_graphs.go](1137_graphs.go) | Go 1.14 x64 | graphs | O(E) | AC | 0.062 s | 3648 KB |
| [1137_graphs.java](1137_graphs.java) | Java 1.8 | graphs | O(E) | AC | 0.093 s | 2104 KB |
| [1137_graphs.py](1137_graphs.py) | Python 3.12 x64 | graphs | O(E) | AC | 0.093 s | 3688 KB |
| [1137_graphs.rs](1137_graphs.rs) | Rust 1.75 x64 | graphs | O(E) | AC | 0.015 s | 1268 KB |
