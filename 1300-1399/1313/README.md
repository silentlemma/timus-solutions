# 1313. Some Words about Sport

[Timus 1313](https://acm.timus.ru/problem.aspx?space=1&num=1313) · difficulty 34 · implementation

Original problem: idea by Stanislav Vasiliev, prepared by Stanislav Vasiliev and Alexander Klepinin, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given an N × N image (N ≤ 100), print its pixels along the diagonals:
starting at the top left corner, one diagonal after another, each
diagonal from its lower left end up to its upper right end. The example
shows the order.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then N rows of N natural numbers, each at most 100.

## Output

The N² numbers in diagonal order, on one line.

## Examples

### Example 1

Input:

```
4
1 3 6 10
2 5 9 13
4 8 12 15
7 11 14 16
```

Output:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
```

## Solution

Diagonal s holds the cells whose row and column add up to s, for s from
0 to 2N − 2. Walking a diagonal from its lowest cell up means taking
the row i from min(s, N − 1) down to max(0, s − N + 1), with column
s − i. `O(N²)`.

Pitfalls:

- the diagonals of the lower right half are shorter and stop before
  row 0, hence the max(0, s − N + 1) bound (test 04);
- N = 1 is a single pixel (test 02).

## Optimized solutions

The optimized Java solution parses the numbers by hand instead of
`StringTokenizer`, keeps the picture in one flat `byte` array, since
every number is at most 100, and writes the numbers digit by digit into
a 1 KB output buffer: 392 KB instead of 1176 KB, with the same time. The
walk along the diagonals is the same.

The optimized Python solution keeps the colours, at most 100, in a
`bytearray`, makes the text of each colour once and builds the answer as
bytes: 484 KB instead of 1892 KB, with the same time.

## Language notes

- Except in C++ and in the optimized Java and Python solutions, the
  numbers are copied through as text: they are never needed as integers.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1313_implementation.cpp](1313_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284904 |
| [1313_implementation.go](1313_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 1352 KB | 11303290 |
| [1313_implementation.java](1313_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.078 s | 1176 KB | 11284908 |
| [1313_implementation.py](1313_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 1892 KB | 11284907 |
| [1313_implementation.rs](1313_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 588 KB | 11284910 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1313_implementation_optimized.java](1313_implementation_optimized.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 392 KB | 11303592 |
| [1313_implementation_optimized.py](1313_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.062 s | 484 KB | 11303739 |
