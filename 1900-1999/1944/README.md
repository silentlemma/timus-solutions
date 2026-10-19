# 1944. An ASCII Map with Point Priority

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 239 · implementation

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Draw distinct integer points on a Cartesian grid, with x increasing right
and y increasing upwards. Each cell represents one coordinate pair.
Use * for an input point, + for the origin, - for the x-axis, | for
the y-axis and . elsewhere. A point overrides either axis and the origin;
axes may therefore be completely hidden. Draw the smallest rectangle
containing every point and the origin. Limits: 1 second, 64 MB.

## Input

n with 1≤n≤250, followed by n distinct integer pairs (x,y), where
−100≤x,y≤100. No two records describe the same point.

## Output

Rows go from U=max(0,max y) down to D=min(0,min y), inclusive. Columns
go from L=min(0,min x) through R=max(0,max x). Thus every row has
W=R−L+1 symbols, and there are H=U−D+1 rows. Print only the grid.

## Checking

Compare the complete drawing in row/column order with exact symbols;
spaces are not empty cells. Each generated row ends with a newline.

## Examples

```
8
-10 5
-7 3
-4 2
-9 4
0 1
6 -1
3 0
8 -3
```

```
*.........|........
.*........|........
...*......|........
......*...|........
..........*........
----------+--*-----
..........|.....*..
..........|........
..........|.......*
```

## Solution

Initialize all four bounds to zero and expand them over the points.
For coordinate (x,y), row=U−y and column=x−L. This maps the rectangle
bijectively to indices 0..H−1 and 0..W−1, in the required orientation.

Fill an H×W grid with dots. At column −L of every row, place |.
Fill row U with -, then set its column −L to +. Finally overwrite
each input point's mapped cell with *. Emit rows from first to last.

The initial dots handle background cells. The vertical and horizontal
passes mark exactly x=0 and y=0. Their intersection is replaced by +,
and the last pass gives every point priority over those symbols.
Distinct points map to distinct cells. The zero-initialized bounds include
the origin even if all data lie in one quadrant, and no smaller bounds
could include all required coordinates. Therefore shape, symbols and
orientation are all correct, including a one-row or one-column drawing.

O(n+WH) time and space, including points and output. W,H≤201, and the
largest output is H(W+1)≤40602 ASCII bytes with newlines, below 64 KiB.
Bounds and indices fit ordinary signed integers.

Include zero in both coordinate ranges. Increasing screen row means
decreasing y; do not swap row and column offsets. The origin is + only
when no point occupies it. A point on an axis remains *. Do not print
numeric labels, spaces, extra borders or margins.

## Language notes

Python uses bytearrays, Go byte slices, C++ strings, Java char arrays,
and Rust byte vectors. Java appends complete rows rather than array
object representations. All output symbols are ASCII. Emit the already
newline-terminated drawing directly, avoiding an extra blank line.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB |
