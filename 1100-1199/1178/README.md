# 1178. Pairing up cities with straight roads that do not cross

[Timus 1178](https://acm.timus.ru/problem.aspx?space=1&num=1178) · difficulty 150 · geometry

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is an even number `N ≤ 10000` of cities at integer points with
coordinates up to `10⁹` in absolute value, no three on one line. Join
them in pairs by straight roads, each city in exactly one road, so that no
two roads cross.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the coordinates of the cities.

## Output

`N/2` lines, each with the numbers of the two cities a road joins.

## Checking

Any plan is accepted if it pairs every city exactly once and no two roads
meet; the checker compares the roads whose x-ranges overlap.

## Examples

### Example 1

Input:

```
4
0 2
1 1
3 4
4 4
```

Output:

```
1 3
2 4
```

## Solution

Sort the cities by `x` and join the first with the second, the third
with the fourth, and so on. Each road then lies in its own vertical strip
between the `x` of its ends, and the strips of different roads overlap at
most in one border line. On that line each road has only an end, and the
ends are different cities, so the roads do not meet there. A road can be
vertical when its two cities share `x`, but then no other city lies on
that line, as no three cities are on one line. So no two roads meet.
`O(N log N)`.

Pitfalls:

- ties on `x` need no special care, though the solutions break them by
  `y` to make the output reproducible;
- coordinates reach `10⁹`, so they are read as 64-bit integers, although
  the solution only compares them.

Every printed plan passed the checker on all tests, including ten
thousand cities on conics with many shared `x` values.

## Language notes

- All languages sort the city numbers by the pair `(x, y)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1178_geometry.cpp](1178_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 388 KB |
| [1178_geometry.go](1178_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1676 KB |
| [1178_geometry.java](1178_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 6872 KB |
| [1178_geometry.py](1178_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 3276 KB |
| [1178_geometry.rs](1178_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 764 KB |
