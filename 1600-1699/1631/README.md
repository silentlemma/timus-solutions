# 1631. Drunk King 2

[Timus 1631](https://acm.timus.ru/problem.aspx?space=1&num=1631) · difficulty 489 · math

Original problem by Igor Chevdar, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A king tours an m × n chessboard with odd sides: it starts and ends in a
corner, visits every other square exactly once, never crosses its own
path, and, being drunk, never makes two moves in a row in the same
direction. Find the length of the shortest such tour, measuring between
square centres (a straight move is 1, a diagonal one √2).

## Input

One line with m and n (6 < m, n < 500, both odd).

## Output

The length of the shortest tour with precision 10⁻⁹.

## Examples

### Example 1

Input:

```
7 7
```

Output:

```
55.213203435596425732025330863145
```

## Solution

The tour is a closed path through all m · n squares, so it has exactly
m · n moves. If D of them are diagonal, the length is
m · n + D · (√2 − 1), and the task is to make D as small as possible.

Diagonals cannot be avoided. Two orthogonal moves in a row have to turn,
so at every square at most one move is horizontal and at most one is
vertical. In a row the horizontal moves therefore pair up neighbouring
squares, and with an odd number of squares at least one is left out;
the same holds for every column. Each left-out square needs a diagonal
move, so already D ≥ (m + n) / 2. This simple bound is not tight: the
remaining conditions push the least possible count up to
D = m + n + 1 (not proved here). The statement's picture of a 7 × 7 tour uses 15 diagonals,
and 49 + 15 · (√2 − 1) = 55.2132… is the expected answer. The program
prints this formula with 12 decimals; the largest value, about 2.5 · 10⁵,
still keeps an absolute error near 10⁻¹¹ in doubles. `O(1)`.

Pitfalls:

- the tour is closed, so the number of moves is m · n, not m · n − 1;
- Java formats with the default locale, which may print a decimal
  comma; `Locale.US` keeps the point.

The answers agree with an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1631_math.cpp](1631_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB |
| [1631_math.go](1631_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB |
| [1631_math.java](1631_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1800 KB |
| [1631_math.py](1631_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 412 KB |
| [1631_math.rs](1631_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 260 KB |
