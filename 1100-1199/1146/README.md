# 1146. The sub-rectangle with the largest sum in a square array

[Timus 1146](https://acm.timus.ru/problem.aspx?space=1&num=1146) · difficulty 79 · dp

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given an `N × N` array, `N ≤ 100`, of integers from −127 to 127, find the
largest sum of a sub-rectangle, that is of a block of at least `1 × 1`
neighbouring rows and columns.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then the `N²` numbers row by row, separated by any white space.

## Output

The largest sum.

## Examples

### Example 1

Input:

```
4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2
```

Output:

```
15
```

## Solution

Fix the top row of the rectangle and move the bottom row down one row at
a time, keeping for every column the sum of its cells between the two
rows. For a fixed pair of rows, the best rectangle is the best run of
neighbouring columns in that list of column sums, which Kadane's scan
finds in one pass: keep the best sum of a run ending at the current
column, restarting at the column when the run so far is negative. The
column sums for the next bottom row are the old ones plus one row, so
each pair of rows costs `O(N)` and the whole search `O(N³)`, about half a
million steps for `N = 100`.

Pitfalls:

- the rectangle must not be empty: when all numbers are negative the
  answer is the largest one, not `0`, so the best value starts at a cell
  of the array;
- the numbers can be spread over lines in any way, so they are read as a
  stream of tokens;
- sums do not exceed `100² · 127`, which fits in 32 bits.

The answers were compared with a check of every rectangle using a table
of prefix sums on 150 random arrays up to `9 × 9`.

## Optimized solutions

The optimized Python solution reads the input in 4 KB blocks, keeps each
row in an `array` of bytes (every value is between −127 and 127) and
adds a row to the column sums with `map` instead of a Python loop:
632 KB instead of 1372 KB, with the same time. The optimized Rust
solution parses the numbers by hand from `stdin().lock()`, keeps the
matrix in one flat vector of `i8` and reuses one vector of column sums:
212 KB instead of 372 KB, although the time grows from 0.015 s to
0.046 s.

## Language notes

- All languages run the same scan.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1146_dp.cpp](1146_dp.cpp) | G++ 13.2 x64 | dp | O(N³) | AC | 0.015 s | 248 KB | 11279486 |
| [1146_dp.go](1146_dp.go) | Go 1.14 x64 | dp | O(N³) | AC | 0.031 s | 1308 KB | 11279491 |
| [1146_dp.java](1146_dp.java) | Java 1.8 | dp | O(N³) | AC | 0.078 s | 620 KB | 11279494 |
| [1146_dp.py](1146_dp.py) | Python 3.12 x64 | dp | O(N³) | AC | 0.187 s | 1372 KB | 11279492 |
| [1146_dp.rs](1146_dp.rs) | Rust 1.75 x64 | dp | O(N³) | AC | 0.015 s | 372 KB | 11279497 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1146_dp_optimized.py](1146_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N³) | AC | 0.171 s | 632 KB | 11303714 |
| [1146_dp_optimized.rs](1146_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N³) | AC | 0.046 s | 212 KB | 11303715 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
