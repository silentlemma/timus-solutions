# 1332. Genie Bomber

[Timus 1332](https://acm.timus.ru/problem.aspx?space=1&num=1332) · difficulty 615 · geometry

Original problem by Alexander Bikbaev, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100 cities are discs of the same radius r with different integer
centers, |x|, |y| ≤ 10 000. One bomb destroys everything within distance
R of where it falls, and a city is destroyed only if it lies wholly in
that disc. Find the most cities one bomb can destroy; 1 ≤ R, r ≤ 10 000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines with the centers, then R and r.

## Output

The largest number of destroyed cities.

## Examples

### Example 1

Input:

```
3
0 0
0 4
4 0
3 1
```

Output:

```
2
```

### Example 2

Input:

```
5
0 0
0 1
0 2
0 3
0 4
1 1
```

Output:

```
1
```

## Solution

A city lies wholly in the blast exactly when its center is within
D = R − r of the bomb. If D < 0 no city can be destroyed, and the task
is to cover as many centers as possible with a disc of radius D.

Take a best disc and push it while it keeps all its centers. It can be
moved until a center sits on its edge, and then turned around that
center until a second one reaches the edge too, unless it holds a
single center. So it is enough to try the discs whose center is a
city's center, and the discs of radius D through two centers at most 2D
apart. There are two such discs for each pair, with their centers at
distance √(D² − (d/2)²) on either side of the middle of the pair. Each
of the N + N(N − 1) places is checked against all centers, with a small
tolerance for centers exactly on the edge. `O(N³)`.

Pitfalls:

- the city has to fit wholly, so the reach is R − r, and with R < r
  the answer is 0 (test 03);
- with R = r the reach is 0 and one city is destroyed at a time
  (tests 02 and 04);
- centers exactly on the edge count; with integer points such as (3, 4)
  on a circle of radius 5 this needs the tolerance (tests 06 and
  gen3).

The answers were compared with an angular sweep around each center on
400 random small cases.

## Language notes

- All five solutions try the same places and compare squared
  distances.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1332_geometry.cpp](1332_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.015 s | 348 KB |
| [1332_geometry.go](1332_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 1348 KB |
| [1332_geometry.java](1332_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.125 s | 1956 KB |
| [1332_geometry.py](1332_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.203 s | 1016 KB |
| [1332_geometry.rs](1332_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.046 s | 400 KB |
