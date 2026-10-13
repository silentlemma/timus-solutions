# 1401. Gamers

[Timus 1401](https://acm.timus.ru/problem.aspx?space=1&num=1401) · difficulty 159 · constructive

Original problem by Alex Samsonov, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tile a 2ⁿ × 2ⁿ board, n ≤ 9, with one cell removed by L-shaped pieces of
three cells. Print the board with 0 on the removed cell and the number
of the piece on every other cell, pieces numbered from 1 to
(4ⁿ − 1) / 3, or -1 if there is no tiling.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n, then the row and column of the removed cell.

## Output

2ⁿ lines of 2ⁿ numbers. Any tiling is accepted.

## Examples

### Example 1

Input:

```
2
1 1
```

Output:

```
0 1 3 3
1 1 4 3
2 4 4 5
2 2 5 5
```

## Solution

A tiling always exists, by halving. Split the board into four quarters;
the removed cell lies in one of them. Put one piece on the three cells
around the middle of the board that belong to the other three quarters.
Now every quarter is a 2ⁿ⁻¹ × 2ⁿ⁻¹ board with exactly one cell taken,
which is the same task, and a 1 × 1 board needs nothing. The solutions
keep the squares still to do on a stack instead of recursing, each with
its taken cell, and give the pieces numbers in the order they are put
down. `O(4ⁿ)`.

Pitfalls:

- the answer is never -1;
- a 512 × 512 board prints 262 144 numbers, so the output is
  buffered (generated tests).

The tests are judged by a checker that asks for 0 at the removed cell
only and for every number from 1 to (4ⁿ − 1) / 3 on three cells forming
an L inside a 2 × 2 square.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1401_constructive.cpp](1401_constructive.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 3760 KB |
| [1401_constructive.go](1401_constructive.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 4732 KB |
| [1401_constructive.java](1401_constructive.java) | Java 1.8 | constructive | O(4^n) | AC | 0.203 s | 13044 KB |
| [1401_constructive.py](1401_constructive.py) | Python 3.12 x64 | constructive | O(4^n) | AC | 0.375 s | 10628 KB |
| [1401_constructive.rs](1401_constructive.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.031 s | 4276 KB |
