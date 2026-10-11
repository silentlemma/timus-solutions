# 1212. Places for one more ship in battleship

[Timus 1212](https://acm.timus.ru/problem.aspx?space=1&num=1212) · difficulty 493 · geometry

Original problem by Anton Botov and Anatoly Uglov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A battleship board has `N` rows and `M` columns, both up to 30000, and up
to 30 ships of one to four cells already stand on it. Ships may not touch
each other, not even at a corner. Count the ways to place one more ship
of `K` cells, horizontally or vertically.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M` and the number of ships `L`; then each ship as the column and
row of its top left cell, its length and `V` or `H`; then `K`.

## Output

The number of places for the new ship.

## Examples

### Example 1

Input:

```
4 4 2
1 2 2 V
3 1 2 H
2
```

Output:

```
4
```

## Solution

Every placed ship forbids the rectangle around it, one cell wider on
every side. Count the horizontal places first. The rows split into bands
at the top edge and just below the bottom edge of every forbidden
rectangle; inside a band every row meets the same rectangles, so all its
rows have the same count. For one row of a band, take the forbidden
column ranges in order and add `max(0, length − K + 1)` for every free
stretch between them; multiply by the height of the band. The vertical
places are the same count on the board turned on its side. A ship of one
cell is the same either way, so then only one count is taken. With at
most 61 bands, `O(L² log L)`.

Pitfalls:

- the first number of a ship is its column and the second its row;
- a one-cell ship must not be counted twice;
- forbidden rectangles stick out past the edges of the board and must be
  clipped when cutting bands;
- the answer can reach about `1.8·10⁹`, beyond 32-bit integers.

The answers were compared with a brute force over every cell on 450
random small boards, and with a separately written solution on every
test.

## Language notes

- All languages give the forbidden rectangles named fields and reuse the
  same counting function for both directions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1212_geometry.cpp](1212_geometry.cpp) | G++ 13.2 x64 | geometry | O(L² log L) | AC | 0.031 s | 432 KB |
| [1212_geometry.go](1212_geometry.go) | Go 1.14 x64 | geometry | O(L² log L) | AC | 0.031 s | 1144 KB |
| [1212_geometry.java](1212_geometry.java) | Java 1.8 | geometry | O(L² log L) | AC | 0.140 s | 1940 KB |
| [1212_geometry.py](1212_geometry.py) | Python 3.12 x64 | geometry | O(L² log L) | AC | 0.078 s | 684 KB |
| [1212_geometry.rs](1212_geometry.rs) | Rust 1.75 x64 | geometry | O(L² log L) | AC | 0.046 s | 232 KB |
