# 1653. Death Conveyor

[Timus 1653](https://acm.timus.ru/problem.aspx?space=1&num=1653) · difficulty 5743 · geometry

Original problem by Pavel Atnashev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A space station is a regular polyhedron (one of the five Platonic
solids) centred at the origin, with a gun at every vertex pointing away
from the centre. At first one gun points along Oz and an edge from it
lies in the half-plane x ≥ 0 of Oxz. For every attack the station turns
so that the gun nearest to the attacker points straight at it, and stays
that way until the next attack. Find the total angle turned.

## Input

The name of the solid (tetrahedron, hexahedron, octahedron, dodecahedron
or icosahedron), then n (1 ≤ n ≤ 100) and n attack vectors, the
directions in which the ships fly towards the centre. The nearest gun is
never ambiguous.

## Output

The total angle in radians with 5 digits after the decimal point.

## Examples

### Example 1

Input:

```
tetrahedron
5
0.00000 0.00000 -1.00000
-1.00000 0.00000 1.00000
0.00000 0.00000 -1.00000
-1.00000 0.00000 1.00000
0.00000 0.00000 -1.00000
```

Output:

```
1.78225
```

## Solution

A ship flying along v towards the centre comes from the direction −v.
The vertices of each solid are taken from their classic coordinates
(cube corners, golden-ratio rectangles for the icosahedron and
dodecahedron) and scaled to unit length. To match the starting position,
one vertex becomes the new z axis and a neighbouring vertex, with its z
part removed, the new x axis; every choice of vertex and neighbour gives
the same station, since the solid's rotations map them onto each other.

The station's orientation is kept as a rotation matrix. For each attack,
the gun with the largest dot product with the target is the nearest. The
smallest rotation bringing it onto the target turns by the angle between
them around the axis gun × target; that angle is added to the total, and
the rotation, built with Rodrigues' formula, is composed into the
orientation. A gun already on target needs no turn. `O(V² + n · V)` for V
vertices.

Pitfalls:

- the attack vector points towards the centre, so the target is its
  opposite;
- the turn changes the orientation for all later attacks, so the
  rotations have to be composed, not just their angles summed;
- the vectors need not have unit length (test 02).

The answers match an independent accepted implementation on 120 random
tests, all with a clear nearest gun.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1653_geometry.cpp](1653_geometry.cpp) | G++ 13.2 x64 | geometry | O(V² + n · V) | AC | 0.015 s | 484 KB |
| [1653_geometry.go](1653_geometry.go) | Go 1.14 x64 | geometry | O(V² + n · V) | AC | 0.031 s | 1152 KB |
| [1653_geometry.java](1653_geometry.java) | Java 1.8 | geometry | O(V² + n · V) | AC | 0.187 s | 5208 KB |
| [1653_geometry.py](1653_geometry.py) | Python 3.12 x64 | geometry | O(V² + n · V) | AC | 0.078 s | 1176 KB |
| [1653_geometry.rs](1653_geometry.rs) | Rust 1.75 x64 | geometry | O(V² + n · V) | AC | 0.046 s | 280 KB |
