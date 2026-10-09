# 1040. Numbering the edges so that every vertex sees coprime numbers

[Timus 1040](https://acm.timus.ru/problem.aspx?space=1&num=1040) · difficulty 1001 · dfs, constructive

Original problem by Dmitry Filimonenkov, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected undirected graph has `N` vertices (`2 ≤ N ≤ 50`) and `M` edges
(`1 ≤ M ≤ N(N − 1)/2`), without loops or multiple edges. Number the edges
with `1..M`, each number used once, so that at every vertex with two or
more edges the greatest common divisor of their numbers is 1. Print `NO`
if this is impossible.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `M`, then `M` lines with the two ends of each edge.

## Output

`YES` and, on the next line, the numbers of the edges in input order; or
`NO`.

## Checking

Any valid numbering is accepted. The checker verifies that the answer is
`YES`, that the numbers are a permutation of `1..M`, and that the gcd at
every vertex with at least two edges is 1.

## Examples

### Example 1

Input:

```
6 6
1 2
2 3
2 4
4 3
5 6
4 5
```

Output:

```
YES
1 2 4 3 6 5
```

### Example 2

Input:

```
2 1
2 1
```

Output:

```
YES
1
```

## Solution

The answer is always `YES`, because two consecutive numbers are coprime.
Run a depth-first search from any vertex and give every edge the next
number of a counter the first time the search looks at it, whether it
leads to a new vertex or to a visited one:

```text
dfs(v):
    mark v
    for every edge e = (v, w):
        if e has no number:
            number[e] = ++counter
            if w is not marked: dfs(w)
```

Take a vertex `w` entered through edge number `k`. None of its other edges
has a number yet: an edge from an earlier vertex to `w` would already have
brought the search into `w`. Nothing is numbered between `k` and the call
`dfs(w)`, so the first other edge of `w` gets `k + 1`, and `gcd(k, k + 1)`
is 1. The start vertex gets the number 1 on its first edge. A vertex with a
single edge needs nothing. `O(N + M)`.

Pitfalls:

- the edges back to visited vertices must be numbered in the same pass;
  numbering only the tree edges and the rest afterwards breaks the
  argument;
- `NO` is never the answer: the graph is connected;
- the answer lists the numbers in the order of the input edges.

## Language notes

- All languages use a recursive DFS; the depth is at most 50.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1040_dfs.cpp](1040_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + M) | AC | 0.015 s | 252 KB |
| [1040_dfs.go](1040_dfs.go) | Go 1.14 x64 | dfs | O(N + M) | AC | 0.031 s | 1208 KB |
| [1040_dfs.java](1040_dfs.java) | Java 1.8 | dfs | O(N + M) | AC | 0.093 s | 688 KB |
| [1040_dfs.py](1040_dfs.py) | Python 3.12 x64 | dfs | O(N + M) | AC | 0.078 s | 672 KB |
| [1040_dfs.rs](1040_dfs.rs) | Rust 1.75 x64 | dfs | O(N + M) | AC | 0.031 s | 372 KB |
