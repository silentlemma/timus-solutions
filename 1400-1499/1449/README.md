# 1449. Credit Operations 2

[Timus 1449](https://acm.timus.ru/problem.aspx?space=1&num=1449) · difficulty 1463 · matching

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N firms (2 ≤ N ≤ 100) took credits from N banks; A[i, j] is the credit
of firm i from bank j (0 ≤ A[i, j] ≤ 10⁶). Choose non-negative integer
bribes BR[i] for the firms and BC[j] for the banks so that every credit
satisfies A[i, j] ≤ BR[i] + BC[j] and the total of all bribes is as
small as possible. Print any optimal choice.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N × N credit matrix.

## Output

BR on the first line, BC on the second.

## Examples

### Example 1

Input:

```
4
5 8 4 3
3 6 2 1
4 6 4 1
4 3 5 4
```

Output:

```
2 0 1 2
3 6 3 2
```

## Solution

This is the linear-programming dual of the assignment problem. For any
permutation σ the bribes cover the credits A[i, σ(i)], so the total is
at least the weight of the heaviest perfect matching; the Hungarian
method produces potentials that reach exactly that weight. Run it on the
costs −A: it keeps u[i] + v[j] ≤ −A[i, j] with equality on the matching
it finds, so BR = −u and BC = −v cover every credit and add up to the
heaviest matching, and the potentials stay integers.

The potentials may be negative, but adding t to every BR and subtracting
it from every BC changes neither the total nor any sum BR[i] + BC[j].
Shift until the smallest BR is 0. Then no BC is negative: if BC[j] were
negative, every BR[i] ≥ A[i, j] − BC[j] would be positive, including the
one that is 0. `O(N³)`.

Pitfalls:

- an all-zero matrix still needs an answer, all zeros (test 02);
- a single bank holding every credit can be paid by that bank alone
  (test 07);
- the bribes must be non-negative, which the raw potentials are not.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1449_matching.cpp](1449_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.015 s | 284 KB |
| [1449_matching.go](1449_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.031 s | 1368 KB |
| [1449_matching.java](1449_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.093 s | 780 KB |
| [1449_matching.py](1449_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.171 s | 1520 KB |
| [1449_matching.rs](1449_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.031 s | 424 KB |
