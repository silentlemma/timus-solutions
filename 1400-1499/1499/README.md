# 1499. Kerchiefs

[Timus 1499](https://acm.timus.ru/problem.aspx?space=1&num=1499) · difficulty 1475 · constructive

Original problem by Alex Samsonov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A regular polygon with vertices 1 … N (3 ≤ N ≤ 50000) already has K
non-crossing cuts along diagonals (0 ≤ K ≤ N − 3). Add cuts along
diagonals, crossing none of the others, until the polygon is split into
triangles, and print the new cuts.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, K, then K lines with the two vertices of a cut.

## Output

The number of new cuts, then the cuts as pairs of vertices. Any
triangulation is accepted.

## Examples

### Example 1

Input:

```
5
1
1 4
```

Output:

```
1
3 1
```

## Solution

Every triangulation of an N-gon has N − 3 diagonals, so exactly
N − 3 − K cuts are missing. The given cuts split the polygon into convex
faces, and any face is triangulated by a fan of diagonals from one of
its vertices.

The faces are found with a stack while walking the vertices 1 … N in
order. Push each vertex v; then, for every given cut u–v with u < v,
taken from the nearest u to the farthest, the stack segment from u to v
forms one face: pop back to u, fan the face from u, and push v back.
After the walk the stack holds the face that contains the side N–1,
which is fanned too. There are N + K pushes and at most as many pops,
so the walk is linear apart from sorting the cuts at each vertex.
`O(N log N)`.

Pitfalls:

- a cut may be given with the larger vertex first (test 06);
- several cuts can end at one vertex and must close their faces from
  the inside out (tests 05, 12);
- with all N − 3 cuts given, or with N = 3, the answer is 0 (tests 02,
  03, gen3).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1499_constructive.cpp](1499_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.078 s | 2108 KB |
| [1499_constructive.go](1499_constructive.go) | Go 1.14 x64 | constructive | O(N log N) | AC | 0.093 s | 9344 KB |
| [1499_constructive.java](1499_constructive.java) | Java 1.8 | constructive | O(N log N) | AC | 0.171 s | 10440 KB |
| [1499_constructive.py](1499_constructive.py) | Python 3.12 x64 | constructive | O(N log N) | AC | 0.187 s | 14896 KB |
| [1499_constructive.rs](1499_constructive.rs) | Rust 1.75 x64 | constructive | O(N log N) | AC | 0.031 s | 4108 KB |
