# 1569. Networking the “Iset”

[Timus 1569](https://acm.timus.ru/problem.aspx?space=1&num=1569) · difficulty 885 · bfs

Original problem by Sergey Pupyrev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected plan joins N ≤ 100 nodes with M channels, at most one per
pair. Choose N − 1 of the planned channels that still connect all nodes
so that the largest distance between two nodes is as small as possible,
and print them.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then the two nodes of each planned channel.

## Output

The chosen channels, one pair of nodes per line. Any best network is
accepted.

## Examples

### Example 1

Input:

```
4 4
1 2
2 3
2 4
3 4
```

Output:

```
1 2
2 3
2 4
```

## Solution

This is a spanning tree of least diameter, with distances counted in
channels. The middle of any tree is
either a node, when the diameter is even, or the middle of a channel,
when it is odd. If the best tree has diameter 2r with middle node c,
every node is within r of c in that tree and so in the plan, and the
tree of shortest paths from c has diameter at most 2r. Likewise, for
diameter 2r + 1 with middle channel (a, b), every node is within r of
a or b, and the tree of shortest paths grown from both ends together,
plus the channel itself, has diameter at most 2r + 1.

So breadth-first search from every node gives all distances; each node
c scores 2·max dist(c, ·), each channel (a, b) scores
2·max min(dist(a, ·), dist(b, ·)) + 1, and the tree of shortest paths
from the best centre is the answer. This takes O(N·(N + M)) time. The
results were checked against trying every spanning tree on 300 random
small plans.

Pitfalls:

- the middle of the best tree may be a channel, giving an odd diameter
  that no node centre reaches (test 05);
- a channel centre must keep that channel in the tree;
- several best networks exist, so a checker compares the largest
  distance and that every channel is in the plan.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1569_bfs.cpp](1569_bfs.cpp) | G++ 13.2 x64 | bfs | O(N (N + M)) | AC | 0.015 s | 424 KB |
| [1569_bfs.go](1569_bfs.go) | Go 1.14 x64 | bfs | O(N (N + M)) | AC | 0.031 s | 2144 KB |
| [1569_bfs.java](1569_bfs.java) | Java 1.8 | bfs | O(N (N + M)) | AC | 0.171 s | 3664 KB |
| [1569_bfs.py](1569_bfs.py) | Python 3.12 x64 | bfs | O(N (N + M)) | AC | 0.218 s | 1576 KB |
| [1569_bfs.rs](1569_bfs.rs) | Rust 1.75 x64 | bfs | O(N (N + M)) | AC | 0.031 s | 584 KB |
