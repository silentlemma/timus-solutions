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

## Optimized solutions

`1463_trees_optimized.cpp`. Keep linear leaf peeling with degree/XOR accumulators and the two best removed branches. The same child links reconstruct the optimum route. A 16 KiB block reader and writer replace formatted numeric I/O; graph state and tie rules stay unchanged. The readable standard-I/O counterpart 1463_trees.cpp and all original DFS teaching sources remain with their own metrics. Both leaf-peeling variants take O(N+K) time and O(N) graph state, plus fixed I/O buffers.

Exact-source Accepted #11326974: 0.015 s / 1448 KB. Saved G++ 13.2 comparison, 2026-11-20: time rank 1/42, memory rank 1/42.

Readable standard-I/O version `1463_trees.cpp`. The C++ version removes leaves until each tree is exhausted. At each city it keeps the current degree and the XOR of its remaining neighbors and flight weights. At a leaf these two XOR values give the only remaining flight. The two best removed branches through each city suffice to score and reconstruct the best route. This takes O(N + K) time and O(N) extra space. The metrics come from submission 11317012.

The Python version uses the same leaf removal. It combines each removed branch with the best branch already found at its parent, then updates that best branch. The ends of the two branches are enough to reconstruct the best route. It also takes O(N + K) time and O(N) extra space. The metrics come from submission 11317010.

Go removes leaves using a compact array of city records. XOR keeps track of the remaining neighbour and edge weight without adjacency lists. Submission 11317154 took 0.078 s and used 1976 KB, versus 0.125 s and 11580 KB for the base.

Rust removes leaves with compact city records and recovers the remaining neighbour and edge weight by XOR. Submission 11317155 took 0.015 s and used 980 KB, versus 0.031 s and 10112 KB for the base.

Java removes leaves and uses XOR to recover the remaining neighbour and edge weight. Submission 11317156 took 0.140 s and used 1276 KB, versus 0.156 s and 3896 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322150 · Go 1.14 x64 №11322151 · Java 1.8 №11322152 · Python 3.12 x64 №11322154 · Rust 1.75 x64 №11322155.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1463_dp.cpp](1463_dp.cpp) | G++ 13.2 x64 | dp | O(N + K) | AC | 0.14 s | 5372 KB | 11322150 |
| [1463_dp.go](1463_dp.go) | Go 1.14 x64 | dp | O(N + K) | AC | 0.125 s | 11580 KB | 11322151 |
| [1463_dp.java](1463_dp.java) | Java 1.8 | dp | O(N + K) | AC | 0.156 s | 3896 KB | 11322152 |
| [1463_dp.py](1463_dp.py) | Python 3.12 x64 | dp | O(N + K) | AC | 0.312 s | 34776 KB | 11322154 |
| [1463_dp.rs](1463_dp.rs) | Rust 1.75 x64 | dp | O(N + K) | AC | 0.031 s | 10112 KB | 11322155 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1463_trees_optimized.cpp](1463_trees_optimized.cpp) | G++ 13.2 x64 | trees | O(N + K) | AC | 0.015 s | 1448 KB | 11326974 |
| [1463_trees.cpp](1463_trees.cpp) \* | G++ 13.2 x64 | trees | O(N + K) | AC | 0.109 s | 1504 KB | 11317012 |
| [1463_trees.py](1463_trees.py) | Python 3.12 x64 | trees | O(N + K) | AC | 0.203 s | 10696 KB | 11317010 |
| [1463_trees.go](1463_trees.go) | Go 1.14 x64 | trees | O(N + K) | AC | 0.078 s | 1976 KB | 11317154 |
| [1463_trees.rs](1463_trees.rs) \* | Rust 1.75 x64 | trees | O(N + K) | AC | 0.015 s | 980 KB | 11317155 |
| [1463_trees.java](1463_trees.java) | Java 1.8 | trees | O(N + K) | AC | 0.140 s | 1276 KB | 11317156 |

\* Accepted. The C++ rating target is still open. Accepted. The saved rating has no comparable Rust submissions from other authors.
