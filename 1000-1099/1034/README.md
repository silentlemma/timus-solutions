# 1034. Moving three queens between peaceful positions

[Timus 1034](https://acm.timus.ru/problem.aspx?space=1&num=1034) · difficulty 810 · bruteforce

Original problem by Dmitry Filimonenkov, from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` queens (`4 ≤ N ≤ 50`) stand on an `N × N` board in a peaceful position:
no queen attacks another one. Count the peaceful positions that can be
obtained from the given one by moving exactly three queens. The queens are
not distinguishable: a position is the set of occupied cells, so swapping
queens between occupied cells gives the same position.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the coordinates `X Y` (`1 ≤ X, Y ≤ N`) of the
queens.

## Output

The number of peaceful positions reachable by moving exactly three queens.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
2 1
1 3
3 4
4 2
```

Output:

```
0
```

### Example 2

Input:

```
9
2 5
3 8
7 1
8 7
9 4
6 6
1 3
5 9
4 2
```

Output:

```
4
```

## Solution

In a peaceful position every row and every column holds exactly one queen,
so a position is a permutation: row `r` → column `col[r]`. Moving exactly
three queens means the new position differs from the old one in exactly
three cells. The other `N − 3` queens stay and keep their rows and columns,
so the three moved queens must land on the same three rows and the same
three columns, in a new matching between them. Of the 6 matchings of three
rows to three columns, one is the old position and three keep one queen in
place (only two queens move); the remaining two are the cyclic shifts of
the columns. Different triples or shifts give different positions.

So: for every triple of rows `a < b < c` and both cyclic shifts, place the
three queens at the new cells and check the diagonals. Keep counters of the
queens on each diagonal `r + c` and `r − c`; remove the three old queens,
then each new cell must find both of its diagonals empty (this also catches
two new queens attacking each other). That is `2 · C(N, 3) ≈ 39 000` checks
of constant time, `O(N^3)` in total.

Pitfalls:

- swapping just two queens is a move of two queens, not three, and must
  not be counted;
- do not count a shift twice: the two cyclic shifts of a triple are two
  different positions, the other four matchings are not wanted;
- a new queen may attack another new queen, not only the queens that stay.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: diagonal counters updated in place
  and restored after each check.
- **Python**: sets of the occupied diagonals; for each triple the three old
  diagonals are removed from a copy of the sets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1034_bruteforce.cpp](1034_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(N^3) | AC | 0.015 s | 196 KB |
| [1034_bruteforce.go](1034_bruteforce.go) | Go 1.14 x64 | bruteforce | O(N^3) | AC | 0.015 s | 1104 KB |
| [1034_bruteforce.java](1034_bruteforce.java) | Java 1.8 | bruteforce | O(N^3) | AC | 0.093 s | 1016 KB |
| [1034_bruteforce.py](1034_bruteforce.py) | Python 3.12 x64 | bruteforce | O(N^3) | AC | 0.187 s | 604 KB |
| [1034_bruteforce.rs](1034_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(N^3) | AC | 0.031 s | 216 KB |
