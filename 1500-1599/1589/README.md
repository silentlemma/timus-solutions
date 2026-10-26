# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · difficulty 14456 · greedy

Original problem by Stanislav Vasiliev and Sergey Pupyrev, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Sokoban level of at most 8 × 8 cells: walls `#`, goals `.`, boxes `$`
(`*` on a goal) and the player `@` (`+` on a goal). The player walks on
free cells and may push one box at a time by walking into it, never
pull it. Print a plan that brings every box onto a goal: the moves `u`,
`d`, `l`, `r`, in upper case when they push a box, at most 10 000 of
them. A solution always exists, and any valid plan is accepted.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

The level, row by row; rows may be ragged and have spaces outside the
walls.

## Output

One line with the plan.

## Examples

### Example 1

Input:

```
########
#@  $ .#
########
```

Output:

```
rrRR
```

### Example 2

Input:

```
######
##   .#
#@  ###
#   * #
#   $ #
#     #
#######
```

Output:

```
dddrrrruLdlUUUluRR
```

## Solution

The search runs over pushes, not steps. A state is the set of boxes and
the area the player can walk to, named by its lowest cell; both fit in
one 64-bit key, and the area is found by growing a bit mask.

The greedy search takes states by `pushes + 20·h`, where h is the least
total number of pushes that lone boxes need to reach distinct goals (the
Hungarian method); the large weight makes the search nearly greedy. A
state is dropped when:

- a box would stand on a dead cell, from which a lone box reaches no
  goal;
- boxes off goals stay frozen: none can move along either axis even with
  every movable box taken away step by step, or none can be pushed by
  the player even with every pushable box taken away and the player's
  area grown;
- the matching has no finite cost;
- some set of two, three or four boxes containing the moved one cannot
  be solved on its own: for every such set a table, built by pull
  searches from every set of goals of that size, holds the player cells
  from which it can.

A corral, an area the player cannot enter with an unfinished box on its
border or a goal inside, whose border pushes all go inward (and stay the
same with the outside boxes gone), restricts the moves to those pushes.
The states seen are kept in an open-addressing set of keys and the nodes
in a flat array; the plan is rebuilt from the move stored with each
node, and the steps between pushes come from a breadth-first walk.

On a dense level from the forum, 13 boxes on 36 cells, more than 30
million states are reachable from the start and 22 million from the
solved position, but only about 6 300 lie on both sides; the greedy
search needs 1.8 s there.

In the table, P is preprocessing time, E expanded states and B boxes.

Pitfalls:

- the boxes may already be on their goals: print an empty line (test
  03);
- the player may start on a goal (`+`) and rows may start with spaces
  (test 04);
- a box on a goal walled off from the player, ignoring other boxes,
  never moves and is excluded from the search (test 05);
- the limits leave little room for the greedy search: up to 3.8 s and
  57 MB on the judge.

The plans pass the checker on the tests here and on 2 291 generated
levels, the greedy ones within 2.4 s and 63 MB each.

## Language notes

- Go, Java and Rust follow the C++ step by step; their plans are those
  of C++ byte for byte.
- The greedy Java ranks box subsets with plain loops and keeps every
  buffer in a primitive array: a first version exceeded the limit on the
  judge's test 88.
- Python has no solution here: the greedy search needs 3.8 s in C++, and
  earlier Python searches, among them a bidirectional one, exceeded the
  limit on the judge's tests 55 to 67.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1589_greedy.cpp](1589_greedy.cpp) | G++ 13.2 x64 | greedy | O(P + E · B⁴) | AC | 3.812 s | 57152 KB |
| [1589_greedy.go](1589_greedy.go) | Go 1.14 x64 | greedy | O(P + E · B⁴) | AC | 2.546 s | 58752 KB |
| [1589_greedy.java](1589_greedy.java) | Java 1.8 | greedy | O(P + E · B⁴) | AC | 4.078 s | 31196 KB |
| [1589_greedy.rs](1589_greedy.rs) | Rust 1.75 x64 | greedy | O(P + E · B⁴) | AC | 2.984 s | 55436 KB |
