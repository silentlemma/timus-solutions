# 1458. War Games

[Timus 1458](https://acm.timus.ru/problem.aspx?space=1&num=1458) · difficulty 1221 · constructive

Original problem by Dmitry Kovalioff, Nikita Rybak and Ilya Grebnov, with thanks to Sergey Sofronov for the idea, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An N × N parade ground (N even, 2 ≤ N ≤ 1000) has a soldier in every
cell, each in one of two positions, W or B. The command "cell (i, j)"
makes every soldier in row i or column j, 2N − 1 soldiers in all, switch
to the other position. Find the shortest list of commands after which
all soldiers stand the same way, either way.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines of N letters W and B.

## Output

The number of commands, then the cells of the commands. Any shortest
list is accepted.

## Examples

### Example 1

Input:

```
4
WBWB
BWWW
WWBW
WBWB
```

Output:

```
2
2 3
3 1
```

## Solution

Commands commute and a repeated command cancels, so a solution is a set
of cells. Giving every command in row a and in column b switches the
soldier at (a, b) 2N − 1 times, every other soldier of that row or
column N times and every remaining soldier twice; with N even only
(a, b) changes. So any single soldier can be switched alone, and to make
everyone W the soldiers standing B must be switched: adding up their
crosses, cell (i, j) is commanded when row i of B, column j of B and the
cell itself contain an odd number of B in total. Since single soldiers
can be switched, the 2^(N²) sets of cells reach all 2^(N²) patterns, so
no two sets act alike and this set is the only one for its target.

Making everyone B instead needs exactly the other cells, because the
all-cells set switches everybody. So take whichever of the two sets is
smaller: k or N² − k commands. `O(N²)`.

Pitfalls:

- a ground where everyone already stands alike, either way, needs no
  command (tests 02, 03);
- for N ≥ 4, one soldier standing differently needs a cross of 2N − 1
  commands (tests 07, gen2);
- up to half a million commands must be printed quickly (gen1, gen3,
  gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1458_constructive.cpp](1458_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.218 s | 5236 KB |
| [1458_constructive.go](1458_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.078 s | 15380 KB |
| [1458_constructive.java](1458_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.218 s | 25812 KB |
| [1458_constructive.py](1458_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.453 s | 42840 KB |
| [1458_constructive.rs](1458_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.062 s | 7264 KB |
