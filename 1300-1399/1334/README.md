# 1334. Checkers

[Timus 1334](https://acm.timus.ru/problem.aspx?space=1&num=1334) · difficulty 540 · simulation

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players take turns putting checkers of their colors on the dark
squares of a chessboard, white first; there are 32 moves. A player
loses with the move after which some checker can be captured: a checker
A can be captured by a checker B of the other color that stands next to
it on a diagonal, if the square right behind A on that diagonal is free.
Print the number of the losing move, or `Draw`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

32 lines with squares in chess notation, like `a1`: white's moves on
the odd lines and black's on the even ones.

## Output

The number of the losing move, or `Draw`.

## Examples

### Example 1

Input:

```
a1
a3
a5
a7
b2
b4
b6
b8
c1
c3
c5
c7
d2
d4
d6
d8
e1
e3
e5
e7
f2
f4
f6
f8
g1
g3
g5
g7
h2
h4
h6
h8
```

Output:

```
5
```

## Solution

Put the checkers on the board one by one. After each move, look at every
checker and each of the four diagonals: if the neighbor there has the
other color and the square behind it is on the board and free, a
capture is possible and the move just made loses. A capture by either
player counts, including one by the player who just moved, and so does
a capture backwards. At most 32 · 32 · 4 checks.

Pitfalls:

- a jump that would land off the board is not a capture, as with a
  checker in a corner (test 03);
- the player who moves can lose by giving the capture to themselves
  (test 05);
- move 32 can never lose: by then every dark square is taken and there
  is nowhere to land, so move 31 is the last one that can (test 07).

## Language notes

- All five solutions check the whole board after every move.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1334_simulation.cpp](1334_simulation.cpp) | G++ 13.2 x64 | simulation | O(1) | AC | 0.015 s | 132 KB |
| [1334_simulation.go](1334_simulation.go) | Go 1.14 x64 | simulation | O(1) | AC | 0.015 s | 1036 KB |
| [1334_simulation.java](1334_simulation.java) | Java 1.8 | simulation | O(1) | AC | 0.140 s | 1596 KB |
| [1334_simulation.py](1334_simulation.py) | Python 3.12 x64 | simulation | O(1) | AC | 0.078 s | 536 KB |
| [1334_simulation.rs](1334_simulation.rs) | Rust 1.75 x64 | simulation | O(1) | AC | 0.046 s | 208 KB |
