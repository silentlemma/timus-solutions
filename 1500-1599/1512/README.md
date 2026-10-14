# 1512. Zinium

[Timus 1512](https://acm.timus.ru/problem.aspx?space=1&num=1512) · difficulty 886 · constructive

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place N queens (4 ≤ N ≤ 100000) on an N × N board so that no two share a
row, a column or a diagonal.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The column and row of each queen, one queen per line, in any order. Any
valid placement is accepted.

## Examples

### Example 1

Input:

```
8
```

Output:

```
1 5
2 1
3 8
4 4
5 2
6 7
7 3
8 6
```

## Solution

Search is hopeless at this size, but explicit placements are known. For
even N with N mod 6 ≠ 2, put the queen of column i ≤ N/2 in row 2i and
the queen of column N/2 + i in row 2i − 1: every queen of the left half
sits on a different diagonal from every queen of the right half, and
inside each half the rows grow by 2 per column, so no two share a
diagonal there either. For even N with N mod 6 = 2 that fails; instead,
with s = (2(i − 1) + N/2 − 1) mod N, put column i in row 1 + s and
column N + 1 − i in row N − s. Neither placement uses the main diagonal,
so an odd N takes the placement for N − 1 and adds a queen in the
corner (N, N). Checked for every N from 4 to 3000 and for the largest
ones. `O(N)`.

Pitfalls:

- the simple even/odd pattern breaks exactly when N mod 6 = 2, as for
  N = 8 in the example (tests 01, 05, gen2, gen7);
- an odd N needs the free corner of the board for N − 1 (tests 03, 06,
  gen3, gen6);
- many placements are right, so the tests use a checker (all tests);
- the output of 100000 lines is best built in one buffer (gen5).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1512_constructive.cpp](1512_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.031 s | 3232 KB |
| [1512_constructive.go](1512_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 4076 KB |
| [1512_constructive.java](1512_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 7808 KB |
| [1512_constructive.py](1512_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.140 s | 13344 KB |
| [1512_constructive.rs](1512_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 3960 KB |
