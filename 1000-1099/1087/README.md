# 1087. A take-away game where taking the last stone loses

[Timus 1087](https://acm.timus.ru/problem.aspx?space=1&num=1087) · difficulty 277 · games

Original problem by Anton Botov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pile has `n` stones (`1 ≤ n ≤ 10000`). Two players take turns removing
`k₁`, `k₂`, …, or `kₘ` stones (`1 ≤ m ≤ 50`, `1 ≤ kᵢ ≤ n`); a move is
always possible. The player who takes the last stone loses. Print 1 if
the first player wins with best play, otherwise 2.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `m`, then `k₁ … kₘ`.

## Output

1 or 2.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
17 3
1 3 4
```

Output:

```
2
```

## Solution

Let `win[x]` say whether the player to move with `x` stones left wins.
With 0 stones left, the other player has just taken the last stone, so
`win[0]` is true. For `x ≥ 1`, the player wins if some allowed move
`k ≤ x` leads to a losing position: `win[x] = OR over k of not win[x − k]`.
Fill the table from 1 to `n`. `O(n·m)`.

Pitfalls:

- this is the misère rule: emptying the pile is a loss, so a move that
  takes all the remaining stones is never a winning one, and `win[0]` is
  true, not false as in the usual game;
- move sizes may repeat, and a move larger than the pile is not allowed.

The answers were checked against a memoised game search driven by an
explicit stack from `n` downwards.

## Language notes

- Python removes repeated move sizes with `set` before the loop.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1087_games.cpp](1087_games.cpp) | G++ 13.2 x64 | games | O(n·m) | AC | 0.015 s | 204 KB |
| [1087_games.go](1087_games.go) | Go 1.14 x64 | games | O(n·m) | AC | 0.031 s | 1092 KB |
| [1087_games.java](1087_games.java) | Java 1.8 | games | O(n·m) | AC | 0.109 s | 1652 KB |
| [1087_games.py](1087_games.py) | Python 3.12 x64 | games | O(n·m) | AC | 0.093 s | 568 KB |
| [1087_games.rs](1087_games.rs) | Rust 1.75 x64 | games | O(n·m) | AC | 0.015 s | 228 KB |
