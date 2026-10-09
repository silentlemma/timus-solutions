# 1035. The fewest threads for a two-sided stitch pattern

[Timus 1035](https://acm.timus.ru/problem.aspx?space=1&num=1035) · difficulty 1370 · graphs, dsu

Original problem by Pavel Zaletsky, from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sheet has a grid of `N × M` square cells (`1 ≤ N, M ≤ 200`). A stitch
covers one diagonal of one cell and lies on one side of the sheet, front or
back; each diagonal of each cell carries at most one stitch per side. A
thread makes a sequence of stitches joined at grid vertices, and two
consecutive stitches of a thread always lie on opposite sides (the needle
passes through the sheet at the shared vertex). Given the stitches on both
sides, find the smallest number of threads that make the whole pattern.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `M` (rows and columns), then `2N` lines of `M` characters: the
first `N` lines describe the front, the next `N` lines the back, seen in
the same orientation as the front. A character is `.` (no stitch), `/` or
`\` (one diagonal) or `X` (both diagonals).

## Output

The minimum number of threads.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4 5
.....
.\...
..\..
.....
.....
....\
.\X..
.....
```

Output:

```
4
```

### Example 2

Input:

```
3 3
\..
.\.
..\
...
.\.
...
```

Output:

```
2
```

## Solution

Take the grid vertices as the vertices of a graph and the stitches as
edges coloured by side. A thread is a trail whose edges alternate colours,
and the task is to split all edges into the fewest such trails.

Look at one connected group of stitches and, at every vertex `v`, at
`f(v)` front and `b(v)` back stitch ends. Inside a trail a vertex is
passed with one front and one back stitch, so at least `|f(v) − b(v)|`
trail ends lie at `v`. A trail has two ends, which gives the lower bound
`S / 2`, where `S` is the sum of `|f(v) − b(v)|` over the group, and a
group with stitches always needs at least one thread. Both bounds are
reached: if `S = 0`, every vertex is balanced and a connected graph with
balanced colours has an alternating closed trail through all of its edges
(Kotzig's theorem). Otherwise pair the missing ends with `S / 2` extra
connectors, which balances the group; the closed trail through it, cut at
the connectors, gives exactly `S / 2` threads.

So the answer is the sum over the groups of `max(1, S / 2)`. A union-find
over the `(N + 1)(M + 1)` vertices finds the groups, an array keeps
`f(v) − b(v)`. `O(N · M · α)`.

Pitfalls:

- the back is given in the same orientation as the front: a `\` on the
  back joins the same vertices as a `\` on the front;
- stitches of one side never join directly: a line of front stitches
  needs a thread for every stitch;
- a group whose vertices are all balanced still needs one thread; empty
  vertices are no groups at all, and a pattern without stitches needs 0.

## Language notes

- All languages use the same union-find with path halving; Java reads the
  rows with `BufferedReader`: `StreamTokenizer` would take `/` for the
  start of a comment.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1035_dsu.cpp](1035_dsu.cpp) | G++ 13.2 x64 | dsu | O(N·M·α) | AC | 0.015 s | 844 KB |
| [1035_dsu.go](1035_dsu.go) | Go 1.14 x64 | dsu | O(N·M·α) | AC | 0.031 s | 2276 KB |
| [1035_dsu.java](1035_dsu.java) | Java 1.8 | dsu | O(N·M·α) | AC | 0.109 s | 5076 KB |
| [1035_dsu.py](1035_dsu.py) | Python 3.12 x64 | dsu | O(N·M·α) | AC | 0.203 s | 2916 KB |
| [1035_dsu.rs](1035_dsu.rs) | Rust 1.75 x64 | dsu | O(N·M·α) | AC | 0.031 s | 1440 KB |
