# 1315. MDPAR and MIIAR

[Timus 1315](https://acm.timus.ru/problem.aspx?space=1&num=1315) · difficulty 1836 · bfs

Original problem: idea by Alexander Klepinin, prepared by Alexander Klepinin and Ivan Dashkevich, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cave is a W × H grid of rock (`#`) and open cells (`.`), W, H ≤ 500,
with the surface above the top row. Water fills every open cell that
has a path to the surface through open cells, moving between cells
with a common side, that never goes down. A caver stands in cell (X, Y),
counted from the left and from the bottom, and can swim at most
D ≤ 1000 cells under water before needing air. Air remains in the open
cells that the water does not reach. Can the caver get out alone? While
the cave is dry, a way out is guaranteed.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W, H, X, Y and D, then H rows of the cave from the top.

## Output

`Can be rescued by himself` or `Rescue operation required`.

## Examples

### Example 1

Input:

```
9 4 8 2 5
##..##..#
##.#.####
##......#
#########
```

Output:

```
Rescue operation required
```

### Example 2

Input:

```
9 4 8 2 6
##..##..#
##.#.####
##......#
#########
```

Output:

```
Can be rescued by himself
```

## Solution

First find the water. A cell is flooded if it can reach the surface
going up, left or right only, so search backwards from the open cells
of the top row, going down, left and right.

Then the caver. The two examples fix how swimming is counted: a stretch
under water lasts from the last breath to the next one, and every move
on it counts, including the move into an air cell or out through the
top row. In the example, the stretch from the air pocket to the surface
takes 6 moves, so D = 5 fails and D = 6 succeeds.

Give every cell a label: the fewest moves made under water since the
last breath when standing there, over all ways in.

- moving into flooded water adds 1 to the label;
- moving into air resets it to 0, which a swimmer may do only with a
  move to spare, label + 1 ≤ D (from air into air is free);
- leaving through the top row needs label + 1 ≤ D.

A smaller label is never worse, so only the smallest label per cell
matters. Labels run from 0 to D, so buckets indexed by label serve as
the priority queue. When a label 0 appears in an air pocket while
larger labels are being processed, the scan simply goes back to bucket
0. `O(W · H · k)`, where k is how often a cell's label drops, small in
practice.

Pitfalls:

- an air pocket is a cell above water with no way up, like the cell
  above the corridor in the example, and it lets the caver breathe
  (tests 01–04);
- the caver may start in an air pocket or in water, and both start with
  a label of 0 (tests 03 and 06);
- the surface move itself counts: a flooded shaft of k cells needs
  D ≥ k (tests 08 and 09).

The answers were compared with a breadth-first search over all states
(cell, moves since the last breath) on 700 small random caves.

## Language notes

- Python surrounds the cave with a frame of rock, so that no move needs
  a bounds check, and builds the grid with `bytes.translate`.
- Python runs under PyPy: one of the judge's tests takes just over 1 s
  with CPython, while ours take under 0.2 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1315_bfs.cpp](1315_bfs.cpp) | G++ 13.2 x64 | bfs | O(W * H * k) | AC | 0.125 s | 3256 KB |
| [1315_bfs.go](1315_bfs.go) | Go 1.14 x64 | bfs | O(W * H * k) | AC | 0.171 s | 10180 KB |
| [1315_bfs.java](1315_bfs.java) | Java 1.8 | bfs | O(W * H * k) | AC | 0.328 s | 8736 KB |
| [1315_bfs.py](1315_bfs.py) | PyPy 3.10 x64 | bfs | O(W * H * k) | AC | 0.687 s | 9596 KB |
| [1315_bfs.rs](1315_bfs.rs) | Rust 1.75 x64 | bfs | O(W * H * k) | AC | 0.218 s | 6708 KB |
