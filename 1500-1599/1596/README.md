# 1596. Nightmare Knight

[Timus 1596](https://acm.timus.ru/problem.aspx?space=1&num=1596) · difficulty 8902 · constructive

Original problem by Vladimir Basunkov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find a closed knight's tour of an N × M board (6 ≤ N, M ≤ 1000): the
knight visits every cell exactly once and returns to its start. Print,
for every cell, which of the 8 knight moves leaves it, numbered in the
order (2, 1), (2, −1), (−2, 1), (−2, −1), (1, 2), (1, −2), (−1, 2),
(−1, −2) as (row, column) steps, or `No solution`. Any tour is accepted.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

N and M: N rows and M columns.

## Output

N rows of M move numbers, or `No solution`.

## Examples

### Example 1

Input:

```
6 7
```

Output:

```
5 1 5 6 2 6 2
7 2 6 8 7 8 8
1 4 8 6 7 6 4
1 2 6 1 1 6 4
5 5 4 3 5 3 8
7 3 7 7 7 3 4
```

### Example 2

Input:

```
7 7
```

Output:

```
No solution
```

## Solution

A knight always changes the colour of its square, so a closed tour
needs as many light squares as dark ones: with N and M both odd there is
none. For sides of at least 6 that is the only obstacle (Schwenk's
theorem), and the tour is built from small pieces.

Each side is cut into pieces from 6 to 11 long: eights while at least 14
remain, then a six if needed, then the rest. An even side gives only even
pieces, so every block has an even area. Each of the 27 possible block
shapes has a closed tour stored in the program, chosen to contain two
extra moves: (1, C − 2)–(3, C − 1) near the top right corner and
(R − 2, 1)–(R − 1, 3) near the bottom left corner. Every closed tour
also contains the moves (0, 0)–(2, 1) and (0, 0)–(1, 2), since the
corner cell has only those two neighbours. The stored tours were found
once, offline, by a depth-first search with Warnsdorff's ordering,
random tie-breaking with a fixed seed and restarts;
[1596_constructive_table.py](1596_constructive_table.py) prints them.

The tour is kept as an undirected cycle, two neighbours per cell. Two
neighbouring blocks in a row are joined by dropping the left block's
move (1, C − 2)–(3, C − 1) and the right block's corner move
(0, 0)–(2, 1), and adding the two knight moves between their ends
across the border. Dropping one move from each of two separate cycles
leaves two paths, and the two new moves close them into one cycle.
The rows of blocks are then joined the same way, transposed, at their
left ends: the upper block's (R − 2, 1)–(R − 1, 3) and the lower block's
(0, 0)–(1, 2). Each corner takes part in at most one join, so the moves
a join needs are always still there. A walk around the cycle from the
top left cell writes the direction numbers: `O(N·M)`.

The tests use a checker that follows the moves. It accepted the output
on several hundred board sizes with sides up to 31 and on the largest
boards.

Pitfalls:

- (2, 1) means two rows down and one column right; the first example
  confirms it, and swapping the two gives an invalid answer;
- 10⁶ cells make about 2 MB of output, which has to be written in one
  go.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1596_constructive.cpp](1596_constructive.cpp) | G++ 13.2 x64 | constructive | O(N·M) | AC | 0.015 s | 9508 KB |
| [1596_constructive.go](1596_constructive.go) | Go 1.14 x64 | constructive | O(N·M) | AC | 0.109 s | 11740 KB |
| [1596_constructive.java](1596_constructive.java) | Java 1.8 | constructive | O(N·M) | AC | 0.125 s | 13912 KB |
| [1596_constructive.py](1596_constructive.py) | Python 3.12 x64 | constructive | O(N·M) | AC | 1.125 s | 13368 KB |
| [1596_constructive.rs](1596_constructive.rs) | Rust 1.75 x64 | constructive | O(N·M) | AC | 0.046 s | 17660 KB |
