# 2053. Generate a planar graph with over three hundred thousand cycles

[Timus 2053](https://acm.timus.ru/problem.aspx?space=1&num=2053) · difficulty 3446 · constructive

Original problem by Alexander Ipatov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Draw a plane graph with sixteen vertices at distinct integer points and
straight edges that meet only at common ends and pass through no other
vertex, so that it has more than 300 000 simple cycles. A cycle is
counted once, regardless of its starting vertex and direction. The
limits are 1 second and 64 MB.

## Input

There is no input.

## Output

Sixteen lines with the coordinates of the vertices, each within [−1000,
1000], and then the 16 × 16 adjacency matrix as rows of 0 and 1,
symmetric with a zero diagonal.

## Checking

A checker verifies the points, the matrix and the geometry of the edges
and counts the simple cycles exactly; any valid graph is accepted. The
example of the original problem only shows the format and is not a
correct answer, so its stored output is marked `format_only` and is not
checked.

## Examples

This example only shows the format: its six vertices give just 21
cycles, so it is not a correct answer.

```

```

```
0 0
5 -6
-5 -6
-9 3
0 8
9 3
011111
101001
110100
101010
100101
110010
```

The illustration is a five-vertex rim joined to a centre. Its triangles
and larger cycles total 21; it fails both actual size and cycle-count
requirements. Our construction below instead has 16 vertices, 42 edges
and exactly 301843 cycles.

## Solution

### Construct the graph algorithmically

Use zero-based indices `v=4r+c` on a conceptual four-by-four grid. Add
every horizontal and vertical neighbour edge, giving 24 edges, and each
cell's top-left to bottom-right diagonal, giving nine more. These
indices specify a graph, not its final coordinates.

The boundary-side vertex lists are `(0,1,2,3)`, `(3,7,11,15)`,
`(15,14,13,12)` and `(12,8,4,0)`. For each side `(a,b,c,d)` add `a-d`
and `a-c`. Finally add `3-12`. All added edges are distinct, so there
are 42. The outer triangle will use vertices zero, three and twelve. The
programs generate these edges with loops; they do not store an answer
matrix.

### Compute integer coordinates

Fix vertex zero at `(-900,-900)`, vertex three at `(900,-900)` and
vertex twelve at `(0,900)`. Every remaining vertex is required to equal
the average of its neighbours. For either coordinate the thirteen
unknowns satisfy `degree(v)·p_v - sum_{internal neighbours u} p_u =
sum_{fixed neighbours u} p_u`. Build a thirteen-row augmented matrix
with two right-hand sides and solve it by Gaussian elimination with
partial pivoting. Round each component with `floor(value+0.5)`.

The system is nonsingular. Extend a vector on internal vertices by zero
on the boundary. Its quadratic form is a sum of `(x_u-x_v)²` over
internal edges and `x_v²` over edges to the fixed boundary. Vanishing
forces equal values along every edge and zero at the boundary; graph
connectivity forces the entire vector to vanish. Hence the matrix is
positive definite. A maximum principle also bounds each exact coordinate
by the extrema of the fixed coordinates: an internal strict maximum
could not be an average, and a maximum plateau propagates to the
boundary.

Rounding a general harmonic drawing is not automatically safe. Here the
graph is fixed, so we verify its actual rounded coordinates exactly.
Rational elimination gives the sixteen points in the executable
certificate below. Every rational coordinate is at least `513/46262`
away from a half-integer rounding boundary; double precision has ample
margin in this small system. All five actual programs produce this
integer certificate. Exact orientation and on-segment tests verify
distinct points, bounds, no point inside another edge and no forbidden
edge intersections. All triples of these points are also noncollinear.

### Prove the cycle count

Let `DP[M][v]` count paths visiting exactly the vertex set `M`, ending
at `v` and starting at the smallest vertex of `M`. Initialise
`DP[{v}][v]=1`. Extend a state to any unvisited neighbour greater than
its start vertex. This restriction keeps the smallest start fixed. Every
vertex-simple path appears once, by deleting its final edge and using
induction on its length.

For a set of at least three vertices, a path closes into a simple cycle
exactly when its endpoint is adjacent to its start. Sum all such states.
Every undirected cycle appears twice, once per traversal direction;
choosing the smallest start already removes rotational duplicates.
Divide by two. Since the verified straight-line embedding has no
forbidden intersections or vertex contacts, these graph cycles are
exactly valid polygonal cycles.

The counts for lengths three through sixteen are
`28,46,116,365,1140,3174,7922,17578,33714,53732,67908,63842,39852,12426`.
Their exact sum is `301843>300000`. The following complete finite
verification constructs the graph and checks geometry and every cycle
length. It is a certificate verifier, not the submitted generator; the
generator computes its coordinates from the linear system.

```python
from array import array

GRID = 4
COORDINATE_BOUND = 1000
MIN_CYCLE_LENGTH = 3
points = [(-900, -900), (-275, -647), (12, -731), (900, -900),
          (-258, -48), (-239, -415), (27, -541), (310, -669),
          (-77, 241), (-74, -67), (49, -285), (301, -502),
          (0, 900), (25, 178), (56, -72), (222, -114)]
adjacency = [0] * (GRID * GRID)

def link(a, b):
    adjacency[a] |= 1 << b
    adjacency[b] |= 1 << a

for r in range(GRID):
    for c in range(GRID):
        v = GRID * r + c
        if c + 1 < GRID:
            link(v, v + 1)
        if r + 1 < GRID:
            link(v, v + GRID)
        if r + 1 < GRID and c + 1 < GRID:
            link(v, v + GRID + 1)
corners = [0, GRID - 1, GRID * GRID - 1, GRID * GRID - GRID]
for side, a in enumerate(corners):
    d = corners[(side + 1) % GRID]
    step = (d - a) // (GRID - 1)
    link(a, d)
    link(a, d - step)
link(corners[1], corners[-1])

def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def on_segment(a, b, p):
    return orientation(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and (min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))

def geometric(points, adjacency):
    size = len(points)
    if len(set(points)) != size or any((abs(x) > COORDINATE_BOUND for p in points for x in p)):
        return False
    edges = [(a, b) for a in range(size) for b in range(a + 1, size) if adjacency[a] & 1 << b]
    for a, b in edges:
        if any((v not in (a, b) and on_segment(points[a], points[b], p) for v, p in enumerate(points))):
            return False
    for index, (a, b) in enumerate(edges):
        for c, d in edges[index + 1:]:
            if len({a, b, c, d}) < 4:
                continue
            pa, pb, pc, pd = (points[a], points[b], points[c], points[d])
            x, y = (orientation(pa, pb, pc), orientation(pa, pb, pd))
            z, w = (orientation(pc, pd, pa), orientation(pc, pd, pb))
            if x * y < 0 and z * w < 0:
                return False
            if on_segment(pa, pb, pc) or on_segment(pa, pb, pd):
                return False
            if on_segment(pc, pd, pa) or on_segment(pc, pd, pb):
                return False
    return True

def cycle_histogram(adjacency):
    size = len(adjacency)
    full = (1 << size) - 1
    paths = array('Q', [0]) * ((1 << size) * size)
    for vertex in range(size):
        paths[(1 << vertex) * size + vertex] = 1
    totals = [0] * (size + 1)
    for mask in range(1, 1 << size):
        anchor = mask & -mask
        allowed = full ^ (anchor << 1) - 1
        length = mask.bit_count()
        endpoints = mask
        while endpoints:
            bit = endpoints & -endpoints
            endpoints ^= bit
            last = bit.bit_length() - 1
            value = paths[mask * size + last]
            if not value:
                continue
            if length >= MIN_CYCLE_LENGTH and adjacency[last] & anchor:
                totals[length] += value
            choices = adjacency[last] & ~mask & allowed
            while choices:
                new_bit = choices & -choices
                choices ^= new_bit
                end = new_bit.bit_length() - 1
                paths[(mask | new_bit) * size + end] += value
    return [value // 2 for value in totals]

assert geometric(points, adjacency)
histogram = cycle_histogram(adjacency)
assert histogram[3:] == [28, 46, 116, 365, 1140, 3174, 7922,
                        17578, 33714, 53732, 67908, 63842, 39852, 12426]
assert sum(histogram) == 301843 > 300000
```

The assertions finish successfully. An independent literal vertex-simple
DFS also enumerates the same cycle histogram; it is not a count inferred
from random tests or from faces alone.

The six-vertex illustration cannot be submitted. Counting just
triangles, faces or Hamiltonian cycles is insufficient. The required
inequality is strict. A symmetric matrix alone does not ensure a legal
straight-line embedding: test vertices on edges, nonincident crossings
and collinear overlap. The grid is only a naming scheme; using its old
unrounded coordinates with the final added edge would cross edges. Keep
the three fixed boundary vertices and use a consistent `floor(x+0.5)`
rule for negative coordinates too. Count cycles up to rotation and
reversal exactly once.

## Language notes

The submitted programs build the graph and solve a system of size `V-3`,
requiring `O(V^3)` time and `O(V^2)` space, with fixed `V=16`. They do
not count cycles at runtime. The separate verifier uses `O(V^2·2^V)`
time and `O(V·2^V)` space; at sixteen vertices its path table occupies
eight MiB.

All ports use double-precision elimination and integer output. Java and Rust use primitive numeric arrays, while C++ and
Go use fixed-size graph arrays. There is no input parser or stored
coordinate lookup.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2053_constructive.cpp](2053_constructive.cpp) | G++ 13.2 x64 | constructive | O(V^3) | AC | 0.001 s | 356 KB |
| [2053_constructive.go](2053_constructive.go) | Go 1.14 x64 | constructive | O(V^3) | AC | 0.001 s | 1024 KB |
| [2053_constructive.java](2053_constructive.java) | Java 1.8 | constructive | O(V^3) | AC | 0.015 s | 368 KB |
| [2053_constructive.py](2053_constructive.py) | Python 3.12 x64 | constructive | O(V^3) | AC | 0.062 s | 668 KB |
| [2053_constructive.rs](2053_constructive.rs) | Rust 1.75 x64 | constructive | O(V^3) | AC | 0.001 s | 204 KB |
