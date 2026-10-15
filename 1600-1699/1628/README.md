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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1628_implementation.cpp](1628_implementation.cpp) | G++ 13.2 x64 | implementation | O(m + n + (m + k) log(k + 1)) | AC | 0.109 s | 6528 KB |
| [1628_implementation.go](1628_implementation.go) | Go 1.14 x64 | implementation | O(m + n + k log k) | AC | 0.125 s | 13204 KB |
| [1628_implementation.java](1628_implementation.java) | Java 1.8 | implementation | O(m + n + k log k) | AC | 0.109 s | 10240 KB |
| [1628_implementation.py](1628_implementation.py) | Python 3.12 x64 | implementation | O(m + n + k log k) | AC | 0.218 s | 25760 KB |
| [1628_implementation.rs](1628_implementation.rs) | Rust 1.75 x64 | implementation | O(m + n + k log k) | AC | 0.046 s | 9408 KB |
