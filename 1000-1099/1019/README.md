# 1019. The longest white interval after repaintings of a line

[Timus 1019](https://acm.timus.ru/problem.aspx?space=1&num=1019) · difficulty 464 · sorting, dsu

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The segment `[0, 10^9]` of the number line is white. Then `N` repaintings
(`1 ≤ N ≤ 5000`) are applied in order: the `i`-th paints the segment from
`a_i` to `b_i` (`0 < a_i < b_i < 10^9`, integers) white or black. Find the
longest white interval of the result; among intervals of the same length
take the leftmost one.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines `a b c`, where `c` is `w` (white) or `b` (black).

## Output

The ends `x y` (`x < y`) of the longest white interval.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
2 999999998 b
100 500 w
500 900 w
300 310 b
```

Output:

```
310 900
```

### Example 2

Input:

```
1
1 999999999 w
```

Output:

```
0 1000000000
```

## Solution

**Coordinate compression.** Only the points `0`, `10^9` and all `a_i`,
`b_i` matter: between two neighbouring points of this sorted set the colour
never changes. They cut the line into at most `2N + 1` pieces
`[x_k, x_{k+1})`, and a repainting of `[a, b]` covers exactly the pieces from
the index of `a` up to the index of `b`, excluding the latter.

**Painting.** Apply the repaintings to the pieces in order: at most
`5000 · 10 001 = 5 · 10^7` simple assignments, fine in compiled languages.

**Painting backwards with a DSU.** The colour of a piece is the colour of the
last repainting that covers it. Go through the repaintings from the last one
and paint only pieces that are still unpainted; a "next unpainted piece"
pointer array with path compression (a DSU on a line) jumps over painted
ones. Every piece is painted at most once: `O((N + M) α)` after sorting,
where `M` is the number of pieces. Pieces that no repainting reaches stay
white.

**The answer.** Scan the pieces from left to right, joining neighbouring
white pieces into runs; a run `[x_i, x_j)` has length `x_j - x_i`. Update
the best run only on a strictly greater length, which keeps the leftmost of
equal ones. A white run always exists: the piece `[0, min a)` is never
repainted.

Pitfalls:

- touching white segments, like `[10, 20]` and `[20, 30]`, form one interval;
- a black segment inside a white one splits it;
- the ends `0` and `10^9` belong to the line even if no repainting mentions
  them.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: compression and direct painting.
- **C++** and **Python** also paint backwards with the DSU, which keeps the
  Python version linear.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1019_dsu_sorting.cpp](1019_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.015 s | 212 KB |
| [1019_dsu_sorting.py](1019_dsu_sorting.py) | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.078 s | 3560 KB |
| [1019_sorting.cpp](1019_sorting.cpp) | G++ 13.2 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 208 KB |
| [1019_sorting.go](1019_sorting.go) | Go 1.14 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 1784 KB |
| [1019_sorting.java](1019_sorting.java) | Java 1.8 | sorting | O(N^2) after sorting | AC | 0.203 s | 3960 KB |
| [1019_sorting.rs](1019_sorting.rs) | Rust 1.75 x64 | sorting | O(N^2) after sorting | AC | 0.046 s | 692 KB |
