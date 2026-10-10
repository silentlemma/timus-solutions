# 1114. Placing up to A and B identical balls of two colours into N boxes

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · difficulty 193 · combinatorics

Original problem from the first selection contest for the Bulgarian IOI team.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` boxes in a row (`1 ≤ N ≤ 20`), `A` identical red balls and
`B` identical blue balls (`0 ≤ A, B ≤ 15`). Any number of balls, of
either colour, may go into each box, boxes may stay empty and balls may
stay unused. Count the different placements.

Time limit: 0.6 seconds. Memory limit: 64 MB.

## Input

`N A B` on one line.

## Output

The number of placements.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 1 1
```

Output:

```
9
```

## Solution

The two colours are independent, so the answer is the product of the
counts for each colour. Putting at most `A` identical balls into `N`
boxes is the same as putting exactly `A` into `N + 1` boxes, the extra
box holding the unused ones; by stars and bars that is `C(A + N, N)`. The
answer is `C(A + N, N) · C(B + N, N)`, read from Pascal's triangle.
`O((A + N)²)` for the triangle, or `O(1)` with the table built once.

Pitfalls:

- the largest case `N = 20, A = B = 15` gives `C(35, 20)² ≈ 1.05 · 10^19`,
  which passes the signed 64-bit maximum `9.22 · 10^18` but fits in an
  unsigned 64-bit integer;
- unused balls are allowed: counting only placements of all `A` balls
  would give `C(A + N − 1, N − 1)` instead.

The answers were checked against a DP over the boxes that counts the
fillings using each number of balls and sums them up to `A` and `B`.

## Language notes

- C++, Go and Rust multiply in unsigned 64-bit integers; Java has no
  unsigned type, so it multiplies `long` values, whose 64 bits are right
  modulo `2^64`, and prints them with `Long.toUnsignedString`; Python's
  integers do not overflow.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 140 KB |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 1060 KB |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O((A + N)²) | AC | 0.109 s | 1648 KB |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O((A + N)²) | AC | 0.078 s | 372 KB |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O((A + N)²) | AC | 0.015 s | 232 KB |
