# 1639. Chocolate 2

[Timus 1639](https://acm.timus.ru/problem.aspx?space=1&num=1639) · difficulty 32 · games

Original problem by Alexander Pronchenkov (prepared by Ivan Burmistrov), from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players take turns breaking an m × n chocolate bar: a move takes any
piece and breaks it into two along the grooves. The player who cannot
move, because only 1 × 1 pieces remain, loses. Should Karlsson move
first or second to win for sure?

## Input

Two integers m and n (1 ≤ m, n ≤ 50).

## Output

`[:=[first]` if moving first wins, otherwise `[second]=:]`.

## Examples

### Example 1

Input:

```
2 4
```

Output:

```
[:=[first]
```

### Example 2

Input:

```
1 3
```

Output:

```
[second]=:]
```

## Solution

Every move turns one piece into two, so it raises the number of pieces
by exactly one. The game starts with one piece and ends with m · n, so
it always lasts m · n − 1 moves, whatever the players do. The first
player makes the last move, and wins, exactly when m · n − 1 is odd,
that is, when m · n is even. `O(1)`.

Pitfalls:

- no strategy matters, so there is nothing to search;
- a 1 × 1 bar allows no move, so the first player loses at once
  (test 03).

## Optimized solutions

The optimized Java solution parses the two numbers by hand with
`System.in.read` instead of using `Scanner`: 372 KB instead of 1608 KB,
with the same time. It tests the parity of `m · n` directly, which is
the opposite of the parity of the number of moves `m · n − 1`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1639_games.cpp](1639_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 120 KB | 11288461 |
| [1639_games.go](1639_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1132 KB | 11288462 |
| [1639_games.java](1639_games.java) | Java 1.8 | games | O(1) | AC | 0.125 s | 1608 KB | 11288464 |
| [1639_games.py](1639_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 412 KB | 11288463 |
| [1639_games.rs](1639_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 236 KB | 11303478 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1639_games_optimized.java](1639_games_optimized.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 372 KB | 11303628 |
