# 1084. The part of a square garden a tethered goat can reach

[Timus 1084](https://acm.timus.ru/problem.aspx?space=1&num=1084) · difficulty 150 · geometry

Original problem by Irina Danilina, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goat is tied with a rope of length `r` to a peg in the centre of a
square garden with side `a` (both integers from 1 to 100). It eats
everything it can reach without leaving the garden. Find the eaten area
with three digits after the decimal point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`a` and `r`.

## Output

The eaten area.

## Checking

Numbers are compared with an absolute error of 0.0011: the answers are
printed with three decimals, so the last digit may differ by one.

## Examples

### Example 1

Input:

```
10 6
```

Output:

```
95.091
```

## Solution

The eaten part is the intersection of the square with a circle of radius
`r` around its centre. Let `h = a/2`.

- `r ≤ h`: the circle fits inside, and the area is `πr²`.
- `r² ≥ 2h²`: the rope reaches the corners, and the whole square `a²` is
  eaten.
- Otherwise each side cuts a circular cap off the circle. A cap at
  distance `h` from the centre has area `r²·arccos(h/r) − h·√(r² − h²)`,
  and the four caps do not overlap because the circle does not reach the
  corners. The area is `πr² − 4·cap`.

`O(1)`.

Pitfalls:

- the middle case needs both bounds: with `r` at least the half-diagonal
  the caps would overlap and the formula would subtract too much;
- the test `r² ≥ 2h²` compares squares and avoids a square root of 2.

The answers were checked against a numeric integration of the eaten
height `min(a, 2√(r² − x²))` over `x` with Simpson's rule, split where
the formula changes.

## Language notes

- C++ takes `π` as `acos(-1)`, since `M_PI` is not part of standard C++.
- Java formats the answer with `Locale.US` to get a decimal point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1084_geometry.cpp](1084_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 148 KB |
| [1084_geometry.go](1084_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1084_geometry.java](1084_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1792 KB |
| [1084_geometry.py](1084_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 376 KB |
| [1084_geometry.rs](1084_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB |
