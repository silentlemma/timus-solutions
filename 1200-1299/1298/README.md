# 1298. Knight

[Timus 1298](https://acm.timus.ru/problem.aspx?space=1&num=1298) · difficulty 234 · backtracking

Original problem: folklore (prepared by Den Raskovalov), from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On an N × N board (1 ≤ N ≤ 8), find a knight's tour: a path of knight
moves that visits every square exactly once. Print the squares in
order, as a letter for the column and a number for the row, or
`IMPOSSIBLE` if there is no tour.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

N² squares, one per line, or `IMPOSSIBLE`.

## Checking

Any correct tour is accepted. The checker reads the N² squares and
verifies that they are all different, all on the board, and that each
one is a knight move from the one before. When no tour exists, the
output must be exactly `IMPOSSIBLE`.

## Examples

### Example 1

Input:

```
3
```

Output:

```
IMPOSSIBLE
```

### Example 2

Input:

```
5
```

Output:

```
a1
c2
e1
d3
e5
c4
d2
e4
c5
a4
b2
d1
e3
d5
b4
a2
c1
e2
c3
b1
a3
b5
d4
b3
a5
```

## Solution

A depth-first search builds the path one square at a time and undoes a
step when it gets stuck, trying every starting square in turn. On its
own this could take very long on an 8 × 8 board, so the next squares
are tried in the order of Warnsdorff's rule: first the square with the
fewest free squares one move further. Dead ends then appear rarely and
late.

With this order the search never has to step back for N from 5 to 8:
it finds a tour from a1 in exactly N² calls. For N = 2, 3 and 4 there
is no tour, and the search shows it by trying every start, which takes
29 976 calls for N = 4. N = 1 is the single square a1. Since every
branch the rule would skip is still tried, the answer is exact, not a
heuristic guess.

Pitfalls:

- N = 1 has a tour of one square, a1 (test 03);
- 4 × 4 has no tour, although its board is larger than 3 × 3's
  (test 05);
- the tour does not have to be closed: the last square need not attack
  the first.

## Language notes

- All five languages break ties in the same stable order, so they
  print the same tours.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1298_backtracking.cpp](1298_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 216 KB |
| [1298_backtracking.go](1298_backtracking.go) | Go 1.14 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 4468 KB |
| [1298_backtracking.java](1298_backtracking.java) | Java 1.8 | backtracking | O(N^2) for N >= 5 | AC | 0.156 s | 7116 KB |
| [1298_backtracking.py](1298_backtracking.py) | Python 3.12 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.171 s | 544 KB |
| [1298_backtracking.rs](1298_backtracking.rs) | Rust 1.75 x64 | backtracking | O(N^2) for N >= 5 | AC | 0.015 s | 244 KB |
