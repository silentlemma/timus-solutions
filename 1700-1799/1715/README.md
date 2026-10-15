# 1715. Another Ball Killer

[Timus 1715](https://acm.timus.ru/problem.aspx?space=1&num=1715) · difficulty 1010 · simulation

Original problem: folklore, prepared by Eugene Krokhalev, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m board is filled with balls of five colours. A move removes a
figure, a connected group of two or more balls of one colour (sharing
sides), and scores k(k − 1) for k balls. The balls above fall down, and
an emptied column makes the columns to its right shift left. A lazy
player picks a main colour and repeats: while some figure of another
colour exists, remove the largest such figure; then remove the largest
figure of the main colour, if any. Ties go to the figure holding the
lowest ball, and then the leftmost of the lowest balls. For every
colour present on the board, print the score this player gets with
that main colour.

## Input

n and m (1 ≤ n, m ≤ 50), then n rows from top to bottom of the letters
B, G, R, W and Y.

## Output

For each colour present, in the order B, G, R, W, Y, a line
"colour: score".

## Examples

### Example 1

Input:

```
3 6
WWWGBG
WBGGGB
GGGGBB
```

Output:

```
B: 74
G: 92
W: 74
```

## Solution

Play the game as described. A search finds all figures of the wanted
kind (main colour or not) by breadth-first search. For each figure it
keeps its size and its lowest ball, taking the leftmost one on the
lowest row, and picks the best by size, then by that ball's row, then
by its column. Removing a figure empties its cells. Each column is then
packed down, and the nonempty columns are packed to the left.

Every move removes at least two balls, so a game has at most nm / 2
moves. Each move costs one or two searches over the board, so a game
takes `O((nm)²)` time, a few million cell visits for 50 × 50, and
up to five games are played.

Pitfalls:

- the tie-break is about one ball: among the largest figures take the
  lowest ball of all, and if a row has several, the leftmost. It is not
  the figure whose leftmost ball is lowest;
- after every removal the non-main colours are tried again before the
  next main move, as falling balls can create new figures;
- a board without figures still prints 0 for every colour present
  (tests 02 and 03);
- the Python solution is sent to PyPy: CPython needs about 2.5 s on a
  random 50 × 50 board.

The scores match an independent accepted implementation on 300 small
random boards and on large boards with two and five colours.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1715_simulation.cpp](1715_simulation.cpp) | G++ 13.2 x64 | simulation | O((nm)²) per colour | AC | 0.531 s | 560 KB |
| [1715_simulation.go](1715_simulation.go) | Go 1.14 x64 | simulation | O((nm)²) per colour | AC | 0.468 s | 7032 KB |
| [1715_simulation.java](1715_simulation.java) | Java 1.8 | simulation | O((nm)²) per colour | AC | 0.453 s | 5256 KB |
| [1715_simulation.py](1715_simulation.py) | PyPy 3.10 x64 | simulation | O((nm)²) per colour | AC | 1.812 s | 9088 KB |
| [1715_simulation.rs](1715_simulation.rs) | Rust 1.75 x64 | simulation | O((nm)²) per colour | AC | 0.906 s | 368 KB |
