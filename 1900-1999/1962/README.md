# 1962. Circular Seating with Required Neighbors

[Timus 1962](https://acm.timus.ru/problem.aspx?space=1&num=1962) · difficulty 796 · graphs

Original problem from Open Ural FU Personal Contest 2013 | author not listed on Timus.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Seat n distinct people numbered 1 through n around a circular table.
Person 1 has a fixed chair. For each person i from 1 through m, person
k_i must occupy one of the two neighboring chairs. Count seatings modulo
1,000,000,007. Reflections count separately; rotations do not. With two
people, the same other person is the neighbor on both sides. Limits:
1 second, 64 MB.

## Input

Integers n,m with 2≤n≤100 and 0≤m≤n, then m integers k_i, one per line.
Each satisfies 1≤k_i≤n and k_i≠i. The requesting people are exactly
the prefix 1,…,m; the input does not give arbitrary pairs of labels.

## Output

One integer: the number of valid anchored seatings modulo 1,000,000,007.

## Checking

Outputs are compared token by token.

## Examples

```
6 6
2
1
1
5
6
5
```

```
4
```

```
4 3
2
3
1
```

```
0
```

## Solution

The first sample forces paths 2–1–3 and 4–5–6. Their circular block order
is unique, and each path has two orientations, giving 1!·2²=4. The second
forces a triangle on people 1,2,3. No required edge can be opened to insert
person 4, so no seating exists.

Represent a requirement as one undirected edge. Mutual requests add only
one edge. Reject as soon as any vertex has more than two distinct neighbors.
Otherwise, connected components are paths, isolated vertices, or cycles.
Find them by an iterative traversal, recording the number of vertices and
the sum of their degrees. A component is a cycle exactly when its degree
sum equals twice its number of vertices.

A proper cycle makes the answer zero: each of its vertices already needs
both neighboring positions inside that cycle, leaving no attachment for
the remaining people. A cycle containing all n vertices gives exactly two
orientations, with person 1 fixing their rotations.

If there are no cycles, contract each path, including an isolated vertex,
to one block. Let C be the number of blocks and P the number of paths with
at least two vertices. There are (C−1)! circular orders of these distinct
blocks. Each nontrivial path has two orientations, whereas an isolated
vertex has one, so the answer is (C−1)!·2^P modulo 1,000,000,007.

This is a bijection for n≥3. Required path edges force consecutive chairs,
so every valid seating produces an oriented cyclic block order. Expanding
such blocks satisfies every requirement. Whether person 1 is an endpoint,
an internal vertex, or isolated, exactly one rotation of the expanded
order puts person 1 in the fixed chair. There is no extra factor for the
length of that person's block.

Handle n=2 separately: the only possible anchored order is always valid.
The two orientations of its single path would describe the same seating.
Compute powers and factorials with reduction after every multiplication.

`O(n+m)` time and `O(n+m)` space. Adjacency lists have length at most two
before each accepted insertion, so duplicate lookup takes constant time;
an insertion making a degree three terminates immediately.

Deduplicate mutual requests. Count isolated people as blocks. A full cycle
gives two, a proper cycle gives zero. Do not divide by two for reflection,
or multiply by a block length for the fixed guest. An unconstrained input
gives (n−1)!, and one full path gives two for n≥3. Mark vertices when
pushing them onto the traversal stack. Native modular products need
64-bit arithmetic: a factorial step can exceed a 32-bit integer.

## Language notes

C++ uses int64_t, Go 1.14 int64, Java 8 long, and Rust 1.75 u64 for modular
products. Each uses adjacency lists and an explicit stack. Python 3.12
uses integer arithmetic and modular pow; recursion is unnecessary.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1962_graphs.cpp](1962_graphs.cpp) | G++ 13.2 x64 | graphs | O(n+m) | AC | 0.015 s | 440 KB |
| [1962_graphs.go](1962_graphs.go) | Go 1.14 x64 | graphs | O(n+m) | AC | 0.031 s | 1088 KB |
| [1962_graphs.java](1962_graphs.java) | Java 1.8 | graphs | O(n+m) | AC | 0.125 s | 1724 KB |
| [1962_graphs.py](1962_graphs.py) | Python 3.12 x64 | graphs | O(n+m) | AC | 0.093 s | 656 KB |
| [1962_graphs.rs](1962_graphs.rs) | Rust 1.75 x64 | graphs | O(n+m) | AC | 0.046 s | 236 KB |
