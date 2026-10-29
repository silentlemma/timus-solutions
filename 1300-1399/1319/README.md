# 1319. Hotel

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · difficulty 39 · implementation, math

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

## Optimized solutions

**Formula** (C++, Java, Rust). No table is stored: the number in each
cell is computed from its position, and the lines are printed as they
are computed. The diagonal of the cell in row `r` and column `c` has
`len = N − |c − r|` cells. On or above the main diagonal (`c ≥ r`) the
diagonals before it hold `1 + 2 + … + (len − 1) = len·(len − 1)/2`
numbers, and the cell is number `r + 1` on its own, so it holds
`len·(len − 1)/2 + r + 1`. Below it the cell is counted from the end:
the later diagonals and the rest of its own leave
`N² − len·(len + 1)/2 + c + 1`. Java and Rust also read `N` byte by
byte. Java needs 0.062 s instead of 0.093 s and 508 KB instead of
2008 KB; C++ and Rust need less memory with the same time, 124 KB
instead of 244 KB and 200 KB instead of 364 KB.

The formula is written in Python as well, printing each line as it is
computed: 296 KB instead of 888 KB, although the time grows from 0.046 s
to 0.078 s.

## Language notes

- The simple solutions fill the table the same way and print it at the
  end.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284938 |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB | 11284939 |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB | 11284941 |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB | 11284940 |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB | 11284942 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1319_math.cpp](1319_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.001 s | 124 KB | 11303594 |
| [1319_math.java](1319_math.java) | Java 1.8 | math | O(N^2) | AC | 0.062 s | 508 KB | 11303596 |
| [1319_math.py](1319_math.py) \* | Python 3.12 x64 | math | O(N^2) | AC | 0.078 s | 296 KB | 11303740 |
| [1319_math.rs](1319_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.001 s | 200 KB | 11303597 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
