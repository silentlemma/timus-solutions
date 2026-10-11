# 1215. The smallest shell that still hits the target

[Timus 1215](https://acm.timus.ru/problem.aspx?space=1&num=1215) · difficulty 300 · geometry

Original problem by Anton Botov and Anatoly Uglov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shell lands at a given point and leaves a round crater as wide as the
shell. The target is a convex polygon with 3 to 100 corners listed
counterclockwise, all coordinates integers in `[−2000, 2000]`. Find the
smallest shell diameter whose crater touches the target, to three
decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The point of impact and `N`, then the `N` corners.

## Output

The smallest diameter with three decimals.

## Examples

### Example 1

Input:

```
2 -1 8
0 1
1 0
2 0
3 1
3 2
2 3
1 3
0 2
```

Output:

```
2.000
```

## Solution

The crater touches the target exactly when its radius is at least the
distance from the impact to the polygon, so the answer is twice that
distance. If the point is inside or on the boundary, the distance is 0;
since the corners go counterclockwise, that is the case when the point is
on the left of, or on, every edge, which integer cross products decide
exactly. Otherwise the nearest point of the polygon lies on its boundary,
so the distance is the smallest distance to an edge as a segment: to the
foot of the perpendicular when it falls inside the segment, else to the
nearer end. `O(N)`.

Pitfalls:

- a point on the boundary counts as a hit with diameter `0.000`;
- distances to the whole lines of the edges are too small when the
  nearest point is a corner;
- the answer is a diameter, twice the distance.

The answers were compared with a separately written solution on 300
random targets with shots outside, inside and at the corners.

## Language notes

- All languages test the inside case with exact integer cross products
  and print with three decimals; Java formats with `Locale.US`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1215_geometry.cpp](1215_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 220 KB |
| [1215_geometry.go](1215_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1084 KB |
| [1215_geometry.java](1215_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 2004 KB |
| [1215_geometry.py](1215_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 568 KB |
| [1215_geometry.rs](1215_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 268 KB |
