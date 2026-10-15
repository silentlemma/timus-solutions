# 1699. Turning Turtles

[Timus 1699](https://acm.timus.ru/problem.aspx?space=1&num=1699) · difficulty 1074 · trees

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On a grid field the open cells are connected in exactly one way: there
is a unique path between any two of them. Turtles move between side
neighbours, and a route costs the number of 90° turns along it. Answer
q queries: the number of turns from one open cell to another.

## Input

h and w (1 ≤ w · h ≤ 100000), the field of `#` (open) and `.` cells,
then q (1 ≤ q ≤ 50000) and the queries r1 c1 r2 c2.

## Output

The number of turns for every query, one per line.

## Examples

### Example 1

Input:

```
5 4
.#..
###.
..##
.##.
....
4
1 2 2 1
2 3 4 3
4 2 3 4
1 2 4 2
```

Output:

```
1
0
2
3
```

## Solution

The open cells form a tree. Root it at any open cell with a
breadth-first search. For every cell remember its parent, its depth,
the direction of the step from its parent, and T, the number of turns
on the way from the root. T of a child is T of its parent, plus one if
the step changes direction there.

A route between a and b climbs from a to their meeting cell m and goes
down to b. Let a′ and b′ be the children of m on the two sides. Turns
on the part from m down to b are T(b) − T(b′), and the same holds on
a's side. At m itself the route turns unless it goes straight through,
that is unless the steps into a′ and into b′ point in opposite
directions. If m is b itself, only a's side counts. Binary lifting
finds m together with a′ and b′: lift the deeper cell to just below the
other one's depth, then lift both while their ancestors differ.
`O((n + q) log n)`.

Pitfalls:

- the turn at the meeting cell is easy to miss, and so is the straight
  case where there is none (test 04);
- equal depths and a route where one end is an ancestor of the other
  need separate handling;
- a winding corridor makes the tree 50000 deep, so the searches avoid
  recursion.

The answers match a walk along every route on small fields and an
independent accepted implementation on large random, snake-like and
branchy fields.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1699_trees.cpp](1699_trees.cpp) | G++ 13.2 x64 | trees | O((n + q) log n) | AC | 0.156 s | 9112 KB |
| [1699_trees.go](1699_trees.go) | Go 1.14 x64 | trees | O((n + q) log n) | AC | 0.093 s | 21240 KB |
| [1699_trees.java](1699_trees.java) | Java 1.8 | trees | O((n + q) log n) | AC | 0.171 s | 14812 KB |
| [1699_trees.py](1699_trees.py) | Python 3.12 x64 | trees | O((n + q) log n) | AC | 0.703 s | 44716 KB |
| [1699_trees.rs](1699_trees.rs) | Rust 1.75 x64 | trees | O((n + q) log n) | AC | 0.062 s | 20416 KB |
