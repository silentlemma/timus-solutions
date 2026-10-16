# 1805. Chapaev and a Cipher Grille

[Timus 1805](https://acm.timus.ru/problem.aspx?space=1&num=1805) · difficulty 1010 · combinatorics

Original problem by Alexander Ipatov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cipher grille is an n × n square with n²/4 windows such that in its
four positions, turned by quarter turns, the windows cover every cell
exactly once. Written as a 0/1 matrix, read row by row, grilles are
ordered lexicographically. Print the k-th one.

## Input

n and k (4 ≤ n ≤ 10, n even, 1 ≤ k ≤ 10¹⁸); k does not exceed the
number of grilles.

## Output

The grille as n rows of n digits.

## Examples

### Example 1

Input:

```
4 15
```

Output:

```
0000
0000
1101
0001
```

## Solution

A quarter turn moves every cell around an orbit of four cells, and a
grille opens exactly one cell of each orbit, so there are 4^(n²/4)
grilles, at most 4²⁵. Go through the cells in order and try 0 first.
With this cell closed, each orbit without a window can still open any
of its cells not passed yet, so the number of such grilles is the
product of those counts. If k is at most that number the cell stays
0; otherwise k drops by it and the cell becomes the window of its
orbit. A cell whose orbit already has its window is 0, and the last
cell of an orbit without one is forced to 1, since the product with a
zero factor is 0. `O(n⁴)`.

In the example the grilles with the top two rows closed number
2⁴ = 16 ≥ 15, since each orbit keeps its two lower cells, so those rows
stay closed and the choice happens in the lower half.

Pitfalls:

- the counts reach 4²⁵, about 10¹⁵, so they need 64-bit integers;
- an orbit that has its window is no longer a factor of the product;
- 0 comes before 1, so the closed choice is counted first.

The answers agree with an independent accepted implementation on the
first, last and random grilles of every size, and with a full list of
the 256 grilles of side 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1805_combinatorics.cpp](1805_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n^4) | AC | 0.015 s | 388 KB |
| [1805_combinatorics.go](1805_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n^4) | AC | 0.031 s | 1096 KB |
| [1805_combinatorics.java](1805_combinatorics.java) | Java 1.8 | combinatorics | O(n^4) | AC | 0.109 s | 1660 KB |
| [1805_combinatorics.py](1805_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n^4) | AC | 0.109 s | 596 KB |
| [1805_combinatorics.rs](1805_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n^4) | AC | 0.031 s | 240 KB |
