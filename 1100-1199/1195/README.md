# 1195. Who wins an unfinished game of noughts and crosses

[Timus 1195](https://acm.timus.ru/problem.aspx?space=1&num=1195) · difficulty 260 · games

Original problem by Leonid Volkov and Oleg Kats, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 3×3 noughts-and-crosses board has exactly three crosses and three
noughts and no complete line yet; crosses moved first, so they move now.
Find the result with best play on both sides.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Three lines of `X`, `O` and `#` for an empty cell.

## Output

`Crosses win`, `Ouths win` or `Draw`.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1195_games_optimized.cpp` (G++ 13.2 x64): 15 repository cases; 1372 additional source-bound comparisons.

- `1195_games_optimized.java` (Java 1.8): 15 repository cases; 1372 additional source-bound comparisons.

- `1195_games_optimized.py` (PyPy 3.10 x64): 15 repository cases; 1372 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
XXO
#X#
#OO
```

Output:

```
Ouths win
```

### Example 2

Input:

```
O#O
#X#
XOX
```

Output:

```
Draw
```

### Example 3

Input:

```
XX#
XOO
#O#
```

Output:

```
Crosses win
```

## Solution

Only three cells are empty, so the whole game tree has at most
`3·2·1` lines of play. A plain minimax decides it: the side to move tries
every empty cell; a move that completes a line wins, otherwise the result
is the opposite of the opponent's best result from there; a full board is
a draw. `O(1)`.

Pitfalls:

- the side to move is always crosses, because both sides have made three
  moves;
- the check for a completed line must look at the mark just placed, not
  at both marks;
- the answer for noughts is spelled `Ouths win`.

The answers were compared with a separately written solution on all 1372
boards with three crosses, three noughts and no complete line.

## Optimized solutions

Keep the same exhaustive minimax and the eight winning lines. A legal input has three crosses and three noughts without an existing win, so just three cells remain: there is no need for a table of all boards. Try a legal move, return a win immediately if it completes a line, otherwise negate the opponent's result and maximize; a full board is a draw. Native mutable-board versions restore the cell before every early return. Python uses two nine-bit masks and the remaining-cell mask, with the same game tree. Small direct input/output removes scanner/stream overhead. The fixed three-ply search is O(1); all1372legal six-mark boards were independently checked for the new Python source.

- `1195_games_optimized.cpp`: 0.015 s / 100 KB; base `1195_games.cpp`: 0.015 s / 352 KB; relative change: time -0.0%, memory -71.6%.
- `1195_games_optimized.java`: 0.109 s / 352 KB; base `1195_games.java`: 0.109 s / 1544 KB; relative change: time -0.0%, memory -77.2%.
- `1195_games_optimized.py`: 0.125 s / 280 KB; base `1195_games.py`: 0.078 s / 528 KB; relative change: time +60.3%, memory -47.0%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1195_games.cpp`; covering source `1195_games_optimized.cpp`; time/memory places 1/1, other-author entries 54/54.

- Go: preferred teaching base `1195_games.go`; covering source `1195_games.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1195_games.java`; covering source `1195_games_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1195_games.py`; covering source `1195_games_optimized.py`; time/memory places 18/5, other-author entries 24/24.

- Rust: preferred teaching base `1195_games.rs`; covering source `1195_games.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1195_games.cpp](1195_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 352 KB | 11283475 |
| [1195_games.go](1195_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1084 KB | 11283476 |
| [1195_games.java](1195_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 1544 KB | 11283479 |
| [1195_games.py](1195_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 528 KB | 11283478 |
| [1195_games.rs](1195_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 212 KB | 11283480 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1195_games_optimized.cpp](1195_games_optimized.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 100 KB | 11309257 |
| [1195_games_optimized.java](1195_games_optimized.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 352 KB | 11309258 |
| [1195_games_optimized.py](1195_games_optimized.py) \* | PyPy 3.10 x64 | games | O(1) | AC | 0.125 s | 280 KB | 11309730 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
