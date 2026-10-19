# 1870. Zinium 2

[Timus 1870](https://acm.timus.ru/problem.aspx?space=1&num=1870) · difficulty 714 · constructive

Original problem by Igor Chevdar (prepared by Eugene Kurpilyanskiy), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place n queens on an n × n toroidal chessboard (the top row is glued to
the bottom one and the left column to the right one, so diagonals wrap
around) so that no two queens attack each other, or say that this is
impossible.

## Input

n (4 ≤ n ≤ 10⁵).

## Output

"Yes" and, for x = 1, …, n, the row of the queen in column x; or "No".
Any valid placement is accepted.

## Examples

### Example 1

Input:

```
5
```

Output:

```
Yes
2 4 1 3 5
```

### Example 2

Input:

```
8
```

Output:

```
No
```

## Solution

Number rows and columns from 0. On the torus two queens attack each
other when they share x, y, x + y mod n or x − y mod n, so each of
these must take every value once.

If n is prime to 6, put the queen of column i on row 2i mod n. The rows
2i, the sums 3i and the differences −i are all different because 2 and
3 are invertible modulo n.

Otherwise there is no placement. If n is even, add up x + y over all
queens. Since the sums take every residue once, the total is
n(n − 1)/2 ≡ n/2 (mod n). But it is also Σx + Σy = n(n − 1) ≡ 0, a
contradiction. If 3 divides n (and n is odd), add up the squares
instead. Since (x + y)² + (x − y)² = 2x² + 2y², the sum of squares S of
all residues satisfies S + S ≡ 2S + 2S, so 2S ≡ 0 (mod n). With
S = (n − 1)n(2n − 1)/6 this needs 3 to divide (n − 1)(2n − 1), but
both factors are 2 modulo 3. `O(n)`.

For the first example the rows are 1, 3, 5, 2, 4 counting from 1,
another valid answer.

Pitfalls:

- the answer depends on n modulo 6, not on n being prime: 35 has a
  placement, 9 and 8 do not;
- the step 2 is the smallest that works; step 1 puts all queens on one
  diagonal;
- the output has up to 10⁵ numbers, so it should be built in one piece.

The placements pass a checker for every n from 4 to 400 and for the
largest n, and the "No" answers agree with an independent accepted
implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1870_constructive.cpp](1870_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 1520 KB |
| [1870_constructive.go](1870_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1656 KB |
| [1870_constructive.java](1870_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 5372 KB |
| [1870_constructive.py](1870_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.125 s | 7276 KB |
| [1870_constructive.rs](1870_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 5832 KB |
