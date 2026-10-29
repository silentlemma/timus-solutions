# 1020. The length of a thread around round nails

[Timus 1020](https://acm.timus.ru/problem.aspx?space=1&num=1020) · difficulty 100 · geometry

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` round nail heads (`1 ≤ N ≤ 16`) of the same radius `R` stand at the
vertices of a convex polygon, given in order around it (clockwise or
counter-clockwise); the heads do not overlap and the coordinates are at most
100 in absolute value. A thread is pulled tight around all the heads. Find
its length, rounded to two digits after the decimal point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and the real number `R`, then `N` lines with the real coordinates of the
centres, in order around the polygon.

## Output

The length of the thread with two digits after the decimal point.

## Checking

The output is compared token by token; numbers may differ by at most 0.01.

## Examples

### Example 1

Input:

```
3 1
0 0
3 0
0 4
```

Output:

```
18.28
```

### Example 2

Input:

```
1 2.5
1.5 -2.0
```

Output:

```
15.71
```

## Solution

The thread consists of straight segments and arcs. Each straight segment is
tangent to two neighbouring heads on the outer side, so it is the side
between their centres shifted outwards by `R`: its length equals the side of
the polygon. At a nail the thread turns from one side's direction to the
next one's along an arc of radius `R`, by the exterior angle of the polygon
at that vertex. The exterior angles of a convex polygon add up to a full
turn, `2π`, so all the arcs together make one circle of radius `R`.

Answer: the perimeter of the polygon plus `2πR`, `O(N)`.

Pitfalls:

- `N = 1`: the thread is just the circle `2πR`; `N = 2`: the "perimeter"
  is the distance there and back;
- the polygon may be given clockwise — the formula does not care;
- print with exactly two decimals.

## Optimized solutions

The optimized C++ and Java solutions walk the polygon while reading, so
the nails are never stored. Java also reads the input in 1 KB blocks and
cuts each number out by hand instead of using `Scanner`, and rounds with
`BigDecimal` the way `String.format` does. C++ 156 KB instead of 224 KB,
with the same time; Java 780 KB instead of 2096 KB, with the same time.

## Language notes

The same formula everywhere. The simple Java solution parses and prints
with `Locale.US`, so that the decimal separator is a point.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1020_geometry.cpp](1020_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 224 KB | 11278243 |
| [1020_geometry.go](1020_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1084 KB | 11278244 |
| [1020_geometry.java](1020_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 2096 KB | 11278246 |
| [1020_geometry.py](1020_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.062 s | 392 KB | 11278245 |
| [1020_geometry.rs](1020_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 264 KB | 11278249 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1020_geometry_optimized.cpp](1020_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 156 KB | 11303701 |
| [1020_geometry_optimized.java](1020_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 780 KB | 11303958 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
