# 1878. Rubinchik's Cube

[Timus 1878](https://acm.timus.ru/problem.aspx?space=1&num=1878) · difficulty 219 · implementation

Original problem by Denis Mukhametianov, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A puzzle is made of four transparent 4 × 4 layers on a common axis.
Each layer has four coloured squares, one of each of four colours,
placed so that a quarter turn of the layer moves each of them into the
next quadrant. Each layer's four squares form an orbit under this turn,
and all layers have the same clockwise cyclic colour order, up to
rotation, as in the [original layer diagram](https://acm.timus.ru/image/get.aspx/a394d0eb-f9d5-4bc2-846a-74ef972e9e4b).
Seen from above the layers fill the 4 × 4 grid. The
puzzle is solved when every 2 × 2 quadrant has a single colour. One
move turns one layer by 90° either way. Given the view from above, find
the fewest moves that solve the puzzle.

## Input

Four lines of four colours from 1 to 4: the view from above.

## Output

The least number of moves.

## Examples

### Example 1

Input:

```
2 1 2 3
1 1 2 2
4 4 3 3
1 4 3 4
```

Output:

```
1
```

## Solution

All layers share the same cyclic colour order, so aligning their colour 1
squares also aligns every other colour. Every layer has exactly one square
of colour 1, and that square tells
the layer's orientation: its quadrant. Number the quadrants in the
order a quarter turn moves a square through them (top left, top right,
bottom right, bottom left). The puzzle is solved when all four colour 1
squares are in the same quadrant t. A layer whose square is in quadrant
p then needs min(d, 4 − d) moves, where d = (p − t) mod 4. Try all four
t and take the cheapest. `O(1)`.

In the example three colour 1 squares are in the top-left quadrant and
one in the bottom-left, a quarter turn away: one move.

Pitfalls:

- aligning colour 1 relies on the shared cyclic colour order (as in test
  01); having each colour once per layer alone is not enough;
- the solved state may have colour 1 in any quadrant: the cube may end
  up turned as a whole;
- a layer half a turn away costs two moves whichever way it turns;
- the quadrants must be numbered round the circle, not row by row,
  for the distances to be right.

The Python solution agrees with an independent breadth-first search over
physical layer turns on all 1,536 solvable boards, including every
number-to-colour assignment.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1878_implementation.cpp](1878_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB |
| [1878_implementation.go](1878_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1084 KB |
| [1878_implementation.java](1878_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1668 KB |
| [1878_implementation.py](1878_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 420 KB |
| [1878_implementation.rs](1878_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 212 KB |
