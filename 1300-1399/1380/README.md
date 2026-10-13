# 1380. Ostap's Chess

[Timus 1380](https://acm.timus.ru/problem.aspx?space=1&num=1380) · difficulty 4157 · implementation

Original problem by Ivan Popelyshev, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a chess position, which need not make sense, the side to move and
up to 60 moves, check every move. The pieces move as in chess, but
there is no castling, no en passant and no promotion. A move is legal
if it moves one piece of the side to move as that piece may move and
leaves no king of that side attacked. After each move print
`Incorrect` if it is illegal, else `Mate`, `Draw` (stalemate), `Check`
or `Correct` for the side now to move. Stop after an illegal move, a
mate or a draw, then print an empty line and the board.

Time limit: 1 second. Memory limit: 64 MB.

## Input

64 numbers, rank 8 first: 0 for an empty square, 1 to 6 for a white
pawn, knight, bishop, rook, queen or king, negative for black. Then the
number of moves P, `White` or `Black`, and P moves like `e2-e4`.

## Output

One word per move, then an empty line and the board in the input
format.

## Examples

### Example 1

Input:

```
-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 2 3 5 6 3 2 4
2
White
e2-e4
e7-e4
```

Output:

```
Correct
Incorrect

-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 0 1 1 1
4 2 3 5 6 3 2 4
```

### Example 2

Input:

```
-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 2 3 5 6 3 2 4
8
White
e2-e4
e7-e5
d1-f3
h7-h6
f1-c4
g7-g6
f3-f7
e8-f7
```

Output:

```
Correct
Correct
Correct
Correct
Correct
Correct
Mate

-4 -2 -3 -5 -6 -3 -2 -4
-1 -1 -1 -1 0 5 0 0
0 0 0 0 0 0 -1 -1
0 0 0 0 -1 0 0 0
0 0 3 0 1 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 0 1 1 1
4 2 3 0 6 0 2 4
```

### Example 3

Input:

```
0 0 0 0 0 6 0 -6
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1
White
h6-a6
```

Output:

```
Correct

0 0 0 0 0 6 0 -6
0 0 0 0 0 0 0 0
5 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

## Solution

Simulate the game on an 8 × 8 array:

- a piece reaches a square if the square is not its own colour's and
  the move fits: a knight's L, a king's single step, a sliding piece's
  line with every square between empty, a pawn's step forward onto an
  empty square, two steps from its second rank over an empty square,
  or a diagonal step forward onto an enemy piece;
- a side is in check if some enemy piece reaches some king of that
  side;
- a move is legal if the piece is of the side to move, reaches the
  target, and after making the move no king of that side is in check;
  otherwise it is undone;
- after a legal move the other side is looked at: it has a move if any
  of its pieces has a legal move to any square. No move and in check is
  mate, no move otherwise a draw.

At most 64 · 64 moves are tried per position, each checked against at
most 64 attackers per king: tiny. `O(P · 64³)`.

The statement leaves some cases open; the judge's tests follow these
rules, as found on the problem's discussion board:

- the board is printed after the last move even when every move was
  correct (example 3);
- a pawn steps two squares from its second rank wherever it came from,
  but not from its first rank (tests 04 and 05);
- a king may be taken; a side without a king is never in check, and
  with no other piece it has no move: a draw (test 06);
- a side can have several kings, and a move must leave all of them safe
  (tests 10 to 12).

## Language notes

- All five solutions try moves in place and undo them.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1380_implementation.cpp](1380_implementation.cpp) | G++ 13.2 x64 | implementation | O(P·64³) | AC | 0.031 s | 396 KB |
| [1380_implementation.go](1380_implementation.go) | Go 1.14 x64 | implementation | O(P·64³) | AC | 0.015 s | 1128 KB |
| [1380_implementation.java](1380_implementation.java) | Java 1.8 | implementation | O(P·64³) | AC | 0.125 s | 1736 KB |
| [1380_implementation.py](1380_implementation.py) | Python 3.12 x64 | implementation | O(P·64³) | AC | 0.078 s | 1092 KB |
| [1380_implementation.rs](1380_implementation.rs) | Rust 1.75 x64 | implementation | O(P·64³) | AC | 0.046 s | 240 KB |
