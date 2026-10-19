# 2104. Folding a two-sided strip until it shows one colour

[Timus 2104](https://acm.timus.ru/problem.aspx?space=1&num=2104) · difficulty 375 · games

Original problem by Nikita Sivukhin, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 1 × n strip has colours A and B on its squares, on both sides. Alice
and Bob take turns, Alice first; a turn folds the strip in half (only
when its length is even), inwards or outwards. If after a turn the strip
shows a single colour on both sides, A means Alice wins and B means Bob
wins, whoever made the fold. If the player to move cannot fold and
nobody has won, it is a draw. Who wins with best play? The limits are
2 seconds and 64 MB.

## Input

n ≤ 5·10⁵, then the two sides as strings of A and B.

## Output

`Alice`, `Bob` or `Draw`.

## Examples

### Example 1

Input:

```
4
BBAA
BABB
```

Output:

```
Bob
```

### Example 2

Input:

```
3
AAA
BBB
```

Output:

```
Draw
```

### Example 3

Input:

```
2
AA
BB
```

Output:

```
Alice
```

## Solution

A fold puts the right half on top of or below the left half. One way the
outside faces are the left half of the top side and the reversed right
half of the top side; the other way they are the reversed right half of
the bottom side and the left half of the bottom side. The faces that end
up inside are never seen again. So every position has at most two moves,
each halving the length, and the game has at most log₂ n ≈ 19 levels.

A plain minimax over this tree is enough: after each fold check whether
the new strip shows one colour; otherwise recurse with the other player
to move, and an odd length is a draw. Each player takes the result that
is best for their own side, stopping as soon as a move wins. Level k has
at most 2ᵏ strips of length n / 2ᵏ, so the work is O(n log n).

In the first example both folds of Alice leave strips that Bob folds
into B/B, so Bob wins.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2104_games.cpp](2104_games.cpp) | G++ 13.2 x64 | games | O(n log n) | AC | 0.031 s | 3832 KB |
| [2104_games.go](2104_games.go) | Go 1.14 x64 | games | O(n log n) | AC | 0.046 s | 8076 KB |
| [2104_games.java](2104_games.java) | Java 1.8 | games | O(n log n) | AC | 0.125 s | 14932 KB |
| [2104_games.py](2104_games.py) | Python 3.12 x64 | games | O(n log n) | AC | 0.265 s | 3968 KB |
| [2104_games.rs](2104_games.rs) | Rust 1.75 x64 | games | O(n log n) | AC | 0.015 s | 2132 KB |
