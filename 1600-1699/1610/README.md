# 1610. Cacti Are in Fashion

[Timus 1610](https://acm.timus.ru/problem.aspx?space=1&num=1610) · difficulty 1987 · games

Original problem by Alexander Ipatov and Vladimir Yakovlev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cactus is a connected undirected graph in which every edge lies on at most one
simple cycle; one vertex is the root. Two players take turns cutting an
edge; whatever is no longer connected to the root falls away. The player
who cuts the last edge still attached to the root wins. Who wins with
best play? The cactus has at most 50000 vertices and is given as
edge-disjoint paths.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, m and the root r, then m paths, each as its vertex count and vertices.

## Output

`First` or `Second`.

## Examples

### Example 1

Input:

```
17 2 1
15 3 4 5 6 7 8 3 2 9 10 11 12 13 14 9
6 2 1 15 16 17 15
```

Output:

```
First
```

### Example 2

Input:

```
16 2 1
15 3 4 5 6 7 8 3 2 9 10 11 12 13 14 9
5 2 1 15 16 1
```

Output:

```
Second
```

## Solution

This is Green Hackenbush, and the player to move wins exactly when the
Grundy value of the rooted graph is not 0. Two classical rules give the
value of a cactus. By the colon principle, a branch hanging from a
vertex by a single edge counts as g + 1, where g is the value of what
hangs below that edge. By the fusion principle, the vertices of a cycle
can be merged into one without changing the value: the cycle turns into
as many loops as it has edges, each loop is worth 1, so the cycle itself
counts as its length mod 2, and whatever hung from its vertices now
hangs from the merged one.

A depth-first search from the root, without recursion, makes every
non-tree edge join a vertex to one of its ancestors; each such edge
closes one cycle, listed at its top vertex. Then the vertices are
processed from the deepest up: a vertex XORs g + 1 over its tree
children that are not on a cycle with it, and for each cycle it tops,
the parity of the cycle and the values of the cycle's other vertices.
`O(n + m)` in all, since every edge lies on at most one cycle.

The results were checked against an exhaustive search of the game on
250 random small cacti of up to 12 edges.

Pitfalls:

- an even cycle at the root is worth 0, so a lone square loses for the
  player to move, while a triangle wins (tests 05 and 06);
- the root may be any vertex, even one in the middle of a path
  (tests 01 and 09);
- recursion 50000 deep overflows the stack in several languages, so the
  search keeps its own stack.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1610_games.cpp](1610_games.cpp) | G++ 13.2 x64 | games | O(n + m) | AC | 0.093 s | 5800 KB |
| [1610_games.go](1610_games.go) | Go 1.14 x64 | games | O(n + m) | AC | 0.125 s | 13364 KB |
| [1610_games.java](1610_games.java) | Java 1.8 | games | O(n + m) | AC | 0.203 s | 14784 KB |
| [1610_games.py](1610_games.py) | Python 3.12 x64 | games | O(n + m) | AC | 0.343 s | 24436 KB |
| [1610_games.rs](1610_games.rs) | Rust 1.75 x64 | games | O(n + m) | AC | 0.062 s | 11688 KB |
