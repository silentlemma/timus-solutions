# 1912. Escaping While Staying Adjacent

[Timus 1912](https://acm.timus.ru/problem.aspx?space=1&num=1912) · difficulty 1267 · bfs

Original problem by Stanislav Vasilyev, prepared by Denis Mukhametianov, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two participants occupy different cells of a rectangular room grid. Their
rooms share a side or corner, and this adjacency must be maintained.
One participant at a time may cross a thin orthogonal wall, paying one
passage; thick walls cannot be crossed. They cannot occupy the same room.
The exterior has no walls and walking there is free. Find the minimum
total thin-wall passages needed for both participants to get outside,
or report that escape is impossible. Limits: 1 second, 64 MB.

## Input

First n,m with 2≤n,m≤250. Then exactly 2n+1 lines of 2m+1 characters.
Room centers are at odd row and column indices in the drawing, counting
from zero. `1` and `2` mark the initial rooms; a space marks an empty room.
`+` marks a corner, `.` a thin wall, and `-` or `|` a thick wall.
The two initial rooms are distinct and share at least a corner.
Preserve spaces when reading the drawing. Adjacency allows diagonal
neighbors, but crossing between rooms is only through an orthogonal wall.

## Output

Print the minimum total passages, or `Death` if both cannot escape.

## Checking

One exact integer or the exact token `Death`, checked token by token.

## Examples

```
3 4
+.+-+-+-+
| . .1. |
+-+-+-+.+
| .2. . |
+.+.+.+-+
| . | | |
+.+.+-+-+
```

```
13
```

```
2 2
+-+-+
.1|2.
+-+-+
| | |
+-+-+
```

```
Death
```

## Solution

Search joint positions rather than separate shortest paths. Even if both
participants can escape independently, moving one may break adjacency;
the second example demonstrates this.

Add a one-cell exterior ring around the room grid. A thin-wall crossing,
including a perimeter wall, costs one. Adjacent exterior positions are
connected by free walking edges. While one participant is still inside,
the other's relevant exterior positions are within one cell of that
boundary room, so this ring is sufficient. Those exterior neighbors form
an orthogonally connected strip or corner L. Free diagonal exterior walks
can therefore be replaced by orthogonal ones. A shared exterior position
can also be avoided by a free repositioning before the final exit.
Thus distinct positions and orthogonal moves in this finite ring preserve
the optimum. Do not collapse the exterior into one giant vertex: it would
incorrectly allow the second example to escape.

The participants have identical abilities and the goal treats them equally.
Sort their linear cell indices a<b, forgetting their labels. Their relative
offset is one of (0,1), (1,−1), (1,0), (1,1). With padded width W, encode
the state as `4·a+orientation`; the second cell is a plus one of
1,W−1,W,W+1. Identity swapping is a graph symmetry, so this quotient loses
no feasible path or cost.

For each orientation, precompute the legal relative moves from the eight
candidates: two participants times four orthogonal directions. Reject
coincidence and loss of adjacency, canonicalize the new pair, and retain
the acting participant, wall-direction bit, encoded-state change and
actor-position offset. Only four relative moves remain. At runtime a
four-bit wall mask checks actual legality and padded-grid bounds.

Run 0-1 BFS. A crossing costs one; exterior walking costs zero. Put zero
edges at the front of the deque and unit edges at the back. Record a state
as finalized when popped, and stop at the first popped state with both
positions outside. Stop neither when only one has escaped nor merely on
discovering a goal, since zero-cost edges affect priority.

Every legal move is represented and every represented move is physically
legal, with the correct crossing cost. The finite exterior and identity
quotient preserve all optima, and 0-1 BFS finds the minimum-cost goal.
If the queue empties, escape is impossible.

There are at most 4(n+2)(m+2)≤254 016 states and four candidate edges per
state. Time and storage are O(nm). Distances fit signed 32 bits: a shortest
path needs no repeated-state cycle and each edge costs at most one.

## Language notes

All ports use packed distance and wall arrays, with precomputed transitions
to avoid sorting or hash lookups during the search. Python 3.12 uses `array`
and byte arrays. Go 1.14 and Java 8 use growing integer ring deques, avoiding
boxed queue nodes; C++ and Rust 1.75 use standard deques. Read the ASCII
scheme by complete lines, stripping only line terminators. No recursion
depends on maze size.

The answers agree with a plain Dijkstra over labelled participant pairs
on all 24 576 configurations of a 2 × 2 room and on 200 random small
mazes; closed forms check 250 × 250 fields.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1912_bfs.cpp](1912_bfs.cpp) | G++ 13.2 x64 | bfs | O(nm) | AC | 0.015 s | 1632 KB |
| [1912_bfs.go](1912_bfs.go) | Go 1.14 x64 | bfs | O(nm) | AC | 0.031 s | 3116 KB |
| [1912_bfs.java](1912_bfs.java) | Java 1.8 | bfs | O(nm) | AC | 0.140 s | 4296 KB |
| [1912_bfs.py](1912_bfs.py) | Python 3.12 x64 | bfs | O(nm) | AC | 0.765 s | 2532 KB |
| [1912_bfs.rs](1912_bfs.rs) | Rust 1.75 x64 | bfs | O(nm) | AC | 0.031 s | 1992 KB |
