# 1649. Abstractionism to the People

[Timus 1649](https://acm.timus.ru/problem.aspx?space=1&num=1649) · difficulty 6429 · backtracking

Original problem by Eugene Krokhalev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m canvas starts empty. Bacteria are settled one at a time, each
into an empty cell; a new bacterium adds one to every settled
neighbouring cell (up, down, left, right), and a cell that reaches 5
drops back to 1. Given the final counts (1 to 4 in every cell), find an
order of settling all cells that produces them, or report that none
exists.

## Input

n and m (1 ≤ n, m ≤ 20), then n rows of m counts from 1 to 4.

## Output

`No`, or `Yes` and the cells in settling order, one "row column" per
line. Any valid order is accepted.

## Examples

### Example 1

Input:

```
3 3
2 2 1
3 1 3
1 2 2
```

Output:

```
Yes
2 2
2 1
1 1
1 2
2 3
1 3
3 3
3 2
3 1
```

## Solution

A cell starts at 1 and gains one for each neighbour settled after it,
modulo 4. So an order works exactly when every cell v has a number of
later neighbours congruent to need(v) − 1 modulo 4, between 0 and deg(v).
It is fixed except for one case: an inner cell (four neighbours) showing
1 may have 0 or 4 later neighbours.

Peeling works from both ends of the order. A cell whose free neighbours
must all come later can be moved to the very front of any valid order
without breaking it, so it is settled first and removed. Likewise a
cell that must have no later free neighbour is settled last; its
neighbours then expect one fewer later neighbour, modulo 4. Each removal
can make more cells forced, so a stack keeps peeling, and a cell that
asks for more later neighbours than it has left proves the picture
impossible. Independent pieces of the canvas are solved one by one.

When nothing is forced, the first cell of any valid order still has all
its neighbours later, so it must be one of the undecided inner cells
showing 1. Such a cell, in any valid order, comes either before or after
all its neighbours, so branching on just one of them, first or last,
misses nothing. Two counting checks prune the search: the later-neighbour
counts must add up to the number of edges, which fixes how many
undecided cells go first, and touching undecided cells must alternate
(two firsts or two lasts cannot be neighbours), so each group of them
contributes one of its two chessboard colours; a subset-sum over the
groups tells whether the count can be met. In practice one branch
starts a cascade of forced moves either way, so the search stays tiny.
Exponential in the worst case, linear peeling per branch.

Pitfalls:

- an inner 1 is the only ambiguous count; a border 1 is always last
  among its free neighbours;
- after a neighbour is settled last, a count of 1 wraps to 4 (three later
  neighbours still required);
- the answer may be `No` even when every count is in range, as in a
  2 × 2 block of ones (test 07).

A checker replays the order; the answers agree with an independent
accepted implementation on Yes or No and pass the checker on 400 random
and adversarial canvases, including chessboard orders where every inner
cell shows 1.

Complexity: `O(2^U·(nm)^2)`, where U is the initial number of inner cells
showing 1, each tried first or last.

## Language notes

- Python raises the recursion limit: every branch nests a call.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1649_backtracking.cpp](1649_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.015 s | 276 KB |
| [1649_backtracking.go](1649_backtracking.go) | Go 1.14 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.031 s | 1388 KB |
| [1649_backtracking.java](1649_backtracking.java) | Java 1.8 | backtracking | O(2^U·(nm)^2) | AC | 0.218 s | 3508 KB |
| [1649_backtracking.py](1649_backtracking.py) | Python 3.12 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.125 s | 1136 KB |
| [1649_backtracking.rs](1649_backtracking.rs) | Rust 1.75 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.062 s | 376 KB |
