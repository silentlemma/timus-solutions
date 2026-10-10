# 1195. Who wins an unfinished game of noughts and crosses

[Timus 1195](https://acm.timus.ru/problem.aspx?space=1&num=1195) · difficulty 260 · games

Original problem by Leonid Volkov and Oleg Kats, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 3×3 noughts-and-crosses board has exactly three crosses and three
noughts and no complete line yet; crosses moved first, so they move now.
Find the result with best play on both sides.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Three lines of `X`, `O` and `#` for an empty cell.

## Output

`Crosses win`, `Ouths win` or `Draw`.

## Examples

### Example 1

Input:

```
XXO
#X#
#OO
```

Output:

```
Ouths win
```

### Example 2

Input:

```
O#O
#X#
XOX
```

Output:

```
Draw
```

### Example 3

Input:

```
XX#
XOO
#O#
```

Output:

```
Crosses win
```

## Solution

Only three cells are empty, so the whole game tree has at most
`3·2·1` lines of play. A plain minimax decides it: the side to move tries
every empty cell; a move that completes a line wins, otherwise the result
is the opposite of the opponent's best result from there; a full board is
a draw. `O(1)`.

Pitfalls:

- the side to move is always crosses, because both sides have made three
  moves;
- the check for a completed line must look at the mark just placed, not
  at both marks;
- the answer for noughts is spelled `Ouths win`.

The answers were compared with a separately written solution on all 1372
boards with three crosses, three noughts and no complete line.

## Language notes

- All languages run the same recursive search on a 9-cell array.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1195_games.cpp](1195_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 352 KB |
| [1195_games.go](1195_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1084 KB |
| [1195_games.java](1195_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 1544 KB |
| [1195_games.py](1195_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 528 KB |
| [1195_games.rs](1195_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 212 KB |
