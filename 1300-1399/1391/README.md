# 1391. Snake

[Timus 1391](https://acm.timus.ru/problem.aspx?space=1&num=1391) · difficulty 5173 · graphs

Original problem by Dmitry Ivankov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A maze of H × W cells, H ≤ 300 and W ≤ 30, has walls 'X' and free cells
'.', and a single entrance on its border. A snake of length L is a chain
of L distinct cells next to each other. Every unit of time it moves one
cell forward, left or right, the body following the head; it dies if it
cannot move without hitting a wall or itself. At time 0 the head is at
the entrance and the rest of the body is outside. For every L from 2 to
17 find the earliest time the head is back at the entrance, or -1. No
snake of length 18 gets out alive.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

H and W, the entrance cell, then H rows of W characters.

## Output

16 lines: the best time for lengths 2 to 17, or -1.

## Examples

### Example 1

Input:

```
9 9
1 5
XXXX.XXXX
XXX...XXX
XX..X..XX
....XX..X
X.X.X.X.X
..XX.....
X...XXX..
XXXXX....
X.....XXX
```

Output:

```
10
10
10
22
22
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
```

## Solution

The snake cannot turn back, so to get out it has to run around a cycle
of the maze. The best escape is a lasso: a shortest path from the
entrance to a nearest cell J of a reachable simple cycle of c cells,
once around the cycle, and the same path back, in 2·dist(J) + c units.
The head comes back to J after c moves; entering the departing tail's
cell is allowed, so the loop works exactly when c ≥ L, and the way
back is free behind the body. A reachable cycle of c ≥ 18 cells would
let a snake of length 18 out, so only cycles of 4 to 16 cells count;
on a grid every cycle has an even number of cells.

For each even c the solutions need the smallest distance of any cycle
cell, over all reachable cycles of c cells. Order the reachable cells
by breadth-first distance from the entrance and look for cycles from
every cell in turn, using only cells later in the order, so each cycle
is found from its nearest cell. The search is a depth-first walk of at
most 16 steps that stops when the Manhattan distance back to the start
is too long. A length is settled at the first cell that closes it, and
the search ends once all seven lengths are settled. The answer for L
is the minimum of 2·best(c) + c over c ≥ L.

Pitfalls:

- the cycle needs at least L cells, not L + 1: the head may enter the
  cell the tail is just leaving (test 03);
- grid cycles have an even number of cells, so a snake of length 17
  never gets out (test 05);
- according to the forum one judge test has a cycle of more than 17
  cells, against the promise, and its answers ignore that cycle; the
  solutions count cycles of at most 16 cells, which also keeps the
  search short (test 06 is such a maze).

The answers were compared with a breadth-first search over whole snake
positions, for every length, on 300 random mazes of at most 16 cells and
on all the other tests except test 06.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1391_graphs.cpp](1391_graphs.cpp) | G++ 13.2 x64 | graphs | O(H·W·3^16) | AC | 0.046 s | 584 KB |
| [1391_graphs.go](1391_graphs.go) | Go 1.14 x64 | graphs | O(H·W·3^16) | AC | 0.078 s | 2148 KB |
| [1391_graphs.java](1391_graphs.java) | Java 1.8 | graphs | O(H·W·3^16) | AC | 0.140 s | 1320 KB |
| [1391_graphs.py](1391_graphs.py) | Python 3.12 x64 | graphs | O(H·W·3^16) | AC | 1.656 s | 2664 KB |
| [1391_graphs.rs](1391_graphs.rs) | Rust 1.75 x64 | graphs | O(H·W·3^16) | AC | 0.046 s | 1036 KB |
