# 2169. Orienting a graph with one outgoing and three incoming edges at most

[Timus 2169](https://acm.timus.ru/problem.aspx?space=1&num=2169) · difficulty 1754 · dsu, graphs

Original problem by Valentin Zuev, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple undirected graph has N vertices and M edges. Count, modulo
10⁹ + 7, the ways to direct every edge so that each vertex has at most
one outgoing edge and at most three incoming ones. The limits are
2 seconds and 256 MB.

## Input

N and M, 1 ≤ N ≤ 10⁵, 0 ≤ M ≤ 10⁵, then M edges without loops or
repeats.

## Output

The number of orientations modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
5 4
1 2
1 3
1 4
1 5
```

Output:

```
4
```

### Example 2

Input:

```
6 4
1 2
1 3
2 3
4 5
```

Output:

```
4
```

## Solution

With at most one outgoing edge per vertex, a connected component with
V vertices has at most V edges, so the components are counted
separately and multiplied.

- **More edges than vertices:** no orientation, the answer is 0.
- **A tree (V − 1 edges):** exactly one vertex, the sink, has no
  outgoing edge, and every edge then points toward it. The sink gets all
  of its edges incoming and any other vertex all but one, so the choices
  are the vertices of degree at most 3, provided no vertex has degree
  above 4.
- **One cycle (V edges):** every vertex has an outgoing edge, so the
  cycle is directed one of two ways and the trees hanging off it point
  into it. Each vertex receives all but one of its edges, which only
  needs degree at most 4, giving 2 ways.

A disjoint set union collects each component's vertex and edge counts,
and the degree check runs on every vertex.

In the first example the center has degree 4 and cannot be the sink, so
the sink is one of the four leaves.

This takes O((N + M) α(N)).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2169_dsu_graphs.cpp](2169_dsu_graphs.cpp) | G++ 13.2 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 1784 KB |
| [2169_dsu_graphs.go](2169_dsu_graphs.go) | Go 1.14 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 8108 KB |
| [2169_dsu_graphs.java](2169_dsu_graphs.java) | Java 1.8 | dsu, graphs | O((N + M) α(N)) | AC | 0.125 s | 2352 KB |
| [2169_dsu_graphs.py](2169_dsu_graphs.py) | Python 3.12 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.406 s | 18680 KB |
| [2169_dsu_graphs.rs](2169_dsu_graphs.rs) | Rust 1.75 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 6876 KB |
