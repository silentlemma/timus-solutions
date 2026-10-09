# 1092. Clearing a sign table with transversal flips

[Timus 1092](https://acm.timus.ru/problem.aspx?space=1&num=1092) · difficulty 2322 · constructive

Original problem by Dmitry Filimonenkov, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A table of size `(2N + 1) × (2N + 1)` (`N ≤ 20`) holds `+` and `-` signs.
A transversal is a set of `2N + 1` cells with exactly one cell in every
row and every column. One operation flips all signs of a transversal.
Find a sequence of operations after which at most `2N` plus signs
remain, or report that there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `2N + 1` rows of the table.

## Output

`There is solution:` and one line per operation, the column of the
transversal in every row; or `No solution`.

## Checking

Any suitable sequence is accepted. The checker applies the operations
and counts the plus signs that remain.

## Examples

### Example 1

Input:

```
1
+++
++-
+-+
```

Output:

```
There is solution:
2 1 3
3 1 2
2 1 3
2 3 1
1 2 3
1 3 2
```

## Solution

Work modulo 2 with `n = 2N + 1`. Two transversals that agree everywhere
except in rows `i` and `l`, where one takes columns `j`, `l` and the other
`l`, `j`, together flip exactly the four corners of a rectangle. Rectangle
flips keep the parity of every row and every column, and they can turn
the table into any other table with the same parities: going through the
cells outside the last row and the last column, each wrong cell is fixed
by the rectangle with the corner `(l, l)`, and the last row and column
then agree by themselves because their parities match. One transversal,
on the other hand, flips the parity of every row and every column.

A table whose odd rows are `R` and odd columns are `C` needs at least
`max(|R|, |C|)` plus signs, and that many are enough: pair odd rows with
odd columns, and put the leftover lines, which come in pairs because
`|R|` and `|C|` have the same parity, into row or column 0. This is at
most `2N` unless all `n` rows or all `n` columns are odd; then one
transversal first makes them all even, and the other side cannot have
been all even before, because `n` is odd. So a solution always exists:

1. if every row or every column is odd, flip the main diagonal;
2. build the target table with `max(|R|, |C|)` plus signs;
3. for every cell outside the last row and column that differs from the
   target, flip its rectangle with two transversals.

At most `2(n − 1)² + 1` operations, `O(n³)` time with the flips.

Pitfalls:

- `No solution` is never the answer;
- the statement's row of numbers lists the column for each row, so a
  transversal is printed as a permutation;
- a table that already has few plus signs may still be changed, which is
  fine: any final table with at most `2N` plus signs is accepted.

The checker replays the operations; the Python version was also run on
hundreds of random tables of all sizes.

## Language notes

- Every language stores a copy of each transversal, because the same
  array is changed for the second flip of the pair.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1092_constructive.cpp](1092_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^3) | AC | 0.015 s | 1752 KB |
| [1092_constructive.go](1092_constructive.go) | Go 1.14 x64 | constructive | O(n^3) | AC | 0.031 s | 4832 KB |
| [1092_constructive.java](1092_constructive.java) | Java 1.8 | constructive | O(n^3) | AC | 0.140 s | 7252 KB |
| [1092_constructive.py](1092_constructive.py) | Python 3.12 x64 | constructive | O(n^3) | AC | 0.109 s | 3592 KB |
| [1092_constructive.rs](1092_constructive.rs) | Rust 1.75 x64 | constructive | O(n^3) | AC | 0.031 s | 2116 KB |
