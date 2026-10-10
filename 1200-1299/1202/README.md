# 1202. The shortest walk through a chain of rectangles

[Timus 1202](https://acm.timus.ru/problem.aspx?space=1&num=1202) · difficulty 442 · greedy

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to `10⁵` rectangles on squared paper form a chain from left to right:
the first has its lower left corner at `(0, 0)`, each one starts where
the previous one ends horizontally, and every side is from 2 to 100
cells long. Where two neighbours touch, their shared border disappears. A
traveller walks along grid lines from `(1, 1)` to one cell inside the
upper right corner of the last rectangle, may not walk along any
rectangle border, and can only pass from one rectangle to the next
through the vanished part of their border. Find the length of the
shortest walk, or `-1` if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n`, then each rectangle as `x1 y1 x2 y2`, lower left and upper right
corners.

## Output

The length of the shortest walk, or `-1`.

## Examples

### Example 1

Input:

```
2
0 0 3 5
3 1 5 7
```

Output:

```
8
```

## Solution

The walk has to get from `x = 1` to `x = x2 − 1` of the last rectangle,
and it can always do so without ever stepping left, so the horizontal
part is fixed. Between rectangles `i` and `i + 1` the walk crosses the
line `x = x2ᵢ` at a whole height strictly inside both rectangles, that is
in `[max(y1) + 1, min(y2) − 1]`; if that range is empty there is no walk.
Inside a rectangle any change of height is possible on an inner vertical
line, so the vertical length is the total change of height between the
start, the chosen crossing heights and the goal.

To minimise that, move only when forced: keep the current height and, at
each border, clamp it into the allowed range. By induction the cheapest
way to stand at height `h` after border `i` costs the greedy total so far
plus `|h − greedy height|`, so the greedy choice is never worse. `O(n)`.

Pitfalls:

- rectangles that touch along fewer than two units, or only at a corner,
  leave no crossing at all;
- rectangles may extend below zero;
- with a single rectangle the answer is just the distance from `(1, 1)`
  to the goal, and 0 for a 2×2 rectangle.

The answers were compared with a separately written solution on 400
random chains and on every test.

## Language notes

- Go and Java read the input with hand-written byte readers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1202_greedy.cpp](1202_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.234 s | 132 KB |
| [1202_greedy.go](1202_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 1088 KB |
| [1202_greedy.java](1202_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 540 KB |
| [1202_greedy.py](1202_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.328 s | 39384 KB |
| [1202_greedy.rs](1202_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 8696 KB |
