# 1480. Coupons

[Timus 1480](https://acm.timus.ru/problem.aspx?space=1&num=1480) · difficulty 471 · constructive

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Arrange the numbers 1 … N² (2 ≤ N ≤ 50) in an N × N table so that the
largest sum of two cells sharing a side is as small as possible. Print
that sum and a table reaching it; written row by row in order, the sum
would be 2N² − 1.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The smallest possible largest sum, then N rows of the table. Any
fitting table is accepted.

## Examples

### Example 1

Input:

```
2
```

Output:

```
6
1 4
3 2
```

## Solution

Colour the table like a chessboard. Two large numbers must never meet,
so put N², N² − 1, … on the cells of one colour in reading order, and
1, 2, … on the other colour, also in reading order. Every sum then
pairs a small number with a large one, and the worst pair is a small
number with the large number just above it: about N/2 cells of each
colour lie between them in reading order, and the sum comes to
N² + ⌊N/2⌋ + 1 (checked for every N up to 50).

No table does better. An exhaustive search that places the numbers
from the largest down, giving every cell the cap left by its placed
neighbours, finds no table with a smaller sum for any N up to 9, and
this is the value the judge expects. `O(N²)`.

Pitfalls:

- the first line is the sum, not N; the table follows (all tests);
- the colouring works the same for odd and even N, but ⌊N/2⌋ rounds
  down (tests 05, 06, 07);
- the obvious table in reading order gives 2N² − 1, as the statement
  notes, far from optimal.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1480_constructive.cpp](1480_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 128 KB |
| [1480_constructive.go](1480_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 1108 KB |
| [1480_constructive.java](1480_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 1640 KB |
| [1480_constructive.py](1480_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.078 s | 432 KB |
| [1480_constructive.rs](1480_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 256 KB |
