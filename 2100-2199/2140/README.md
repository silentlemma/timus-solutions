# 2140. Fewest walk, jump, drop and climb moves through a voxel map

[Timus 2140](https://acm.timus.ru/problem.aspx?space=1&num=2140) · difficulty 1128 · bfs

Original problem by Vadim Barinov, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map of A × B × H unit cubes has free and filled cells. A character
stands in a free cell above a floor (on the lowest layer or on a filled
cell) and moves in four horizontal directions with four kinds of moves:
walk to the neighbour, jump two cells over a free middle cell with a
free cell under it, drop to the neighbour one layer lower, and climb to
the neighbour one layer higher, each with its own rules about which
cells must be free. Find a shortest sequence of moves from the start to
the goal, or report NO. Any shortest sequence is accepted. The limits
are 3 seconds and 256 MB.

## Input

A, B and H, each at most 50, the map as H blocks of A lines of B
characters from the bottom layer up, then the start and the goal.

## Output

NO, or YES, the number of moves and the moves as "type direction".

## Checking

A checker independently computes the minimum number of moves and replays
the submitted route to check its validity and optimality. It ignores the
stored answer file.

## Examples

### Example 1

Input:

```
1 2 1
..
1 1 1
1 2 1
```

Output:

```
YES
1
walk east
```

### Example 2

Input:

```
3 4 2
.#..
....
.#..
....
....
....
1 1 1
3 4 1
```

Output:

```
YES
4
climb east
jump south
drop east
walk east
```

## Solution

All moves take the same time, so this is a breadth-first search over
the at most 125 000 cells where the character can stand, with up to
16 moves from each: four kinds in four directions. Each move checks its
cells exactly as the statement says:

- walk: the neighbour is a standing cell;
- jump: the neighbour and the cell below it are free and the cell two
  steps away is a standing cell;
- drop: the neighbour is free and the cell below it is a standing cell;
- climb: the cell above the character is free and the neighbour of that
  cell is a standing cell.

A border of filled padding around the map removes all bounds checks,
and a cell stands above a floor when it is free and the cell below is
filled, the padding under the lowest layer counting as filled. The
search remembers the move that first reached every cell, and the route
is read back from the goal. The work is O(A B H).

In the second example the character climbs onto the wall, jumps over
the free middle cell, drops back and walks to the goal in four moves.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2140_bfs.cpp](2140_bfs.cpp) | G++ 13.2 x64 | bfs | O(A B H) | AC | 0.031 s | 1612 KB |
| [2140_bfs.go](2140_bfs.go) | Go 1.14 x64 | bfs | O(A B H) | AC | 0.046 s | 4656 KB |
| [2140_bfs.java](2140_bfs.java) | Java 1.8 | bfs | O(A B H) | AC | 0.125 s | 4964 KB |
| [2140_bfs.py](2140_bfs.py) | Python 3.12 x64 | bfs | O(A B H) | AC | 0.265 s | 9140 KB |
| [2140_bfs.rs](2140_bfs.rs) | Rust 1.75 x64 | bfs | O(A B H) | AC | 0.046 s | 3184 KB |
