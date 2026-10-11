# 1319. Hotel

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · difficulty 39 · implementation

Original problem by Stanislav Vasiliev, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hotel's mail rack is an N × N block of cells (1 ≤ N ≤ 100), numbered
along diagonals: number 1 is in the top right corner, each diagonal goes
from top to bottom, and the diagonals follow one another towards the
bottom left corner, where N² stands. Print the numbered table.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

N lines of N numbers separated by spaces.

## Examples

### Example 1

Input:

```
3
```

Output:

```
4 2 1
7 5 3
9 8 6
```

## Solution

The cells of one diagonal have the same difference column − row. Going
through that difference from N − 1 down to −(N − 1), and through the
rows of each diagonal from the top, gives the cells in numbering order.
`O(N²)`.

Pitfalls:

- the first diagonal is the single top right cell, not the main
  diagonal (test 01);
- N = 1 is a single cell with 1 (test 02).

## Language notes

- All five solutions fill the table the same way and print it at the
  end.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB |
