# 1454. Rectangles 2

[Timus 1454](https://acm.timus.ru/problem.aspx?space=1&num=1454) · difficulty 2532 · backtracking

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Five rectangles W[i] × H[i] are given (1 ≤ W[i], H[i] ≤ 1000). Decide
whether all five, turned as needed and without overlapping or cutting,
can be put together into one big rectangle.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Five lines, W[i] and H[i] on each.

## Output

"YES" or "NO".

## Examples

### Example 1

Input:

```
2 4
3 2
5 3
2 5
2 5
```

Output:

```
YES
```

## Solution

The big rectangle has the total area A, so its width w is a divisor of
A, and by symmetry only widths with w² ≤ A need trying. For a fixed size
the pieces are placed by skyline filling: keep the outline of the filled
part as stretches of equal level, take the lowest stretch (the leftmost
among the lowest), and put some unused piece, in either orientation,
into its left corner. In any tiling the lowest-leftmost free cell is the
bottom-left corner of some piece, and that piece cannot be wider than
the stretch, bounded by higher neighbours or box sides; so this search
finds every tiling.

Five pieces allow at most 5! · 2⁵ piece orders with orientations per size,
and the size and height limits cut most of them; trying a piece of the
same shape twice at the same corner is skipped. The area has at most a
few hundred divisors, so the whole search is tiny.

Pitfalls:

- a pinwheel, where no piece spans a full side of the big rectangle
  (tests 02, 06, 14);
- a prime total area leaves only strips of width 1 (test 04);
- pieces must be tried in both orientations (tests 07, 10, 11).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1454_backtracking.cpp](1454_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.015 s | 188 KB |
| [1454_backtracking.go](1454_backtracking.go) | Go 1.14 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.031 s | 1268 KB |
| [1454_backtracking.java](1454_backtracking.java) | Java 1.8 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.140 s | 2356 KB |
| [1454_backtracking.py](1454_backtracking.py) | Python 3.12 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.093 s | 680 KB |
| [1454_backtracking.rs](1454_backtracking.rs) | Rust 1.75 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.031 s | 396 KB |
