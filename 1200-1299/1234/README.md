# 1234. A brick through a hole in the floor

[Timus 1234](https://acm.timus.ru/problem.aspx?space=1&num=1234) · difficulty 688 · geometry

Original problem by Elena Andreeva, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A brick of A × B × C has to be pushed down a rectangular D × E hole that
goes straight down endlessly. Can it go through? All lengths are from 1
to 10 with at most one decimal.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B, C, D and E on one line.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
1.0 2.0 1.5 1.4 1.0
```

Output:

```
NO
```

### Example 2

Input:

```
1.0 2.0 1.5 1.5 1.0
```

Output:

```
YES
```

## Solution

The brick goes down end first, so it passes if one of its faces fits into
the D × E rectangle, and the face of its two shorter sides, q ≤ p, is the
easiest. With the hole's sides b ≤ a, there are three cases:

- q > b: the face is at least q wide in every direction, more than the
  hole's width b, `NO`;
- p ≤ a: it fits straight, `YES`;
- p > a: it may still fit turned. Carver's criterion says a p × q
  rectangle then fits into an a × b one exactly when
  `((a+b)/(p+q))² + ((a−b)/(p−q))² ≥ 2`.

All lengths are whole tenths, so the program reads them as integers of
tenths and multiplies the criterion out:
`(a+b)²(p−q)² + (a−b)²(p+q)² ≥ 2(p+q)²(p−q)²`. That decides even the
exact fits with no rounding. `O(1)`.

Pitfalls:

- an exact fit counts: the second example and tests 03, 04 and 07 touch
  the hole's sides;
- turned fits can be very close: in test 05 the left side of the
  criterion is about 2 − 5·10⁻⁶ and in test 06 about 2 + 3·10⁻⁷, so
  floating point with a loose tolerance answers one of them wrongly.

The criterion was compared with a scan of angles on thousands of random
cases, and with exact fractions on all 197 one-decimal cases where it is
within 2·10⁻⁴ of 2.

## Language notes

- All languages convert each length to tenths with rounding (`x · 10`
  is not always a whole number in floating point) and then use integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1234_geometry.cpp](1234_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 140 KB |
| [1234_geometry.go](1234_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1108 KB |
| [1234_geometry.java](1234_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 532 KB |
| [1234_geometry.py](1234_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 440 KB |
| [1234_geometry.rs](1234_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
