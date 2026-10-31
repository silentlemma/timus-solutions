# 1471. Distance in the Tree

[Timus 1471](https://acm.timus.ru/problem.aspx?space=1&num=1471) · difficulty 163 · trees

Original problem by Dmitry Zhukov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has n vertices (1 ≤ n ≤ 50000), numbered from 0 to n − 1, and
n − 1 weighted edges (weights from 0 to 1000). For each of m questions
(1 ≤ m ≤ 75000) print the length of the path between two given
vertices.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the edges as u v w, then m and the pairs of vertices.

## Output

One distance per line.

## Examples

### Example 1

Input:

```
3
1 0 1
2 0 1
3
0 1
0 2
1 2
```

Output:

```
1
1
2
```

## Solution

Hang the tree from vertex 0 and store each vertex's distance to the root.
The path between a and b goes up to their lowest common ancestor, so its
length is dist(a) + dist(b) − 2·dist(lca). The ancestor comes from the
Euler tour: a depth-first walk that writes a vertex when it enters it
and again after each child. Between the first entries of a and b the
tour passes through their ancestor and nowhere higher, so the ancestor
is the shallowest vertex on that stretch. A sparse table of minima over
stretches of length 2^k answers that with two overlapping lookups.
`O(n log n)` to build, `O(1)` per question.

Pitfalls:

- a path of 50000 vertices is too deep for recursion in most languages,
  so the walk keeps its own stack (gen3);
- vertex 0 may be a leaf, and edges come in either direction (test 03);
- a single vertex has no edges at all, and a question may name the same
  vertex twice (test 02).

## Optimized solutions

The optimized C++ solution finds the ancestor with heavy paths instead
of the Euler tour. A breadth-first walk from vertex 0 gives parents,
depths and distances with no recursion and no stack; subtree sizes are
then summed in reverse order, each vertex's heavy child is the child
with the largest subtree, and the heavy edges form chains, each vertex
remembering the top of its chain. For a question, the vertex whose chain
top is deeper jumps to the parent of that top until both are on one
chain, and the shallower of the two is the ancestor. Each jump crosses a
light edge, which at least doubles the subtree size, so a question takes
`O(log n)` jumps, and every array has `n` entries instead of the
`O(n log n)` sparse table. The numbers are parsed by hand from a 4 KB
buffer refilled with `fread`: {1471_trees_bfs.cpp}.

The optimized Go solution keeps the Euler tour and the sparse table but
parses the digits by hand from a 1 MB `bufio` reader instead of
`fmt.Fscan`, and packs the adjacency lists of both directions of every
edge into flat arrays indexed by per-vertex offsets instead of a slice
of edge structs per vertex: {1471_trees_optimized.go}.

The optimized Go solution with the `bfs` tag finds the ancestor with
heavy paths instead of the Euler tour. A breadth-first walk from vertex
0 gives parents, depths and distances with no recursion and no stack;
subtree sizes are then summed in reverse order, each vertex's heavy
child is the child with the largest subtree, and the heavy edges form
chains, each vertex remembering the top of its chain. For a question,
the vertex whose chain top is deeper jumps to the parent of that top
until both are on one chain, and the shallower of the two is the
ancestor. Each jump crosses a light edge, which at least doubles the
subtree size, so a question takes `O(log n)` jumps, and every array has
`n` entries instead of the `O(n log n)` sparse table. The numbers are
parsed by hand from a 4 KB buffer read from the standard input:
{1471_trees_bfs.go}.

The optimized Java solution with the `bfs` tag finds the ancestor with
heavy paths instead of the Euler tour. A breadth-first walk from vertex
0 gives parents, depths and distances with no recursion and no stack;
subtree sizes are then summed in reverse order, each vertex's heavy
child is the child with the largest subtree, and the heavy edges form
chains, each vertex remembering the top of its chain. For a question,
the vertex whose chain top is deeper jumps to the parent of that top
until both are on one chain, and the shallower of the two is the
ancestor. Each jump crosses a light edge, which at least doubles the
subtree size, so a question takes `O(log n)` jumps, and every array has
`n` entries instead of the `O(n log n)` sparse table. The numbers are
parsed by hand from 4 KB blocks of the input instead of
`StreamTokenizer`: {1471_trees_bfs.java}.

The optimized Python solution with the `bfs` tag finds the ancestor with
heavy paths instead of the Euler tour. A breadth-first walk from vertex
0 gives parents, depths and distances with no recursion and no stack;
subtree sizes are then summed in reverse order, each vertex's heavy
child is the child with the largest subtree, and the heavy edges form
chains, each vertex remembering the top of its chain. For a question,
the vertex whose chain top is deeper jumps to the parent of that top
until both are on one chain, and the shallower of the two is the
ancestor. Each jump crosses a light edge, which at least doubles the
subtree size, so a question takes `O(log n)` jumps, and every list has
`n` entries instead of the `O(n log n)` sparse table. The input is read
in 4 KB chunks instead of line by line, the adjacency lists are freed
before the questions, and the answers are written in batches of 1024:
{1471_trees_bfs.py}.

The optimized Rust solution finds the ancestor with heavy paths instead
of the Euler tour. A breadth-first walk from vertex 0 gives parents,
depths and distances with no recursion and no stack; subtree sizes are
then summed in reverse order, each vertex's heavy child is the child
with the largest subtree, and the heavy edges form chains, each vertex
remembering the top of its chain. For a question, the vertex whose chain
top is deeper jumps to the parent of that top until both are on one
chain, and the shallower of the two is the ancestor. Each jump crosses a
light edge, which at least doubles the subtree size, so a question takes
`O(log n)` jumps, and every vector has `n` entries instead of the
`O(n log n)` sparse table. The numbers are parsed by hand from a 4 KB
buffer instead of reading the whole input into a `String`, and the
distances are `i32`, since they are at most 49 999 · 1000 < 5 · 10⁷:
{1471_trees_bfs.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1471_trees_bfs.cpp`: time reduction +71.56%; memory reduction
  +54.89%; base: `1471_trees.cpp`.

- `1471_trees_bfs.go`: time reduction +68.80%; memory reduction +61.41%;
  base: `1471_trees.go`.

- `1471_trees_optimized.go`: time reduction +62.80%; memory reduction
  +13.02%; base: `1471_trees.go`.

- `1471_trees_bfs.java`: time reduction +8.56%; memory reduction
  +32.17%; base: `1471_trees.java`.

- `1471_trees_bfs.py`: time reduction +61.69%; memory reduction +42.82%;
  base: `1471_trees.py`.

- `1471_trees_bfs.rs`: time reduction +0.00%; memory reduction +61.97%;
  base: `1471_trees.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1471_trees.cpp](1471_trees.cpp) | G++ 13.2 x64 | trees | O(n log n + m) | AC | 0.218 s | 9772 KB | 11286556 |
| [1471_trees.go](1471_trees.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.250 s | 24328 KB | 11307211 |
| [1471_trees.java](1471_trees.java) | Java 1.8 | trees | O(n log n + m) | AC | 0.187 s | 18492 KB | 11307212 |
| [1471_trees.py](1471_trees.py) | Python 3.12 x64 | trees | O(n log n + m) | AC | 0.937 s | 44300 KB | 11307213 |
| [1471_trees.rs](1471_trees.rs) | Rust 1.75 x64 | trees | O(n log n + m) | AC | 0.046 s | 22180 KB | 11286571 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1471_trees_bfs.cpp](1471_trees_bfs.cpp) | G++ 13.2 x64 | trees, bfs | O(n + m log n) | AC | 0.062 s | 4408 KB | 11307214 |
| [1471_trees_bfs.go](1471_trees_bfs.go) | Go 1.14 x64 | trees, bfs | O(n + m log n) | AC | 0.078 s | 9388 KB | 11307215 |
| [1471_trees_optimized.go](1471_trees_optimized.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.093 s | 21160 KB | 11307220 |
| [1471_trees_bfs.java](1471_trees_bfs.java) | Java 1.8 | trees, bfs | O(n + m log n) | AC | 0.171 s | 12544 KB | 11307216 |
| [1471_trees_bfs.py](1471_trees_bfs.py) | Python 3.12 x64 | trees, bfs | O(n + m log n) | AC | 0.359 s | 25332 KB | 11307218 |
| [1471_trees_bfs.rs](1471_trees_bfs.rs) | Rust 1.75 x64 | trees, bfs | O(n + m log n) | AC | 0.046 s | 8436 KB | 11307219 |
