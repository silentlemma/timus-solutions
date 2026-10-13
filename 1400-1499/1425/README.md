# 1425. Queen 2

[Timus 1425](https://acm.timus.ru/problem.aspx?space=1&num=1425) · difficulty 1713 · hashing

Original problem by Nikita Rybak, Dmitry Kovalioff and Ilya Grebnov, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The board is an N-dimensional cube of S cells per side (1 ≤ N ≤ 5,
2 ≤ S ≤ 100). A rook moves any non-zero number of cells along one
coordinate; a bishop moves the same non-zero number of cells along all
N coordinates at once, each in either direction; a queen moves as
either. A queen stands on an empty board at (C[1], …, C[N]). Count the
cells where it can be after exactly two moves.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

N and S, then the N coordinates of the queen.

## Output

The number of cells.

## Examples

### Example 1

Input:

```
3 3
1 2 3
```

Output:

```
27
```

In the example the first move can go to (2, 2, 3), (3, 2, 3), (1, 1, 3),
(1, 3, 3), (1, 2, 1) or (1, 2, 2) as a rook, or to (2, 3, 2) or
(2, 1, 2) as a bishop.

## Solution

The board may have 10¹⁰ cells, but the answer is small: from the centre
of the largest board it is 858 180. So the cells are generated and
counted in a hash set. A queen has 2N rook directions and 2^N bishop
directions (in one dimension they are the same). The cells after the
first move are those along each direction from the start. From each of
them every direction is followed again, and every cell on the way is
added to the set; the cell of the first move itself is never added from
its own rays, so it counts only if some other first move reaches it.

Numbering a cell as the base-S number of its coordinates turns each ray
into an arithmetic progression of numbers, so a whole ray is a single
range. The compiled solutions put the numbers in an open-addressing
table of 2²¹ slots; Python adds whole ranges to a set. About
(2N + 2^N)² · S cells are generated, roughly 4·10⁶ at most.

Pitfalls:

- the queen may come back to its own cell (test 01);
- on a line of two cells only the starting cell is reachable in two
  moves (test 02);
- in one dimension the bishop and rook moves are the same (tests 09,
  13).

## Language notes

- Python adds each ray to a set as one `range`, so the loop over cells
  runs inside the set code. One set of all reached cells needs over
  64 MB, so the cells are counted in eight passes, each keeping only the
  cells whose first coordinate has a given remainder mod 8: along a ray
  those are every eighth cell, again one `range`. The judge's tests take
  up to 1.8 s and 33 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1425_hashing.cpp](1425_hashing.cpp) | G++ 13.2 x64 | hashing | O((2N + 2^N)^2 S) | AC | 0.062 s | 16376 KB |
| [1425_hashing.go](1425_hashing.go) | Go 1.14 x64 | hashing | O((2N + 2^N)^2 S) | AC | 0.156 s | 19432 KB |
| [1425_hashing.java](1425_hashing.java) | Java 1.8 | hashing | O((2N + 2^N)^2 S) | AC | 0.203 s | 19128 KB |
| [1425_hashing.py](1425_hashing.py) | Python 3.12 x64 | hashing | O((2N + 2^N)^2 S) | AC | 1.812 s | 32572 KB |
| [1425_hashing.rs](1425_hashing.rs) | Rust 1.75 x64 | hashing | O((2N + 2^N)^2 S) | AC | 0.093 s | 16684 KB |
