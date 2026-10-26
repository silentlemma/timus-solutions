# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · difficulty 14456 · astar, greedy

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
one 64-bit key, and the area is found by growing a bit mask. Two
solutions are here: the greedy one, a single best-first search with
deadlock tests (C++, Go, Java, Rust), and the astar one, a chain of
searches with regional deadlock tables, much faster (all five
languages).

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

The astar chain orders states by the same bound, here H, with frozen
boxes on goals as walls, and cuts states the same way except for the
subset tables. The stages:

1. Cheap probes: a forward search and a pull search from the goals, 128
   expansions each, then the board in four rotations with 64 expansions
   each. Most levels end here.
2. The board in its least rotation or reflection is searched with two
   more tests. Regional tables: for the strip three cells wide along
   each side of the floor, a pull search from the strip's goals, in
   which boxes may leave the strip and new ones enter it, records every
   box set in the strip and every player area from which the strip can
   still be finished; a state whose strip is not recorded is dead.
   Packing: pulling boxes off the goals of the solved position, with the
   frozen boxes kept, shows which goals have to be filled last; a state
   that cannot match one of these residues is dead. The priority is
   `H + 30·M - depth`, where M counts the boxes missing from the nearest
   residue, so the search goes deep along a packing order. It stops
   after 600 000 states or 1 s.
3. If that fails, or its plan is longer than 10 000 moves, its memory is
   released and a second chain starts from scratch: the same probes,
   then searches with tables of all box subsets of size three and then
   five near the moved box (built by pull searches with only those
   boxes, the frozen ones as walls), and finally an A* over exact player
   cells and walking costs, which keeps every plan within 10 000 moves.

Every plan is replayed before it is printed. On the dense level the
regional and packing tests let the chain expand 2 700 states.

In the table, P is preprocessing time, E expanded states and B boxes.

Pitfalls:

- the boxes may already be on their goals: print an empty line (test
  03);
- the player may start on a goal (`+`) and rows may start with spaces
  (test 04);
- a box on a goal walled off from the player, ignoring other boxes,
  never moves and is excluded from the search (test 05);
- the plan of a search over areas can exceed 10 000 moves: one of the
  generated levels gave 44 895, and an exact search for a shorter one
  without bounds needed over 170 MB;
- the limits leave little room for the greedy search: up to 3.8 s and
  57 MB on the judge.

The plans pass the checker on the tests here and on 2 291 generated
levels, the greedy ones within 2.4 s and 63 MB each; those of
`1589_astar.cpp` also on 12 000 more levels, many of them evolved to
break the regional search, within 0.71 s and 20 MB each.

## Language notes

- Go, Java and Rust follow the C++ step by step; their plans are those
  of C++ byte for byte.
- The greedy Java ranks box subsets with plain loops and keeps every
  buffer in a primitive array: a first version exceeded the limit on the
  judge's test 88.
- Python runs the astar chain under PyPy, with a few changes for speed:
  only the first probe (the other five cost up to 0.5 s on hard levels,
  mostly in JIT compilation), no probes in the second chain, the first
  stage capped at 4.5 s and 300 000 states, and JIT settings that
  compile less (`trace_limit=3000`, no loop unrolling): on hard levels
  almost half of the time went to compiling. A child's matching goes on
  from the parent's optimal potentials with one augmentation, the strip
  tables update the subset index along with each pull, and the crossing
  distances use precomputed pulls per set of frozen boxes. The greedy
  search, at 3.8 s in C++, is out of reach for Python, and earlier
  Python searches exceeded the limit on the judge's tests 55 to 67.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1589_astar.cpp](1589_astar.cpp) | G++ 13.2 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.156 s | 12132 KB |
| [1589_astar.go](1589_astar.go) | Go 1.14 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.281 s | 25644 KB |
| [1589_astar.java](1589_astar.java) | Java 1.8 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.640 s | 20156 KB |
| [1589_astar.py](1589_astar.py) | PyPy 3.10 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 3.234 s | 49756 KB |
| [1589_astar.rs](1589_astar.rs) | Rust 1.75 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.171 s | 10488 KB |
| [1589_greedy.cpp](1589_greedy.cpp) | G++ 13.2 x64 | greedy | O(P + E · B⁴) | AC | 3.812 s | 57152 KB |
| [1589_greedy.go](1589_greedy.go) | Go 1.14 x64 | greedy | O(P + E · B⁴) | AC | 2.546 s | 58752 KB |
| [1589_greedy.java](1589_greedy.java) | Java 1.8 | greedy | O(P + E · B⁴) | AC | 4.078 s | 31196 KB |
| [1589_greedy.rs](1589_greedy.rs) | Rust 1.75 x64 | greedy | O(P + E · B⁴) | AC | 2.984 s | 55436 KB |
