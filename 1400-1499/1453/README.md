# 1453. Queen

[Timus 1453](https://acm.timus.ru/problem.aspx?space=1&num=1453) · difficulty 1200 · math

Original problem by Dmitry Kovalioff, Ilya Grebnov and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An N-dimensional chessboard is a cube of S × S × ... × S cells
(1 ≤ N ≤ 10000, 2 ≤ S ≤ 100000). A rook moves any non-zero number of
cells along one coordinate; a bishop moves along all N coordinates at
once by the same non-zero amount; a queen moves as either. A queen
stands at (C[1], ..., C[N]) on an empty board. Count the cells it can
move to.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and S, then the N coordinates.

## Output

The number of cells, which may have thousands of digits.

## Examples

### Example 1

Input:

```
3 3
1 2 3
```

Output:

```
8
```

The rook moves reach (2, 2, 3), (3, 2, 3), (1, 1, 3), (1, 3, 3),
(1, 2, 1) and (1, 2, 2), the bishop moves (2, 3, 2) and (2, 1, 2).

## Solution

Rook moves give N (S − 1) cells. In one dimension a bishop moves exactly
like a rook, so that is the whole answer. For N ≥ 2 a bishop move
changes every coordinate and a rook move only one, so the two sets do
not overlap.

A bishop move of length t picks a side in every coordinate, and side ±
in coordinate i is possible when the room on that side, S − C[i] or
C[i] − 1, is at least t. A coordinate where both sides have room t
offers 2 choices, one where only one side has room offers 1, and with
no room at all the length t is impossible. So for lengths t up to the
smallest of max(S − C[i], C[i] − 1) the number of moves is 2^k(t),
where k(t) counts the coordinates with min(S − C[i], C[i] − 1) ≥ t. A
histogram of these minima gives every k(t) in one pass, and the answer
N (S − 1) + Σ 2^k(t) has up to about 3000 digits: count how many t share
each k, then build the sum by doubling from the largest k down, in
decimal limbs of nine digits. `O(N + S + N · D)` for D limbs.

Pitfalls:

- one dimension, where bishop and rook moves are the same cells (test
  02);
- the answer exceeds every built-in integer type (tests 06, gen1 to
  gen3);
- a coordinate at the edge leaves one side only (tests 03, 07, 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1453_math.cpp](1453_math.cpp) | G++ 13.2 x64 | math | O(N + S + N D) | AC | 0.031 s | 612 KB |
| [1453_math.go](1453_math.go) | Go 1.14 x64 | math | O(N + S + N D) | AC | 0.031 s | 2152 KB |
| [1453_math.java](1453_math.java) | Java 1.8 | math | O(N + S + N D) | AC | 0.109 s | 5828 KB |
| [1453_math.py](1453_math.py) | Python 3.12 x64 | math | O(N + S + N D) | AC | 0.109 s | 2376 KB |
| [1453_math.rs](1453_math.rs) | Rust 1.75 x64 | math | O(N + S + N D) | AC | 0.015 s | 1240 KB |
