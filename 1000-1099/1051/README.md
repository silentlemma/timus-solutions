# 1051. Peg solitaire on an infinite grid

[Timus 1051](https://acm.timus.ru/problem.aspx?space=1&num=1051) · difficulty 534 · games, math

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
3 4
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
which do not. So at least two stones remain, and two can be reached.

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

## Language notes

- All languages evaluate the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1051_games_math.cpp](1051_games_math.cpp) | G++ 13.2 x64 | games, math | O(1) | AC | 0.015 s | 128 KB |
| [1051_games_math.go](1051_games_math.go) | Go 1.14 x64 | games, math | O(1) | AC | 0.015 s | 1068 KB |
| [1051_games_math.java](1051_games_math.java) | Java 1.8 | games, math | O(1) | AC | 0.125 s | 1632 KB |
| [1051_games_math.py](1051_games_math.py) | Python 3.12 x64 | games, math | O(1) | AC | 0.078 s | 328 KB |
| [1051_games_math.rs](1051_games_math.rs) | Rust 1.75 x64 | games, math | O(1) | AC | 0.031 s | 224 KB |
