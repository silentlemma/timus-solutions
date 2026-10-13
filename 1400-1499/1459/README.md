# 1459. Archer's Travel

[Timus 1459](https://acm.timus.ru/problem.aspx?space=1&num=1459) · difficulty 1672 · dp

Original problem by Alexander Ipatov, prepared by Vladimir Yakovlev, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An archer is a chess piece that moves one square forward, back, left or
right. It stands on square (1, 1) of an N × M board (2 ≤ N ≤ 5,
2 ≤ M ≤ 10⁹) and must visit every square exactly once and come back to
the start. Count the number of such tours modulo 10⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M.

## Output

The number of tours modulo 10⁹.

## Examples

### Example 1

Input:

```
2 3
```

Output:

```
2
```

## Solution

A tour is a Hamiltonian cycle of the grid walked in one of two
directions, so the answer is twice the number of cycles. Count the
cycles row by row, the rows having width N ≤ 5, with a plug DP: between
two rows, a state records which vertical edges cross the border and how
their ends pair up into paths, written as brackets. Inside a row the
cells are processed one at a time with one extra horizontal plug; a cell
with no plugs starts a new path, a cell with one plug continues it down
or right, and a cell with two plugs joins two paths, fixing the bracket
of the far end when two openings or two closings meet. Joining the two
ends of one path closes a cycle, which is allowed only at the very last
cell with no other plugs left, since a cycle must cover everything.

Width 5 has only 20 states, so one row becomes a small
transfer matrix. The first M − 1 rows are its power by repeated
squaring, from the empty state, and the last row, which may not send
plugs further down but may close the cycle, is applied at the end.
`O(S³ log M)` for S states.

Pitfalls:

- an odd number of squares admits no tour (tests 03, 08, 12);
- two rows have exactly one cycle however long they are (tests 01, 07);
- the count must stay modulo 10⁹ through the matrix products, which
  need 64-bit intermediate values.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1459_dp.cpp](1459_dp.cpp) | G++ 13.2 x64 | dp | O(S^3 log M) | AC | 0.015 s | 224 KB |
| [1459_dp.go](1459_dp.go) | Go 1.14 x64 | dp | O(S^3 log M) | AC | 0.031 s | 1372 KB |
| [1459_dp.java](1459_dp.java) | Java 1.8 | dp | O(S^3 log M) | AC | 0.156 s | 4236 KB |
| [1459_dp.py](1459_dp.py) | Python 3.12 x64 | dp | O(S^3 log M) | AC | 0.156 s | 856 KB |
| [1459_dp.rs](1459_dp.rs) | Rust 1.75 x64 | dp | O(S^3 log M) | AC | 0.031 s | 260 KB |
