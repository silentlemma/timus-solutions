# 2116. Components of a generalized knight graph on a huge board

[Timus 2116](https://acm.timus.ru/problem.aspx?space=1&num=2116) · difficulty 870 · dfs

Original problem by Kirill Deviatkin, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A generalized knight moves B cells along one axis and A cells along the
other. Place as many knights as possible on an N × N board so that no
knight can reach the cell of another by any number of moves. The limits
are 1 second and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁹, then A and B, 0 ≤ A ≤ B ≤ 3.

## Output

The largest number of knights.

## Examples

### Example 1

Input:

```
2
1
1
```

Output:

```
2
```

### Example 2

Input:

```
3
0
1
```

Output:

```
1
```

## Solution

Two knights must lie in different connected components of the move
graph, and one knight per component works, so the answer is the number
of components. For A = B = 0 a move goes nowhere, every cell is its own
component and the answer is N², which needs 64 bits.

Otherwise the board is huge, but the moves are short. Every component
is a class of some invariant of the moves, such as the parity of x + y
for A = B = 1 or the residues of x and y modulo B for A = 0, and once the
board is large enough every class is connected. For each of the nine
pairs (A, B) with B > 0 the count stops changing at N = 2B: an exhaustive
search on all boards up to 40 × 40 confirms it. So a depth-first search
on a board of side min(N, 2B), at most 6 × 6, gives the answer.

Pitfall: handle A = B = 0 before capping the board size. Its component
count is N² and does not stabilize; test [25](tests/25.in) has N = 2 and
answer 4.

In the first example A = B = 1 moves diagonally: the two diagonals of
the 2 × 2 board are separate, so two knights fit. In the second the
moves of length 1 connect every cell of the 3 × 3 board.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2116_dfs.cpp](2116_dfs.cpp) | G++ 13.2 x64 | dfs | O(B^2) | AC | 0.015 s | 412 KB |
| [2116_dfs.go](2116_dfs.go) | Go 1.14 x64 | dfs | O(B^2) | AC | 0.031 s | 1136 KB |
| [2116_dfs.java](2116_dfs.java) | Java 1.8 | dfs | O(B^2) | AC | 0.156 s | 1620 KB |
| [2116_dfs.py](2116_dfs.py) | Python 3.12 x64 | dfs | O(B^2) | AC | 0.093 s | 572 KB |
| [2116_dfs.rs](2116_dfs.rs) | Rust 1.75 x64 | dfs | O(B^2) | AC | 0.062 s | 240 KB |
