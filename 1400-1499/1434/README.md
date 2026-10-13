# 1434. Buses in Vasyuki

[Timus 1434](https://acm.timus.ru/problem.aspx?space=1&num=1434) · difficulty 885 · bfs

Original problem by Evgeny Krokhalev and Ekaterina Vasilyeva, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has N bus routes (N ≤ 1000) over M stops (M ≤ 10⁵), at most
200 000 numbers in all route lists. A ride costs one rouble whatever the
number of stops, and a bus takes you between any two stops of its
route. Find the cheapest way from stop A to stop B: print the cost and
the stops where the ride starts, changes and ends, or −1 if B cannot be
reached.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

N and M, then the N routes as a count and the stops, then A and B.

## Output

−1, or the cost and the list of stops.

## Examples

### Example 1

Input:

```
3 10
5 2 4 6 8 10
3 3 6 9
2 5 10
5 9
```

Output:

```
3
5 10 6 9
```

## Solution

Breadth-first search over stops, where one step is a whole ride: from a
stop, take every route through it that has not been taken yet and mark
every stop of that route one ride further. Each route is opened once,
the first time some stop on it is reached, so the work is the total
length of the routes. Each stop remembers the route that reached it and
each route the stop where it was first taken, which gives the changes
back from B. `O(N + M + S)` for S numbers in the routes.

Pitfalls:

- buses go both ways: in the example route 1 is ridden from 10 back
  to 6 (test 01);
- the answer is −1 when B lies on no route reachable from A (tests 02,
  04, gen3);
- each route must be opened only once, or long routes through many
  stops are scanned again and again (gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1434_bfs.cpp](1434_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M + S) | AC | 0.140 s | 6252 KB |
| [1434_bfs.go](1434_bfs.go) | Go 1.14 x64 | bfs | O(N + M + S) | AC | 0.062 s | 15812 KB |
| [1434_bfs.java](1434_bfs.java) | Java 1.8 | bfs | O(N + M + S) | AC | 0.171 s | 16480 KB |
| [1434_bfs.py](1434_bfs.py) | Python 3.12 x64 | bfs | O(N + M + S) | AC | 0.171 s | 31732 KB |
| [1434_bfs.rs](1434_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M + S) | AC | 0.046 s | 14188 KB |
