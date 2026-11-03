# 1087. A take-away game where taking the last stone loses

[Timus 1087](https://acm.timus.ru/problem.aspx?space=1&num=1087) · difficulty 278 · games

Original problem by Anton Botov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pile has `n` stones (`1 ≤ n ≤ 10000`). Two players take turns removing
`k₁`, `k₂`, …, or `kₘ` stones (`1 ≤ m ≤ 50`, `1 ≤ kᵢ ≤ n`); a move is
always possible. The player who takes the last stone loses. Print 1 if
the first player wins with best play, otherwise 2.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `m`, then `k₁ … kₘ`.

## Output

1 or 2.

## Checking

Output is compared token by token. The actual Python candidate
matched an independent recursive minimax on 3711 games: pile sizes
1 through 35 with move 1 and subsets of moves 2 through 8, including
duplicate and shuffled move entries. The oracle tracks the actual player
and awards a final-stone move to the opponent. It does not use the DP's
artificial empty-pile convention. Each of the three actual candidates
also passed 12 repository inputs in Docker and obtained its own
exact-source Accepted. The 3711 oracle checks were Python executions,
not 3711 executions of C++ and Java.

## Examples

### Example 1

Input:

```
17 3
1 3 4
```

Output:

```
2
```

## Solution

Let `win[x]` mean that the player to move with `x` stones can force
a win. A winning move must remove `k < x` stones and leave a losing
position: `win[x]` is true exactly when some such `k` has
`win[x − k] = false`. Taking exactly `x` stones immediately loses and
is not a winning move. Fill the table in increasing `x`; every dependency
is smaller, so induction proves the recurrence and the answer.

The simple sources use the equivalent terminal convention `win[0] = true`:
if the pile is empty, the previous player has just lost. They may test
`k ≤ x`, since the final-stone move then contributes `not win[0] = false`.
The legal-move promise applies before the game ends; it does not require
the literal move 1 to appear in the input. Repeated move sizes do not
change the outcome. Time is `O(n m)`, logical storage `O(n + m)`.
All five original Accepted bases remain unchanged.

## Optimized solutions

Instead of scanning every move separately at every state, the Python bitset method visits losing positions in increasing order. One compiled big-integer shift marks all positions reachable by a legal move from a losing position as winning. Smaller positions are already classified, which is the same backward-induction invariant as the scalar game DP. Exclude the empty position from winning transitions: taking the last stone must lose. Normalize by the smallest move as justified in the simple analysis.

Here N' is the normalized number of stones, M the number of moves, L the number of losing positions and w the big-integer limb width.

- `1087_games_optimized.cpp`: 0.015 s / 132 KB; base `1087_games.cpp`: 0.015 s / 204 KB; relative change: time -0.0%, memory -35.3%.
- `1087_games_optimized.java`: 0.125 s / 440 KB; base `1087_games.java`: 0.109 s / 1652 KB; relative change: time +14.7%, memory -73.4%.
- `1087_games_bitmask.py`: 0.062 s / 456 KB; base `1087_games.py`: 0.093 s / 568 KB; relative change: time -33.3%, memory -19.7%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1087_games.cpp`; covering source `1087_games_optimized.cpp`; time/memory places 1/1, other-author entries 92/92.

- Go: preferred teaching base `1087_games.go`; covering source `1087_games.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1087_games.java`; covering source `1087_games_optimized.java`; time/memory places 4/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1087_games.py`; covering source `1087_games_bitmask.py`; time/memory places 1/1, other-author entries 22/22.

- Rust: preferred teaching base `1087_games.rs`; covering source `1087_games.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1087_games.cpp](1087_games.cpp) | G++ 13.2 x64 | games | O(n·m) | AC | 0.015 s | 204 KB | 11279057 |
| [1087_games.go](1087_games.go) | Go 1.14 x64 | games | O(n·m) | AC | 0.031 s | 1092 KB | 11279058 |
| [1087_games.java](1087_games.java) | Java 1.8 | games | O(n·m) | AC | 0.109 s | 1652 KB | 11279060 |
| [1087_games.py](1087_games.py) | Python 3.12 x64 | games | O(n·m) | AC | 0.093 s | 568 KB | 11279059 |
| [1087_games.rs](1087_games.rs) | Rust 1.75 x64 | games | O(n·m) | AC | 0.015 s | 228 KB | 11279063 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1087_games_optimized.cpp](1087_games_optimized.cpp) | G++ 13.2 x64 | games | O((M+L) ceil(N'/w)) | AC | 0.015 s | 132 KB | 11308397 |
| [1087_games_optimized.java](1087_games_optimized.java) \* | Java 1.8 | games | O((M+L) ceil(N'/w)) | AC | 0.125 s | 440 KB | 11308400 |
| [1087_games_bitmask.py](1087_games_bitmask.py) | Python 3.12 x64 | games, bitmask | O((M+L) ceil(N'/w)) | AC | 0.062 s | 456 KB | 11309361 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
