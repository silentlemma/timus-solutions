# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · difficulty 14456 · bidirectional

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

Two best-first searches meet in the middle: pushes from the start and
pulls from the solved position (the boxes on the goals, the player in
any free area). They share one open-addressing table of 2²² slots
(2²¹ in Java and Python); a state found by both joins the plan's halves.
Each search takes states by `g + 3h`, where h sums lone-box push
distances to the nearest goal (forward) or from the nearest initial
box cell (reverse). Matching boxes to reachable goals or starting cells
detects when they cannot all be placed. The open lists are buckets
threaded through the table, so their storage is bounded by its size.

Most of the work is in cutting dead positions:

- dead cells for a lone box: no path to a goal (forward) or from a
  starting box cell (reverse);
- frozen boxes (forward only): both axes blocked by a wall/frozen box
  on either side or dead cells on both sides, with a box off goal in
  the frozen group;
- corrals (forward only): if every push around an unreachable region
  goes inward and is ready, only those pushes are tried; an unfinished
  region with no potential boundary push is dead;
- small subsets: for every set of two to four boxes a table, built by
  a search with only those boxes, tells whether they alone can still be
  solved (for the pull search: reached from the start). Checked subsets
  contain the moved box: all pairs and triples, and quadruples within
  three rows and columns of it.

The plan is rebuilt from the move stored with each key, and the steps
between pushes come from a breadth-first walk. In the table, P is
preprocessing time, S stored states, B boxes, F the maximum freeze-check
cost and H the maximum hash-table cost.

Pitfalls:

- the boxes may already be on their goals: print an empty line (test 03);
- the player may start on a goal (`+`) and rows may start with spaces
  (test 04);
- a box on a goal walled off from the player, ignoring other boxes,
  never moves and is excluded from the search (test 05).

The plans were checked on the tests here and on about 1 500 generated
levels; in those checks, the solutions solved every random level
solved by an independent accepted implementation.

## Language notes

- Go reuses the first probe's insertion slot and computes small-subset
  indexes straight from the boxes' floor indexes: a first version,
  about 1.4 times slower than C++, gave up after 4.6 s on the judge's
  test 92, which C++ solves in 2.2 s. Go also searches until 4.85 s.

- Java keeps a table of 2²¹ keys so that the JVM fits in 64 MB and has
  the same speedups as Go. It marks a whole player area when it is
  found, builds the subset tables with bit operations and keeps the
  masks in the keys, which brought the judge's test 92 from over 5 s
  down to 4.34 s.

- Python keeps the states in compact arrays and runs under PyPy; CPython
  is several times slower. It takes about 0.5 s on the tests here, yet
  exceeds the 5 s limit on the judge's test 62, which is far heavier:
  C++ needs 2.2 s on test 92. Three different Python searches were
  tried: this bidirectional one, the same with best-first restarts and
  minimum-cost assignments of boxes to goals (test 55), and a greedy
  search by that assignment with dead cells, frozen boxes, corrals and
  tables of pairs and triples of boxes (test 56). On equal numbers of
  states Python under PyPy is about 35 times slower than C++, so passing
  would need a search that visits far fewer states. It is kept marked
  TLE: it passes all the tests here but is not claimed to fit the time
  limit on every test of the judge.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1589_bidirectional.cpp](1589_bidirectional.cpp) | G++ 13.2 x64 | bidirectional | O(P + S · B · (B³ + F + H)) | AC | 2.203 s | 54384 KB |
| [1589_bidirectional.go](1589_bidirectional.go) | Go 1.14 x64 | bidirectional | O(P + S · B · (B³ + F + H)) | AC | 3.000 s | 58376 KB |
| [1589_bidirectional.java](1589_bidirectional.java) | Java 1.8 | bidirectional | O(P + S · B · (B³ + F + H)) | AC | 4.343 s | 28700 KB |
| [1589_bidirectional.py](1589_bidirectional.py) | PyPy 3.10 x64 | bidirectional | O(P + S · B · (B³ + F + H)) | TLE (test 62) | 5.015 s | 50612 KB |
| [1589_bidirectional.rs](1589_bidirectional.rs) | Rust 1.75 x64 | bidirectional | O(P + S · B · (B³ + F + H)) | AC | 2.390 s | 55068 KB |
