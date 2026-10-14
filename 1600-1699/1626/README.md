# 1626. Interfering Segment

[Timus 1626](https://acm.timus.ru/problem.aspx?space=1&num=1626) · difficulty 6623 · geometry

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple polygon has N vertices (3 ≤ N ≤ 800, integer coordinates of
absolute value at most 10⁴, no three consecutive vertices on a line),
and a segment S lies strictly inside it. Triangulations here use only
polygon vertices, and no vertex may lie on a side of a triangle except
its own corners. Find a triangle of some triangulation that contains S
strictly inside, printing its three vertex numbers, or print
`Impossible`. Any such triangle is accepted.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

N, the vertices in order, then the ends of S.

## Output

Three vertex numbers, or `Impossible`.

## Examples

### Example 1

Input:

```
3
0 0
0 3
4 3
1 2 2 2
```

Output:

```
1 2 3
```

### Example 2

Input:

```
4
0 0
2 0
2 3
0 3
1 1 1 2
```

Output:

```
Impossible
```

## Solution

A triangle belongs to some triangulation exactly when its sides are
polygon edges or diagonals (inside the polygon, touching no other vertex)
and no vertex lies inside it: the rest of the polygon then splits into
smaller polygons that can be triangulated. So the task is to find such
a triangle around S.

Everything is done with bitsets of the N vertices. After orienting the
polygon counterclockwise, for every pair a < b the set of vertices
strictly left of the line a → b is stored. A pair i, j is a diagonal if j
lies inside the interior angle at i and i inside the angle at j, if no
edge properly crosses the segment, and if no vertex lies on the open
segment. Candidate crossing edges have different strict-left flags at
their ends for i → j (the left set xor itself circularly shifted by one),
and at i and j for their line; only those candidates are checked exactly.

Then, for every diagonal or edge a → b with both ends of S strictly on
its left, the third corners k are the common neighbours of a and b that
also keep both ends of S inside the triangle, again an and of bitsets.
The triangle a, b, k is empty when the three left sets have no common
vertex besides its corners. The first such triangle is the answer.
`O(N³)` time.

Python builds the left sets differently: around each vertex the others
are sorted by angle, so every left set is a circular range of that order
and comes from prefix bitsets in `O(1)` big-number operations, with the
nearest vertex in each direction marking which segments are free of
other vertices. It keeps only the current vertex's sets, so the empty
triangle test looks at the corners instead: no polygon edge at a corner
may point into the triangle. The boundary cannot cross the sides, so it
then stays outside, and so do all vertices. In the table, w is the number
of bits per big-number limb.

Pitfalls:

- a vertex can lie exactly on a would-be diagonal (tests 03, 04);
- in a rectangle both diagonals may cross S (the second example);
- the example's triangle may be printed in any order of its corners, so
  a checker replays every condition.

The answers pass the checker on all tests, where an independent accepted
implementation gives the same verdict on every generated polygon.

## Language notes

- Python runs under PyPy: CPython takes about 2.4 s on the largest tests
  here against a limit of 5 s, too close for the judge, and PyPy about
  0.9 s. PyPy frees the short-lived bit masks only when it collects, so
  the solution calls the collector every 64 rows; without that the
  garbage alone broke the 64 MB limit.
- Java builds the left sets in int arithmetic, which coordinates up to
  10⁴ allow; that halves its time.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1626_geometry.cpp](1626_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 1.468 s | 35068 KB |
| [1626_geometry.go](1626_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 2.343 s | 40844 KB |
| [1626_geometry.java](1626_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 4.531 s | 41600 KB |
| [1626_geometry.py](1626_geometry.py) | PyPy 3.10 x64 | geometry | O(N² log N + N²⌈N/w⌉) | AC | 3.281 s | 17224 KB |
| [1626_geometry.rs](1626_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 2.500 s | 37932 KB |
