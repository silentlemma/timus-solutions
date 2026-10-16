# 1824. Ifrit Bomber

[Timus 1824](https://acm.timus.ru/problem.aspx?space=1&num=1824) · difficulty 1065 · backtracking

Original problem by Igor Andrianov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n cities, points on the plane. A bottle dropped on a city
destroys every city within distance r of it. Bottles may be dropped
only on cities. Find the fewest bottles that destroy all cities and the
cities to drop them on.

## Input

n and r (1 ≤ n ≤ 30, 1 ≤ r ≤ 1000), then n lines with the integer
coordinates of the cities, from 0 to 1000.

## Output

The least number of bottles, then the numbers of the cities to drop
them on. Any optimal choice is accepted.

## Examples

### Example 1

Input:

```
4 50
10 10
500 500
501 501
999 999
```

Output:

```
3
1 3 4
```

## Solution

This is a minimum dominating set of the graph joining cities at
distance at most r, with 30 vertices, so each city's reach fits in a
bitmask cover[i].

Try budgets k = 1, 2, … and search for at most k drops covering the
set of cities still left. Some drop must hit the uncovered city u with
the fewest cities in reach, so the search branches only over the cities
in reach of u, most new hits first. Three cuts keep it small:

- if even k drops of the largest current gain cannot cover what is
  left, give up;
- a candidate whose new hits are a subset of an already tried
  candidate's is skipped, since its branch can only be worse;
- a failed state (cities left, budget) is remembered, so it is not
  searched again with the same or a smaller budget.

The first budget that succeeds is optimal. The worst case is
exponential, but every test, including random maps that need up to 17
bottles, chains and lattices, takes milliseconds.

In the example cities 2 and 3 are √2 apart and one bottle takes both,
while 1 and 4 are far from everything: three bottles.

Pitfalls:

- distance exactly r counts as a hit, so compare squared integers;
- nothing forbids two cities at the same point;
- a greedy choice of the city hitting the most is not optimal.

The counts agree with an independent accepted implementation on a few
hundred random maps of every shape the generator makes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1824_backtracking.cpp](1824_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(2^n) worst case | AC | 0.031 s | 220 KB |
| [1824_backtracking.go](1824_backtracking.go) | Go 1.14 x64 | backtracking | O(2^n) worst case | AC | 0.031 s | 1204 KB |
| [1824_backtracking.java](1824_backtracking.java) | Java 1.8 | backtracking | O(2^n) worst case | AC | 0.156 s | 3944 KB |
| [1824_backtracking.py](1824_backtracking.py) | Python 3.12 x64 | backtracking | O(2^n) worst case | AC | 0.078 s | 656 KB |
| [1824_backtracking.rs](1824_backtracking.rs) | Rust 1.75 x64 | backtracking | O(2^n) worst case | AC | 0.015 s | 420 KB |
