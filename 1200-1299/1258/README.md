# 1258. Billiards in an office

[Timus 1258](https://acm.timus.ru/problem.aspx?space=1&num=1258) · difficulty 418 · geometry

Original problem by Pavel Egorov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A programmer walks in straight lines through a W × D room
(2 ≤ W, D ≤ 1000), bouncing off the walls like a billiard ball. The
start and the end are integer points strictly inside the room, and the
walls hit are listed in order: L, R, F, B for the left (x = 0), right
(x = W), front (y = 0) and back (y = D) walls, at most 1000 hits, never
in a corner. Find the length of the walk, rounded to four digits after
the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W and D, then x0 y0, then x1 y1, then the string of hits (possibly
empty).

## Output

The length of the walk.

## Examples

### Example 1

Input:

```
10 20
9 1
1 19
FLRLRB
```

Output:

```
52.8015
```

## Solution

Mirror the room at every hit instead of turning the walker: the walk
becomes one straight segment, whose horizontal and vertical extents add
up separately.

Along x, only the L and R hits matter, and they must alternate. With
none, the extent is |x1 − x0|. Otherwise the walker first goes to the
first side wall (x0 for L, W − x0 for R), crosses the room W wide
between each two consecutive side hits, and goes from the last side wall
to the end (x1 for L, W − x1 for R):

```text
dx = first + (k − 1) · W + last
```

The same with F, B and D gives dy, and the answer is √(dx² + dy²).
The order in which side and front/back hits interleave does not change
the length. `O(K)` for K hits.

Pitfalls:

- the line of hits may be empty or missing altogether (test 02);
- the first hit on an axis may be either wall (tests 03, 06);
- dx and dy reach about 10⁶, so dx² + dy² needs 64 bits (test 08).

The answers were compared with the length of the straight segment from
which each random test was built (its crossings of the mirrored grid
give the hits) on 200 cases.

## Language notes

- All languages count the hits per axis and use the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1258_geometry.cpp](1258_geometry.cpp) | G++ 13.2 x64 | geometry | O(K) | AC | 0.001 s | 220 KB |
| [1258_geometry.go](1258_geometry.go) | Go 1.14 x64 | geometry | O(K) | AC | 0.031 s | 1120 KB |
| [1258_geometry.java](1258_geometry.java) | Java 1.8 | geometry | O(K) | AC | 0.109 s | 1532 KB |
| [1258_geometry.py](1258_geometry.py) | Python 3.12 x64 | geometry | O(K) | AC | 0.125 s | 504 KB |
| [1258_geometry.rs](1258_geometry.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.046 s | 264 KB |
