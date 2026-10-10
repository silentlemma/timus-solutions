# 1197. How many squares a lone knight attacks

[Timus 1197](https://acm.timus.ru/problem.aspx?space=1&num=1197) · difficulty 28 · implementation

Original problem: folklore, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A knight stands alone on a chessboard. For each of `N ≤ 64` given
squares, count how many squares of the board the knight attacks from
there.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` squares in chess notation: a letter from `a` to `h` for
the file and a digit from `1` to `8` for the rank.

## Output

For each square, the number of attacked squares on its own line.

## Examples

### Example 1

Input:

```
3
a1
d4
g6
```

Output:

```
2
8
6
```

## Solution

A knight has eight possible jumps, two squares one way and one square
across. Try all eight and count the ones that land on the board. `O(N)`.

Pitfalls:

- near an edge or a corner only some jumps stay on the board, so every
  jump needs both coordinates checked;
- the letter is the column and the digit the row, but the board is
  symmetric, so swapping them would not change the answer.

The answers were compared with a separately written solution on all 64
squares.

## Language notes

- All languages keep the eight jumps in a table and loop over it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1197_implementation.cpp](1197_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.001 s | 396 KB |
| [1197_implementation.go](1197_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1072 KB |
| [1197_implementation.java](1197_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1576 KB |
| [1197_implementation.py](1197_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.046 s | 328 KB |
| [1197_implementation.rs](1197_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 216 KB |
