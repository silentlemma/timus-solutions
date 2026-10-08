# 1008. Converting between two encodings of a connected pixel figure

[Timus 1008](https://acm.timus.ru/problem.aspx?space=1&num=1008) · difficulty 367 · bfs

Original problem from the Third Open USTU Collegiate Programming Contest (PhysTech Cup), 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A figure is a non-empty set of black pixels with coordinates `1 ≤ x, y ≤ 10`
that is 4-connected (pixels sharing a side are neighbours). It can be written
in two ways:

1. **List**: the number of pixels, then one line `x y` per pixel, sorted by
   `x` and then by `y`.
2. **Description**: the line `x y` of the *start* pixel — the one with the
   smallest `x`, and among those the smallest `y` — followed by one line per
   pixel in breadth-first order from the start. The line of a pixel lists,
   in the order `R` (x+1), `T` (y+1), `L` (x-1), `B` (y-1), those of its
   neighbours that have not been mentioned yet; these are appended to the
   queue in that order. Every line except the last ends with `,`, the last
   one with `.`.

Given one encoding, print the other.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

One of the two encodings. Lines have no leading or trailing spaces; `x` and
`y` are separated by one space.

## Output

The other encoding.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
7
2 5
3 3
3 4
3 5
4 3
5 3
5 4
```

Output:

```
2 5
R,
B,
B,
R,
R,
T,
.
```

### Example 2

Input:

```
2 5
R,
B,
B,
R,
R,
T,
.
```

Output:

```
7
2 5
3 3
3 4
3 5
4 3
5 3
5 4
```

## Solution

The description *is* a breadth-first search, so both directions are the same
search.

- **List → description**: mark the pixels on a grid, find the start, run BFS;
  for each dequeued pixel try the four directions in the order `R T L B`,
  and every black, not yet seen neighbour is marked, enqueued and written.
- **Description → list**: replay the search. The queue starts with the start
  pixel; line `i` belongs to the `i`-th pixel of the queue, and each letter
  appends the neighbour in that direction. At the end the queue holds all
  pixels; sort them by `(x, y)`.

Which encoding is given: only the description ends with `.`, so it suffices
to look at the last token. Reading whitespace-separated tokens also handles
an empty line `,` (it is a token) and CRLF line ends.

At most 100 pixels, so everything is `O(100)`; a grid with a border of empty
cells (indices `0..11`) avoids bounds checks.

Pitfalls:

- a single pixel is described as its coordinates and a line with just `.`;
- the start is the lowest among the *leftmost* pixels, not the lowest overall;
- a neighbour is written only once, by the pixel that discovers it first.

## Language notes

The same BFS everywhere. The Java version fills a grid when replaying the
description and prints it column by column, which yields the sorted order
without sorting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1008_bfs.cpp](1008_bfs.cpp) | G++ 13.2 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.015 s | 380 KB |
| [1008_bfs.go](1008_bfs.go) | Go 1.14 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.015 s | 1112 KB |
| [1008_bfs.java](1008_bfs.java) | Java 1.8 | bfs | O(P + W·H) | AC | 0.093 s | 536 KB |
| [1008_bfs.py](1008_bfs.py) | Python 3.12 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.078 s | 624 KB |
| [1008_bfs.rs](1008_bfs.rs) | Rust 1.75 x64 | bfs | O(P log P), P ≤ 100 pixels | AC | 0.046 s | 252 KB |
