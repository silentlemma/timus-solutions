# 2087. Switch the turnouts only where the last train went elsewhere

[Timus 2087](https://acm.timus.ru/problem.aspx?space=1&num=2087) · difficulty 3536 · trees, segment_tree

Original problem by Denis Mukhametianov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A railway drawn on a grid is a tree: the depot and the stations are
leaves, the turnouts inner nodes, every edge has length 1, and each
turnout starts in a given position (forward, left or right). Trains
leave the depot one by one at given times, move one unit per time unit
and must reach given stations; a turnout may only be switched at the
moment a train reaches it. Output the fewest switches, each with its
moment, turnout and new position. Any order of the switches is
accepted. The limits are 4 seconds and 256 MB.

## Input

N and M, 2 ≤ N, M ≤ 500, the (2N − 1) × (2M − 1) map, then Q ≤ 2·10⁵
trains with their departure times and destination stations, in order of
departure.

## Output

The number of switches, then the switches `T X Y C`.

## Checking

A checker compares the number of switches and replays the trains with
the printed switches.

## Examples

### Example 1

Input:

```
3 3
S-F-X
..|..
L-R-R
|...|
X.X-R
4
1 1 3
2 3 1
4 1 3
6 3 2
```

Output:

```
4
3 1 2 R
5 1 2 F
7 1 2 R
8 2 2 L
```

### Example 2

Input:

```
2 3
S-F-X
..|..
..X..
3
1 2 2
2 1 3
4 1 3
```

Output:

```
2
2 1 2 R
3 1 2 F
```

## Solution

Trains move at the same speed and leave in order, so they pass every
turnout in departure order, a train with departure time T reaches a
turnout at depth h at moment T + h, and each turnout points where the
last train through it went (or stays in its initial position). A train
needs a switch exactly at the turnouts on its path that point away from
its station, and switching them is forced, so the minimum is the sum of
these mismatches over all trains.

The map is read into a rooted tree with depths, Euler intervals and a
heavy-path decomposition for lowest common ancestors. For every node the
leaf reached by following the initial positions is precomputed. For a
new train with destination d, start from the leaf e where the current
positions would take it from the root (the previous destination, since
the previous train set every turnout on its own path). While e ≠ d, the
lowest common ancestor j of d and e is a mismatched turnout: a switch at
moment T + depth(j) towards the child c on the way to d. Below c the
turnouts point where the latest train with a destination inside c's
subtree went, which a segment tree over the Euler order (storing the
last train for each station) finds as a range maximum; if no train has
entered that subtree yet, the initial leaf of c is used. That leaf is
the new e. Each step produces one switch of the answer, so with at most
2·10⁵ switches the total is O((Q + R) log N), where R is the answer.

In the second example the first train needs the turnout turned right at
moment 2, the second needs it forward again at moment 3, and the third
goes the same way as the second.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2087_trees_segment_tree.cpp](2087_trees_segment_tree.cpp) | G++ 13.2 x64 | trees, segment_tree | O((Q + R) log N) | AC | 0.218 s | 19964 KB |
| [2087_trees_segment_tree.go](2087_trees_segment_tree.go) | Go 1.14 x64 | trees, segment_tree | O((Q + R) log N) | AC | 0.328 s | 67884 KB |
| [2087_trees_segment_tree.java](2087_trees_segment_tree.java) | Java 1.8 | trees, segment_tree | O((Q + R) log N) | AC | 0.390 s | 27940 KB |
| [2087_trees_segment_tree.py](2087_trees_segment_tree.py) | Python 3.12 x64 | trees, segment_tree | O((Q + R) log N) | AC | 2.968 s | 111308 KB |
| [2087_trees_segment_tree.rs](2087_trees_segment_tree.rs) | Rust 1.75 x64 | trees, segment_tree | O((Q + R) log N) | AC | 0.218 s | 44632 KB |
