# 1944. An ASCII Map with Point Priority

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 238 · implementation

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

Compare every symbol and newline in the complete drawing, not just
whitespace-separated tokens. Both published new programs passed all 26
repository inputs and 69 independent extra inputs in their target Docker
compilers. Each actual extra output and exit code was re-read against an
independent per-coordinate oracle: occupied points first, then origin,
axes and background. Cases cover the origin, one row or column, hidden
axes, all quadrants, ±100, 250 points, explicit plus signs, CRLF and EOF.
The separate Python candidate also passed these 69 target runs and 2048
host executions including every nonempty subset of the 3×3 grid; those
2048 executions are not claimed as C++ or Java tests. All three candidates
have their own exact-source Accepted, but admission is checked separately.

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

## Optimized solutions

Render one row at a time rather than allocate the complete drawing. Sort packed point coordinates so points of a row are consecutive. Initialize the row with background and the visible axis, construct the horizontal axis and origin when needed, then overlay points last. This preserves the exact symbol priority and descending vertical order. Reuse a row buffer and stream it; storage depends on the points and row width, not the drawing area. Sorting does not remove the time needed to print every cell.

- `1944_implementation_optimized.cpp`: 0.015 s / 116 KB; base `1944_implementation.cpp`: 0.015 s / 472 KB; relative change: time -0.0%, memory -75.4%.
- `1944_implementation_optimized.java`: 0.125 s / 476 KB; base `1944_implementation.java`: 0.125 s / 844 KB; relative change: time -0.0%, memory -43.6%.
- `1944_implementation_optimized.py`: 0.140 s / 332 KB; base `1944_implementation.py`: 0.093 s / 636 KB; relative change: time +50.5%, memory -47.8%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1944_implementation.cpp`; covering source `1944_implementation_optimized.cpp`; time/memory places 1/1, other-author entries 50/50.

- Go: preferred teaching base `1944_implementation.go`; covering source `1944_implementation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1944_implementation.java`; covering source `1944_implementation.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1944_implementation.py`; covering source `1944_implementation_optimized.py`; time/memory places 11/1, other-author entries 11/11.

- Rust: preferred teaching base `1944_implementation.rs`; covering source `1944_implementation.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB | 11291904 |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB | 11291906 |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB | 11291912 |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB | 11291907 |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB | 11291920 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1944_implementation_optimized.cpp](1944_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N log N+WH) | AC | 0.015 s | 116 KB | 11308709 |
| [1944_implementation_optimized.java](1944_implementation_optimized.java) | Java 1.8 | implementation | O(N log N+WH) | AC | 0.125 s | 476 KB | 11308715 |
| [1944_implementation_optimized.py](1944_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N log N+WH) | AC | 0.140 s | 332 KB | 11309399 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
