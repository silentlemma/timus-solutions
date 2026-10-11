# 1320. Graph Decomposition

[Timus 1320](https://acm.timus.ru/problem.aspx?space=1&num=1320) · difficulty 283 · dsu

Original problem: idea by Alexander Petrov, prepared by Alexander Petrov and Leonid Volkov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph has an even number of edges, from 2 to 1050, on vertices
numbered from 1 to 1000. Decide whether its edges can be split into
pairs of adjacent edges, that is, edges with a common vertex.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The edges, each as a pair of vertex numbers, until the end of input.
There are no loops and no repeated edges.

## Output

1 if such a split exists, otherwise 0.

## Examples

### Example 1

Input:

```
1 2
2 3
3 1
1 10
```

Output:

```
1
```

### Example 2

Input:

```
1 2
2 3
3 1
4 10
```

Output:

```
0
```

## Solution

Two adjacent edges always lie in the same connected component, so every
component needs an even number of edges. That is also enough: a
connected graph with an even number of edges can always be split. Take
a depth-first search tree and handle the vertices from the deepest up.
At a vertex v, pair the still free edges at v other than the one to its
parent; if one is left over, pair it with the edge to the parent,
otherwise the parent edge stays free for the parent. Every vertex but
the root leaves no free edges below it, and at the root the free edges
are paired among themselves, which works because the total is even.

So the answer only needs the number of edges in each component. A
disjoint set union over the vertices keeps it at each root: joining two
components adds their counts, and every edge adds one.
Finally, check that every root has an even count. Here V is the vertex
range and M is the number of edges. Roots are linked without rank or
size balancing, so path halving gives a safe total bound of
`O(V + M log V)`, including initialization and the final root scan.

Pitfalls:

- the whole graph always has an even number of edges, but a component
  may not: a triangle and a separate edge give 0 (test 02, also two
  separate triangles in test 06);
- the number of edges is not given, the input simply ends;
- two triangles sharing a vertex form one component of six edges and
  can be split (test 07).

The rule was compared with a search over all pairings on 487 random
graphs with up to 14 edges.

## Language notes

- All five solutions use the same disjoint set union with path halving.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1320_dsu.cpp](1320_dsu.cpp) | G++ 13.2 x64 | dsu | O(V + M log V) | AC | 0.015 s | 184 KB |
| [1320_dsu.go](1320_dsu.go) | Go 1.14 x64 | dsu | O(V + M log V) | AC | 0.015 s | 1112 KB |
| [1320_dsu.java](1320_dsu.java) | Java 1.8 | dsu | O(V + M log V) | AC | 0.109 s | 420 KB |
| [1320_dsu.py](1320_dsu.py) | Python 3.12 x64 | dsu | O(V + M log V) | AC | 0.093 s | 656 KB |
| [1320_dsu.rs](1320_dsu.rs) | Rust 1.75 x64 | dsu | O(V + M log V) | AC | 0.015 s | 264 KB |
