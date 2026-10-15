# 1674. Drunk King

[Timus 1674](https://acm.timus.ru/problem.aspx?space=1&num=1674) · difficulty 6070 · constructive

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A drunk king moves like a chess king to a neighbouring cell but never
makes two moves in a row in the same direction. Starting in the top
left corner of an N × M board, it must visit every cell once and come
back, without its path crossing itself. Print `No` if this is
impossible, otherwise `Yes` and a picture of the tour: cells as `o`,
moves as `-`, `|`, `/` and `\` between them.

## Input

N and M (2 ≤ N, M ≤ 500).

## Output

`No`, or `Yes` and the picture in 2N − 1 lines.

## Examples

### Example 1

Input:

```
6 8
```

Output:

```
Yes
o-o o-o o-o o-o
|  \| |/  |/  |
o-o o o o o o-o
  |    / \   \
o-o o-o o-o o-o
|    \   \   \
o-o o-o o-o o-o
  |  \   \   \
o-o o o o-o o o
|  /| | |  /| |
o-o o-o o-o o-o
```

### Example 2

Input:

```
5 5
```

Output:

```
No
```

Any valid tour is accepted; for the first example this solution draws a
different one.

## Solution

A tour exists for 2 × 2 and for every board with both sides at least 4
except 5 × 5; boards with a side of 2 or 3 (other than 2 × 2) have none.
An exhaustive search confirms this for sides 2 and 3 up to length 8
and for 5 × 5; the construction below covers the boards with a tour.

- A 4 × m board has a closed tour, the strip: a zigzag along the top two
  rows to the right end, down, a zigzag back along the bottom two rows,
  and up the left end. Its transpose serves m × 4.
- A board is reduced to a base whose sides are 4 to 7 plus multiples of
  4. Bases that are not strips (5 × 6, 5 × 7, 6 × 6, 6 × 7, 7 × 7 and
  their transposes) are stored tours. When both sides have the form
  4k + 1 the base is 5 × 9 instead, since 5 × 5 has no tour. The stored
  tours come from a search,
  [1674_constructive_table.py](1674_constructive_table.py).
- The board grows by four columns, then by four rows, at a time. The new
  block gets its own strip tour, and three moves at the seam are
  replaced by three diagonals: the vertical at the old right edge, the
  vertical at the new left edge and one diagonal of the new strip go,
  three crossing-free diagonals come. Every cell keeps two moves, no
  cell is passed straight through, and the two cycles become one.

The picture is drawn straight into a character grid, so changing a move
is overwriting one character. `O(N · M)`.

Pitfalls:

- 2 × 2 is a tour although its sides are below 4 (test 03), 5 × 5 has
  none although they are not (test 02);
- with both sides of the form 4k + 1 the reduction would reach 5 × 5,
  hence the 5 × 9 base (tests 07 and gen4);
- the picture lines keep their trailing spaces; the checker accepts
  them either way.

A checker parses the picture and verifies that every cell has two moves,
no cell is passed straight through and the moves form one cycle (two
crossing diagonals would need the same character, so they cannot both be
drawn). It accepts every board up to 30 × 30 and the largest ones, and
the answers agree with an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1674_constructive.cpp](1674_constructive.cpp) | G++ 13.2 x64 | constructive | O(N M) | AC | 0.062 s | 2868 KB |
| [1674_constructive.go](1674_constructive.go) | Go 1.14 x64 | constructive | O(N M) | AC | 0.031 s | 7140 KB |
| [1674_constructive.java](1674_constructive.java) | Java 1.8 | constructive | O(N M) | AC | 0.140 s | 10252 KB |
| [1674_constructive.py](1674_constructive.py) | Python 3.12 x64 | constructive | O(N M) | AC | 0.390 s | 6260 KB |
| [1674_constructive.rs](1674_constructive.rs) | Rust 1.75 x64 | constructive | O(N M) | AC | 0.031 s | 3120 KB |
