# 1622. Endspiel

[Timus 1622](https://acm.timus.ru/problem.aspx?space=1&num=1622) · difficulty 3122 · backtracking

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Peg solitaire on the cross-shaped board of 33 cells (a 7 × 7 square
without its 2 × 2 corners, columns A–G, rows 1–7): 32 pegs fill every
cell except the centre D4. A move jumps a peg horizontally or vertically
over a neighbouring peg onto an empty cell and removes the jumped peg.
Given a cell, print 31 moves that leave one peg exactly there, or
`Impossible`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The cell of the last peg.

## Output

31 moves `from-to`, one per line, or `Impossible`.

## Examples

### Example 1

Input:

```
D4
```

Output:

```
D2-D4
B3-D3
C1-C3
E1-C1
D3-B3
A3-C3
E3-E1
G3-E3
C4-C2
C1-C3
A4-C4
C4-C2
E4-C4
G4-E4
E4-E2
E1-E3
C5-C3
C2-C4
A5-C5
D5-B5
E6-E4
G5-E5
C7-C5
C4-C6
E7-C7
C7-C5
B5-D5
D5-F5
E3-E5
F5-D5
D6-D4
```

### Example 2

Input:

```
D3
```

Output:

```
Impossible
```

## Solution

Which cells are possible follows from an invariant. Split the cells into
three classes by (r + c) mod 3. A jump involves three consecutive cells
of a line, one of each class, and changes the peg count of every class by
one, so all three parities flip. The same holds for the classes of
(r − c) mod 3. After 31 jumps the parities are fixed, which fixes both
residues of the last peg, and so r and c modulo 3: they must match the
centre, which is possible. On the board this leaves only D4, D1, D7, A4
and G4; every other cell is `Impossible`.

The moves come from a depth-first search over the board as a 33-bit mask,
remembering positions already found dead. Searching for D4 or D7 takes a
fraction of a second, while D1 directly takes much longer; but the start
is symmetric, so A4, D1 and G4 are D7 turned by quarter turns: search for
D7 and turn every move of the answer.

Pitfalls:

- the example's moves are only one answer; a checker replays the moves;
- a target cell next to the centre (D3) is already impossible.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1622_backtracking.cpp](1622_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(S) | AC | 0.015 s | 420 KB |
| [1622_backtracking.go](1622_backtracking.go) | Go 1.14 x64 | backtracking | O(S) | AC | 0.031 s | 1244 KB |
| [1622_backtracking.java](1622_backtracking.java) | Java 1.8 | backtracking | O(S) | AC | 0.109 s | 1952 KB |
| [1622_backtracking.py](1622_backtracking.py) | Python 3.12 x64 | backtracking | O(S) | AC | 0.093 s | 804 KB |
| [1622_backtracking.rs](1622_backtracking.rs) | Rust 1.75 x64 | backtracking | O(S) | AC | 0.046 s | 460 KB |
