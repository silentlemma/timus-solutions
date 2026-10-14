# 1516. Nostalgia

[Timus 1516](https://acm.timus.ru/problem.aspx?space=1&num=1516) · difficulty 1767 · backtracking

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An 8 × 8 checkers board holds 1 to 12 white and 1 to 12 black men, all
on squares of one colour. A man captures an adjacent enemy man
diagonally, in any direction, if that man is not on the edge of the
board and the square right behind it is empty: it jumps there, and the
captured man leaves the board at once. One move may chain any number of
captures. Find the fewest men of either colour to take off the board so
that some white man can then capture all the black men left in one
move. There are no kings, even on the promotion rows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The 8 rows of the board from the top: 'W' white, 'B' black, '.' empty.

## Output

The smallest number of men to take off.

## Examples

### Example 1

Input:

```
W.......
.W......
..B...B.
.....W..
..B.B...
........
........
........
```

Output:

```
1
```

## Solution

Taking off every black man always works, so the answer is at most their
number. Otherwise some white man makes a chain of captures; try them
all with a depth-first search from every white man. The capturing man
leaves its own square empty. Along a chain, a white man on a landing
square has to be taken off and costs one, and a black man on a landing
square has to be taken off too, which leaves it uncaptured. Every
black man the chain does not capture has to be taken off, so each
point of the search gives the cost
(whites taken off) + (blacks) − (blacks captured). Each jump captures a
different black man, so chains have at most 12 jumps, and in practice
the search is tiny. Boards are kept as 64-bit masks.

Pitfalls:

- black men on the edge cannot be captured, so they must be taken off;
  if all are there, the answer is their number (test 02, gen4);
- a man of either colour on a landing square has to be taken off
  (tests 04, 05);
- captured men leave at once and the start square is free, so a chain
  can run in a loop back to where it began (test 06);
- the men may stand on the light squares (test 07);
- every white man has to be tried (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1516_backtracking.cpp](1516_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(W * 4^B) | AC | 0.015 s | 380 KB |
| [1516_backtracking.go](1516_backtracking.go) | Go 1.14 x64 | backtracking | O(W * 4^B) | AC | 0.031 s | 1072 KB |
| [1516_backtracking.java](1516_backtracking.java) | Java 1.8 | backtracking | O(W * 4^B) | AC | 0.109 s | 496 KB |
| [1516_backtracking.py](1516_backtracking.py) | Python 3.12 x64 | backtracking | O(W * 4^B) | AC | 0.093 s | 784 KB |
| [1516_backtracking.rs](1516_backtracking.rs) | Rust 1.75 x64 | backtracking | O(W * 4^B) | AC | 0.015 s | 224 KB |
