# 1763. Expert Flea

[Timus 1763](https://acm.timus.ru/problem.aspx?space=1&num=1763) · difficulty 4980 · math

Original problem by Igor Chevdar, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A round table is split into n sectors numbered clockwise. Starting on
sector 1, a walker moves to a neighbouring sector or jumps over two
sectors, so from sector i to i ± 1 or i ± 3 around the circle. Count
the walks that visit every sector exactly once and come back to sector
1, modulo 10⁹ + 9.

## Input

n (6 ≤ n ≤ 10⁹).

## Output

The number of walks modulo 10⁹ + 9.

## Examples

### Example 1

Input:

```
6
```

Output:

```
12
```

## Solution

The walks are the Hamiltonian cycles of the circle with chords of
length 3, each counted in both directions. They can be counted sector
by sector: deciding the edges from each sector forward, to i + 1 and
i + 3, only the last few sectors and the three first ones, which get
their wrap-around edges at the very end, are still open. A state
records the degree of each open sector and which open ends belong to
the same path, and the cycle may close only on the very last edge.
That makes a finite set of states with fixed transitions, so the
counts obey a linear recurrence.

The recurrence was found with the Berlekamp–Massey method from the
counts for 7 to 200 sectors made by that search: it has order 19 and
stays the same whether 40 or 194 terms are used, and it reproduces
every count up to 200. The search itself agrees with a plain search
over all walks up to 33 sectors. With six sectors the jumps of +3 and
−3 land on the same sector, so 6 is answered on its own.

To get the count for large n, x^(n − 7) is reduced modulo the
recurrence's characteristic polynomial by repeated squaring, and the
resulting coefficients mix the first 19 counts. `O(k² log n)` for
k = 19.

For six sectors the walks are 12: 6 undirected cycles, each taken in
both directions.

Pitfalls:

- with six sectors the moves +3 and −3 coincide, which breaks the
  pattern of the other tables;
- some coefficients are negative and must be brought back into range;
- the count is not monotone: 9 sectors give 110 walks, fewer than 8.

The answers agree with the counts of the search for every table up to
200 sectors and with an independent accepted implementation on 80
random tables up to 10⁹ sectors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1763_math.cpp](1763_math.cpp) | G++ 13.2 x64 | math | O(k^2 log n), k = 19 | AC | 0.015 s | 380 KB |
| [1763_math.go](1763_math.go) | Go 1.14 x64 | math | O(k^2 log n), k = 19 | AC | 0.031 s | 1092 KB |
| [1763_math.java](1763_math.java) | Java 1.8 | math | O(k^2 log n), k = 19 | AC | 0.125 s | 1652 KB |
| [1763_math.py](1763_math.py) | Python 3.12 x64 | math | O(k^2 log n), k = 19 | AC | 0.093 s | 560 KB |
| [1763_math.rs](1763_math.rs) | Rust 1.75 x64 | math | O(k^2 log n), k = 19 | AC | 0.031 s | 244 KB |
