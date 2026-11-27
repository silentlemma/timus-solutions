# 1195. Who wins an unfinished game of noughts and crosses

[Timus 1195](https://acm.timus.ru/problem.aspx?space=1&num=1195) · difficulty 260 · games

Original problem by Leonid Volkov and Oleg Kats, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 3×3 noughts-and-crosses board has exactly three crosses and three
noughts and no complete line yet; crosses moved first, so they move now.
Find the result with best play on both sides.

A winning line consists of three identical marks in one row, one column or either of the two diagonals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Three lines of `X`, `O` and `#` for an empty cell.

## Output

`Crosses win`, `Ouths win` or `Draw`.

## Checking

The repository checker requires one answer line. It compares the tokens within that line, so spacing within a line is normalized but moving words onto another line is not equivalent. The permitted outputs are `Crosses win`, `Ouths win` and `Draw`.

- `1195_games_optimized.cpp` (G++ 13.2 x64): 15 repository cases; 1372 additional source-bound comparisons.

- `1195_games_optimized.java` (Java 1.8): 15 repository cases; 1372 additional source-bound comparisons.

- `1195_games_optimized.py` (PyPy 3.10 x64): 15 repository cases; 1372 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
XXO
X#O
O##
```

Output:

```
Ouths win
```

### Example 2

Input:

```
XXO
OOX
###
```

Output:

```
Draw
```

### Example 3

Input:

```
XXO
XOO
###
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

`1195_games_optimized.java`. Java keeps the same exact three-ply negamax. Two nine-bit masks represent the marks; row, column and diagonal masks detect a win, and a winning move returns immediately. The input always leaves three empty cells, so no memoization table is needed. A 64-byte input buffer replaces individual stream reads; the three answer strings are unchanged. Time and auxiliary space are O(1) on this fixed board. The complete domain of 1372 valid six-mark boards was compared with an independent board-based solver.

Exact-source Java 1.8 Accepted #11327339 is 0.093 s / 372 KB; saved 2026-11-20 comparison: time 3/25, memory 2/25. It passes the shared time criterion below 1024 KB and has no separate first-place target or marker. Earlier #11309258 is the separate historical pair 0.109 s / 352 KB; its memory must not replace the current 372 KB.

- `1195_games_optimized.java`: 0.093 s / 372 KB; retained teaching base `1195_games.java`: 0.109 s / 1544 KB.

`1195_games_optimized.rs`. Keep negamax on the given six-move tic-tac-toe position. Two nine-bit masks replace the mutable board vector; eight winning masks replace three-cell comparisons, and a winning move returns immediately. No memoization or different game rule is introduced. With E empty cells, worst-case search O(E!) and stack O(E), bounded by the fixed 3×3 board. Direct byte input/output preserves the exact Crosses/Draw/Ouths strings.

Compared with `1195_games.rs`: time 0.046 s → 0.015 s; memory 212 KB → 56 KB.

Keep the same exhaustive minimax and the eight winning lines. A legal input has three crosses and three noughts without an existing win, so just three cells remain: there is no need for a table of all boards. Try a legal move, return a win immediately if it completes a line, otherwise negate the opponent's result and maximize; a full board is a draw. Native mutable-board versions restore the cell before every early return. Python uses two nine-bit masks and the remaining-cell mask, with the same game tree. Small direct input/output removes scanner/stream overhead. The fixed three-ply search is O(1); all1372legal six-mark boards were independently checked for the new Python source.

- `1195_games_optimized.cpp`: 0.015 s / 100 KB; base `1195_games.cpp`: 0.015 s / 352 KB; relative change: time -0.0%, memory -71.6%.

- `1195_games_optimized.py`: 0.125 s / 280 KB; base `1195_games.py`: 0.078 s / 528 KB; relative change: time +60.3%, memory -47.0%.

## Language notes

Use the shared [rating criteria](../../RATING_CRITERIA.md). The source-bound cache qualifies both C++ versions, Go, optimized Java, simple Python and both Rust versions. Simple Java fails the numerical target but remains an unstarred teaching source; optimized PyPy fails on time and retains its marker. Below 1024 KB compare time only. Go at 1084 KB passes both metrics against its one exact-version rival. Rust has no exact-version rivals and uses the ordinary same-language fallback, with one rival in another compiler version; qualification is not inferred from memory savings alone. There is no separate first-place or 30%-improvement rule. Rival times below 0.015 s are excluded; our smaller times are floored only for comparison.

Only the player-relative-score comment in `1195_games.py` changed in this review; its executable AST and simple algorithm are unchanged. The table retains historical Accepted #11283478 and its paired metrics. The current bytes require fresh exact-source Accepted in the later submission batch.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1195_games.cpp](1195_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 352 KB | 11283475 |
| [1195_games.go](1195_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1084 KB | 11283476 |
| [1195_games.java](1195_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 1544 KB | 11283479 |
| [1195_games.py](1195_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 560 KB | 11331067 |
| [1195_games.rs](1195_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 212 KB | 11283480 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1195_games_optimized.cpp](1195_games_optimized.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 100 KB | 11309257 |
| [1195_games_optimized.java](1195_games_optimized.java) | Java 1.8 | games | O(1) | AC | 0.093 s | 372 KB | 11327339 |
| [1195_games_optimized.py](1195_games_optimized.py) \* | PyPy 3.10 x64 | games | O(1) | AC | 0.125 s | 280 KB | 11309730 |
| [1195_games_optimized.rs](1195_games_optimized.rs) | Rust 1.75 x64 | games | O(E!) search; O(E) stack | AC | 0.015 s | 56 KB | 11325545 |

\* The optimized PyPy source at 0.125 s misses the current time target; the simple CPython source at 0.078 s passes.
