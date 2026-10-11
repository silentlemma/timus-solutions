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

N, then N rows of N numbers.

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

- the diagonals of the lower right half are shorter and start below
  row s, hence the max(0, s − N + 1) bound (test 04);
- N = 1 is a single pixel (test 02).

## Language notes

- Except in C++, the numbers are copied through as text: they are
  never needed as integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1313_implementation.cpp](1313_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB |
| [1313_implementation.go](1313_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.015 s | 1332 KB |
| [1313_implementation.java](1313_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.078 s | 1176 KB |
| [1313_implementation.py](1313_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 1892 KB |
| [1313_implementation.rs](1313_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 588 KB |
