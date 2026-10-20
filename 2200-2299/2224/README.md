# 2224. Two players racing on a 2 × N strip without revisiting cells

[Timus 2224](https://acm.timus.ru/problem.aspx?space=1&num=2224) · difficulty 1477 · games

Original problem by Vadim Barinov, from the Ural Championship 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players stand on different cells of a 2 × N board and move in
turns, Blue first, each time to a side-adjacent cell that nobody has
visited and that is not occupied. A player who cannot move loses. Who
wins with best play? The limits are 0.5 seconds and 256 MB.

## Input

N, 3 ≤ N ≤ 10⁹, then Blue's cell and Red's cell.

## Output

Blue or Red.

## Examples

### Example 1

Input:

```
3
1 2
2 3
```

Output:

```
Blue
```

### Example 2

Input:

```
3
1 1
2 1
```

Output:

```
Red
```

## Solution

Reflect the board so Blue is not to the right of Red. Let left be the
number of columns left of Blue, right the number of columns right of
Red, and gap the distance between their columns. A tail of k free
columns behind a player is worth up to 2k moves walked in a snake, so
the game is about who keeps the longer tail, and the cells between the
players decide who has to give way first.

- **Same row.** Each player can walk away into the own tail at once,
  while the middle part is shared. Blue wins with the longer tail, and
  with equal tails exactly when the gap is even, because then Blue is
  the one who reaches the middle first and takes the extra cells.
- **Different rows.** With gap 0 the players stand in one column and
  Red can answer every move symmetrically, so Red wins; equal tails also
  let Red mirror Blue, so Red wins. With gap 1 Blue steps diagonally in
  front of Red and cuts Red's row, and Blue wins. When the tails differ
  by exactly one column, the race through the middle decides it, and
  Blue wins exactly when the gap is odd. Otherwise the longer tail wins.

These rules were checked against an exhaustive minimax over every
starting position on all boards from 2 × 3 to 2 × 8.

In the first example Blue is one column from Red in the other row and
wins; in the second the players share a column and Red wins.

This takes O(1).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2224_games.cpp](2224_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.031 s | 180 KB |
| [2224_games.go](2224_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 892 KB |
| [2224_games.java](2224_games.java) | Java 1.8 | games | O(1) | AC | 0.187 s | 1388 KB |
| [2224_games.py](2224_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.093 s | 248 KB |
| [2224_games.rs](2224_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 16 KB |
