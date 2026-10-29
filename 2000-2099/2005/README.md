# 2005. The Shortest Allowed Five-Stop Route

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · difficulty 94 · bruteforce

Original problem by Mikhail Rubinchik. (Prepared by Oleg Merkurev), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Visit five locations exactly once, starting at 1 and finishing at 5.
Location 3 must not be the penultimate stop. Given distances between
every pair, find a route of minimum total distance and its length. Any
optimal allowed route is acceptable.

## Input

A 5 by 5 integer distance matrix. Every entry is between 0 and 10000,
diagonal entries are zero, distances are symmetric and satisfy the
triangle inequality: `d[i][j]≤d[i][k]+d[k][j]`. Time limit 0.5 seconds,
memory 64 MB.

## Output

On the first line print the minimum total distance. On the second print
the five location numbers in visiting order, separated by spaces. Ties
may be resolved arbitrarily.

## Checking

A checker verifies that the route is allowed, that the printed length is
its length and that it is optimal; any optimal route is accepted.

## Examples

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

The displayed route costs `2600+5300+1900+3700=13500`; its penultimate
stop is 4, so it obeys the restriction.

## Solution

Point 1 is first and point 5 is last, so only the order of points 2, 3
and 4 varies: six orders, of which the two with 3 just before 5 are
forbidden. Try the four others, add up the four distances of each route,
and keep the shortest. `O(1)`.

Pitfalls:

- the rule concerns the stop just before the last one;
- a route costs from 0 to 40 000, so the minimum starts from "none yet",
  not from 0 or 10 000.

## Language notes

- Python takes the orders from `itertools.permutations`; the other
  languages go through the points with three nested loops.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11303437 |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1104 KB | 11303440 |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1616 KB | 11303442 |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 432 KB | 11303445 |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 236 KB | 11303446 |
