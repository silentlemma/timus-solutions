# 1485. Football and Lie

[Timus 1485](https://acm.timus.ru/problem.aspx?space=1&num=1485) · difficulty 1675 · graphs

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N teams (1 ≤ N ≤ 100) played a round robin: 3 points for a win, 1 for a
draw, 0 for a loss. Captain i said A_ij = 1 "we scored points against
j", A_ij = 0 "we scored none against j", or A_ij = −1 nothing. Every
captain either always lies or always tells the truth. Print any table B
of points, B_ij being what team i got against team j, that fits, or
"Impossible".

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N × N matrix A.

## Output

The N × N table B, or "Impossible".

## Examples

### Example 1

Input:

```
3
-1 1 0
1 -1 -1
0 1 -1
```

Output:

```
0 0 1
3 0 3
1 0 0
```

### Example 2

Input:

```
5
-1 1 1 0 0
0 -1 1 -1 -1
1 0 -1 -1 -1
0 -1 -1 -1 1
1 -1 -1 0 -1
```

Output:

```
Impossible
```

## Solution

Let T_i mean that captain i tells the truth, and s_ij that team i scored
against team j. A statement ties s_ij to T_i: s_ij = T_i for A_ij = 1,
s_ij = not T_i for A_ij = 0. A match only needs s_ij or s_ji, since one
scoring side is a win and two are a draw. Where a captain said nothing,
that side can simply score, so only pairs where both captains spoke give
a condition: a clause of two literals on the T variables.

That is 2-SAT. Build the implication graph on the 2N literals, with
not a → b and not b → a for every clause a or b, and find its strongly
connected components with Tarjan's algorithm. It is unsatisfiable exactly
when some T_i and its negation share a component. Otherwise T_i is true
when its component comes later in topological order than that of its
negation. Then every s_ij is fixed or free, and the table follows.
`O(N²)`.

Pitfalls:

- a captain who said nothing constrains nothing, and a team may play
  only unmentioned matches (tests 03, 04);
- two captains who both claim no points against each other cannot both
  be truthful (test 07);
- any fitting table is accepted, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1485_graphs.cpp](1485_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) | AC | 0.015 s | 392 KB |
| [1485_graphs.go](1485_graphs.go) | Go 1.14 x64 | graphs | O(N^2) | AC | 0.031 s | 1556 KB |
| [1485_graphs.java](1485_graphs.java) | Java 1.8 | graphs | O(N^2) | AC | 0.140 s | 1028 KB |
| [1485_graphs.py](1485_graphs.py) | Python 3.12 x64 | graphs | O(N^2) | AC | 0.109 s | 1368 KB |
| [1485_graphs.rs](1485_graphs.rs) | Rust 1.75 x64 | graphs | O(N^2) | AC | 0.015 s | 448 KB |
