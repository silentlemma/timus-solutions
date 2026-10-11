# 1255. Packing 1 × K coffins into a square

[Timus 1255](https://acm.timus.ru/problem.aspx?space=1&num=1255) · difficulty 281 · math

Original problem by Stanislav Vasilyev and Alexey Lakhtin, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

How many 1 × K rectangles (coffins) fit, without overlapping and parallel
to the sides, into an N × N square (1 < N, K < 10 000)?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K.

## Output

The largest number of coffins.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
8
```

## Solution

If K > N nothing fits. Otherwise write N = qK + r with 0 ≤ r < K and let
s = min(r, K − r). The answer is

```text
(N² − s²) / K
```

and it is always a whole number, since N ≡ r and so N² ≡ r² ≡ (K − r)²
modulo K.

That many fit:

- for r ≤ K/2, coffins lying along the rows fill the first qK columns of
  every row, and coffins standing along the columns fill the last r
  columns in all but r rows, leaving an r × r corner empty;
- for r > K/2, four blocks of coffins arranged like a pinwheel around
  the centre leave a hole of (K − r) × (K − r).

No more fit: colour each cell by `(row + column) mod K`. A coffin covers
K consecutive cells of a row or a column, so exactly one cell of each
colour, and the number of coffins is at most the size of the smallest
colour class, which a count along the diagonals shows to be exactly
(N² − s²) / K. `O(1)`.

Pitfalls:

- the leftover square has side min(r, K − r), not r: for N = 7, K = 4,
  r = 3 but only a 1 × 1 hole is left, and 12 coffins fit (test 08);
- N² reaches 10⁸, which still fits in 32 bits.

The formula was compared with an exhaustive search for all N and K from
2 to 7.

## Language notes

- All languages evaluate the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1255_math.cpp](1255_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1255_math.go](1255_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1132 KB |
| [1255_math.java](1255_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1600 KB |
| [1255_math.py](1255_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 376 KB |
| [1255_math.rs](1255_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 220 KB |
