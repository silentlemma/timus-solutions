# 1920. Every Even Cycle Length in a Square Grid

[Timus 1920](https://acm.timus.ru/problem.aspx?space=1&num=1920) · difficulty 728 · constructive

Original problem by Alexey Samsonov, prepared by Dmitry Ivankov; NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find a simple cycle containing exactly L nodes of an n×n square grid.
Consecutive nodes, including the last and first, must be one unit apart.
Every node can be used at most once. Print a valid cycle or report that
none exists. Coordinates are integers from 1 to n in each direction.
Limits: 1 second, 64 MB.

## Input

Two integers n,L with 2≤n≤100 and 4≤L≤20,000.

## Output

If no cycle exists, print `Unsuitable device`. Otherwise print
`Overwhelming power of magic`, followed by L pairs of coordinates,
one pair per line, in traversal order. Do not repeat the first node at
the end. Any valid cycle, starting point and direction are accepted.

## Checking

A custom checker validates the heading, coordinate count, integer bounds,
distinct vertices and unit Manhattan distance for every edge, including
the closing edge. It rejects a false impossibility declaration. The
expected path is not a canonical answer and is not compared token by token.

## Examples

```
2 6
```

```
Unsuitable device
```

```
3 6
```

```
Overwhelming power of magic
1 1
2 1
3 1
3 2
2 2
1 2
```

## Solution

Color a node (r,c) by the parity of r+c. Each grid edge changes color,
so every cycle has even length. Distinctness also requires L≤n².
We prove these two necessary conditions sufficient by constructing cycles
of every even length from 4 through M=n²−(n mod 2).

Start with the boundary of a 2×2 square, a cycle of length 4.
An extension replaces an existing edge u—v by u—a—b—v, where a,b are
two unused neighboring nodes on the other side of that edge. The extension
adds two vertices, preserves all unit edges and produces one simple cycle.

Let W=n−(n mod 2), an even number. Use the following fixed extension order:

1. Extend the two-row rectangle to width W, one new column at a time.
   Replace its right vertical edge by a detour through the new column.
2. Add rows 3 through n. In each new row, process column pairs (1,2),
   (3,4), …, (W−1,W). Replace the horizontal edge immediately above a
   pair by a detour through that pair of new nodes.
3. If n is odd, add the last column using row pairs (1,2), (3,4), …,
   (n−2,n−1). Detour through each pair from the vertical edge to its left.

All required edges exist when used. The first stage retains the full
bottom boundary. Each second-stage detour creates the horizontal pair
edge needed for the next row and preserves the right vertical boundary.
The third stage uses disjoint edges of that boundary. Every new pair is
unused. Stopping halfway through a row therefore remains valid.

For even n, stage 2 includes all n² nodes. For odd n, stage 3 includes all
but the lower-right corner, giving n²−1 nodes. Since every extension adds
exactly two, stopping after (L−4)/2 extensions gives every required even
length up to M. This proves both the construction and rejection condition.

Store each directed cycle edge in a successor array indexed by r·n+c
with zero-based coordinates. When inserting an extension, first check
the edge direction; if it is reversed, reverse both old endpoints and
both new endpoints. Change three successor links, then finally traverse
exactly L vertices from the upper-left node and output one-based coordinates.

O(n²+L) time and O(n²+L) space including initialization, the successor
array and buffered output. The geometric link updates take O(1) per
two added vertices. Impossible inputs are rejected in O(1).

An odd grid cannot use all its nodes in a cycle. A maximum cycle for
odd n still uses n²−1 nodes, not just n(n−1). Do not skip the final column.
Keep both pairs of endpoints consistent when reversing an edge. Stop
after the exact number of extensions, allow an incomplete final row,
and include the closing edge without printing a repeated first node.

## Language notes

All node indices and lengths fit ordinary integers. C++, Go, Java and
Rust use flat arrays or vectors for successor links and explicit loops.
Python generates the same extension order lazily. Java, Python and Rust
buffer output; Go uses buffered I/O and C++ disables stream synchronization.
The cycle is represented by links rather than repeated insertion into a list.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1920_constructive.cpp](1920_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 472 KB |
| [1920_constructive.go](1920_constructive.go) | Go 1.14 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 1408 KB |
| [1920_constructive.java](1920_constructive.java) | Java 1.8 | constructive | O(n^2 + L) | AC | 0.125 s | 948 KB |
| [1920_constructive.py](1920_constructive.py) | Python 3.12 x64 | constructive | O(n^2 + L) | AC | 0.093 s | 2028 KB |
| [1920_constructive.rs](1920_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 296 KB |
