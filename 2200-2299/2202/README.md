# 2202. Joining point pairs by non-crossing curves around a rectangle outline

[Timus 2202](https://acm.timus.ru/problem.aspx?space=1&num=2202) · difficulty 1238 · graphs, segment_tree

Original problem by Valentin Zuev, from the University Academic School Olympiad in Informatics 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N pairs of distinct points must be joined one pair at a time by curves
that never cross each other and never touch the outline of the
rectangle (0, 0)–(W, H), except that a curve may start or end at a point
lying on the outline. Tell whether all pairs can be joined. The limits
are 3 seconds and 256 MB.

## Input

N, W and H, 1 ≤ N ≤ 10⁵, 1 ≤ W, H ≤ 10⁸, then N pairs of points with
coordinates up to 10⁸ in absolute value.

## Output

YES or NO.

## Examples

### Example 1

Input:

```
1 2 2
-1 1 3 1
```

Output:

```
YES
```

### Example 2

Input:

```
3 4 4
0 0 3 3
4 0 1 3
2 4 2 0
```

Output:

```
YES
```

### Example 3

Input:

```
3 4 4
0 0 4 4
4 0 0 4
2 4 2 0
```

Output:

```
NO
```

## Solution

The outline is a closed curve, so a pair with one point strictly inside
and the other strictly outside can never be joined: the answer is NO.

A pair with at least one point strictly inside or strictly outside
draws a curve that touches the outline in at most one point, and such
a curve never separates anything. Drawing these pairs first and the
others around them, they can be ignored.

What is left are pairs with both points on the outline. Each of their
curves is a chord that runs either entirely inside or entirely outside
the rectangle, because it cannot cross the outline. Number the points by
their position along the outline; two chords on the same side cross
exactly when their endpoints interleave. So the answer is YES exactly
when the interleaving graph of these chords is bipartite, one side for
inside and one for outside.

That graph can have Θ(N²) edges, so the coloring only builds a spanning
forest. A segment tree over outline positions stores, for each
unvisited endpoint, the position of its partner, with the minimum and
the maximum per node. A chord [l, r] crosses another chord exactly when
some endpoint strictly between l and r has its partner outside [l, r],
so one query finds an uncolored crossing chord, which gets the opposite
color and is erased from the tree. Each chord is found once.

Finally each color class is checked with a stack scan along the
outline: the chords of one class must nest properly, or the graph is
not bipartite.

In the third example the three chords join (0, 0)–(4, 4), (4, 0)–(0, 4)
and (2, 4)–(2, 0); every two of them interleave, so they form a
triangle and the answer is NO.

Sorting and the tree queries take O(N log N).

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 73 (3.015 s), while PyPy 3.10 is accepted in 1.453 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2202_graphs_segment_tree.cpp](2202_graphs_segment_tree.cpp) | G++ 13.2 x64 | graphs, segment_tree | O(N log N) | AC | 0.125 s | 9188 KB |
| [2202_graphs_segment_tree.go](2202_graphs_segment_tree.go) | Go 1.14 x64 | graphs, segment_tree | O(N log N) | AC | 0.171 s | 22444 KB |
| [2202_graphs_segment_tree.java](2202_graphs_segment_tree.java) | Java 1.8 | graphs, segment_tree | O(N log N) | AC | 0.312 s | 16340 KB |
| [2202_graphs_segment_tree.py](2202_graphs_segment_tree.py) | PyPy 3.10 x64 | graphs, segment_tree | O(N log N) | AC | 1.453 s | 33364 KB |
| [2202_graphs_segment_tree.rs](2202_graphs_segment_tree.rs) | Rust 1.75 x64 | graphs, segment_tree | O(N log N) | AC | 0.078 s | 18172 KB |
