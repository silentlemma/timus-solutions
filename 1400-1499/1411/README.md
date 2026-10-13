# 1411. 40 Islands Knights

[Timus 1411](https://acm.timus.ru/problem.aspx?space=1&num=1411) · difficulty 3019 · constructive

Original problem by Alexander Klepinin, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Islands stand at every node of a W × H grid (1 ≤ W, H ≤ 50). Bridges
may join islands that are horizontal, vertical or diagonal neighbours,
and bridges may not cross. Every island must have exactly three
bridges, and the network must stay connected after any one bridge is
destroyed. Print any such map, or "Imaginary world" if there is none.

The map has 2H − 1 lines of 2W − 1 characters: `O` for an island, one
of `-|/\` for a bridge and a space elsewhere.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W and H.

## Output

A map or "Imaginary world".

## Examples

### Example 1

Input:

```
8 5
```

Output:

```
O-O-O-O-O-O O-O
|\| |  \|/|/|/|
O-O O-O O O O O
 \ / /|  /  |/|
O-O O-O-O-O O-O
|\  |    / \  |
O-O O O-O-O O-O
|/ /| |\  |\ \|
O-O-O-O-O-O-O-O
```

## Solution

Every island has three bridge ends, so 3WH is even and an odd number of
islands is impossible. A side of length 1 or 2 is impossible too: in a grid
two islands wide the two top corners force both diagonals of the first
cell, and they cross. A search program shows that 3 × 4 and 3 × 6
(and their transposes) have no map either. All other grids with sides
at least 3 and even WH have a map.

The map is glued from small blocks. The code stores precomputed bridgeless
cubic maps with the whole border built for widths 4 and 6 with heights 4 to
7, and for height 3 with widths 8, 10, 12 and 14. Two such maps are
glued along a seam by removing one border bridge on each side and
adding the two bridges that cross the seam instead: every island keeps
three bridges, and every bridge still lies on a cycle, so no single loss
can split the map.

If W is odd, H is even, so build the transposed map and transpose it
back for output, swapping `-` and `|`. Split W into 4s and a last part of
4 or 6, and H into 4s and a last part from 4 to 7 (for H = 3, W into 8s and
a last part from 8 to 14). Each row of blocks is glued along seams in
its lowest two rows, and the rows are glued along the last two columns,
so no line ends with a space. `O(WH)`.

Pitfalls:

- 6 × 3 has no map, but 8 × 3 and 3 × 8 do (tests 05, 07, 08);
- any valid map is accepted, so the tests use a checker for degrees,
  crossings and bridges;
- a seam with a single bridge would leave a bridge whose loss splits
  the map, so each seam gets two.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1411_constructive.cpp](1411_constructive.cpp) | G++ 13.2 x64 | constructive | O(WH) | AC | 0.015 s | 420 KB |
| [1411_constructive.go](1411_constructive.go) | Go 1.14 x64 | constructive | O(WH) | AC | 0.078 s | 1152 KB |
| [1411_constructive.java](1411_constructive.java) | Java 1.8 | constructive | O(WH) | AC | 0.171 s | 1732 KB |
| [1411_constructive.py](1411_constructive.py) | Python 3.12 x64 | constructive | O(WH) | AC | 0.078 s | 888 KB |
| [1411_constructive.rs](1411_constructive.rs) | Rust 1.75 x64 | constructive | O(WH) | AC | 0.062 s | 260 KB |
