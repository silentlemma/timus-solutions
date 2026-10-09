# 1099. Pairing night guards: maximum matching in a general graph

[Timus 1099](https://acm.timus.ru/problem.aspx?space=1&num=1099) · difficulty 1144 · matching, graphs

Original problem by Jivko Ganev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 222` guards, and a list of pairs of guards who can work
together (until the end of the input). Every guard works with at most
one partner, and nobody works alone. Schedule as many guards as possible:
print their number and the pairs.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then pairs `i j` until the end of the input.

## Output

The number of scheduled guards `C`, then `C/2` pairs.

## Checking

Any maximum set of pairs is accepted. The checker verifies that the
number equals the maximum and that every pair is allowed and uses each
guard at most once.

## Examples

### Example 1

Input:

```
3
1 2
2 3
1 3
```

Output:

```
2
1 2
```

## Solution

This is a maximum matching in a general graph, which, unlike a bipartite
graph, has odd cycles, so plain augmenting paths are not enough. Edmonds'
blossom algorithm handles them. Start with a greedy matching. Then, from
every exposed guard, grow an alternating tree by breadth-first search:
from an outer vertex `v`, a neighbour `to` that is unmatched ends an
augmenting path; a matched neighbour goes into the tree together with its
partner. When `v` meets another outer vertex, the two tree paths and the
edge between them form an odd cycle (a blossom). Its vertices get the
blossom's base (the lowest common ancestor), become outer and join the
queue, and the parent links around the cycle are set so that a path
through the blossom can still be followed. When an augmenting path is
found, flipping the matched and unmatched edges along it grows the
matching by one. `O(N³)`.

Pitfalls:

- the number of pairs is not given, so they are read until the end of
  the input;
- a pair may repeat or come in both orders, and a line that names the
  same guard twice is not a pair, so such lines are ignored;
- a graph with no pairs at all gives `0` and nothing more.

The checker relies on the expected count; the counts were checked with
the rank of a random Tutte matrix modulo a large prime, which is twice the
size of a maximum matching, on all tests and hundreds of random small
graphs.

## Language notes

- Rust keeps the arrays of the search in a `Matcher` struct, since the
  helper functions change them.
- Java and C++ build sorted adjacency lists from sets, which removes
  repeated pairs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1099_matching.cpp](1099_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.046 s | 2364 KB |
| [1099_matching.go](1099_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.046 s | 5768 KB |
| [1099_matching.java](1099_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.156 s | 5940 KB |
| [1099_matching.py](1099_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.093 s | 5612 KB |
| [1099_matching.rs](1099_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.015 s | 2044 KB |
