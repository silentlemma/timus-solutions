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

## Language notes

- The station numbers index arrays directly, since they are below
  32 768; Python keeps a dictionary instead.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1314_bfs.cpp](1314_bfs.cpp) | G++ 13.2 x64 | bfs | O(V + E) | AC | 0.015 s | 1272 KB |
| [1314_bfs.go](1314_bfs.go) | Go 1.14 x64 | bfs | O(V + E) | AC | 0.015 s | 1920 KB |
| [1314_bfs.java](1314_bfs.java) | Java 1.8 | bfs | O(V + E) | AC | 0.093 s | 2884 KB |
| [1314_bfs.py](1314_bfs.py) | Python 3.12 x64 | bfs | O(V log V + E) | AC | 0.062 s | 1980 KB |
| [1314_bfs.rs](1314_bfs.rs) | Rust 1.75 x64 | bfs | O(V + E) | AC | 0.031 s | 1532 KB |
