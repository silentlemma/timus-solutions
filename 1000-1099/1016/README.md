# 1016. The cheapest walk of a rolling cube on a chessboard

[Timus 1016](https://acm.timus.ru/problem.aspx?space=1&num=1016) · difficulty 823 · dijkstra, graphs

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cube with a number from 0 to 1000 on each face stands on a square of an
8×8 chessboard; its edge equals the side of a square. One move rolls it
over an edge of its bottom face onto a side neighbour. The cost of a walk is
the sum of the numbers on the bottom face over all squares it stands on,
including the first and the last one (a number is counted every time its
face is at the bottom). Find a walk of minimal cost between two different
given squares.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

One line: the start and the target square in chess notation (`a`–`h` and
`1`–`8`), then the numbers on the near, far, top, right, bottom and left
faces at the start. "Near" faces rank 1, "right" faces file `h`.

## Output

One line: the minimal cost, then the squares of the walk from the start to
the target, separated by spaces.

## Checking

Any optimal walk is accepted. The checker rolls the cube along the printed
walk: each step must go to a side neighbour on the board, the walk must start
and end at the given squares, and its cost must equal both the printed sum
and the minimum.

## Examples

### Example 1

Input:

```
b2 b3 0 9 1 3 1 1
```

Output:

```
5 b2 a2 a1 b1 b2 b3
```

### Example 2

Input:

```
a1 h8 1 1 1 1 1 1
```

Output:

```
15 a1 a2 a3 a4 a5 a6 b6 b7 c7 c8 d8 e8 f8 g8 h8
```

## Solution

The cost of the next square depends on which face ends up at the bottom, so
the position alone is not a state: the **state** is the square together with
the orientation of the cube. A cube has 24 orientations, so there are
`64 · 24 = 1536` states, each with at most 4 moves.

**Orientations.** Keep for every position (near, far, top, right, bottom,
left) the index of the original face that is there. A roll is a fixed
permutation of positions, e.g. rolling towards the far side moves top → far
→ bottom → near → top. Starting from the identity and applying the four
rolls until nothing new appears gives the 24 orientations and a transition
table `next[orientation][direction]`.

**Shortest path.** Moving into a state costs the number on its bottom face,
and the start state costs its own bottom face. All costs are non-negative,
so Dijkstra's algorithm finds the cheapest walk; remember the predecessor of
every state and, at the end, take the cheapest of the 24 states on the
target square and follow the predecessors back. `O(S log S)` with
`S = 1536` — instant.

Pitfalls:

- the shortest walk in squares is often not the cheapest: the cube may
  loop around to bring a cheap face down;
- equal numbers on different faces: track the faces by their position in
  the input, not by their values;
- count the bottom face of the start square as well.

## Language notes

The same Dijkstra everywhere, with the standard priority queue of each
language (`container/heap` in Go, `BinaryHeap` with `Reverse` in Rust).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1016_dijkstra.cpp](1016_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 428 KB |
| [1016_dijkstra.go](1016_dijkstra.go) | Go 1.14 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 1236 KB |
| [1016_dijkstra.java](1016_dijkstra.java) | Java 1.8 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.140 s | 3892 KB |
| [1016_dijkstra.py](1016_dijkstra.py) | Python 3.12 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.046 s | 920 KB |
| [1016_dijkstra.rs](1016_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 468 KB |
