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

`1195_games_optimized.rs`. Keep negamax on the given six-move tic-tac-toe position. Two nine-bit masks replace the mutable board vector; eight winning masks replace three-cell comparisons, and a winning move returns immediately. No memoization or different game rule is introduced. With E empty cells, worst-case search O(E!) and stack O(E), bounded by the fixed 3×3 board. Direct byte input/output preserves the exact Crosses/Draw/Ouths strings.

Compared with `1195_games.rs`: time 0.046 s → 0.015 s; memory 212 KB → 56 KB.

Keep the same exhaustive minimax and the eight winning lines. A legal input has three crosses and three noughts without an existing win, so just three cells remain: there is no need for a table of all boards. Try a legal move, return a win immediately if it completes a line, otherwise negate the opponent's result and maximize; a full board is a draw. Native mutable-board versions restore the cell before every early return. Python uses two nine-bit masks and the remaining-cell mask, with the same game tree. Small direct input/output removes scanner/stream overhead. The fixed three-ply search is O(1); all1372legal six-mark boards were independently checked for the new Python source.

- `1195_games_optimized.cpp`: 0.015 s / 100 KB; base `1195_games.cpp`: 0.015 s / 352 KB; relative change: time -0.0%, memory -71.6%.
- `1195_games_optimized.java`: 0.109 s / 352 KB; base `1195_games.java`: 0.109 s / 1544 KB; relative change: time -0.0%, memory -77.2%.
- `1195_games_optimized.py`: 0.125 s / 280 KB; base `1195_games.py`: 0.078 s / 528 KB; relative change: time +60.3%, memory -47.0%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1195_games_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1195_games_optimized.rs](1195_games_optimized.rs) \* | Rust 1.75 x64 | games | O(E!) search; O(E) stack | AC | 0.015 s | 56 KB | 11325545 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
