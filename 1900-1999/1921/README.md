# 1921. A Grid with an Exact Longest Equal-Letter Run

[Timus 1921](https://acm.timus.ru/problem.aspx?space=1&num=1921) · difficulty 1264 · constructive

Original problem by Grigoriy Nazarov, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fill an n×m grid using only the first k uppercase Latin letters.
There must be l−1 consecutive equal letters in some row, column or
diagonal, but no l consecutive equal letters in any such direction.
Diagonals have either slope, with unit steps in both coordinates.
Equivalently, the longest straight equal-letter run must be exactly l−1.
It is permitted to leave some of the available letters unused.
Limits: 2 seconds, 64 MB.

## Input

Four integers n,m,k,l with 1≤n,m≤100, 1≤k≤26 and 2≤l≤100.

## Output

Print `NO` if no filling exists. Otherwise print `YES`, followed by n
rows of m letters each. Any filling satisfying both run conditions is valid.

## Checking

A custom checker verifies the heading, grid dimensions, allowed letters,
and the maximum equal-letter run in all four unoriented directions.
That maximum must be exactly l−1, not merely less than l.
A false `NO` is rejected using the complete feasibility criterion below.
Layouts are not compared with one particular expected grid.

## Examples

```
3 4 4 2
```

```
YES
ABCB
CDAD
ABCB
```

```
2 2 1 2
```

```
NO
```

## Solution

Write q=l−1 and d=max(n,m). If d<q, no row, column or diagonal is long
enough to contain the required run, so the answer is impossible.

If k=1, every cell is A. Its longest run is d, hence this case works
exactly when d=q. No placement choices can change that condition.

If q=1, any two horizontally, vertically or diagonally adjacent cells
must differ. A 2×2 square contains four pairwise adjacent cells and needs
four letters. A nontrivial one-dimensional grid needs two; a single cell
needs one. Thus the exact required alphabet size is min(n,2)·min(m,2).
With zero-based row r and column c, assign letter index

```text
(r mod 2) · min(m,2) + (c mod 2).
```

This also uses A and B, rather than A and C, in a single-column grid.
Distinct neighboring parity pairs give a proper filling whenever enough
letters are available.

For the remaining case q≥2 and k≥2, two letters suffice whenever d≥q.
If m≥q, use the following zero-based letter index:

```text
(r + floor(c/q)) mod 2.
```

Each row has alternating constant blocks of length q, except possibly
the last shorter block. At least one full block exists, so the required
run is present. Vertical neighbors always differ.

Along either diagonal direction, row parity changes at every step.
The block parity changes only when a block boundary is crossed.
Two diagonal neighbors can be equal only at such a crossing. Boundary
crossings are q steps apart, and q≥2, so two equal steps cannot occur
consecutively. Every monochromatic diagonal run has length at most 2≤q.
The global longest run is therefore exactly q.

If m<q, then n≥q; transpose the formula to
(c+floor(r/q)) mod 2. This exchanges rows and columns while preserving
both diagonal directions. These constructions cover every remaining
feasible case and prove that all rejections are necessary.

O(nm) time and O(nm) space including the returned grid and buffered
output. An impossible case is recognized in O(1).

A checkerboard has long monochromatic diagonals and is not a valid
general solution. Check both diagonal slopes. Avoiding length l alone
does not guarantee the required length l−1. A single available letter
must be treated separately, as must l=2. Transpose the block construction
when only the number of rows reaches q. Do not require all k letters
to appear, or emit C in a one-column case with k=2.

## Language notes

Only small integer division, parity and character arithmetic are needed.
All ports use zero-based coordinates in the formulas and map indices
to letters starting at A. Go 1.14 computes the small minimum and maximum
explicitly; the other native versions use standard operations.
All implementations buffer rows or output, and need no search or recursion.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1921_constructive.cpp](1921_constructive.cpp) | G++ 13.2 x64 | constructive | O(n*m) | AC | 0.015 s | 408 KB |
| [1921_constructive.go](1921_constructive.go) | Go 1.14 x64 | constructive | O(n*m) | AC | 0.031 s | 1104 KB |
| [1921_constructive.java](1921_constructive.java) | Java 1.8 | constructive | O(n*m) | AC | 0.109 s | 516 KB |
| [1921_constructive.py](1921_constructive.py) | Python 3.12 x64 | constructive | O(n*m) | AC | 0.093 s | 584 KB |
| [1921_constructive.rs](1921_constructive.rs) | Rust 1.75 x64 | constructive | O(n*m) | AC | 0.015 s | 240 KB |
