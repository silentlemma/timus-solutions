# 1947. Tracing a Meander

[Timus 1947](https://acm.timus.ru/problem.aspx?space=1&num=1947) · difficulty 1731 · bruteforce

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 5×5 board contains twelve `/` tiles, twelve `\` tiles and one empty
square `*`. Each tile has two separate arcs between edge midpoints.
With T, R, B, L meaning top, right, bottom, left, the connections are:

| Tile | First arc | Second arc |
|---|---|---|
| `/` | T↔L | R↔B |
| `\` | T↔R | B↔L |

Arcs in neighboring tiles join across their common edge. The two arcs
inside one tile do not join. A winning board has a continuous curve
joining two different outer sides and passing through at least three
distinct tiles. Adjacent sides are allowed. A hole interrupts a curve.

One move shifts a straight block of 1..4 adjacent tiles by one square
toward the hole, filling it and leaving a hole at the other end.
Tiles keep their orientation. Determine whether the board already wins,
can win after one move, or cannot win within one move. Limits: 1 s, 64 MB.

## Input

Five lines of five symbols. Exactly twelve `/`, twelve `\` and one `*`.

## Output

Print `WIN` if the initial board wins. Otherwise print any winning move:
`L`, `R`, `U` or `D` followed by the number of shifted tiles, 1..4.
The letter describes tile motion; the hole moves in the opposite direction.
If none works, print `FAIL`. Already winning boards must produce `WIN`.

## Checking

A checker accepts any winning move: it applies the move, traces the
curves and checks that one of them joins two different sides through at
least three tiles. `WIN` must be printed when the board already wins,
and `FAIL` only when no move works.

## Examples

```
*/\//
\/\\\
\////
/\\\\
\//\/
```

```
WIN
```

```
\/\/\
\/\//
//\/*
\\\/\
\//\/
```

```
D2
```

## Solution

Test the initial board first. To test a board, start at each of its twenty
outer edge midpoints. Follow the incoming port's unique partner inside
the tile, then enter the neighboring tile through the opposite port.
Stop at a hole, an outer edge, or a repeated (cell, incoming port) state.
Record distinct cell IDs, because the same tile can contribute both arcs.
An outer exit wins precisely when its side differs from the starting side
and at least three distinct cells were visited.

If the board does not win, enumerate directions and block lengths 1..4.
Keep only moves whose final hole lies inside the board. Copy the board
and repeatedly swap the hole with its next neighbor. For printed L/R/U/D,
the hole steps right/left/down/up. Test the changed board and return the
first winning command. If all fail, return `FAIL`. Every hole has exactly
eight legal moves: four other cells in its row and four in its column.

Correctness: interior graph ports have degree two and endpoints occur
only at the outer boundary or the hole. Every winning curve is therefore
a boundary-to-boundary path, and one of the twenty starts traces it
completely. Conversely, every successful trace certifies exactly the
required connected curve. Distinct-cell tracking enforces the length rule.
Successive swaps shift each selected tile once, so they implement the
specified block move. The enumeration visits every legal one-move result.
The initial check enforces `WIN` priority; the complete search makes the
returned move valid or proves `FAIL`.

O(1) time and space for the fixed 5×5 board. At most nine boards are
tested, with twenty boundary traces each. There are 48 tile arcs and
100 possible incoming-port states; state tracking guarantees termination.

Do not join all four tile ports or interpret the glyph as one diagonal.
A short corner connection, a same-side curve and an internal cycle do
not win. Count tiles, not arcs, and do not reverse tile-motion letters.
Moving a block means each tile moves one square, not one tile several.

## Language notes

C++, Go, Java and Rust use boolean arrays for port states and visited
tiles; Python uses sets and a 25-bit cell mask. Each candidate uses a
fresh board copy. All versions use only the standard library.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1947_bruteforce.cpp](1947_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB |
| [1947_bruteforce.go](1947_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1080 KB |
| [1947_bruteforce.java](1947_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.109 s | 500 KB |
| [1947_bruteforce.py](1947_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.109 s | 704 KB |
| [1947_bruteforce.rs](1947_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 248 KB |
