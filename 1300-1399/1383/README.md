# 1383. Flower-garden Designs

[Timus 1383](https://acm.timus.ru/problem.aspx?space=1&num=1383) · difficulty 8198 · geometry

Original problem by Andrew Rumyantsev, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 10 000 projects each give a list of points with integer coordinates
of absolute value at most 1000, at most 200 000 points in all. Two
projects are the same if one becomes the other after reordering its points and
applying an affine map that keeps orientation: a matrix of positive
determinant and a shift. Print the classes of equal projects.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then each project: its length M and M lines of coordinates.

## Output

The number of classes, then each class as a list of project numbers
ending with 0.

## Examples

### Example 1

Input:

```
7
5
1 2
0 0
6 0
0 4
2 7
5
1 2
3 9
0 1
2 3
9 2
5
-43 -37
-73 -47
-3 3
-23 -7
-3 63
3
0 0
1 0
0 1
3
0 0
1 0
3 0
3
10 3
3 7
5 2
3
6 1
6 5
6 7
```

Output:

```
4
4 6 0
5 7 0
1 3 0
2 0
```

## Solution

Give every project a canonical key, equal for two projects exactly
when they are the same, and group the projects by key. Repeated points
count, so the key describes the list with its repeats. For C++, Go,
Java and Rust:

- All points equal: the key is just their number.
- All points on one line: an affine map can stretch the line and turn
  it around, so place the end points at 0 and 1 and list the positions
  of all points, sorted. Read it from the other end too and keep the
  smaller list.
- Otherwise use the strict convex hull, counterclockwise; an affine
  map of positive determinant takes it to the hull of the image in the
  same order. Each hull vertex, with the next and the previous vertex,
  defines a frame: the map that sends it to (0, 0), the next one to
  (1, 0) and the previous one to (0, 1) has positive determinant. In
  that frame all coordinates are fractions over the same denominator,
  the cross product of the two edges. Divided by their common gcd they
  become unique, so equal point sets get equal integer lists. First
  compare only the hull in each frame. Then, for the frames where the
  hull looks smallest, list all points, sorted, and keep the smallest
  list. This handles hulls with symmetries.

The classes are printed by the size of their projects, then by their
first project, which matches the example. `O(S log S + Σ h²)` for S
points and hulls of h vertices.

Pitfalls:

- mirror equivalence requires an orientation-reversing affine symmetry
  (tests 04 and 13);
- a line can be read in either direction (test 03);
- repeated points matter (tests 02, 03 and 06);
- a square hull gives four equally small hull frames; interior points
  and repeat counts still matter (test 05 and generated test 2).

The classes were compared on 350 random batches of small projects and
their images under random integer maps of either sign with a direct
search that tries to map one triangle of a project onto every triangle
of another. The tests are judged by a checker that accepts the classes
in any order.

## Language notes

- Java keeps points, frame pairs and keys in arrays of plain numbers, a
  pair packed into one long so that sorting needs no comparator: with an
  object per point and boxed keys it exceeded the time limit on the
  judge's test 8, and now takes 1.67 s of the 2 s.
- Python finds the frames without trying them all. It writes the hull as
  the cyclic sequence of what an affine map keeps of every three
  consecutive edges, their three cross products divided by their gcd,
  and takes the least rotation of that sequence in linear time. When
  every point is a hull vertex, this sequence with the repeat counts is
  already the key; otherwise only the frames at the least rotations are
  used, those of a symmetric hull narrowed down further by the centroid,
  and the points are listed in them. It runs on CPython; the earlier
  version that tried every frame exceeded the time limit on the judge's
  test 8 even under PyPy. `O((r + 1) S log S)` for at most r remaining
  frames per project.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1383_geometry.cpp](1383_geometry.cpp) | G++ 13.2 x64 | geometry | O(S log S + Σh²) | AC | 1.109 s | 5216 KB |
| [1383_geometry.go](1383_geometry.go) | Go 1.14 x64 | geometry | O(S log S + Σh²) | AC | 1.640 s | 7884 KB |
| [1383_geometry.java](1383_geometry.java) | Java 1.8 | geometry | O(S log S + Σh²) | AC | 1.671 s | 7768 KB |
| [1383_geometry.py](1383_geometry.py) | Python 3.12 x64 | geometry | O((r + 1) S log S) | AC | 1.125 s | 38932 KB |
| [1383_geometry.rs](1383_geometry.rs) | Rust 1.75 x64 | geometry | O(S log S + Σh²) | AC | 0.703 s | 5672 KB |
