# 1540. Battle for the Ring

[Timus 1540](https://acm.timus.ru/problem.aspx?space=1&num=1540) · difficulty 1071 · games

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are K chains of rings (1 ≤ K ≤ 50, up to 100 rings each), every
ring with a gold content from 1 to 100. A move picks a chain and a ring
in it and removes all rings of that chain whose content is at most the
picked one's; the chain may fall apart into several. Whoever removes the
last ring wins. Gandalf moves first: print `S` if Saruman wins, or `G`
and Gandalf's winning first move, the chain and the ring, smallest
chain first and then smallest ring.

Time limit: 1 second. Memory limit: 64 MB.

## Input

K, then each chain as its length followed by the contents of its rings.

## Output

`S`, or `G` and the chain and ring numbers of the first winning move.

## Examples

### Example 1

Input:

```
2
3 1 2 1
1 1
```

Output:

```
G
1 1
```

### Example 2

Input:

```
2
3 2 1 2
1 1
```

Output:

```
S
```

## Solution

The chains are independent games, so by Sprague–Grundy the position is
lost exactly when the xor of their Grundy values is 0.

Which pieces can appear? Removing the rings up to x leaves the maximal
runs of rings above x. A later move inside such a run removes rings up
to some y > x and leaves the maximal runs above y, which are also
maximal in the whole chain. So every piece is a maximal run above some
content; these runs nest, forming a tree whose root is the chain and
where the children of a run are the runs above its smallest content.

For a run, a move with content x leaves a frontier of the tree: the
descendants whose smallest content is above x while their parent's is
not. Going through x in increasing order with a heap keyed by the
smallest content, each node is replaced by its children once, so the
xor values of all moves in a run take time linear in its subtree (times
a logarithm). The Grundy value is the mex of those values, computed
from the leaves up; with at most 2·100 runs per chain this is fast.

If the total xor T is not 0, the winning moves in chain i are those that
leave it with xor T ⊕ g(i); scanning chains and rings in order and using
the root's table of move values gives the required smallest move.
Several rings may share the winning content; the first one is named.
`O(K·L² log L)` for chains of length L.

Pitfalls:

- equal rings all go in one move, and the answer names the first of them
  (tests 05, 08);
- the first winning move may lie in a later chain (test 07);
- a chain can split into equal pieces whose values cancel (test 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1540_games.cpp](1540_games.cpp) | G++ 13.2 x64 | games | O(K * L^2 * log L) | AC | 0.031 s | 580 KB |
| [1540_games.go](1540_games.go) | Go 1.14 x64 | games | O(K * L^2 * log L) | AC | 0.015 s | 6244 KB |
| [1540_games.java](1540_games.java) | Java 1.8 | games | O(K * L^2 * log L) | AC | 0.187 s | 6460 KB |
| [1540_games.py](1540_games.py) | Python 3.12 x64 | games | O(K * L^2 * log L) | AC | 0.203 s | 1180 KB |
| [1540_games.rs](1540_games.rs) | Rust 1.75 x64 | games | O(K * L^2 * log L) | AC | 0.031 s | 816 KB |
