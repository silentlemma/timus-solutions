# 1314. Chase in Subway

[Timus 1314](https://acm.timus.ru/problem.aspx?space=1&num=1314) · difficulty 561 · bfs

Original problem: idea by Leonid Volkov, prepared by Alexander Somov, Leonid Volkov and Igor Goldberg, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A metro has up to 50 lines of 2 to 50 stations each; a station is a
number up to 32 767, and a station that appears on several lines (or
several times on one line) is a single place where they meet. A
fugitive enters at the first of M stations recorded by a beacon and
travels to a chosen target along a shortest route, counting only the
stops travelled. The beacon records every station on the way, in order.
Print, in increasing order, every station that can be the target.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N; N lines, each K and then K stations; then M and the M stations
recorded.

## Output

The possible targets, one per line.

## Examples

### Example 1

Input:

```
3
2 61 62
5 75 20 85 50 61
3 10 20 30
3 30 20 85
```

Output:

```
50
61
62
85
```

## Solution

Join neighbouring stations of every line by an edge. Let s be the first
recorded station and e the last one, and let d be the distance in
stops. The fugitive follows a shortest route from s to the target t,
and the record is its beginning, so:

- the record must be a walk along edges and itself a shortest route,
  d(s, e) = M − 1;
- t can be the target exactly when a shortest route from s to t passes
  through e, which is d(s, t) = d(s, e) + d(e, t).

Two breadth-first searches, from s and from e, give all the distances.
`O(V + E)` for the stations and the edges, at most 2500 of each;
Python takes `O(V log V + E)` because it sorts the targets.

The statement promises a consistent record. If it is not one (an
unknown station, two stations that are not neighbours, or a detour),
no target fits and nothing is printed.

Pitfalls:

- e itself is a target, since the trip may end right there (test 01);
- with a single recorded station every station reachable from it fits
  (tests 02 and 07);
- a record of two stations that are not neighbours fits nothing
  (test 04);
- a station further along the line does not fit when a shortcut reaches
  it sooner (test 05).

The answers were compared with listing every shortest route from s
on 400 small random networks.

## Optimized solutions

Compress station numbers in sorted order and store the neighbor lists in one flat array. A
single BFS from the first recorded station gives the distance layers. Once the recorded
prefix is verified, mark the last station and propagate the marks along edges to the next
layer in BFS order. Exactly those marked stations admit a shortest continuation. Compression
takes O((V + E) log(V + E)) time and all arrays use O(V + E) space. Submission 11316949 took 0.015 s and used 224 KB. The simple version took 0.015 s and used 1256 KB.

Go assigns compact station indices with a bitset and stores the adjacency array and BFS queue in fixed arrays. A high bit in each distance marks stations that can continue the recorded shortest path. Go 1.14 x64, submission 11322926. Time 0.015 → 0.015 s, memory 1844 → 376 KB.

Rust maps station IDs to compact indices and stores adjacent stations in one contiguous array. Submission 11317248 took 0.062 s and used 320 KB, versus 0.046 s and 1532 KB for the base.

Java stores compact station indices and adjacency links in short arrays. Submission 11317252 took 0.109 s and used 636 KB, versus 0.093 s and 2864 KB for the base.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1314_bfs_implementation_optimized.rs`. Represent adjacency with linked arrays, 16-bit vertex identifiers and signed next/head indices instead of thousands of separate vectors. The breadth-first distances are unchanged. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328977 (Rust 1.75 x64): **0.015 s / 556 KB**. Archived comparison: `1314_bfs.rs` (Rust 1.75 x64) — 0.046 s / 1532 KB (#11322322).

## Language notes

- The station numbers index arrays directly, since they are below
  32 768; Python keeps a dictionary instead.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322317 · Go 1.14 x64 №11322318 · Python 3.12 x64 №11321737 · Java 1.8 №11322321 · Rust 1.75 x64 №11322322.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1314_bfs.cpp](1314_bfs.cpp) | G++ 13.2 x64 | bfs | O(V + E) | AC | 0.015 s | 1256 KB | 11322317 |
| [1314_bfs.go](1314_bfs.go) | Go 1.14 x64 | bfs | O(V + E) | AC | 0.015 s | 1844 KB | 11322318 |
| [1314_bfs.java](1314_bfs.java) | Java 1.8 | bfs | O(V + E) | AC | 0.093 s | 2864 KB | 11322321 |
| [1314_bfs.py](1314_bfs.py) | Python 3.12 x64 | bfs | O(V log V + E) | AC | 0.078 s | 1884 KB | 11321737 |
| [1314_bfs.rs](1314_bfs.rs) | Rust 1.75 x64 | bfs | O(V + E) | AC | 0.046 s | 1532 KB | 11322322 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1314_bfs_optimized.cpp](1314_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O((V + E) log(V + E)) | AC | 0.015 s | 224 KB | 11316949 |
| [1314_bfs_optimized.go](1314_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(S + V + E) | AC | 0.015 s | 376 KB | 11322926 |
| [1314_bfs_optimized.rs](1314_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(S + V + E) | AC | 0.062 s | 320 KB | 11317248 |
| [1314_bfs_optimized.java](1314_bfs_optimized.java) | Java 1.8 | bfs | O(S + V + E) | AC | 0.109 s | 636 KB | 11317252 |
| [1314_bfs_implementation_optimized.rs](1314_bfs_implementation_optimized.rs) | Rust 1.75 x64 | bfs, implementation | O(V + E) | AC | 0.015 s | 556 KB | 11328977 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
