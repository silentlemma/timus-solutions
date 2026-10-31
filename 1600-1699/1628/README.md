# 1628. White Streaks

[Timus 1628](https://acm.timus.ru/problem.aspx?space=1&num=1628) · difficulty 164 · implementation

Original problem by Alexander Ipatov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A calendar is an m × n table: row i is a week, column j a day of the
week. Some k cells are painted black (the bad days), the rest are white.
A segment is a 1 × l or l × 1 rectangle of cells. Count the white
streaks: the white segments maximal by inclusion.

## Input

The first line holds m, n and k (1 ≤ m, n ≤ 30000, 0 ≤ k ≤ 60000).
Each of the next k lines holds a black cell x y (1 ≤ x ≤ m, 1 ≤ y ≤ n);
the cells are distinct.

## Output

The number of white streaks.

## Examples

### Example 1

Input:

```
3 5 4
1 1
1 5
2 2
3 3
```

Output:

```
8
```

### Example 2

Input:

```
5 1 2
2 1
3 1
```

Output:

```
2
```

## Solution

In every row, the black cells split the row into white runs, and so do
they in every column. A run of length 2 or more is a streak. A single
white cell is different: it is a 1 × 1 segment in both directions, so it
is counted once, and only if it cannot grow either way, that is, when
its row neighbours and its column neighbours are all black or off the
table. Otherwise the cell already lies in a longer streak.

So the rows count their runs of length at least 2 plus their single
cells closed above and below, and the columns count only their runs of
length at least 2. Each row and column sorts its own black cells, and a
set checks neighbours: C++ uses an ordered set, the others hash sets.
C++: `O(m + n + (m + k) log(k + 1))`; others: `O(m + n + k log k)`.

Pitfalls:

- a single white cell must not be counted twice, once per direction
  (test 05);
- with one row or one column, every white cell is closed by the border
  in the other direction (the second example);
- an all-white table with m, n > 1 has m + n streaks, so rows and
  columns without black cells still count (test 06).

The answers match an independent accepted implementation on 120 random
calendars and the largest one.

## Optimized solutions

The optimized C++ solution keeps two flat arrays of keys instead of a
`vector` per row and per column and a `set` of pairs: `x · (n + 2) + y`
orders the black cells row by row, `y · (m + 2) + x` column by column.
After sorting, one pass over each array walks all rows or all columns,
and a single white cell is checked above and below by binary search for
the keys of its neighbours in the row array. The keys stay below
`30000 · 30002 + 30001 < 2³¹`, since m, n ≤ 30000, so they fit in `int`.
The numbers are parsed by hand from a 4 KB buffer refilled with `fread`:
{1628_implementation_optimized.cpp}.

The optimized Go solution keeps two flat slices of keys instead of a
slice per row and per column and a hash set of cells: `x · (n + 2) + y`
orders the black cells row by row, `y · (m + 2) + x` column by column.
After sorting, one pass over each slice walks all rows or all columns,
and a single white cell is checked above and below by binary search for
the keys of its neighbours in the row slice. The numbers are parsed by
hand from a 4 KB buffer instead of `fmt.Fscan`:
{1628_implementation_optimized.go}.

The optimized Java solution keeps two flat `int` arrays of keys instead
of an array per row and per column and a `HashSet` of `Long` keys:
`x · (n + 2) + y` orders the black cells row by row, `y · (m + 2) + x`
column by column. After sorting, one pass over each array walks all rows
or all columns, and a single white cell is checked above and below by
binary search for the keys of its neighbours in the row array. The keys
stay below `30000 · 30002 + 30001 < 2³¹`, since m, n ≤ 30000, so they
fit in `int`. The numbers are parsed by hand from 4 KB blocks of the
input: {1628_implementation_optimized.java}.

The optimized Python solution keeps two flat lists of integer keys
instead of a list per row and per column and a set of coordinate tuples:
`x · (n + 2) + y` orders the black cells row by row, `y · (m + 2) + x`
column by column. After sorting, one pass over each list walks all rows
or all columns, and a single white cell is checked above and below with
`bisect_left` for the keys of its neighbours in the row list. The input
is read in 4 KB chunks instead of all at once:
{1628_implementation_optimized.py}.

The optimized Rust solution keeps two flat vectors of `i32` keys instead
of a vector per row and per column and a hash set of cells:
`x · (n + 2) + y` orders the black cells row by row, `y · (m + 2) + x`
column by column. After sorting, one pass over each vector walks all
rows or all columns, and a single white cell is checked above and below
by binary search for the keys of its neighbours in the row vector. The
keys stay below `30000 · 30002 + 30001 < 2³¹`, since m, n ≤ 30000, so
they fit in `i32`. The numbers are parsed by hand from a 4 KB buffer
instead of reading the whole input into a `String`:
{1628_implementation_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1628_implementation_optimized.cpp`: time reduction +86.24%; memory
  reduction +90.75%; base: `1628_implementation.cpp`.

- `1628_implementation_optimized.go`: time reduction +63.20%; memory
  reduction +84.94%; base: `1628_implementation.go`.

- `1628_implementation_optimized.java`: time reduction -14.68%; memory
  reduction +86.68%; base: `1628_implementation.java`.

- `1628_implementation_optimized.py`: time reduction -7.34%; memory
  reduction +75.34%; base: `1628_implementation.py`.

- `1628_implementation_optimized.rs`: time reduction +0.00%; memory
  reduction +92.97%; base: `1628_implementation.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.109 s | 6528 KB | 11288406 |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB | 11288407 |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB | 11288409 |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB | 11288408 |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.031 s | 9440 KB | 11304016 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1628_implementation_optimized.cpp](1628_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.015 s | 604 KB | 11307222 |
| [1628_implementation_optimized.go](1628_implementation_optimized.go) | Go 1.14 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.046 s | 1988 KB | 11307224 |
| [1628_implementation_optimized.java](1628_implementation_optimized.java) | Java 1.8 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.125 s | 1364 KB | 11307223 |
| [1628_implementation_optimized.py](1628_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.234 s | 6352 KB | 11307226 |
| [1628_implementation_optimized.rs](1628_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.031 s | 664 KB | 11307225 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
