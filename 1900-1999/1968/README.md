# 1968. Recovering Colors in a Staggered Pyramid

[Timus 1968](https://acm.timus.ru/problem.aspx?space=1&num=1968) · difficulty 1641 · constructive

Original problem from the Open Ural FU Personal Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pyramid consists of unit-height blocks with 2×2 square horizontal
footprints. The bottom layer covers an m×n rectangle. Each higher layer
is shifted inward by one unit on each side and has one fewer block row
and column. Layers stop when either block-grid dimension becomes one.
Each block is red or colorless. A top-view m×n grid records, for every
unit cell, how many red blocks cover it.

Recover block colors. No red block may be exactly above a colorless
block with the same footprint. Partial overlap with a colorless block
is permitted. At least one valid coloring is guaranteed. Limits:
1 second, 64 MB.

## Input

Even integers m,n, 2≤m,n≤40, followed by m rows of n nonnegative integers:
the red-block coverage counts of the unit cells. The data are consistent
with the pyramid and the color restriction.

## Output

Describe layers from bottom to top using R for red and W for colorless.
Layer z, numbered from zero, has m/2−z rows of n/2−z characters.
Separate consecutive layers with one empty line. Any valid coloring is accepted.

## Checking

A checker verifies the sizes of the layers, the symbols, the exact top
view and that no red block stands right above a colourless block with
the same footprint; any valid colouring is accepted.

## Examples

```
4 6
0 0 1 1 0 0
0 0 1 2 1 0
0 0 0 1 2 1
0 0 0 0 1 1
```

```
WRW
WWR

WR
```

## Solution

In the sample the red bottom blocks have top-left corners (0,2) and
(2,4), using zero-based unit coordinates. The red upper block starts
at (1,3). Adding their three 2×2 projections gives the photo; overlaps
produce the two cells of value 2. These positions yield WRW/WWR below
and WR above. The upper red block partially overlaps colorless blocks,
which is allowed: their footprints are not identical.

### Recover counts for each footprint

Let F[x,y] be the number of red blocks, across all layers, whose
horizontal top-left corner is (x,y). Such a block covers four unit cells.
For the given photo A,

A[i,j]=F[i,j]+F[i−1,j]+F[i,j−1]+F[i−1,j−1],

where values outside the rectangle are zero. Process rows left to right,
from top to bottom, solving

F[i,j]=A[i,j]−F[i−1,j]−F[i,j−1]−F[i−1,j−1].

All three subtracted terms are already known. This triangular system
uniquely determines the red multiplicity of every footprint. Validity
of the input ensures nonnegative counts, zeros at impossible positions,
and enough physical blocks for each count. No clipping is needed.

### Put the red blocks at the bottom of each chain

Block (r,c) in layer z has footprint corner (x,y)=(z+2r,z+2c).
The identical footprint occurs two layers below at (r+1,c+1), not in
the adjacent layer. All such blocks form a vertical chain with levels
of one parity, beginning at level zero or one.

The color restriction forces all red blocks of a chain to precede all
colorless blocks from bottom to top. Therefore if the recovered count
is F[x,y], color exactly the lowest F[x,y] blocks red. The block at
level z has floor(z/2) aligned blocks below it, so it is red precisely
when F[z+2r,z+2c]>floor(z/2).

This construction satisfies the restriction by design and preserves
every footprint's red count. Summing those footprints therefore
reproduces A by the projection equation, proving correctness.

Let B=Σ_z(m/2−z)(n/2−z) be the number of blocks. Time and stored space
are `O(mn+B)`, including the returned layers; excluding output, extra
space is `O(mn)`. At the largest 40×40 base, B=2870.

“Exactly above” means the same 2×2 footprint. Requiring all partially
overlapped lower blocks to be red would reject the sample. Aligned
chains skip every other layer. All three terms in the inversion formula
are subtracted, including the diagonal one. The layer offset is one
unit per level, while neighboring blocks are two units apart. Preserve
blank separators and stop when either grid dimension reaches one.

## Language notes

Ordinary signed integers suffice: photo counts are at most twenty and
footprint red multiplicities at most ten. All versions store the count
matrix and construct strings per layer. Python 3.12, C++ with G++ 13.2,
Go 1.14, Java 8 and Rust 1.75 use no recursion or external libraries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1968_constructive.cpp](1968_constructive.cpp) | G++ 13.2 x64 | constructive | O(m*n+B) | AC | 0.031 s | 424 KB |
| [1968_constructive.go](1968_constructive.go) | Go 1.14 x64 | constructive | O(m*n+B) | AC | 0.031 s | 1144 KB |
| [1968_constructive.java](1968_constructive.java) | Java 1.8 | constructive | O(m*n+B) | AC | 0.125 s | 2904 KB |
| [1968_constructive.py](1968_constructive.py) | Python 3.12 x64 | constructive | O(m*n+B) | AC | 0.078 s | 600 KB |
| [1968_constructive.rs](1968_constructive.rs) | Rust 1.75 x64 | constructive | O(m*n+B) | AC | 0.015 s | 268 KB |
