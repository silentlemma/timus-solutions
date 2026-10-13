# 1466. Magic Square

[Timus 1466](https://acm.timus.ru/problem.aspx?space=1&num=1466) · difficulty 3125 · backtracking

Original problem by Alexander Ipatov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A square of n² × n² cells (1 ≤ n ≤ 3) is split into n² blocks of n × n.
It is magic if it holds the numbers 0 to n² − 1 with 0 in the top left
cell, no number repeats in a row, a column or a block, and these
uniqueness rules still hold after swapping any two blocks that share a
side. Some k cells are already filled. Decide whether the square can be
completed to a magic one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and k, then k triples a, b, c: column a, row b and the number c.

## Output

"YES" or "NO".

## Examples

### Example 1

Input:

```
2 4
0 0 0
1 2 1
2 1 2
3 3 3
```

Output:

```
NO
```

### Example 2

Input:

```
2 0
```

Output:

```
YES
```

## Solution

The swap rule pins the structure down. Swapping two blocks side by side
keeps every row intact, and the columns stay valid only if, at each
offset c inside a block, both blocks hold the same set of numbers in
that column: the sets in one block column split all numbers, so a set
from the neighbour must fit exactly into its partner. Hence within a
block row all blocks share their column sets, and likewise, by vertical
swaps, within a block column all blocks share their row sets. So every
number v has a row offset π_v(J) that it takes in every block of block
column J, and a column offset σ_v(I) in every block of block row I, and
π_v, σ_v are permutations because the number appears once per row and
column of the whole square. The uniqueness and swap rules hold exactly
when, for every pair (I, J), the numbers take the n × n positions
(π_v(J), σ_v(I)) once each; conversely any such family satisfies those rules.

Up to the names of the numbers, such a family is a set of n² pairs
(π, σ), and a short search finds them all: one for n ≤ 2 and 28 for
n = 3. For each of them, a filled cell (a, b, c) names the one pair that
lands there, so number c must take that pair. The square can be
completed exactly when, for some family, no number is forced onto two
pairs and no pair onto two numbers; the free numbers take the remaining
pairs in any order. The corner 0 is treated as one more filled cell.

Pitfalls:

- an ordinary valid sudoku is usually not magic (test 09);
- 0 must sit in the corner (test 06) and cannot repeat in its row
  (test 15).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1466_backtracking.cpp](1466_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1) with 28 structures | AC | 0.031 s | 256 KB |
| [1466_backtracking.go](1466_backtracking.go) | Go 1.14 x64 | backtracking | O(1) with 28 structures | AC | 0.031 s | 1136 KB |
| [1466_backtracking.java](1466_backtracking.java) | Java 1.8 | backtracking | O(1) with 28 structures | AC | 0.140 s | 4352 KB |
| [1466_backtracking.py](1466_backtracking.py) | Python 3.12 x64 | backtracking | O(1) with 28 structures | AC | 0.328 s | 704 KB |
| [1466_backtracking.rs](1466_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1) with 28 structures | AC | 0.062 s | 436 KB |
