# 1657. Cube Snake

[Timus 1657](https://acm.timus.ru/problem.aspx?space=1&num=1657) · difficulty 1538 · backtracking

Original problem by Stanislav Vasilyev (prepared by Sergey Pupyrev), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A snake puzzle is a string of 27 small cubes. In a straight cube (`F`)
the string goes through opposite faces, in a turning cube (`T`) through
adjacent ones; the end cubes count as straight. Fold the snake into a
3 × 3 × 3 cube and print each cube's position relative to the previous
one, or report that it cannot be done.

## Input

27 letters `F` and `T`.

## Output

26 letters from `RLFBUD` (right, left, forward, back, up, down), or
`IMPOSSIBLE`. Any valid folding is accepted.

## Examples

### Example 1

Input:

```
FFTTTFTTFTTTFTFTTTTFTFTFTFF
```

Output:

```
UURDFFRBBUFLLDDRBRFFLLUURR
```

### Example 2

Input:

```
FFTFTFTFTTTTFFFTTTFTTFTTTFF
```

Output:

```
IMPOSSIBLE
```

## Solution

Folding is a path through all 27 cells of the cube: after a straight
cube the next step keeps the direction, after a turning cube it takes
one of the four directions across. A depth-first search tries these in
turn, never entering a used cell, and gives up on a branch as soon as
the free cells split into more than one piece, since the rest of the
snake could not reach all of them.

Two observations make the search small enough for Python. The cells
take two colours like a chessboard, 14 of one and 13 of the other, and
the snake alternates colours, so it must start on the larger colour: a
corner or the centre of a face. And the cube's symmetries make all
corners alike and all first steps from a corner alike, while from a face
centre there are only two kinds of step, into the centre or along the
face. So the search starts from just three first moves.

Pitfalls:

- the first and last cubes are straight by definition, whatever the
  input says;
- an all-straight snake is a rod of 27 and never folds (test 03);
- many foldings exist, so a checker replays the moves.

The answers agree with an independent accepted implementation on Yes or
No, and pass the checker, on 120 snakes, including random ones and
snakes of random foldings with one cube changed.

Complexity: `O(4^C)` for C = 27 cells, with at most four directions
after each turning cube.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1657_backtracking.cpp](1657_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(4^C) | AC | 0.046 s | 372 KB |
| [1657_backtracking.go](1657_backtracking.go) | Go 1.14 x64 | backtracking | O(4^C) | AC | 0.046 s | 5852 KB |
| [1657_backtracking.java](1657_backtracking.java) | Java 1.8 | backtracking | O(4^C) | AC | 0.125 s | 6092 KB |
| [1657_backtracking.py](1657_backtracking.py) | Python 3.12 x64 | backtracking | O(4^C) | AC | 0.796 s | 776 KB |
| [1657_backtracking.rs](1657_backtracking.rs) | Rust 1.75 x64 | backtracking | O(4^C) | AC | 0.062 s | 220 KB |
