# 1734. Endgame Database

[Timus 1734](https://acm.timus.ru/problem.aspx?space=1&num=1734) · difficulty 2169 · combinatorics

Original problem by Igor Chevdar, from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the checkers positions on an n × n board with exactly k pieces.
A piece is a white or black man or king and stands on a dark square;
both colours must be present, and no man stands on the row where it
would be crowned (white men not on the last row, black men not on the
first). Print the count modulo 10⁹ + 7.

## Input

n and k (4 ≤ n ≤ 1000, n even, 2 ≤ k ≤ n²/4).

## Output

The number of positions modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
4 2
```

Output:

```
172
```

## Solution

There are n²/2 dark squares: n/2 on the first row, n/2 on the last and
m = n²/2 − n in between. A dark square on the first or last row takes
three kinds of piece and any other square four, so the positions with k
pieces, colours aside, number

Σ C(n, a)·3^a·C(m, k − a)·4^(k − a)

over a, the pieces on the two edge rows.

From this take away the positions of one colour, twice by symmetry.
For white, a square on the last row takes only the king and any other
square the man or the king, which gives

Σ C(n/2, a)·C(m + n/2, k − a)·2^(k − a).

Since k ≥ 2, the board is never empty. Factorials up to n²/2 and their
inverses give the binomials. `O(n²)` for the factorials, `O(n log k)`
for the sums.

For n = 4 and k = 2 the first sum is 96 + 192 + 54 = 342 and the
second 60 + 24 + 1 = 85, so the answer is 342 − 2·85 = 172.

Pitfalls:

- both edge rows lose one kind of piece, not only the opponent's
  promotion row;
- for one colour the edge rows differ: on its own first row both kinds
  fit, on its last row only the king;
- the difference must be taken back into 0 … 10⁹ + 6.

The counts match a listing of every position for all k on 4 × 4 boards
and for k up to 4 on 6 × 6 boards, and an independent accepted
implementation on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1734_combinatorics.cpp](1734_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n²) | AC | 0.031 s | 7736 KB |
| [1734_combinatorics.go](1734_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n²) | AC | 0.046 s | 9672 KB |
| [1734_combinatorics.java](1734_combinatorics.java) | Java 1.8 | combinatorics | O(n²) | AC | 0.171 s | 9468 KB |
| [1734_combinatorics.py](1734_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n²) | AC | 0.281 s | 39668 KB |
| [1734_combinatorics.rs](1734_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n²) | AC | 0.046 s | 7896 KB |
