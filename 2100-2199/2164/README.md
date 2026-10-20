# 2164. Counting substrings that are finished connect-four games

[Timus 2164](https://acm.timus.ru/problem.aspx?space=1&num=2164) · difficulty 1593 · simulation

Original problem by Vadim Barinov, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Connect four is played on 7 rows and 9 columns; a move names a column,
and a move into a full column is a pass that still spends one of the 63
chips. A game ends when the last mover has four in a row, column or
diagonal (a win), or when all 63 chips are spent: a draw if the board is
full, an open end otherwise. In a string of moves, count the substrings
that are complete won games and those that are complete drawn games.
The limits are 1 second and 256 MB.

## Input

The string of digits 1 … 9, of length N, 1 ≤ N ≤ 10⁴.

## Output

The number of won games and the number of drawn games.

## Examples

### Example 1

Input:

```
34353637
```

Output:

```
2 0
```

## Solution

A start position determines the whole game: play the moves from there
until it ends. If a move wins, the substring up to that move is a won
game and no longer substring from this start is a game at all. If 63
moves pass without a win, the substring of length 63 is a draw exactly
when no move was a pass. So every start is simulated for at most 63
moves, N · 63 moves in total.

Each player's chips are a 63-bit board, one bit per cell, column by
column. A move sets one bit, and four in a row along a direction with
bit shift s exists when b & (b ≫ s) & (b ≫ 2s) & (b ≫ 3s) has a set bit,
computed as two ANDs of shifted pairs. A mask of the cells where a line
of four can start keeps the shifts from wrapping around a column edge.
Wins are checked only from the seventh move on, when four chips of one
colour exist.

In the example "3435363" wins in column 3 and "4353637" wins in the
bottom row; no other substring is a finished game.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2164_simulation.cpp](2164_simulation.cpp) | G++ 13.2 x64 | simulation | O(63 N) | AC | 0.031 s | 452 KB |
| [2164_simulation.go](2164_simulation.go) | Go 1.14 x64 | simulation | O(63 N) | AC | 0.031 s | 1152 KB |
| [2164_simulation.java](2164_simulation.java) | Java 1.8 | simulation | O(63 N) | AC | 0.109 s | 1424 KB |
| [2164_simulation.py](2164_simulation.py) | PyPy 3.10 x64 | simulation | O(63 N) | AC | 0.187 s | 2888 KB |
| [2164_simulation.rs](2164_simulation.rs) | Rust 1.75 x64 | simulation | O(63 N) | AC | 0.046 s | 244 KB |
