# 1216. Two pawns and a king: can White promote?

[Timus 1216](https://acm.timus.ru/problem.aspx?space=1&num=1216) · difficulty 2043 · games

Original problem by Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On an `N × N` board, `6 ≤ N ≤ 26`, there are a white pawn, a black pawn
and the black king, and no white king. The usual chess rules apply:
White moves first, pawns may step two squares from their starting rows,
the black pawn may take the white pawn en passant, the black king may
not stand where the white pawn attacks it, and a black pawn reaching the
first row becomes a queen, rook, bishop or knight as Black likes. White
wins by reaching the last row with the pawn; in every other case,
including a position where White cannot move, Black wins. Decide who
wins.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the squares of the white pawn, the black pawn and the black
king, such as `h5`.

## Output

`WHITE WINS` or `BLACK WINS`.

## Examples

### Example 1

Input:

```
10
h5 i5 b3
```

Output:

```
WHITE WINS
```

### Example 2

Input:

```
8
d5 h6 b6
```

Output:

```
BLACK WINS
```

## Solution

Search the game tree with memory. Every White move pushes the white pawn
at least one row forward, so no position can repeat and the search always
ends; a position with White to move is stored with its result.

White, to move, has at most four choices: one step forward, two from the
starting row, or a capture on either side. A move that reaches the last
row wins at once. A double step next to a black pawn on the same row is
lost to the capture en passant and is skipped.

Black, to move, first looks for a capture: the king next to the white
pawn, the black pawn diagonally in front of it, or a promoted piece that
reaches it along a free line. Any of these wins for Black. Otherwise
Black tries every king step to a square the pawn does not attack, every
pawn step (with the four promotions on the first row and the double step
from the starting row) and every move of a promoted piece; White wins
only if it wins after all of them, and a Black side with no move at all
is a Black win under the rules. The positions reached in practice number
in the tens of thousands.

Pitfalls:

- both pawns may take a double step from their starting rows, but only
  the black pawn may capture en passant;
- the king may not step onto the two squares the white pawn attacks, but
  stepping next to the pawn elsewhere is fine and then threatens to take
  it;
- the rules let Black promote to any of four pieces, so each is tried
  rather than assuming the queen is best;
- White wins on reaching the last row even if the new queen could be
  taken at once.

The answers were compared with a separately written solution on 200
random positions of every kind and on every test.

## Language notes

- All languages run the same memoised search; Python raises the
  recursion limit, the search going two levels deeper per row the pawn
  climbs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1216_games.cpp](1216_games.cpp) | G++ 13.2 x64 | games | O(positions) | AC | 0.031 s | 1708 KB |
| [1216_games.go](1216_games.go) | Go 1.14 x64 | games | O(positions) | AC | 0.062 s | 8184 KB |
| [1216_games.java](1216_games.java) | Java 1.8 | games | O(positions) | AC | 0.187 s | 8372 KB |
| [1216_games.py](1216_games.py) | Python 3.12 x64 | games | O(positions) | AC | 0.671 s | 6264 KB |
| [1216_games.rs](1216_games.rs) | Rust 1.75 x64 | games | O(positions) | AC | 0.046 s | 2420 KB |
