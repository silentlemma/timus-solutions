# 2055. Keep a connected road set with the narrowest price range

[Timus 2055](https://acm.timus.ru/problem.aspx?space=1&num=2055) · difficulty 1468 · trees, dsu, two_pointers

Original problem by Nikita Burlakov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected multigraph has n vertices and m roads with prices. Keep a
spanning tree, so that as many roads as possible are removed, and among
spanning trees minimise the difference between the largest and the
smallest kept price. The limits are 1.5 seconds and 128 MB.

## Input

The first line has n and m, 2 ≤ n ≤ 50 000, n − 1 ≤ m ≤ 50 000. Each of
the next m lines has a road `a b c`: two different ends and a price 1 ≤
c ≤ 10⁹. Parallel roads are distinct.

## Output

The numbers of the kept roads, in one line, in any order.

## Checking

A checker verifies that the roads form a spanning tree and that its
price range is optimal; any optimal tree is accepted.

## Examples

```
3 3
1 2 1
2 3 3
3 1 4
```

```
2 3
```

```
4 5
1 2 1
2 3 1
1 3 2
1 4 2
2 4 1
```

```
1 2 5
```

In the first example the three possible tree price ranges are `3−1=2`,
`4−1=3` and `4−3=1`. Roads 2 and 3 achieve the minimum one. In the
second example roads 1, 2 and 5 connect all four vertices and all cost
one, giving the absolute minimum range zero.

## Solution

### Maintain a maximum spanning forest of each prefix

A connected graph needs at least `n−1` roads, and a spanning tree
attains this bound. The first objective therefore requires a tree. Sort
the roads by price, breaking ties consistently by endpoints and original
ID, and assign distinct ranks `0,…,m−1`. We maintain a maximum-rank
spanning forest of every processed prefix.

Use one ordinary DSU for connectivity of the entire processed graph. If
a new road joins two components, include it and merge them. Otherwise it
closes a cycle in the maintained forest: find the minimum-rank edge on
the existing endpoint path, remove it and include the new road. The new
rank is larger than every old rank. Maintain a Boolean array of
currently retained ranks; a pointer advancing past deleted ranks gives
the forest's minimum price in `O(m)` total time. Deleted ranks never
reappear.

When the forest has `n−1` edges, it is a tree. The newest road is
included, so its price is the tree's maximum. Record the best difference
and its interval of sorted ranks. A difference of zero permits immediate
termination. At the end, run a fresh DSU over the saved interval and
retain any `n−1` roads that join different components. This avoids
copying a whole tree after every improvement.

### Dynamic forest and edge-node reuse

A link-cut tree represents each graph vertex and each retained road as a
node. Vertex keys are the sentinel `m+1`; an edge node's key is its
current sorted rank. Every auxiliary splay tree stores its minimum-key
node. Iterative splaying pushes pending path reversals before rotations.
The standard `makeroot(u); access(v)` exposes the entire `u–v` path in
in-order sequence, so its aggregate finds the edge to remove.

An edge node has physical degree two. After exposing `u–v`, splay its
minimum edge node `e`. Its left subtree represents `u…a` and its right
subtree `b…v`, where the old edge joins `a` and `b`. Reverse **both**
subtrees and change `e`'s key to the new rank. The represented order
becomes `a…u,e,v…b`: the old road is removed and the recycled edge node
now joins precisely the new endpoints `u,v`. Every other road and every
attached virtual branch remains intact. Reversal does not change a
minimum aggregate; recompute `e` after changing its key. This is a
topology change, not merely a new weight on the old road.

Allocate a fresh edge node only when the ordinary DSU merges components.
There are at most `n−1` such merges, so at most `2n` array slots
suffice, including the unused zero sentinel. A recycled node's index is
no longer its road rank; always retrieve the rank from its key. All path
operations are amortized `O(log n)`.

### Why the resulting range is optimal

First, the update preserves a maximum-rank forest. Joining old
components requires the only newly available crossing road. Within a
component, let `T` be the old maximum tree, `e` the new edge and `f` the
minimum edge on its cycle. A competing tree omitting `e` cannot improve
on `T+e−f`. If it contains `e`, delete `e`; some edge `g` of the old
endpoint path crosses the resulting cut. Replacing `e` by `g` gives an
old-prefix tree, whose total rank is at most that of `T`. Since
`rank(g)≥rank(f)`, the competing tree's total is at most `T+e−f`. Thus
the maintained forest is maximum.

Such a maximum tree also maximizes its minimum price within its prefix.
Otherwise delete one too-cheap tree edge. A competing tree whose edges
are all more expensive must cross the resulting cut with a larger-ranked
edge; exchanging it increases the rank sum, a contradiction.
Tie-breaking causes no problem because strict price increases imply
strict rank increases.

Take a globally optimal tree and the prefix ending with its
largest-ranked edge. Our maintained tree has no larger maximum price and
no smaller minimum price, hence no larger range. Every recorded tree is
feasible, so the best recorded range is exactly the global optimum. The
saved interval is connected; any reconstructed tree inside it has range
at most that optimum, and cannot have a smaller one by optimality. This
also proves the reconstruction correct.

## Language notes

Sorting takes `O(m log m)`, dynamic updates `O(m log n)` amortized and
reconstruction `O(m)`, for `O(m log m+m log n)` total time and `O(n+m)`
space. DSU and forest arrays use `O(n)`; the sorted roads and activity
array use `O(m)`. Rank sums are only part of the proof; implementations
never compute them. Prices and their differences fit signed 32-bit
integers.

C++, Go, Java and Rust use iterative splay/DSU operations, buffered
input and the same edge reuse with explicit helper methods. No graph
recursion or linear scan of a tree path is needed.

Do not confuse the ordinary DSU's prefix connectivity with deletions in
the maintained tree. Include price ties as separate ranked roads, retain
original IDs, and compare keys rather than recycled node indices. Push
lazy reversals before splaying, reverse both sides when reusing an edge
node, and update aggregates after changing its key. Only evaluate
complete trees. The minimum-width tree need not be the
minimum-total-price tree; ordinary Kruskal alone solves the latter
objective.

Python uses no link-cut tree. It moves two pointers over the roads
sorted by price: the right one adds roads to a DSU with rollback, and
while the window connects the graph the left one removes its cheapest
road. A DSU cannot remove its oldest road directly, so the window is
kept as a queue of two stacks: when the front stack is empty, the
window's roads are rolled back and pushed again in an order that puts
the oldest ones on top, and each road is moved O(log m) times in all.
The cheapest connected window gives the answer, and Kruskal on its roads
builds the tree. `O(m log m log n)` with union by size and no path
compression. It runs on CPython, 1.34 s of the 1.5 s on the judge; the
earlier version with the splay forest exceeded the time limit on the
judge's test 11 even under PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2055_dsu_two_pointers.py](2055_dsu_two_pointers.py) | Python 3.12 x64 | dsu, two_pointers | O(m log m log n) | AC | 1.343 s | 12480 KB |
| [2055_trees.cpp](2055_trees.cpp) | G++ 13.2 x64 | trees | O(m log m+m log n) | AC | 0.125 s | 3596 KB |
| [2055_trees.go](2055_trees.go) | Go 1.14 x64 | trees | O(m log m+m log n) | AC | 0.250 s | 9376 KB |
| [2055_trees.java](2055_trees.java) | Java 1.8 | trees | O(m log m+m log n) | AC | 0.312 s | 8148 KB |
| [2055_trees.rs](2055_trees.rs) | Rust 1.75 x64 | trees | O(m log m+m log n) | AC | 0.125 s | 9020 KB |
