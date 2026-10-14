# 1614. National Project “Trams”

[Timus 1614](https://acm.timus.ru/problem.aspx?space=1&num=1614) · difficulty 846 · constructive

Original problem by Alexander Ipatov (idea by Magaz Asanov), from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has 2n tram stops (1 ≤ n ≤ 100). Lay out exactly n tram routes,
each a sequence of exactly 2n stops (a stop may repeat), so that every
two stops are neighbours on some route: a tram can take a passenger
from one to the other without stopping in between. Print the routes, or
`-1` if that is impossible. Any valid set is accepted.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n.

## Output

n lines, each the 2n stops of one route.

## Examples

### Example 1

Input:

```
3
```

Output:

```
1 6 2 1 3 4
2 3 6 5 4 6
5 1 4 2 5 3
```

## Solution

There are n(2n − 1) pairs of stops, and n routes of 2n stops have
exactly n(2n − 1) neighbouring places, so every pair must appear exactly
once. We split the complete graph on 2n stops into n paths
through all stops. It is always possible.

Number the stops 0 … 2n − 1 around a circle. Route k goes k, k + 1,
k − 1, k + 2, k − 2, …, k + n (modulo 2n): it visits every stop once,
and its neighbouring pairs alternate between the sums 2k + 1 and 2k
modulo 2n — all pairs {k − j, k + 1 + j} and all pairs {k + j, k − j}.
Every pair of different stops has some sum s modulo 2n and belongs to
route ⌊s / 2⌋, so the n routes cover all pairs. `O(n²)`.

Pitfalls:

- n = 1 is one route with both stops (test 02);
- the example's routes are different but also valid, so a checker
  verifies that every pair is covered.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1614_constructive.cpp](1614_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 128 KB |
| [1614_constructive.go](1614_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1260 KB |
| [1614_constructive.java](1614_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 2012 KB |
| [1614_constructive.py](1614_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.109 s | 452 KB |
| [1614_constructive.rs](1614_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.046 s | 428 KB |
