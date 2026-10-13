# 1398. Bishop and Pawn

[Timus 1398](https://acm.timus.ru/problem.aspx?space=1&num=1398) · difficulty 856 · games

Original problem by Magaz Asanov, from the trial round of the Ural Championship 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A white bishop and a black pawn on rank 2 to 7 stand on a chessboard
and move by the usual rules, white first. Black wins if the pawn
becomes a queen that the bishop cannot take on the very next move. The
game is a draw if black is to move and the pawn cannot move. White wins
in every other case. Print the result of best play.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The bishop's square, then the pawn's square, in chess notation.

## Output

WHITE, DRAW or BLACK.

## Examples

### Example 1

Input:

```
a1
c2
```

Output:

```
WHITE
```

## Solution

The pawn moves forward on every black turn, so a game lasts at most a
dozen moves, and a minimax over (bishop, pawn, side to move) with a memo
covers all 64·64·2 states. White tries every bishop move along the four
diagonals up to the edge or the pawn, and taking the pawn wins at once.
Black chooses the worst result for white among:

- a step forward, or two steps from rank 7, onto empty squares;
- reaching rank 1: white wins only if the bishop sees the queen;
- taking the bishop diagonally, after which nothing stops the pawn.

With no move at all the pawn is blocked and the game is a draw.
`O(1)`, with at most 8 192 states.

Pitfalls:

- the pawn moves down the board, towards rank 1;
- of all 3 024 starting positions only four are draws: a2 b2, b1 a3,
  g1 h3 and h2 g2 (tests 02 to 05);
- black wins only from rank 2, where the queen comes up on a square of
  the other colour or out of reach (tests 06 and 07);
- the double step and the question whether taking the bishop counts as
  a loss for white never change a result, since white never has to give
  the bishop away.

Two of the solutions were compared on all 3 024 starting positions, and
the four draws match the count given on the forum.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1398_games.cpp](1398_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 152 KB |
| [1398_games.go](1398_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1148 KB |
| [1398_games.java](1398_games.java) | Java 1.8 | games | O(1) | AC | 0.125 s | 1632 KB |
| [1398_games.py](1398_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.109 s | 684 KB |
| [1398_games.rs](1398_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 432 KB |
