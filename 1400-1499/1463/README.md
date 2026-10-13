# 1463. Happiness to People!

[Timus 1463](https://acm.timus.ru/problem.aspx?space=1&num=1463) · difficulty 598 · dp

Original problem by Alexander Toropov, with special thanks to Alexander Ipatov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N cities (1 ≤ N ≤ 50000) with joy A[i] for a visit, and K
links between pairs of cities with joy c for a flight along them, all
values non-negative integers up to 10000. Between any two cities there
is at most one route, so the links form a forest. Find a route through
different cities, starting anywhere, with the largest total joy of its
cities and flights.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K, then the joys A[i], then K lines a, b, c.

## Output

The largest joy, the number of cities on the route, and the route. Any
best route is accepted.

## Examples

### Example 1

Input:

```
2 1
1 1
1 2 1
```

Output:

```
3
2
1 2
```

### Example 2

Input:

```
8 7
1 5 4 6 10 1 2 2
1 2 1
2 3 10
2 4 1
4 5 1
4 6 2
6 7 2
6 8 3
```

Output:

```
37
4
5 4 2 3
```

## Solution

A route in a forest is a path in one tree, and every path has a highest
city when its tree is hung from a root. Root each tree anywhere and
process the cities from the leaves up. For every city v keep the best
route that starts at v and goes down, down[v] = A[v] plus the best value
of c + down[w] over its children w, together with the child that gives
it. The best route whose highest city is v joins the two best of these
child values to A[v]; all values are non-negative, so taking two
children (or one, or none) never hurts. The route is rebuilt by
following the stored children down the two chosen branches.

The trees can be 50000 cities deep, so the traversal uses an explicit
stack instead of recursion. `O(N + K)`.

Pitfalls:

- links may be missing entirely, and the best route can be one city
  (tests 03, 04, 07, gen5);
- a long chain makes recursion overflow (gen2);
- with zero joys every route is a best one (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1463_dp.cpp](1463_dp.cpp) | G++ 13.2 x64 | dp | O(N + K) | AC | 0.125 s | 5364 KB |
| [1463_dp.go](1463_dp.go) | Go 1.14 x64 | dp | O(N + K) | AC | 0.109 s | 11948 KB |
| [1463_dp.java](1463_dp.java) | Java 1.8 | dp | O(N + K) | AC | 0.140 s | 3888 KB |
| [1463_dp.py](1463_dp.py) | Python 3.12 x64 | dp | O(N + K) | AC | 0.265 s | 35104 KB |
| [1463_dp.rs](1463_dp.rs) | Rust 1.75 x64 | dp | O(N + K) | AC | 0.031 s | 10112 KB |
