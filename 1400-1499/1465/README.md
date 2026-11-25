# 1465. Pawn Game

[Timus 1465](https://acm.timus.ru/problem.aspx?space=1&num=1465) · difficulty 489 · games

Original problem by Alexander Toropov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On a board of 3 × N squares (1 ≤ N ≤ 10⁹) the first rank is filled with
white pawns and the third with black ones; the middle rank is empty.
Pawns move and capture as in chess, capturing is compulsory, and a
player who cannot move loses. White moves first. Both play perfectly:
print "White" if White wins and "Black" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

"White" or "Black".

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
3
```

Output:

```
White
```

### Example 2

Input:

```
4
```

Output:

```
Black
```

### Example 3

Input:

```
5
```

Output:

```
White
```

## Acceptance update

Refreshed files: [1465_implementation_parsing_optimized.rs](1465_implementation_parsing_optimized.rs). Their new exact-source Accepted results are listed in the solution tables. Earlier comparison measurements and rankings for these files refer to preceding source snapshots and are retained as historical evidence. The cached audit confirms qualifying coverage in every available language. Teaching versions are retained for clarity; a source that also serves as the fast version must meet the performance criterion.

## Solution

This is Dawson's chess. A pawn pushed into the middle rank is attacked by
the enemy pawns on the neighbouring files, and the compulsory captures
that follow end with the pushed file and its neighbours dead: no pawn
there can move again. So a move on file i of a row of n live files
leaves two independent rows of i − 2 and n − i − 1 files; a move next to
an edge kills two files, and a lone file dies by itself. This is the
octal game 0.137: take one file only if it is the whole row, take two
leaving at most one row, or take three leaving up to two rows.

The first player wins exactly when the Grundy value of n is not zero,
where the value of a row is the smallest number not among the values of
its moves, and two rows combine by xor. The values are computed up to
200 in O(200²). From n = 52 on they repeat with period 34, and by the
periodicity theorem for octal games it is enough to check this up to
2 · 52 + 34 + 3; so a larger N is folded into the last period below 200.
`O(1)` per answer.

Pitfalls:

- a board of N = 10⁹ cannot be simulated, only folded (tests 12 to 15);
- the values settle only from n = 52 on: 14 and 48 files, or 34 and 68,
  have different winners (tests 07, 08, 17, 18);
- in C-like languages the remainder of a negative number is negative,
  so the folding must subtract in the right order.

## Optimized solutions

Go computes the same first200 Grundy values and keeps the same period folding as the ordinary accepted implementation. A fixed 256-entry boolean array replaces a new map for each mex. At size≤200 there are at most200 moves, hence mex≤200; byte-valued Grundy numbers have XOR at most255, so both arrays are safe. All values are computed at runtime, with no stored winner list and no new periodicity assumption. Bounded standard-handle I/O replaces fmt. The fixed precomputation is independent of N, giving O(1) query time/storage.

The accepted base implementations [1465_games.cpp](1465_games.cpp), [1465_games.py](1465_games.py), [1465_games.rs](1465_games.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1465_games_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1465_games.java`: time 0.140 s → 0.14 s; memory 1720 KB → 668 KB.

`1465_games_bitmask.java`. The generator below computes Grundy values by splitting a row at every legal move and taking the mex of the reachable XOR values. It verifies the period of 34 from length 52 up to the induction step. For larger rows, adding or removing 34 files from a sufficiently long component preserves its Grundy value, pairing the options in both directions. Black wins for residues 4, 8, 20, 24 and 28 modulo 34 and for two additional lengths, 14 and 34. Java reads the width and tests one bit of the generated mask in O(1) time and space. [Generate the mask and both exceptions](1465_games_bitmask_table.py).

On Java 1.8, the simple version used 0.140 s and 1720 KB, and the buffered version used 0.14 s and 668 KB. Submission #11328151 used 0.093 s and 340 KB. Compared with the 24 other authors in the Java 1.8 sample, it ranks 1/25 by time and 1/25 by memory, counting ties at the same rank.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1465_games_optimized.py`. Store the 201 win/loss bits of the verified Grundy recurrence, then apply its existing period. The adjacent 1465_games_table.py regenerates the mask from the simple recurrence; no judge answers are embedded. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328554 (Python 3.12 x64): **0.093 s / 672 KB**. Archived comparison: `1465_games.py` (Python 3.12 x64) — 0.109 s / 444 KB (#11286512).


`1465_implementation_parsing_optimized.rs`. Read the position size directly. Keep the exact epoch-marked Grundy recurrence and the established period; no precomputed answer table is added. Specialize direct output to the answer types actually used, avoiding generic formatting dispatch and temporary answer strings. Fixed text uses native writes; numeric writers handle the required signed or unsigned magnitudes exactly. Mathematical decisions and archived simple versions are preserved.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329333 (Rust 1.75 x64): **0.031 s / 72 KB**.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1465_games.cpp](1465_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 172 KB | 11286506 |
| [1465_games.go](1465_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1144 KB | 11286511 |
| [1465_games.java](1465_games.java) | Java 1.8 | games | O(1) | AC | 0.140 s | 1720 KB | 11286514 |
| [1465_games.py](1465_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.109 s | 444 KB | 11286512 |
| [1465_games.rs](1465_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 440 KB | 11286517 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1465_games_optimized.go](1465_games_optimized.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 308 KB | 11315353 |
| [1465_games_optimized.java](1465_games_optimized.java) \* | Java 1.8 | games | O(1) | AC | 0.14 s | 668 KB | 11324821 |
| [1465_games_bitmask.java](1465_games_bitmask.java) | Java 1.8 | games, bitmask | O(1) | AC | 0.093 s | 340 KB | 11328151 |
| [1465_games_optimized.py](1465_games_optimized.py) | Python 3.12 x64 | games | O(1) | AC | 0.093 s | 672 KB | 11328554 |
| [1465_implementation_parsing_optimized.rs](1465_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(1) | AC | 0.046 s | 68 KB | 11330232 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
