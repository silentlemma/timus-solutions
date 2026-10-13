# 1412. Autumn Tide

[Timus 1412](https://acm.timus.ru/problem.aspx?space=1&num=1412) · difficulty 1530 · geometry

Original problem by Pavel Egorov, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Rain falls straight down at 1 mm per minute on a rectangular field with
corners (0, 0), (0, W), (L, 0) and (L, W) (1 ≤ W, L ≤ 10 000). N people
(N ≤ 1000) stand at given points (|X|, |Y| ≤ 10 000), each under an
umbrella shaped as an upper hemisphere of radius 1 m. Water on an
umbrella runs down the shortest way on the hemisphere and drops from
the rim. Umbrellas do not overlap, and tall posts at the field's corners
keep any umbrella from covering a corner. Print the amount of rain that
reaches the field per minute, with 3 digits after the point.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

W and L, then N, then N lines with X and Y.

## Output

The amount of rain on the field.

## Examples

### Example 1

Input:

```
10 10
2
0.5 2
2 10.1
```

Output:

```
99.666
```

## Solution

The shortest way from a point of the hemisphere to its rim runs along
the meridian, so rain falling on the umbrella's disk at angle θ leaves
the rim at the same angle θ: the π units caught by an umbrella are
spread evenly along its rim. Without umbrellas the field gets W·L, and
each umbrella changes that by π times the share of its rim over the
field minus the area of its disk over the field.

The area of the unit disk inside the rectangle is the sum over the four
edges of the signed area of the disk inside the triangle from the
centre to the edge: the edge is cut where it meets the circle, a piece
inside the circle adds its triangle and a piece outside adds its
sector. The share of the rim comes from cutting the circle at the
angles where it meets the four border lines and checking the middle of
every arc. `O(N)`.

Pitfalls:

- despite the word "average" in the statement, the expected number is
  the total over the field, W·L when nothing interferes (tests 01, 05);
- X runs along L, the second number, and Y along W; a forum case only
  agrees with this reading (tests 02, 10);
- a rim or an edge that only touches the circle must not count a whole
  arc or chord as inside, so tangent points split the arcs and the
  disk test is strict (tests 11, 12);
- an umbrella outside the field can still drop water onto it (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1412_geometry.cpp](1412_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 236 KB |
| [1412_geometry.go](1412_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1404 KB |
| [1412_geometry.java](1412_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2164 KB |
| [1412_geometry.py](1412_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 796 KB |
| [1412_geometry.rs](1412_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 280 KB |
