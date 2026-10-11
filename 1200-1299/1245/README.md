# 1245. Covering round stains with at most two pictures

[Timus 1245](https://acm.timus.ru/problem.aspx?space=1&num=1245) · difficulty 940 · geometry

Original problem by Alexander Petrov (statement by Leonid Volkov), from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N round stains (0 < N ≤ 1000) with integer radius and centre, all at most
10 000, must be covered by one or two rectangular pictures with sides
parallel to the axes. Each side of a picture is at least 100, two pictures
must not overlap, and every stain must lie wholly under one picture. Find
the least total area.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then each stain as `R X Y`.

## Output

The least total area.

## Examples

### Example 1

Input:

```
3
50 50 50
50 250 50
10 150 250
```

Output:

```
40000
```

## Solution

A picture is an axis-parallel rectangle, so it holds a stain exactly when
it holds the stain's bounding square `[X − R, X + R] × [Y − R, Y + R]`. A
picture for a group of stains is then the bounding box of their squares,
widened to 100 where it is narrower: `max(w, 100) · max(h, 100)`.

Two rectangles that do not overlap are split by a vertical or a
horizontal line, and each can be widened to 100 on its own side of that
line without overlapping the other. So try one picture, and then every way
to split the stains by a vertical line and by a horizontal one.

For a vertical line, sort the squares by their left edge. Any valid split
is a prefix of this order: everything on the left ends no later than
everything on the right begins, and a square starts before it ends. A
prefix of k squares can hang apart from the rest exactly when its
rightmost edge is at most the left edge of the first remaining square.
With bounding boxes of every prefix and suffix, each split costs O(1).
`O(N log N)`.

Pitfalls:

- the two pictures may touch along an edge: test 04 needs that;
- the 100-millimetre minimum applies to each picture: a single tiny
  stain still needs a 100 × 100 picture (test 02);
- an edge of a square can be negative when R > X; only differences
  matter.

The answers were compared with trying every partition of the stains into
two groups on 800 random small cases.

## Language notes

- Python and Java keep a box as a 4-tuple or array; C++, Go and Rust use
  a small struct.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1245_geometry.cpp](1245_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 264 KB |
| [1245_geometry.go](1245_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1284 KB |
| [1245_geometry.java](1245_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.125 s | 2944 KB |
| [1245_geometry.py](1245_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1260 KB |
| [1245_geometry.rs](1245_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 228 KB |
