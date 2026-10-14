# 1527. Bad Roads

[Timus 1527](https://acm.timus.ru/problem.aspx?space=1&num=1527) · difficulty 1133 · shortest_paths

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities (1 ≤ n ≤ 100) are joined by m one-way roads (1 ≤ m ≤ 10⁴). Each
road takes some time, may cost one toll, and needs a car with at least
a given ground clearance. Find the smallest clearance of a car that can
go from s to f within t minutes and b tolls, and a route for it, or
print -1.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n, m, s and f; then b and t; then each road: from, to, toll (0 or 1),
time and clearance.

## Output

The smallest clearance, the number of roads in a route and the road
numbers in order; or -1. Any fitting route is accepted.

## Examples

### Example 1

Input:

```
2 2 1 2
1 100
1 2 1 100 77
1 2 1 100 66
```

Output:

```
66
1
2
```

### Example 2

Input:

```
2 2 1 2
0 100
1 2 0 101 77
1 2 1 100 66
```

Output:

```
-1
```

## Solution

The answer is the clearance of some road, and a larger clearance only
adds roads, so binary search over the sorted clearances. To test a
clearance, run Dijkstra's algorithm on states (city, tolls paid), using
only roads no higher than it and staying within both limits. A route
that repeats a city can drop the loop without paying more, so at most
n − 1 tolls matter and the budget can be capped there. A state is
skipped when fewer tolls already reach its city as fast, which keeps
the search small. The predecessor road of each state gives the route.
With at most n² states a test costs `O(n·m·log(n·m))`, so
`O(log m · n·m·log(n·m))` in all, and far less in practice.

Pitfalls:

- the toll budget can be 10⁶, but more than n − 1 tolls never help
  (test 08);
- roads may take no time at all (test 03, gen3);
- the cheaper route in money may be too slow, and the reverse (tests
  04, 05);
- the finish may be unreachable within the limits, or at all (tests 02,
  06, gen5);
- clearances can be 0 (test 07);
- many routes can fit, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1527_shortest_paths.cpp](1527_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 484 KB |
| [1527_shortest_paths.go](1527_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 5480 KB |
| [1527_shortest_paths.java](1527_shortest_paths.java) | Java 1.8 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.140 s | 5672 KB |
| [1527_shortest_paths.py](1527_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.187 s | 6608 KB |
| [1527_shortest_paths.rs](1527_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(log m * n * m * log(n * m)) | AC | 0.031 s | 1016 KB |
