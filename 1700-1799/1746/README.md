# 1746. Hyperrook

[Timus 1746](https://acm.timus.ru/problem.aspx?space=1&num=1746) · difficulty 1630 · matrix

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The cells of an n-dimensional grid have integer coordinates from 0 to
m − 1. A hyperrook moves from a cell to any cell that differs in exactly
one coordinate. For q given cells, count the routes of exactly d moves
between every two of them, modulo p.

## Input

n, m, d, p and q (1 ≤ n ≤ 50, 2 ≤ m ≤ 10⁵, 0 ≤ d ≤ 10⁹,
1 ≤ p ≤ 10⁹, 2 ≤ q ≤ 50), then the q cells.

## Output

A q × q table: the number of routes from cell i to cell j, modulo p.

## Examples

### Example 1

Input:

```
2 8 4 10000000 4
3 5
0 5
3 7
0 0
```

Output:

```
896 720 720 560
720 896 560 720
720 560 896 560
560 720 560 896
```

### Example 2

Input:

```
3 3 4 10000000 3
0 2 2
1 1 1
1 2 2
```

Output:

```
90 36 45
36 90 54
45 54 90
```

## Solution

Fix the target cell. All that matters about the current cell is h,
the number of coordinates where it differs from the target. A move
from h either sets one of those h coordinates right (h ways, to
h − 1), sets one of them to another wrong value (h(m − 2) ways, h
stays), or spoils one of the n − h right ones ((n − h)(m − 1) ways, to
h + 1). These counts form an (n + 1) × (n + 1) matrix, and its d-th
power, found by repeated squaring modulo p, gives in row h, column 0 the
number of routes from a cell at distance h to the target. Each answer
then only needs the number of coordinates where the two cells differ.
`O(n³ log d + q²n)`.

In the first example cells 1 and 2 differ in one coordinate and get
720 routes, cells 1 and 4 in two and get 560.

Pitfalls:

- p need not be prime, so the matrix power has to be taken directly,
  without dividing;
- p = 1 makes everything 0, including the routes of length 0;
- the products reach 10¹⁸ before the remainder, so 64-bit arithmetic is
  needed.

The tables match a step-by-step count over the whole grid on 150 small
random cases, and an independent accepted implementation on the large
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1746_matrix.cpp](1746_matrix.cpp) | G++ 13.2 x64 | matrix | O(n³ log d + q²n) | AC | 0.062 s | 532 KB |
| [1746_matrix.go](1746_matrix.go) | Go 1.14 x64 | matrix | O(n³ log d + q²n) | AC | 0.078 s | 2228 KB |
| [1746_matrix.java](1746_matrix.java) | Java 1.8 | matrix | O(n³ log d + q²n) | AC | 0.218 s | 4628 KB |
| [1746_matrix.py](1746_matrix.py) | Python 3.12 x64 | matrix | O(n³ log d + q²n) | AC | 0.625 s | 1084 KB |
| [1746_matrix.rs](1746_matrix.rs) | Rust 1.75 x64 | matrix | O(n³ log d + q²n) | AC | 0.062 s | 332 KB |
