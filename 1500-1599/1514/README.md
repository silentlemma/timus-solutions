# 1514. National Park

[Timus 1514](https://acm.timus.ru/problem.aspx?space=1&num=1514) · difficulty 1748 · geometry

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N trees (3 ≤ N ≤ 50000) stand at integer points with coordinates up to
10⁶ in absolute value; several trees may share a point. Choose three
different trees whose triangle has the smallest perimeter; a triangle
of zero area counts too. Print the perimeter with at least four digits
after the point and the numbers of the three trees.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the coordinates of the N trees.

## Output

The smallest perimeter, then the numbers of the three trees in any
order. Any optimal triple is accepted.

## Examples

### Example 1

Input:

```
5
0 0
1 1
3 0
0 3
3 3
```

Output:

```
6.6503
1 2 3
```

## Solution

Divide and conquer, as for the closest pair of points. Sort the trees by
x, solve the left and the right half, and let d be the best perimeter so
far. Each side of a triangle is at most half its perimeter, so a better
triangle has all three trees closer than d/2 to each other. A better
triangle with trees on both sides of the dividing line therefore lies
in the strip of width d/2 on each side of it: sort the strip by y and,
for each tree, try pairs of later trees less than the initial d/2
higher (including equal y), tightening that tree's bound when d improves.
For d > 0, sufficiently small squares in either half hold at most two
trees (otherwise they beat d), bounding the candidate count; for d = 0
the strip is empty. The total is `O(N log² N)`. Pieces of up to 8 trees
are checked triple by triple.

Pitfalls:

- three trees in one place give the perimeter 0 (test 03, gen7);
- flat triangles count, so three trees on one line give twice the distance
  between the outer two (tests 02, 06, gen2, gen3);
- when all trees share one x and d > 0, every tree in a subproblem
  falls into its strip, and only the bound on y keeps the work small (gen2);
- 50000 trees make about 2·10¹³ triples, far too many to try all (gen1);
- many triples can tie, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1514_geometry.cpp](1514_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log^2 N) | AC | 0.109 s | 1024 KB |
| [1514_geometry.go](1514_geometry.go) | Go 1.14 x64 | geometry | O(N log^2 N) | AC | 0.078 s | 6540 KB |
| [1514_geometry.java](1514_geometry.java) | Java 1.8 | geometry | O(N log^2 N) | AC | 0.515 s | 8444 KB |
| [1514_geometry.py](1514_geometry.py) | Python 3.12 x64 | geometry | O(N log^2 N) | AC | 0.890 s | 16368 KB |
| [1514_geometry.rs](1514_geometry.rs) | Rust 1.75 x64 | geometry | O(N log^2 N) | AC | 0.062 s | 3348 KB |
