# 1970. Joining Rotated Overlapping Photographs

[Timus 1970](https://acm.timus.ru/problem.aspx?space=1&num=1970) · difficulty 1254 · backtracking

Original problem from the Open Ural FU Personal Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 10×10 matrix of colors was photographed in nine overlapping 4×4
pieces. Their top-left corners, before independent rotations and
shuffling, were all pairs of coordinates from {0,3,6}. Thus adjacent
photos share one full row or column. Each photo may be rotated by a
multiple of 90 degrees, but never reflected. Reconstruct any compatible
10×10 matrix, using each of the nine input photos exactly once. A
solution exists. Limits: 1 second, 64 MB.

## Input

Nine 4×4 integer matrices. Every color is between 0 and 99 inclusive.
Consecutive matrices are separated by a blank line; whitespace otherwise
has no significance. The photo count and dimensions are fixed.

## Output

Ten rows of ten space-separated color integers. Any matrix whose nine
designated crops match all input photos under rotation is accepted.

## Checking

A checker cuts the nine pieces out of the printed matrix and matches
them with the input photos under rotations, each photo used once; any
valid matrix is accepted.

## Examples

```
1 1 9 9
1 9 1 1
9 1 1 1
9 1 1 9

9 1 1 9
9 1 1 1
9 1 1 1
9 1 1 9

9 1 1 9
9 1 1 1
1 9 1 1
1 1 9 9

9 1 1 9
1 1 1 1
1 1 1 1
9 1 1 9

9 1 1 9
1 1 1 9
1 1 9 1
9 9 1 1

9 1 1 9
1 1 1 9
1 1 1 9
9 1 1 9

9 9 1 1
1 1 9 1
1 1 1 9
9 1 1 9

9 9 9 9
1 1 1 1
1 1 1 1
9 1 1 9

9 1 1 9
1 9 9 1
1 1 1 1
9 9 9 9
```

```
1 1 9 9 9 9 9 9 1 1
1 9 1 1 1 1 1 1 9 1
9 1 1 1 1 1 1 1 1 9
9 1 1 9 1 1 9 1 1 9
9 1 1 1 1 1 1 1 1 9
9 1 1 1 1 1 1 1 1 9
9 1 1 9 1 1 9 1 1 9
9 1 1 1 9 9 1 1 1 9
1 9 1 1 1 1 1 1 9 1
1 1 9 9 9 9 9 9 1 1
```

## Solution

Precompute all four rotations of each photo. A state is a photo identity
and its orientation. Retain one copy of each distinct orientation for a
photo; identical photos remain distinct resources. Store the four edges
in natural matrix order: top and bottom left to right, left and right
top to bottom. Neighboring states are compatible precisely when their
shared edge arrays are equal; do not reverse an edge again.

Use nine positions in a 3×3 grid. Each position initially permits every
retained state. Recursively choose an unfilled position with the fewest
remaining states; break ties by the number of grid neighbors. Try each
allowed state. Remove all orientations of its photo from every remaining
position, then intersect adjacent domains with the precomputed compatible
states. If any unfilled domain becomes empty, abandon that branch.
Copy the nine small bit masks per recursive level for simple rollback.

The complete result can be globally rotated without changing validity.
Therefore the first input photo may be required to use its supplied
orientation wherever it is placed. This removes only global rotational
symmetry; it does not force that photo into a corner or the center.
There are at most 36 states, so a 64-bit mask suffices.

### Correctness

Every chosen state is an allowed photo rotation. Removing its entire
photo mask prevents reuse. Domain intersections enforce exactly the
equalities with already placed neighbors, so no branch containing a
compatible completion is pruned. The position heuristic only changes
search order. Any valid arrangement can be globally rotated so that the
first photo has orientation zero, and duplicate orientations are identical;
hence these reductions preserve at least one valid arrangement.

At a complete assignment, all horizontal and vertical shared edges agree.
Where four photos meet, corner equality follows transitively through the
adjacent shared edges; no additional diagonal condition is needed. The
4×4 windows at offsets 0,3,6 cover the entire 10×10 board. Copying their
cells therefore yields one consistent board using every photo once.
Exhaustive branching and the existence guarantee ensure a result is found.

For m photos of side s, a conservative search bound is
`O((4m)²s + m!·4^m·m²)` time and `O(m²+ms²)` memory, including copied
domains on the recursion stack. Here m=9, s=4, and propagation sharply
reduces the explored branches. This is exponential search, not a
polynomial-time guarantee for variable-sized puzzles.

In the example, crop output rows 0…3 and columns 0…3: it is exactly the
first input photo. The middle-left crop, rows 3…6 and columns 0…3, is
the second input photo. Both have shared row `9 1 1 9`. The remaining
seven crops similarly use each remaining photo once; joining all nine
produces the printed 10×10 pattern.

The stride is three, not four: the photos overlap. Only rotations are
permitted. Match full four-color edges in consistent coordinate order.
Do not reuse a photo even if its values equal another photo. Global
rotation allows fixing one orientation, not one position. Use 64-bit
masks because 36 states exceed a 32-bit integer. Restore placement on
backtracking; copied domains alone do not restore the selected-state array.

## Language notes

Python uses arbitrary-size integers and bit_count. C++, Go 1.14, Java 8
and Rust 1.75 use 64-bit masks and their bit-count/trailing-zero routines.
Java creates a fresh Solver per input. Depth is at most nine in all versions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1970_backtracking.cpp](1970_backtracking.cpp) | G++ 13.2 x64 | backtracking | O((4*m)^2*s+m!*4^m*m^2) | AC | 0.015 s | 400 KB |
| [1970_backtracking.go](1970_backtracking.go) | Go 1.14 x64 | backtracking | O((4*m)^2*s+m!*4^m*m^2) | AC | 0.031 s | 1120 KB |
| [1970_backtracking.java](1970_backtracking.java) | Java 1.8 | backtracking | O((4*m)^2*s+m!*4^m*m^2) | AC | 0.140 s | 1824 KB |
| [1970_backtracking.py](1970_backtracking.py) | Python 3.12 x64 | backtracking | O((4*m)^2*s+m!*4^m*m^2) | AC | 0.078 s | 1044 KB |
| [1970_backtracking.rs](1970_backtracking.rs) | Rust 1.75 x64 | backtracking | O((4*m)^2*s+m!*4^m*m^2) | AC | 0.015 s | 236 KB |
