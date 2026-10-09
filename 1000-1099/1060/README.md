# 1060. The fewest flips to make a 4 × 4 board one colour

[Timus 1060](https://acm.timus.ru/problem.aspx?space=1&num=1060) · difficulty 375 · bruteforce, bitmask

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 4 × 4 board holds pieces that are black (`b`) or white (`w`) on top. A
move picks a cell and turns over the piece there and its neighbours above,
below, left and right (those that exist). Find the fewest moves after
which all pieces show the same colour (either one), `0` if they already
do, or `Impossible`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Four lines of four characters `b` and `w`.

## Output

The fewest moves, or `Impossible`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
bwbw
wwww
bbwb
bwwb
```

Output:

```
Impossible
```

### Example 2

Input:

```
bwwb
bbwb
bwwb
bwww
```

Output:

```
4
```

## Solution

Write the board as 16 bits; a move at a cell XORs the board with a fixed
mask of up to five bits. XOR is commutative and a mask applied twice
cancels, so the order of the moves does not matter and no cell needs more
than one move: a solution is just a set of cells.

There are `2^16 = 65536` sets. For each, XOR the masks of its cells into
the board and keep the smallest set whose result is all zeros or all ones.
`O(2^16 · 16)`.

Only 4096 of the 65536 positions can be solved, and none needs more than
six moves (a breadth-first search over all positions, used to check the
tests, shows this).

Pitfalls:

- both all-white and all-black are goals;
- cells on the border and in the corners turn fewer pieces;
- a position that is already one colour needs 0 moves.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: a loop over all 65536 sets.
- **Python**: the boards of all sets are built cell by cell, doubling a
  list (each new cell adds its mask to every board so far), which avoids
  a Python loop over 16 bits of every set.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 124 KB |
| [1060_bruteforce_bitmask.go](1060_bruteforce_bitmask.go) | Go 1.14 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.031 s | 1068 KB |
| [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java) | Java 1.8 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 1580 KB |
| [1060_bruteforce_bitmask.py](1060_bruteforce_bitmask.py) | Python 3.12 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 4840 KB |
| [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) | Rust 1.75 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 232 KB |
