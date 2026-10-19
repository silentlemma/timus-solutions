# 2114. Heaviest right triangle of a given size in a grid

[Timus 2114](https://acm.timus.ru/problem.aspx?space=1&num=2114) · difficulty 1001 · prefix_sums

Original problem by Valentin Zuev, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m grid holds non-negative numbers. Water poured on cell (x₀, y₀)
covers the cells (x, y) with x ≥ x₀, y ≥ y₀ and x + y ≤ x₀ + y₀ + k, a
right triangle with legs of k + 1 cells. For each of q values of k find
a cell where the covered sum is the largest, and print the sum and the
cell. The limits are 3 seconds and 256 MB.

## Input

n and m, 1 ≤ n, m ≤ 500, the grid, 0 ≤ aᵢⱼ ≤ 10⁹, then q, 1 ≤ q ≤ 50,
and the values 1 ≤ kᵢ ≤ 10⁵.

## Output

For each k the largest sum and a cell that gives it.

## Checking

A checker accepts any cell with the largest sum.

## Examples

### Example 1

Input:

```
3 5
1 4 7 4 1
4 7 9 7 4
1 4 7 4 1
1
3
```

Output:

```
50 1 2
```

### Example 2

Input:

```
3 3
1 2 3
4 5 6
7 8 9
4
2 3 4 5
```

Output:

```
30 2 1
39 2 1
45 1 1
45 1 1
```

### Example 3

Input:

```
3 5
3 4 3 2 1
2 3 4 3 2
1 2 3 4 3
2
2 3
```

Output:

```
18 1 2
25 1 2
```

### Example 4

Input:

```
9 4
8 1 8 718
88 88 1 8
8 818 1 8
888 8 1 8
1 88 88 8
1 888 8 8
1 8 88 81
1 8 788 1
188 8 8 1
3
3 5 7
```

Output:

```
2626 1 1
2992 2 1
4001 3 1
```

### Example 5

Input:

```
15 6
888 88 1 88 8 8
88 88 1 1 88 88
8 8 111 111 8 8
88 11 1 1 11 88
8 1 88 1 881 88
8 1 88 1 88 118
811 88 1 88 1 8
8 1 88 1 88 118
8 111 1 1 111 8
81 8 1 111 8 18
88 88 1 1 88 88
8 1 88 1 88 188
8 8 188 881 8 8
88 88 1 1 88 88
888 88 1 88 8 8
5
7 13 14 8 7
```

Output:

```
3245 9 1
6371 3 1
6725 2 1
3883 1 1
3245 9 1
```

## Solution

Let T(x, y) be the sum of the triangle at (x, y). The triangle at
(x + 1, y − 1) has the same hypotenuse x + y + k. Compared with it, the
triangle at (x, y) adds the cells of row x from column y to y + k and
loses the cells of column y − 1 from row x + 1 to row x + k + 1. With
prefix sums over rows and over columns both are O(1), so

T(x, y) = T(x + 1, y − 1) + row part − column part.

For the first column there is no left neighbour: T(x, 1) is T(x + 1, 1)
plus the row part, minus the cells of the diagonal x + y = x + k + 2 below
row x, which leave the triangle as it moves up. Prefix sums along every
anti-diagonal give that part in O(1) too.

Going from the bottom row up, each row of values comes from the one
below, so a query takes O(n m), and all queries O(q n m) plus the
prefix sums. A k that reaches the far corner covers the whole grid from
(1, 1). The sums reach 2.5 · 10¹⁴ and need 64-bit integers.

In the first example the triangle from (1, 2) with k = 3 covers
4 + 7 + 4 + 1 + 7 + 9 + 7 + 4 + 7 = 50.

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 101 (3.05 s), while PyPy 3.10 is accepted in 2.0 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2114_prefix_sums.cpp](2114_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(q n m) | AC | 0.109 s | 3892 KB |
| [2114_prefix_sums.go](2114_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(q n m) | AC | 0.140 s | 14424 KB |
| [2114_prefix_sums.java](2114_prefix_sums.java) | Java 1.8 | prefix_sums | O(q n m) | AC | 0.343 s | 8400 KB |
| [2114_prefix_sums.py](2114_prefix_sums.py) | PyPy 3.10 x64 | prefix_sums | O(q n m) | AC | 2.000 s | 46644 KB |
| [2114_prefix_sums.rs](2114_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(q n m) | AC | 0.125 s | 10584 KB |
