# 1695. Work for Robots

[Timus 1695](https://acm.timus.ru/problem.aspx?space=1&num=1695) · difficulty 2913 · backtracking

Original problem by Mikhail Kolodyazhniy, prepared by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every day a nonempty group of robots who are all friends with one
another goes to work, and no group may repeat. Given the friendship
graph of n robots, find the first day on which no new group is left.

## Input

n (1 ≤ n ≤ 50), then the n × n friendship matrix of zeros and ones,
symmetric with zeros on the diagonal.

## Output

The number of that day.

## Examples

### Example 1

Input:

```
6
011100
101100
110100
111000
000001
000010
```

Output:

```
19
```

## Solution

A working group is a clique of the friendship graph, that is an
independent set of the graph of non-friends. Every nonempty group fills
one day, so the answer is the number of nonempty cliques plus one, which
equals the number of independent sets of the non-friend graph with the
empty set counted.

Count the independent sets of a vertex set M recursively:

- if M falls apart into several connected parts, multiply their counts;
- if every two vertices of M are enemies, the sets are the empty one and
  the |M| single vertices: |M| + 1;
- if no vertex has more than two enemies, M is a path or a cycle, with
  Fibonacci counts: P(s) = P(s − 1) + P(s − 2) for a path, and
  P(s − 1) + P(s − 3) for a cycle;
- otherwise take a vertex v with the most enemies, at least three:
  count(M) = count(M − v) + count(M − v − enemies of v).

Branching only on vertices of degree three or more keeps the recursion
small, and a memo on the vertex mask removes repeated subproblems. The
answer reaches 2⁵⁰ when all robots are friends and fits in 64 bits.

Pitfalls:

- the empty group is not a working day, but the day of rusting is one
  more than the number of groups, so counting the empty set gives the
  answer directly;
- all friends gives 2⁵⁰ (test 03), no friends gives n + 1 (test 04);
- a cycle of enemies needs its own formula (test 07).

The answers match a count over all subsets on small graphs and an
independent accepted implementation on random, sparse and regular
graphs of 50 robots.

Complexity: `O(1.38^n·n)`: branching on a vertex with at least three
enemies gives T(n) = T(n − 1) + T(n − 4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1695_backtracking.cpp](1695_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1.38^n·n) | AC | 0.031 s | 956 KB |
| [1695_backtracking.go](1695_backtracking.go) | Go 1.14 x64 | backtracking | O(1.38^n·n) | AC | 0.031 s | 2632 KB |
| [1695_backtracking.java](1695_backtracking.java) | Java 1.8 | backtracking | O(1.38^n·n) | AC | 0.140 s | 4824 KB |
| [1695_backtracking.py](1695_backtracking.py) | Python 3.12 x64 | backtracking | O(1.38^n·n) | AC | 0.265 s | 3316 KB |
| [1695_backtracking.rs](1695_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1.38^n·n) | AC | 0.046 s | 1488 KB |
