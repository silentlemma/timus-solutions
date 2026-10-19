# 1976. Squared Distances to the Nearest Base

[Timus 1976](https://acm.timus.ru/problem.aspx?space=1&num=1976) · difficulty 1296 · geometry

Original problem by Idea by Ilya Bushkov, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rectangular grid has bases at some cell centers. Adjacent centers are
one unit apart. For every cell, find the square of its Euclidean distance
to the closest base. Empty cells impose no obstacle or movement restriction.
Limits: 2 seconds and 64 MB.

## Input

The first line contains n and m, 1≤n,m≤1000. The next n rows form a
binary matrix of m cells each: 1 denotes a base and 0 an empty cell.
At least one base and at least one empty cell are guaranteed.

## Output

Print n rows of m integers. Cell (r,c) must contain
min((r−a)²+(c−b)²), over all base coordinates (a,b). Use one space between
numbers in a row. A base has answer zero; do not take a square root.

## Checking

Outputs are compared token by token.

## Examples

```
3 4
1000
0000
0010
```

```
0 1 4 5
1 2 1 2
4 1 0 1
```

## Solution

### Separate the two coordinates

For a fixed target row r and source column q, let v[q] be the smallest
vertical distance |r−a| to a base (a,q) in that column. A downward scan
records the nearest base above; an upward scan takes the smaller distance
to a base below. A column without any base remains unreachable.

For a target column x the answer becomes

min over reachable q of v[q]²+(x−q)².

Indeed, once q is fixed the horizontal term is constant, so the base
minimizing the full squared distance is exactly a vertically closest base
in column q. Taking the minimum over all q then covers every base.

The implementation uses far=n+m to distinguish unreachable columns.
All true vertical distances are at most n−1. Unreachable entries remain
at least far after both scans and are skipped when forming a row envelope.
Every row still has a reachable column because some base exists globally.

### Integer lower envelope of parabolas

For each reachable column q define f[q]=v[q]² and
Pq(x)=(x−q)²+f[q]. All parabolas have the same quadratic coefficient.
For p<q, the new parabola is no higher than the old one exactly when

2(q−p)x ≥ f[q]+q²−f[p]−p².

Their first integer switching coordinate is therefore

ceil((f[q]+q²−f[p]−p²)/(2(q−p))).

No floating intersection or epsilon is needed. In particular, round toward
positive infinity when the numerator is negative too; ordinary truncated
division is not a replacement for this signed ceiling formula.

Maintain a stack of candidate columns and the first nonnegative integer
coordinate where each becomes preferable. Process q from left to right.
Compute its switching coordinate with the last candidate. If this is no
later than that candidate's own beginning, the last candidate has no
remaining optimal interval and is removed. Repeat, then append q with
its beginning. If the stack becomes empty, q begins at zero. At a tie,
prefer the new parabola; the resulting squared distance is unchanged.

Why can a removed candidate never matter again? After subtracting the
common x², the functions are lines with slopes −2q in strictly decreasing
order. Their lower envelope visits candidates in increasing q order.
A candidate whose interval is overtaken before it begins cannot appear
on that envelope. Removing it and comparing the two new neighbors
preserves exactly the lower envelope on x≥0.

Scan x=0…m−1, advancing a pointer whenever the next candidate's beginning
has been reached. Evaluate the selected parabola with integer arithmetic.
The stack beginnings are strictly increasing, so this pointer never moves
backwards and always selects a minimum.

### Correctness and complexity

The vertical scans compute every finite v[q] exactly. The envelope
argument proves that the row scan returns minq Pq(x). By coordinate
separation, this is the minimum squared distance to any base. Thus every
output cell is correct, including bases, ties, empty rows and empty columns.

Each candidate enters and leaves a stack at most once, and the output
pointer advances at most m times per row. Total time is `O(nm)` and total
memory is `O(nm)`, including the stored vertical grid and input. The row
envelope needs only `O(m)` extra space. Output itself contains nm values.

In the example the bases are at zero-based (0,0) and (2,2). At (0,3),
their squared distances are 9 and 5, so the answer is 5. At (1,1) both
distances are 2. At (2,1) the second base is one unit away, giving 1.
Evaluating all cells gives exactly the three output rows above.

A four-neighbor BFS computes Manhattan distance, not squared Euclidean
distance; for offset (1,1) its square would be 4 instead of 2. Do not
use an eight-neighbor approximation either. Skip unreachable columns
instead of letting a sentinel win. Compute switching coordinates with
signed ceiling division, remove candidates on equal beginnings, and
retain original row/column indices rather than distances alone.

## Language notes

All five programs implement the same exact envelope. Python stores the
vertical grid as lists of rows for direct indexed access. It detects
columns containing bases before scanning, leaving other columns
unreachable. If all vertical distances in a row are at most one, they
already attain the integer lower bound: zero at a base and one
elsewhere. Python returns them directly; other rows use the full
envelope. The compiled versions use integer arrays. C++ and Go implement
signed ceiling division directly; Java uses Math.floorDiv and Rust uses
div_euclid with negation. Row output is buffered so the complete printed
matrix need not be held as strings. Java reuses its row builder and
character buffer without creating a new output String for each row.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1976_geometry.cpp](1976_geometry.cpp) | G++ 13.2 x64 | geometry | O(n*m) | AC | 0.203 s | 3884 KB |
| [1976_geometry.go](1976_geometry.go) | Go 1.14 x64 | geometry | O(n*m) | AC | 0.125 s | 18608 KB |
| [1976_geometry.java](1976_geometry.java) | Java 1.8 | geometry | O(n*m) | AC | 0.296 s | 8196 KB |
| [1976_geometry.py](1976_geometry.py) | Python 3.12 x64 | geometry | O(n*m) | AC | 1.859 s | 33996 KB |
| [1976_geometry.rs](1976_geometry.rs) | Rust 1.75 x64 | geometry | O(n*m) | AC | 0.140 s | 6028 KB |
