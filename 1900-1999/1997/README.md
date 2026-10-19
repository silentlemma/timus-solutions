# 1997. Pairing visits around a forbidden duration interval

[Timus 1997](https://acm.timus.ru/problem.aspx?space=1&num=1997) · difficulty 549 · matching

Original problem by Denis Dublennykh, prepared by Oleg Dolgorukov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A door log records every arrival and departure of visitors. The room is
empty before and after the log. Every visitor must have stayed for at
most `b` time units or for at least `a`; durations strictly between
these limits are forbidden. Determine whether the events can describe
only such visitors. If they can, give any complete assignment of
departures to arrivals.

Bounds: `2≤n≤1000` events, `1≤b,a≤10^9`, `b+1<a`. Event times are
distinct and increasing, between 1 and `10^9`. Direction 0 is arrival
and direction 1 is departure. Time limit 1 second, memory 64 MB.

## Input

The first line contains `a b`; the next contains `n`. Each of the
following `n` lines gives a time and direction.

## Output

Print `Liar` if no complete assignment exists. Otherwise print `No
reason` and one pair of arrival and departure times per visitor. Any
valid pairing and any order of pairs are accepted.

## Checking

A checker verifies that the pairs use every arrival and departure once
and that every duration is allowed; `Liar` is accepted only when no
assignment exists. Any valid assignment in any order is accepted.

## Examples

```
6 3
4
1 0
2 0
5 1
10 1
```

```
No reason
1 10
2 5
```

```
6 3
4
1 0
2 0
6 1
10 1
```

```
Liar
```

In the first example the visits `(1,10)` and `(2,5)` last 9 and 3 units,
satisfying the long and short limits. In the second example the
departure at 6 cannot use either arrival: durations 5 and 4 are both
forbidden. The later departure cannot repair that event.

## Solution

Create a bipartite graph with one left vertex for each arrival and one
right vertex for each departure. Join arrival `e` to departure `x`
exactly when `x>e` and either `x−e≤b` or `x−e≥a`. Equality at either
threshold is allowed. Each edge describes one possible visit.

A valid explanation is exactly a perfect matching. An explanation uses
each arrival and departure once, hence supplies such a matching.
Conversely, the edges of a perfect matching give positive-duration
visits using all events once, with every duration allowed. Thus finding
a perfect matching solves both the decision and construction tasks.
Unequal arrival and departure counts immediately fail.

### Layered augmenting paths

Use Hopcroft–Karp. Store the partner of every vertex, initially
unmatched. A breadth-first search starts at all unmatched left vertices,
traverses possible unmatched edges to right vertices and then the
current matching back to left vertices. Record left-vertex distances and
the shortest distance to a free right endpoint.

Depth-first searches follow only consecutive BFS layers and finish only
at free right vertices at that shortest distance. On a successful
return, replace partners along the alternating path; one previously
unmatched arrival becomes matched. An edge cursor per left vertex
prevents rescanning failed choices within a phase. A failed vertex is
removed from the current layers. Repeat BFS phases until no augmenting
path exists.

Augmenting preserves the matching property and increases cardinality by
one. If a larger matching existed after termination, the symmetric
difference with the current matching would contain an alternating path
with free endpoints, contradicting the failed BFS. Therefore the result
is maximum. It gives an explanation exactly when its size equals the
number of arrivals. Output the matched event times; no special order is
needed.

Each phase costs `O(E+V)`: BFS scans the graph and DFS cursors scan each
edge at most once. A phase exhausts shortest augmenting paths, so their
length increases. After `O(sqrt V)` phases the remaining paths are long;
their vertex-disjointness bounds the remaining possible increases by
`O(sqrt V)`. This yields the standard `O(E sqrt V)` matching bound, in
addition to building the graph.

### Why a local pairing rule is insufficient

For `a=10,b=2`, arrivals at 1 and 10 and departures at 11 and 14 have
the explanation `(10,11),(1,14)`. Pairing the earliest departure with
the oldest eligible arrival instead leaves duration 4 for the other
visitor. Matching keeps the ability to revise earlier choices.

### Complexity

There are at most 500 vertices per side and 250000 edges. Building all
edges takes `O(n²)` time. Matching takes `O(E sqrt V)`, hence total
worst-case time `O(n² sqrt n)` and memory `O(n²)` on every language. A
recursive search advances one left layer per call, so depth is at most
500. All differences fit signed 32 bits; Rust uses 64-bit times as well.

The input gives `a` before `b`. Direction 0 is arrival. Accept duration
exactly `b` or exactly `a`; reject the entire open gap and departures
before arrivals. Finding an edge for every vertex is insufficient:
several arrivals may need the same departure. Reset DFS cursors every
BFS phase and update both sides when augmenting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1997_matching.cpp](1997_matching.cpp) | G++ 13.2 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 772 KB |
| [1997_matching.go](1997_matching.go) | Go 1.14 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 4116 KB |
| [1997_matching.java](1997_matching.java) | Java 1.8 | matching | O(n^2 sqrt n) | AC | 0.093 s | 1168 KB |
| [1997_matching.py](1997_matching.py) | Python 3.12 x64 | matching | O(n^2 sqrt n) | AC | 0.109 s | 4532 KB |
| [1997_matching.rs](1997_matching.rs) | Rust 1.75 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 1656 KB |
