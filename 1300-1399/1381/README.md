# 1381. Cockroaches in the Building

[Timus 1381](https://acm.timus.ru/problem.aspx?space=1&num=1381) · difficulty 3473 · graphs

Original problem by Andrew Rumyantsev, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An endless building has one flat per floor, each with 0 to N
cockroaches, N ≤ 30. Every month the number in a flat becomes a given
function of the numbers in that flat and the flats below and above it
last month; an empty flat between empty flats stays empty. Can the
total number of cockroaches fall in one month, starting from some
finite arrangement? Can it grow? Print `=` if neither, `<` if it can
only fall, `>` if it can only grow and `<>` if both.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

N, then N + 1 blocks of N + 1 lines of N + 1 numbers: number k of line
i in block j is the next value for a flat with j cockroaches, i below
and k above.

## Output

`=`, `<`, `>` or `<>`.

## Examples

### Example 1

Input:

```
1
0 1
0 1

0 0
1 1
```

Output:

```
=
```

### Example 2

Input:

```
2
0 0 0
0 0 0
0 0 0

1 1 1
1 1 1
1 1 1

2 2 2
2 2 2
2 2 0
```

Output:

```
<
```

## Solution

Read the floors upwards as a sequence c, empty outside a finite part.
The total changes by Σ (f(c₋, c, c₊) − c) over all floors, one term per
floor. Treat each pair of neighbouring floors (a, b) as a node of a
graph, and each next floor c as a step (a, b) → (b, c) of weight
f(a, b, c) − b. A finite arrangement is then a closed walk through the
node (0, 0), the empty pair, and its weight is the change of the total.
An empty floor between empty floors adds 0, so the endless empty parts
do not count.

So the total can fall exactly when some closed walk through (0, 0) has
negative weight. Such a walk splits into simple cycles of the part of
the graph that can be reached from (0, 0) and can reach it back. That
part has a negative closed walk exactly when it has a negative cycle,
since such a cycle can be walked around as often as needed. Keep only
that part and look for a negative cycle with Bellman–Ford, starting
from every node at distance 0. The total can grow exactly when there is
a positive cycle, which is the same search with the weights negated.
There are (N + 1)² ≤ 961 nodes and (N + 1)³ ≤ 29 791 steps.
`O(N⁵)`.

Pitfalls:

- the table is indexed by the flat itself first, then the flat below,
  then the flat above;
- a cycle away from (0, 0) does not count: no finite arrangement can
  use it;
- a shift, where every flat copies the one above, keeps the total
  (test 08).

The answers were compared with trying every arrangement of up to 10
floors for 500 random rules with N = 1 or 2.

## Language notes

- Python stops Bellman–Ford early by looking every eighth pass for a
  cycle among the last improvements, which is always a negative one;
  the other languages run up to 961 plain passes.
- Python runs under PyPy: CPython exceeds the 1.5 s limit on the judge's
  test 7, and PyPy takes about 0.53 s in all.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1381_graphs.cpp](1381_graphs.cpp) | G++ 13.2 x64 | graphs | O(N⁵) | AC | 0.171 s | 1404 KB |
| [1381_graphs.go](1381_graphs.go) | Go 1.14 x64 | graphs | O(N⁵) | AC | 0.171 s | 8084 KB |
| [1381_graphs.java](1381_graphs.java) | Java 1.8 | graphs | O(N⁵) | AC | 0.421 s | 2776 KB |
| [1381_graphs.py](1381_graphs.py) | PyPy 3.10 x64 | graphs | O(N⁵) | AC | 0.531 s | 11224 KB |
| [1381_graphs.rs](1381_graphs.rs) | Rust 1.75 x64 | graphs | O(N⁵) | AC | 0.140 s | 2384 KB |
