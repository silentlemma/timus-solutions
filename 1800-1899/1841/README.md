# 1841. Cableways

[Timus 1841](https://acm.timus.ru/problem.aspx?space=1&num=1841) · difficulty 2141 · segment_tree

Original problem by Denis Dublennykh, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A path climbs a mountain as a polyline of n segments whose vertices go
strictly up the slope; the y axis points up the slope. Walking along
segment i costs vᵢ per unit of change in x. Some points of the path are
the lower ends of cableways: a cableway goes straight up the slope from
its start and ends at the next point where it meets the path, and riding
it takes a given time. Nobody walks down. Find the least time from the
foot to the top.

## Input

n (1 ≤ n ≤ 10⁵), then the n + 1 x coordinates of the vertices from the
foot to the top; neighbouring ones differ. Then n lines: vᵢ, the number
mᵢ of cableways starting on segment i, and mᵢ pairs (x of the start,
riding time), in order up the slope. No two cableways start at one
point, a cableway starting at a shared vertex is listed once, and every
cableway ends on the path. Coordinates are at most 10⁶ in absolute
value, times are positive and at most 10⁶, and there are at most 10⁵
cableways.

## Output

The least time to reach the top.

## Examples

### Example 1

Input:

```
4
0 5 15 10 0
1 1 1 100
1 1 7 1
1 0
1 0
```

Output:

```
15
```

### Example 2

Input:

```
3
0 10 0 10
10 0
10 1 10 1
10 0
```

Output:

```
101
```

## Solution

Only the order of points along the path matters, and walking up the
path to a point costs a known amount: the walk to its segment's first
vertex plus vᵢ times the distance in x. Call that the walking cost of
the point; it grows strictly along the path.

Where a cableway lands. A point of the path other than the foot belongs
to exactly one segment if each segment owns its x range without its
first vertex (a start at a shared vertex therefore belongs to the lower
segment). A cableway starting at x on segment s lands on the first
segment after s whose range contains x. Process the segments from the
top down over the start coordinates (compressed except in Python): before
painting segment s over its x range in a segment tree, look up every
cableway owned by s.
A tree node keeps only the last paint laid over it, and paints only go
down the path, so the smallest segment number on the way from a leaf to
the root is the landing segment.

The best times. Let best(p) be the least time to reach point p, and
gain = min(best(p) − walking cost(p)) over the points reached so far; at
the foot gain is 0, and walking preserves that difference, so
best(p) = walking cost(p) + gain at the current point. Process the
starts and the landings by walking cost, landings first at equal cost.
A start records best = cost + gain; a landing sets gain to
min(gain, best(start) + time − cost(landing)). The answer is the walking
cost of the top plus gain. `O((n + m) log(n + m))`; Python: `O(U + (n + m) log U + m log(m + 1))`,
where U = max(x) − min(x) + 1.

In the first example the cableway at x = 1 rises from the first segment
to the last one at walking cost 29 and takes 100, worse than walking.
The one at x = 7 starts at walking cost 7 and also lands on the last
segment, at walking cost 23, after 1 unit of time, so gain becomes
7 + 1 − 23 = −15, and the answer is 30 − 15 = 15.

Pitfalls:

- a cableway starting at a shared vertex belongs to the segment below
  it, whichever segment's line lists it;
- a cableway may land many segments later, or exactly on the start of
  another cableway, which the landing-first order handles;
- times reach about 2·10¹⁷, past 32-bit integers but within 64-bit ones;
- the Python solution runs on PyPy and keeps its data in flat arrays of
  machine integers, about 20 MB; an earlier version with lists of
  Python integers took 69 MB on the judge's test 17.

The answers agree with an independent accepted implementation and with
a shortest-path search on four hundred random mountains, and on the
large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1841_segment_tree.cpp](1841_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.453 s | 22568 KB |
| [1841_segment_tree.go](1841_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.250 s | 27812 KB |
| [1841_segment_tree.java](1841_segment_tree.java) | Java 1.8 | segment_tree | O((n + m) log(n + m)) | AC | 0.421 s | 40208 KB |
| [1841_segment_tree.py](1841_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(U + (n + m) log U + m log(m + 1)) | AC | 0.468 s | 32236 KB |
| [1841_segment_tree.rs](1841_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.125 s | 25724 KB |
