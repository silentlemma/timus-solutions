# 1923. Two Alternating Regions on a Colored Grid

[Timus 1923](https://acm.timus.ru/problem.aspx?space=1&num=1923) · difficulty 546 · bfs

Original problem: folklore, prepared by Dmitry Karpenko; Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n×m grid has digits 0..9 as colors. Side-adjacent cells of one color
form a country. The first side initially owns the entire country containing
the lower-left cell; the second owns the country containing the upper-right
cell. These initial colors differ. The sides alternate turns, starting
with the first. On a turn, the active side changes its alliance to the
given color, retaining all territory and annexing adjacent countries of
that color. It never chooses its own current color or the opponent's
current color. Given the legal sequence of choices, find both final areas.
Each cell has area one. Limits: 1 second, 64 MB.

## Input

Two integers n,m, 2≤n,m≤50, followed by n digit strings of length m.
Then l, 2≤l≤100, followed by exactly l chosen colors in chronological
order. Colors are integers 0..9; whitespace may separate them arbitrarily.

## Output

Print the first side's final area on the first line and the second side's
area on the second line, preserving the lower-left/upper-right order.

## Checking

Compare the two integer tokens exactly, in that order.

## Examples

```
6 12
000233434133
000233434143
001223434133
101023434143
101223434133
110233434143
4
0 4 2 1
```

```
23
18
```

## Solution

Keep an owner for each cell: neutral, first side or second side. Store a
list of cells owned by each side and precompute each cell's four valid
side neighbors. The original digit of a neutral cell never changes.
Once a cell is owned, its original digit no longer determines ownership.

Initialize both corner cells as owned and expand through neutral cells
with the corresponding initial digit. This finds each complete initial
country, rather than merely reserving one corner cell.

For a move choosing color c, scan all cells of the active territory as a
queue. For each neutral neighbor with original color c, assign its owner
immediately and append it to the same queue. Continue through newly
appended cells during this turn. This takes every cell of each adjacent
country, not just its boundary. Existing owned cells remain in the list,
even after the side changes alliance many times.

There is no need to repaint stored digits or remember current alliance
colors in the simulation. The input already guarantees valid choices.
Neutral colors stay original; owned cells are identified exclusively by
the owner array. An opponent's cell is always blocked, regardless of its
original digit.

For correctness, assume each list is exactly its connected owned region.
This holds after the initial floods. During a move, any appended cell
is neutral, has the chosen color and is adjacent to an already owned or
newly appended cell, so its country must be annexed. Conversely, a path
through any neighboring chosen-color country is exhausted by the queue,
so all required annexations happen. Marking before appending prevents
duplicates, while owner checks prevent taking the opponent's territory.
The lists keep all old cells, preserving the invariant after every turn.
Their final lengths are therefore the requested areas.

Each expansion scans at most nm cells with at most four neighbors.
Time is O((l+1)nm). Owners, adjacency and territory lists use O(nm)
space; including the stored move sequence, total space is O(nm+l).

Use the lower-left and upper-right corners, not the opposite pair.
Flood complete initial countries. Keep all previously claimed territory
and process newly claimed cells before ending a turn. Diagonal contact
does not imply adjacency; horizontal neighbors must not wrap between
rows. A cell's original color cannot override its nonneutral owner.
Handle odd l without inventing an extra move. Test sequences must exclude
both current alliance colors at each turn.

## Language notes

Cell (r,c) is encoded as r·m+c with zero-based coordinates. C++, Go,
Java and Rust use a cursor whose bound follows the growing territory.
Python's list iteration visits appended cells in the same pass.
Java uses flat bounded arrays for the two queues; the other versions
use dynamic lists or vectors. All searches are iterative.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1923_bfs.cpp](1923_bfs.cpp) | G++ 13.2 x64 | bfs | O(l*n*m) | AC | 0.015 s | 544 KB |
| [1923_bfs.go](1923_bfs.go) | Go 1.14 x64 | bfs | O(l*n*m) | AC | 0.015 s | 1404 KB |
| [1923_bfs.java](1923_bfs.java) | Java 1.8 | bfs | O(l*n*m) | AC | 0.109 s | 652 KB |
| [1923_bfs.py](1923_bfs.py) | Python 3.12 x64 | bfs | O(l*n*m) | AC | 0.078 s | 1308 KB |
| [1923_bfs.rs](1923_bfs.rs) | Rust 1.75 x64 | bfs | O(l*n*m) | AC | 0.062 s | 396 KB |
