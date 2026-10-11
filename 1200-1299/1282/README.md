# 1282. Game tree

[Timus 1282](https://acm.timus.ru/problem.aspx?space=1&num=1282) · difficulty 337 · games

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A game for two players is given by its tree of N ≤ 1000 nodes rooted at
node 1. The players move in turn, the first one at the root, by going
down to a child. Every leaf holds the result: +1 if the first player
wins, −1 if the second does, 0 for a draw. Which result do both players
reach with best play?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then for nodes 2 to N either `N parent` for an inner node or
`L parent result` for a leaf.

## Output

`+1`, `-1` or `0`.

## Examples

### Example 1

Input:

```
7
N 1
N 1
L 2 -1
L 2 +1
L 3 +1
L 3 +1
```

Output:

```
+1
```

### Example 2

Input:

```
7
N 1
N 1
L 2 -1
L 2 +1
L 3 +1
L 3 0
```

Output:

```
0
```

### Example 3

Input:

```
18
N 1
N 1
N 2
L 2 +1
N 3
L 3 +1
L 3 +1
L 4 -1
L 4 +1
N 4
N 6
L 6 -1
L 6 -1
L 11 -1
L 11 +1
L 12 +1
L 12 -1
```

Output:

```
+1
```

## Solution

This is minimax. The first player moves at nodes of even depth and picks
the largest value among the children, the second player at odd depths
and picks the smallest. A node may be listed before its parent, so the
values are not computed in input order: a breadth-first pass from the
root gives every depth, and walking that order backwards visits all
children before their parent. `O(N)`.

Pitfalls:

- a parent may be listed after its child (test 05);
- a chain of 1000 nodes would make a naive recursion deep (test 06);
- results are written `+1`, with a plus sign, in the input and in the
  output.

The answers were compared with a plain recursive minimax on 149
generated trees.

## Language notes

- All languages walk the same breadth-first order backwards.
- Java strips the plus sign before parsing a result.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1282_games.cpp](1282_games.cpp) | G++ 13.2 x64 | games | O(N) | AC | 0.015 s | 240 KB |
| [1282_games.go](1282_games.go) | Go 1.14 x64 | games | O(N) | AC | 0.031 s | 1208 KB |
| [1282_games.java](1282_games.java) | Java 1.8 | games | O(N) | AC | 0.140 s | 1656 KB |
| [1282_games.py](1282_games.py) | Python 3.12 x64 | games | O(N) | AC | 0.093 s | 780 KB |
| [1282_games.rs](1282_games.rs) | Rust 1.75 x64 | games | O(N) | AC | 0.015 s | 284 KB |
