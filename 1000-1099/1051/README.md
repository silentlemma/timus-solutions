# 1051. Peg solitaire on an infinite grid

[Timus 1051](https://acm.timus.ru/problem.aspx?space=1&num=1051) · difficulty 537 · games, math

Original problem by Stanislav Vasiliev, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An `M × N` rectangle of stones (`1 ≤ M, N ≤ 10000`) stands on the nodes of
an infinite grid. A move: a stone jumps over a horizontal or vertical
neighbour onto the empty node behind it, and the stone jumped over is
removed. Find the smallest number of stones that can remain.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M` and `N`.

## Output

The smallest number of remaining stones.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 6
```

Output:

```
2
```

### Example 2

Input:

```
1 7
```

Output:

```
4
```

## Solution

The answer depends only on the shape:

```text
min(M, N) = 1                      ->  ceil(max(M, N) / 2)
otherwise, M or N divisible by 3   ->  2
otherwise                          ->  1
```

**Why not 1 when a side is divisible by 3.** Colour the node `(x, y)`
with `(x + y) mod 3`. Three consecutive nodes of a row or a column have
three different colours, and a jump empties two of them and fills the
third: each colour count changes by one, so the parities of all three
counts flip together, and whether they are equal or not never changes. A
rectangle with a side divisible by 3 has equal counts of the three
colours (all with the same parity); a single stone has counts `1, 0, 0`,
which do not. So at least two stones remain, and in two dimensions two
can be reached.

**Two dimensions otherwise.** Stones can be removed three in a row with
the help of a neighbouring stone, which shrinks the rectangle side by
side down to a few small cases; they all end with one stone.

**One row.** A jump takes two neighbours and leaves one stone two cells
further along the line, and on a single line the stones cannot be
gathered together again, so every stone takes part in at most one jump:
at least `ceil(n / 2)` stones stay, and jumping pairs from the ends
reaches it.

The formula was also checked by an exhaustive search over all positions
(up to translation) for every board up to `3 × 4`, `2 × 7` and `4 × 4`.
`O(1)`.

Pitfalls:

- one row is different: `1 × 7` leaves 4, not 1;
- `2 × 3` leaves 2, while `2 × 4` leaves 1;
- `M` and `N` can be given in any order.

## Optimized solutions

Rust keeps the exact same constant-time rectangle formula as its Accepted standard-library base: a one-cell-wide row leaves ceil(longerSide/2); otherwise a side divisible by3 gives2, and the remaining cases give1. Read two numbers directly, use min/max instead of a heap vector and sorting, and print through a five-digit stack buffer with C-runtime character I/O and a C entry point. Dimensions≤10000 imply answer≤5000, so the buffer is sufficient. This is a representation/I/O change, not a new game theorem or a stronger complexity claim. Time and extra space remain O(1). All simple sources and their original proof explanation remain; C++/Go/Java/Python reuse their admitted bases.

For a row, each legal jump uses the first or last two stones of the remaining contiguous block. It leaves an isolated stone beyond that end, at least three positions from the new block. Later jumps only shrink the block, so exactly floor(n/2) jumps are possible.

For a rectangle, the first three sequences below reduce four occupied columns to their rightmost column. Their heights are 2, 3 and 4. For a height divisible by 3, use groups of three rows. With remainder 1 use a first group of four rows, and with remainder 2 use a first group of two rows. The two-row sequence uses the empty row above the board. The other sequences stay within their groups. This removes the left three columns. Use the same construction after transposing to remove three rows. Repeat until both dimensions lie between 2 and 4. The six base sequences then reach one stone, or two when a dimension is 3. Every jump leaves a stone, and the colour parity bound above supplies the lower bound of two. In the sequences, the initial top-left stone is at (0,0), with x along columns and y along rows.

```text
4×2 → 1×2
  (0,1)→(0,-1)  (1,1)→(1,-1)  (0,-1)→(2,-1)  (3,1)→(1,1)
  (2,-1)→(2,1)  (1,1)→(3,1)
4×3 → 1×3
  (1,0)→(-1,0)  (3,0)→(1,0)  (0,2)→(0,0)  (0,0)→(2,0)
  (2,1)→(0,1)  (2,2)→(0,2)  (0,2)→(0,0)  (-1,0)→(1,0)
  (1,0)→(3,0)
4×4 → 1×4
  (1,0)→(-1,0)  (3,0)→(1,0)  (1,1)→(-1,1)  (-1,0)→(-1,2)
  (2,2)→(2,0)  (1,0)→(3,0)  (1,3)→(1,1)  (-1,2)→(1,2)
  (3,3)→(1,3)  (0,3)→(2,3)  (1,1)→(1,3)  (1,3)→(3,3)
```

```text
2×2
  (0,0)→(0,2)  (1,0)→(1,2)  (0,2)→(2,2)
3×2
  (0,0)→(0,2)  (1,0)→(1,2)  (2,0)→(2,2)  (1,2)→(3,2)
4×2
  (0,0)→(0,2)  (1,0)→(1,2)  (3,0)→(3,2)  (0,2)→(2,2)
  (3,2)→(1,2)  (2,0)→(2,2)  (1,2)→(3,2)
3×3
  (1,0)→(3,0)  (0,1)→(0,3)  (1,1)→(1,3)  (2,2)→(2,0)
  (3,0)→(1,0)  (0,0)→(2,0)  (0,3)→(2,3)
4×3
  (1,0)→(-1,0)  (2,0)→(4,0)  (0,1)→(0,3)  (1,1)→(1,3)
  (2,1)→(4,1)  (4,0)→(4,2)  (0,3)→(2,3)  (2,3)→(2,1)
  (4,2)→(2,2)  (2,1)→(2,3)
4×4
  (1,0)→(-1,0)  (2,0)→(4,0)  (1,1)→(-1,1)  (-1,0)→(-1,2)
  (2,1)→(4,1)  (4,0)→(4,2)  (0,2)→(0,4)  (2,3)→(0,3)
  (3,3)→(3,1)  (1,2)→(3,2)  (4,2)→(2,2)  (0,4)→(0,2)
  (-1,2)→(1,2)  (1,2)→(3,2)  (3,1)→(3,3)
```

The current cached audit confirms the C++, Go and Python bases as
covering sources under the shared [rating criteria](../../RATING_CRITERIA.md).
C++ compares time rank only; Go uses the exact-compiler small-cohort
reference on both metrics; Python uses that reference on time alone
below 1 MiB. Simple Python is unstarred. Simple Java still fails its
required metrics but is retained unstarred as a teaching source; the
distinct optimized Java source qualifies by time alone at 460 KB.

The current revisions of the five simple 1051_games_math files and
1051_games_math_optimized.java correct only the reduction comment. An isolated row of three leaves two stones; the two-dimensional reduction
uses neighbouring stones, as in the constructive proof above. Their
table Accepted IDs and paired measurements belong to preceding revisions.

`1051_games_math_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1051_games_math.java`: time 0.125 s → 0.109 s; memory 1632 KB → 460 KB.

## Language notes

These notes describe the simple implementations.

- All languages evaluate the same formula.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1051_games_math.cpp](1051_games_math.cpp) | G++ 13.2 x64 | games, math | O(1) | AC | 0.001 s | 112 KB | 11331152 |
| [1051_games_math.go](1051_games_math.go) | Go 1.14 x64 | games, math | O(1) | AC | 0.031 s | 1052 KB | 11331034 |
| [1051_games_math.java](1051_games_math.java) | Java 1.8 | games, math | O(1) | AC | 0.14 s | 1552 KB | 11331055 |
| [1051_games_math.py](1051_games_math.py) | Python 3.12 x64 | games, math | O(1) | AC | 0.078 s | 404 KB | 11331088 |
| [1051_games_math.rs](1051_games_math.rs) | Rust 1.75 x64 | games, math | O(1) | AC | 0.001 s | 220 KB | 11331131 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1051_games_math_optimized.rs](1051_games_math_optimized.rs) | Rust 1.75 x64 | games, math | O(1) | AC | 0.015 s | 64 KB | 11315688 |
| [1051_games_math_optimized.java](1051_games_math_optimized.java) | Java 1.8 | games, math | O(1) | AC | 0.078 s | 456 KB | 11331200 |
