# 1465. Pawn Game

[Timus 1465](https://acm.timus.ru/problem.aspx?space=1&num=1465) · difficulty 489 · games

Original problem by Alexander Toropov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On a board of 3 × N squares (1 ≤ N ≤ 10⁹) the first rank is filled with
white pawns and the third with black ones; the middle rank is empty.
Pawns move and capture as in chess, capturing is compulsory, and a
player who cannot move loses. White moves first. Both play perfectly:
print "White" if White wins and "Black" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

"White" or "Black".

## Examples

### Example 1

Input:

```
3
```

Output:

```
White
```

### Example 2

Input:

```
4
```

Output:

```
Black
```

### Example 3

Input:

```
5
```

Output:

```
White
```

## Solution

This is Dawson's chess. A pawn pushed into the middle rank is attacked by
the enemy pawns on the neighbouring files, and the compulsory captures
that follow end with the pushed file and its neighbours dead: no pawn
there can move again. So a move on file i of a row of n live files
leaves two independent rows of i − 2 and n − i − 1 files; a move next to
an edge kills two files, and a lone file dies by itself. This is the
octal game 0.137: take one file only if it is the whole row, take two
leaving at most one row, or take three leaving up to two rows.

The first player wins exactly when the Grundy value of n is not zero,
where the value of a row is the smallest number not among the values of
its moves, and two rows combine by xor. The values are computed up to
200 in O(200²). From n = 52 on they repeat with period 34, and by the
periodicity theorem for octal games it is enough to check this up to
2 · 52 + 34 + 3; so a larger N is folded into the last period below 200.
`O(1)` per answer.

Pitfalls:

- a board of N = 10⁹ cannot be simulated, only folded (tests 12 to 15);
- the values settle only from n = 52 on: 14 and 48 files, or 34 and 68,
  have different winners (tests 07, 08, 17, 18);
- in C-like languages the remainder of a negative number is negative,
  so the folding must subtract in the right order.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1465_games.cpp](1465_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 172 KB |
| [1465_games.go](1465_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1144 KB |
| [1465_games.java](1465_games.java) | Java 1.8 | games | O(1) | AC | 0.140 s | 1720 KB |
| [1465_games.py](1465_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.109 s | 444 KB |
| [1465_games.rs](1465_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 440 KB |
