# 1490. Fire Circle

[Timus 1490](https://acm.timus.ru/problem.aspx?space=1&num=1490) · difficulty 196 · math

Original problem by Alexander Ipatov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A floor is tiled with 1 × 1 squares. A circle of fire of integer radius
R (R ≤ 10⁵) is centred at a point where four tiles meet. A tile is
spoiled if it shares at least two points with the circle. Count the
spoiled tiles.

Time limit: 1 second. Memory limit: 64 MB.

## Input

R.

## Output

The number of spoiled tiles.

## Examples

### Example 1

Input:

```
2
```

Output:

```
16
```

### Example 2

Input:

```
4
```

Output:

```
60
```

## Solution

The examples show that the whole disc counts, not only its rim. A tile
meets the disc in more than one point exactly when its corner nearest
to the centre lies strictly inside the disc; a tile whose nearest corner
lies on the circle touches it in that single point.

By symmetry count one quarter and multiply by 4. There the tile with
lower-left corner (i, j) counts when i² + j² < R², so column i holds
⌊√(R² − i² − 1)⌋ + 1 tiles, for i from 0 to R − 1. An integer square
root keeps this exact. The answer reaches about π·10¹⁰ and needs 64
bits. `O(R)`.

Pitfalls:

- a tile that only touches the disc at a corner, such as the one beyond
  (3, 4) for R = 5, does not count (tests 04, 05, 06);
- the answer for R = 10⁵ is 31 416 325 412, beyond 32 bits (test 07);
- a floating square root must be corrected to the exact integer one
  (tests 06, 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1490_math.cpp](1490_math.cpp) | G++ 13.2 x64 | math | O(R) | AC | 0.015 s | 128 KB |
| [1490_math.go](1490_math.go) | Go 1.14 x64 | math | O(R) | AC | 0.031 s | 1088 KB |
| [1490_math.java](1490_math.java) | Java 1.8 | math | O(R) | AC | 0.109 s | 1612 KB |
| [1490_math.py](1490_math.py) | Python 3.12 x64 | math | O(R) | AC | 0.078 s | 472 KB |
| [1490_math.rs](1490_math.rs) | Rust 1.75 x64 | math | O(R) | AC | 0.031 s | 232 KB |
