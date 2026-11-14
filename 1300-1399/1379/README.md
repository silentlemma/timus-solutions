# 1379. Cups Transportation

[Timus 1379](https://acm.timus.ru/problem.aspx?space=1&num=1379) · difficulty 581 · graphs

Original problem by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A truck weighing 3000 kg must bring as many cups as it can, 100 g each
and no more than the 10 000 000 ordered, from junction 1 to junction N,
N ≤ 500, within 24 hours. Every two-way road has a travel time in
minutes and a largest allowed weight of the truck in grams. Print the
largest number of cups.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then M lines: the ends of a road, its time and its weight
limit.

## Output

The number of cups.

## Examples

### Example 1

Input:

```
3 3
1 2 10 3000220
2 3 20 3000201
1 3 1 3000099
```

Output:

```
2
```

### Example 2

Input:

```
1 0
```

Output:

```
10000000
```

## Solution

A heavier truck can use fewer roads, so whether it arrives in time only
gets worse as the load grows. A route's weight limit equals that of
some road, so binary search over the road limits of at least
3 000 000 g. For each one, Dijkstra's algorithm uses only the roads
that bear that weight and never keeps a time over 1440 minutes. With
the heaviest weight W that arrives in time, the answer is
min(10 000 000, ⌊(W − 3 000 000) / 100⌋). `O((N + M log M) · log M)`.

Pitfalls:

- with N = 1 the cups are already at the venue: all 10 000 000 of them
  (example 2);
- exactly 24 hours, 1440 minutes, is still in time (test 03);
- the fastest way may bear less than a slower one (test 05);
- a road bearing exactly the empty truck allows no cups at all
  (test 06);
- roads can take no time (test 07).

The answers were compared with trying every simple path on 400 random
graphs of up to 6 junctions.

## Optimized solutions

The optimized C++ version searches distinct loads in whole cups. For each load, Dijkstra
uses a bucket for every minute from 0 to 1440. When a junction gets an earlier arrival time,
move its entry to the earlier bucket. Zero-minute roads can add junctions to the current
bucket, which is processed until empty. Each search takes O(N + M + D) time for D = 1440,
and the edge arrays use O(N + M + D) space. Submission 11316958 took 0.031 s and 3464 KB
versus 0.281 s and 7564 KB for the base.

## Language notes

- Python needs PyPy: a chain of short roads inside a complete graph of
  day-long ones makes searches scan many roads, about 0.5 s with
  CPython and 0.25 s with PyPy.
- Java keeps its heap as an array of plain longs, time and vertex packed
  in one number: a priority queue of small arrays exceeded the time limit
  on the judge's test 46.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322140 · Go 1.14 x64 №11322141 · Java 1.8 №11322142 · Rust 1.75 x64 №11322143 · PyPy 3.10 x64 №11322144.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1379_graphs.cpp](1379_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M log M) · log M) | AC | 0.281 s | 7564 KB | 11322140 |
| [1379_graphs.go](1379_graphs.go) | Go 1.14 x64 | graphs | O((N + M log M) · log M) | AC | 0.562 s | 24828 KB | 11322141 |
| [1379_graphs.java](1379_graphs.java) | Java 1.8 | graphs | O((N + M log M) · log M) | AC | 0.5 s | 11552 KB | 11322142 |
| [1379_graphs.py](1379_graphs.py) | PyPy 3.10 x64 | graphs | O((N + M log M) · log M) | AC | 0.453 s | 58612 KB | 11322144 |
| [1379_graphs.rs](1379_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M log M) · log M) | AC | 0.046 s | 14532 KB | 11322143 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1379_graphs_optimized.cpp](1379_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O((N + M + D) log(M + 1)) | AC | 0.031 s | 3464 KB | 11316958 |
| [1379_graphs_optimized.go](1379_graphs_optimized.go) | Go 1.14 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.093 s | 5748 KB | 11317150 |
| [1379_graphs_optimized.java](1379_graphs_optimized.java) | Java 1.8 | graphs | O((N + M + D) log(M + 2)) | AC | 0.140 s | 6740 KB | 11317007 |
| [1379_graphs_optimized.py](1379_graphs_optimized.py) \* | PyPy 3.10 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.250 s | 16008 KB | 11317003 |
| [1379_graphs_optimized.rs](1379_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O((N + M + D) log(M + 2)) | AC | 0.031 s | 8372 KB | 11317009 |

The PyPy variant packs the destination, travel time and load into each edge. Adjacency lists are ordered by load so a route search can stop scanning when it reaches an edge that cannot carry the truck. The minute buckets ignore entries superseded by a shorter route. The metrics come from submission 11317003.

The Java version also packs each edge into one integer and sorts adjacency lists by load. Its minute buckets move an existing entry when an earlier arrival is found, keeping at most one entry per junction. The metrics come from submission 11317007.

The Rust version sorts packed edges by load and stops scanning a list at the first edge below the required load. Moving entries between minute buckets keeps one per junction. The metrics come from submission 11317009.

The Go version packs each edge into an integer and sorts adjacency lists by load. Each route search stops scanning a list once the load is too low. Submission 11317150 took 0.093 s and used 5748 KB, versus 0.562 s and 24828 KB for the base.

\* Accepted. The Python rating target is still open.

\* Accepted. The saved rating has no comparable Rust submissions from other authors.
