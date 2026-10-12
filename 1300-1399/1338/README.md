# 1338. Automobiles

[Timus 1338](https://acm.timus.ru/problem.aspx?space=1&num=1338) · difficulty 1718 · bfs

Original problem by Alexander Klepinin, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A town plan of W × H cells (1 ≤ W, H ≤ 500) has buildings (`.`), road
(`#`) and control points (`o`) that are also road; road cells connect
through common sides. Control points are numbered from the bottom row up
and from left to right within a row. In each of up to 20 experiments a
target point T is chosen, and from every other control point one car
drives to T along a shortest route. Where several shortest routes go on,
a car prefers south, then north, then west, then east. For each
experiment print how many cars arrive at T from the north, south, east
and west.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

W and H, then H lines of the plan, then M and M target numbers.

## Output

For each experiment a line
`Experiment #N: North: Rn, South: Rs, East: Re, West: Rw`.

## Examples

### Example 1

Input:

```
10 5
..####....
..o..o....
..####.#o.
......##..
.o#####...
1
4
```

Output:

```
Experiment #1: North: 0, South: 1, East: 0, West: 0
```

## Solution

A breadth-first search from T gives each reachable road cell its distance
to T. A car on a cell at distance d > 0 moves to the first neighbor at
distance d − 1 in the order south, north, west, east. So each such cell has one
fixed next cell, and its car arrives at T from the same side as the car
of that next cell. Going through the cells in the order the search
found them, every next cell is already settled, and each cell copies
its side. A cell next to T arrives from the side it stands on: stepping
north onto T means arriving from the south. Counting the sides of all
control points other than T that T can reach gives the answer.
`O((M + 1) · W · H)`.

Pitfalls:

- the numbering starts at the bottom row, not the top (test 04);
- cars from points disconnected from T do not arrive (test 04);
- the preferred turn decides between routes of equal length at every
  step, not only at the start (test 15);
- simulating each car separately takes as long as its route for every
  one of up to 250 000 points, which is far too slow.

The answers were compared with driving every car step by step on 500
random small plans.

## Language notes

- CPython needs about 2.5 seconds on a full plan with 20 experiments,
  too close to the 3-second limit, so the Python solution is submitted
  under PyPy 3.10, where it takes about 0.4 seconds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1338_bfs.cpp](1338_bfs.cpp) | G++ 13.2 x64 | bfs | O((M+1)·W·H) | AC | 0.093 s | 5048 KB |
| [1338_bfs.go](1338_bfs.go) | Go 1.14 x64 | bfs | O((M+1)·W·H) | AC | 0.218 s | 30164 KB |
| [1338_bfs.java](1338_bfs.java) | Java 1.8 | bfs | O((M+1)·W·H) | AC | 0.218 s | 5960 KB |
| [1338_bfs.py](1338_bfs.py) | PyPy 3.10 x64 | bfs | O((M+1)·W·H) | AC | 1.234 s | 31900 KB |
| [1338_bfs.rs](1338_bfs.rs) | Rust 1.75 x64 | bfs | O((M+1)·W·H) | AC | 0.187 s | 9900 KB |
