# 2017. Two consistent groups

[Timus 2017](https://acm.timus.ru/problem.aspx?space=1&num=2017) · difficulty 1332 · graphs, bitmask, bfs

Original problem by Oleg Dolgorukov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `n` people describes a location and lists the people seen there.
A testimony assigns that location to its speaker and to everyone listed.
Find a smallest **nonempty** group such that the testimonies within the
group are mutually consistent, and the testimonies outside the group are
also mutually consistent. The two groups may give different accounts of
a person's location. A missing sighting imposes no restriction: somebody
may have gone unnoticed. A valid partition is guaranteed to exist.

There are `2 ≤ n ≤ 400` people. A location is a nonempty string of at most
20 lowercase Latin letters. Each list has `0 ≤ m ≤ n−1` distinct indices,
in increasing order, between 1 and `n`, and excludes its speaker.
Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `n`. The following `n` lines describe people 1 through
`n`: location, list length `m`, then the `m` indices seen at that location.

## Output

Print the positive minimum group size on the first line and the chosen
one-based indices on the second. Any optimal group and any index order
are allowed.

## Checking

A checker verifies that the group is nonempty, that both the group and
the rest are consistent, and that the size is the smallest possible; any
optimal group is accepted.

## Examples

```
3
bar 0
bar 1 1
pool 2 1 2
```

```
1
3
```

```
3
pool 2 2 3
pool 2 1 3
pool 2 1 2
```

```
1
1
```

## Solution

For person `i`, form a bitset `C_i` containing `i` itself and everyone in its
list. Two testimonies conflict precisely when their locations differ and
`C_i ∩ C_j` is nonempty. Connect the two speakers by an undirected edge.
This includes two speakers placing a **third** person at different locations;
looking only for direct sightings between the two speakers misses such edges.
Equal locations never conflict, even if the lists differ.

A collection of testimonies is consistent exactly when it contains no edge.
Necessity follows from the shared person receiving two locations. Conversely,
without an edge, all claims about each person agree and can be extended to a
complete location assignment. Therefore both groups are consistent exactly
when every edge crosses between them: we need a proper two-coloring, not just
a vertex cover. The existence guarantee makes the graph bipartite.

Use iterative breadth-first search to color every connected component. In a
connected bipartite component, fixing one vertex's side fixes all the others;
the only two choices exchange the color classes. Take the smaller class of
each component. Components have no constraints between them, so these choices
minimize the total size independently. A tie can be broken either way.

An isolated vertex has classes of sizes one and zero, so it contributes
nothing. If the total remains zero, the graph has no edges at all; choose any
single person to satisfy the required positive size. Otherwise every component
with an edge already contributes at least one, so the independently minimized
answer is nonempty and globally optimal.

In the first example, the two `bar` testimonies agree, while the `pool`
testimony conflicts with both: choose person 3. In the second example all
locations agree, so there are no edges and any singleton is optimal.

Let `M` be the total number of listed sightings and `w` the bitset word size.
Building masks and testing every pair takes `O(M + n² ceil(n / w))` time;
coloring adds `O(n²)`. Space is `O(n² + M)` including buffered input.
With 64-bit words, at most seven words are needed for 400 people.

Pitfalls:

- Include the speaker in its own claim set.
- Detect shared third-person claims, even without a direct sighting.
- The selected group must also be consistent; a minimum vertex cover
  alone is insufficient.
- Flip each connected component separately and ignore isolated vertices
  unless the answer is empty.
- Do not require reciprocal sightings or infer a contradiction from
  somebody not being listed.

## Language notes

C++ uses `std::bitset`, Go and Rust use arrays of 64-bit words, Java uses
`BitSet`, and Python uses arbitrary-precision integer masks. Every traversal
is iterative; the same graph and component rule is used in all five programs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2017_graphs_bitmask.cpp](2017_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.015 s | 728 KB |
| [2017_graphs_bitmask.go](2017_graphs_bitmask.go) | Go 1.14 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.046 s | 4208 KB |
| [2017_graphs_bitmask.java](2017_graphs_bitmask.java) | Java 1.8 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.125 s | 5092 KB |
| [2017_graphs_bitmask.py](2017_graphs_bitmask.py) | Python 3.12 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.125 s | 5920 KB |
| [2017_graphs_bitmask.rs](2017_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.031 s | 1692 KB |
