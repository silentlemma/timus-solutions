# 1985. A prime-rich column in a Hamiltonian labeling

[Timus 1985](https://acm.timus.ru/problem.aspx?space=1&num=1985) · difficulty 1970 · constructive

Original problem by Mikhail Rubinchik, with special thanks to Alexander Ipatov, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fill an `n×n` grid with the integers from 1 through `n²`, each exactly
once. Cells containing consecutive integers must share a side. The score
of a column is its number of prime entries; maximize the largest column
score, and output any maximizing grid. The input satisfies `1≤n≤256`.
Time limit: 1 second; memory limit: 64 MB.

## Input

One integer `n`.

## Output

An optimal grid, with `n` rows of `n` integers.

## Checking

A checker verifies the permutation, the side adjacency of consecutive
numbers and that the best column has the optimal number of primes; any
optimal grid is accepted.

## Examples

Input:

```
4
```

Output:

```
2 1 12 11
3 16 13 10
4 15 14 9
5 6 7 8
```

## Solution

Think of the labels as the order of a Hamiltonian walk. Each visit
writes the next integer. All coordinates below are zero-based.

### Optimal score

Checkerboard colors alternate along the walk. All odd labels have one
color; every prime except 2 is odd. A column therefore contains at most
`ceil(n/2)` odd primes and possibly 2, giving the bound `ceil(n/2)+1`.

For `n=1` the score is zero. For `n=3` it is two. To see the latter, the
walk starts on the majority checkerboard color, so the middle column has
only one odd label. A boundary column could have three primes only with
2 in its middle cell. Then 1 is the horizontal neighbor and 3 one
vertical neighbor. Starting from that corner, labels 4 through 9 are
forced around the remaining perimeter; the other endpoint of the
boundary column receives 9, which is composite. Reflection covers the
other positions. A row snake attains two. Use a row snake for these two
small odd sizes. For all other sizes the construction below attains the
bound.

### Preprocessing and a detour

Sieve primes through `n²`, and build `next[x]`, the smallest prime
strictly greater than `x`, or zero if none exists. A gap `g` between odd
primes is even. A detour of width `t=(g−2)/2`, consisting of `t`
horizontal steps, one vertical step, `t` steps back, and one further
vertical step, advances the label by `g` while changing the row by two.
Record each detour width for filling the unused part later.

### Even size

Write 1 at `(0,1)`, 2 at `(0,0)`, and 3 at `(1,0)`. Use
right/down/left/down detours to put successive odd primes in column 0 at
rows `1,3,…,n−1`. Each detour consumes equal left prefixes of two rows;
require `t<n−1` so at least one column remains on their right.

From the bottom prime, traverse the rest of the bottom row to the right.
Fill the remaining row pairs upward: the lower row from right to its
first unused cell, then the upper row from that column back to the
right. Finally fill unused top-row cells from right to column 2. This
visits every cell once. Column 0 contains `n/2` odd primes and 2,
achieving `n/2+1`.

### Odd size at least five

Use column 2 as the target, with a strip of width two on its left and
width `w=n−3` on its right. Find `a` from 0 through `w`, excluding
`w−1`, such that `p=3+2a` and `q=p+2n` are prime. Starting from `q`,
also check that the next `(n−3)/2` prime gaps have widths `0≤t<w`, with
each next prime at most `n²`. Discard a candidate if any check fails.

1. Write 1 at `(1,1)` and 2 at `(1,2)`. Go right `a` cells on row 1, up
   to row 0, then left `a` cells. The current label is prime `p` at
   `(0,2)`.
2. Fill the entire left strip except the already written 1: visit
   `(0,1),(0,0),(1,0),(2,0),(2,1)`, then for each odd row `r=3,5,…,n−2`
   visit `(r,1),(r,0),(r+1,0),(r+1,1)`. Enter `(n−1,2)`, whose label is
   `q=p+2n`.
3. Ascend the target column by right/up/left/up detours. The successive
   even rows `n−3,n−5,…,2` receive successive primes. Each right-strip
   row pair retains an equal unused suffix.
4. Let `L=3+a`. If `L=n`, the top two right strips are already filled:
   simply traverse row 2 to the right. Otherwise `m=n−L≥2`. Traverse row
   2 up to column `L`, go to `(1,L)`, then `(0,L)`, cross row 0 to the
   right edge, cross row 1 back to `L+1`, and cross row 2 from `L+1` to
   the right edge. This fills the remaining top-right rectangle.
   Excluding `a=w−1` avoids the impossible single-column version of this
   step.
5. Fill the lower right-strip row pairs downward, starting with rows 3
   and 4: the upper row right-to-left to its unused boundary, then the
   lower row left-to-right. Use the recorded widths.

The left strip and all remaining right suffixes are disjoint. Every
transition joins neighboring cells, including joins between pairs. Thus
the labels form a Hamiltonian walk. Every even row of column 2 contains
an odd prime, and row 1 contains 2: its score is `(n+1)/2+1`.

### Finite prime conditions and complexity

The prime-width conditions are verified over the entire stated domain,
rather than assumed from an unproved theorem about primes. An
independent trial-division check covers all 128 even sizes and all 126
odd sizes at least five. Every odd size has an admissible prefix. The
largest observed even detour is 8, the largest selected initial odd
width is 14, and the largest ascending odd width is 16; the
size-specific spare-width inequalities also hold. These finite checks
can be reproduced by running the candidate search for each permitted
size. All 256 complete constructions are additionally checked for
permutation, adjacency, and optimality.

In the sample, the first column is `2,3,4,5`, containing three primes,
which equals the upper bound for `n=4`.

The sieve takes `O(n² log log n)` time. The next-prime table, grid
traversal and candidate checks take `O(n²)` time: there are `O(n)`
candidates with `O(n)` constant-time prime transitions each. Memory is
`O(n²)`, and writing the grid itself requires `n²` entries.

Pitfalls:

- 1 is not prime; 2 is the only even prime.
- The exception `n=3` has optimum 2, not 3.
- A valid Hamiltonian labeling can still have a suboptimal column score.
- The next-prime query must be strictly greater than the current label.
- Preserve the recorded detour widths when filling the remaining strips.
- The finite prime certificate applies to `n≤256`; no claim about all
  larger sizes is needed.

## Language notes

All five versions use the same construction, a sieve, and constant-time
next-prime lookups. Python uses a byte array for primality. C++, Go and
Java use integer labels; Rust uses `usize` indices. The largest label is
65,536. Output is buffered or assembled in memory.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1985_constructive.cpp](1985_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 568 KB |
| [1985_constructive.go](1985_constructive.go) | Go 1.14 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 2796 KB |
| [1985_constructive.java](1985_constructive.java) | Java 1.8 | constructive | O(n^2 log log n) | AC | 0.140 s | 6440 KB |
| [1985_constructive.py](1985_constructive.py) | Python 3.12 x64 | constructive | O(n^2 log log n) | AC | 0.109 s | 4260 KB |
| [1985_constructive.rs](1985_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2 log log n) | AC | 0.031 s | 1212 KB |
