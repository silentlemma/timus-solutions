# 1905. Routes Through Space-Time Events

[Timus 1905](https://acm.timus.ru/problem.aspx?space=1&num=1905) · difficulty 1131 · bfs

Original problem by Dmitry Ivankov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Flights connect locations at specified departure and arrival times;
arrival may precede departure. Start at a given location and time and
reach a target location at its specified time, waiting forward when
needed. Before completion, two separate visits to the same location
must never occupy the same instant, including during waiting.
Print any valid flight sequence. Limits: 3 seconds and 64 MB.

## Input

First n and m, with 1 ≤ n ≤ 100 000 and 0 ≤ m ≤ 100 000. Each of the
next m lines gives departure location, arrival location, departure time
and arrival time. Locations are numbered 1,…,n; every time is an integer
from 0 to 10⁶. The last line gives start location, target location,
current time and target time. Flight identities are their 1-based input indices.

## Output

Print `Impossible` if no route exists. Otherwise print k and the k flight
identities in travel order. A route can have zero flights; print 0 and
an empty second line. Any feasible sequence is accepted.

## Checking

The constructive checker validates indices, departure locations, boarding
times and final arrival before or at the target time. Waiting completes
the target event exactly. It collects all closed visit intervals,
sorts them by location and time, and rejects overlaps, including shared
endpoints. Any valid route is accepted.

## Examples

```
4 3
1 2 10 20
2 4 50 20
4 3 20 30
1 3 10 30
```

```
3
1 2 3
```

## Solution

Create one vertex for each distinct (location,time) occurring as a flight
endpoint, the start event or the target event. Equal events must share
one vertex. Within each location, sort events by time and add a directed
waiting edge to the next event. Add each directed flight edge from its
departure event to its arrival event, even for backward time travel.

Run BFS from the start event. Each newly visited vertex stores its parent
and the flight identity used to reach it, or zero for a waiting edge.
If the target is not reached, output `Impossible`. Otherwise follow
parents backward, retain only positive flight identities and reverse them.

Why is ordinary reachability sufficient despite the collision condition?
Every physical route induces a graph walk: waiting passes through all
intermediate event times. Thus no graph path means no physical route.
Conversely, a reachable target has a simple vertex path, as provided by
the BFS parent tree. Suppose two separate visits to one location overlapped
in real time. Their closed intervals have an overlapping endpoint of one
visit. This endpoint is a flight, start or target event; the other visit's
waiting chain also passes through its vertex. The path would repeat that
vertex, contradicting simplicity. Therefore the reconstructed path has no
self-collision. Consecutive waiting edges describe one continuous visit,
and equal-time transfers use a shared event once.

Encode an event by `location·B+time`, with B=1 000 001. Sort all endpoint
keys, deduplicate them and find flight endpoint indices by binary search.
The sorted order groups locations, so waiting edges are implicit: index
i can go to i+1 exactly when their location quotients by B agree.
Store only flight edges in adjacency lists represented by head/next arrays.

There are at most 2m+2 vertices and 3m+1 edges. Sorting and binary searches
take `O((m+1) log(m+2))` time; BFS and reconstruction are linear. Storage
is `O(m+1)`, independent of locations without any event.

The sample waits at location 2 until time 50, takes a backward-time flight
to location 4 at time 20, then immediately transfers to the last flight.

## Language notes

Keys need 64-bit integers: the largest can exceed 10¹¹. Vertex indices
fit in 32 bits. C++, Go, Java and Rust use primitive arrays/vectors;
Python uses packed `array` storage for graph indices and queue, plus one
sorted integer-key list. It deduplicates in place and releases the input
token generator before BFS to keep peak memory low. Python targets CPython 3.12.

Do not require arrival ≥ departure. Include start and target events even
when no flight uses them. Waiting never moves backward, duplicate events
must be unified, and collisions during waiting count as well as endpoint repeats.

The answers agree with a search over flight sequences that checks
collisions directly on 3048 small cases; the checker accepts five valid
routes and rejects 16 broken ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1905_bfs.cpp](1905_bfs.cpp) | G++ 13.2 x64 | bfs | O((m+1) log(m+2)) | AC | 0.125 s | 6596 KB |
| [1905_bfs.go](1905_bfs.go) | Go 1.14 x64 | bfs | O((m+1) log(m+2)) | AC | 0.156 s | 16544 KB |
| [1905_bfs.java](1905_bfs.java) | Java 1.8 | bfs | O((m+1) log(m+2)) | AC | 0.234 s | 9452 KB |
| [1905_bfs.py](1905_bfs.py) | Python 3.12 x64 | bfs | O((m+1) log(m+2)) | AC | 0.609 s | 15064 KB |
| [1905_bfs.rs](1905_bfs.rs) | Rust 1.75 x64 | bfs | O((m+1) log(m+2)) | AC | 0.078 s | 15332 KB |
