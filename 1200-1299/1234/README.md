# 1234. A brick through a hole in the floor

[Timus 1234](https://acm.timus.ru/problem.aspx?space=1&num=1234) · difficulty 687 · geometry

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

- The simple versions convert each length to tenths with rounding (`x · 10`
  is not always a whole number in floating point) and then use integers.

## Optimized solutions

Optimized versions read tenths directly from the input and use the same integer test.

Go reads dimensions directly in tenths and applies the exact integer geometric test. Go 1.14 x64, submission 11322881. Time 0.015 → 0.015 s, memory 1080 → 308 KB.

Python 3.12 x64, submission 11318418. Time 0.078 → 0.062 s, memory 420 → 464 KB.

Java 1.8, submission 11318424. Time 0.109 → 0.109 s, memory 536 → 364 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321887 · Go 1.14 x64 №11322221 · Java 1.8 №11322222 · Python 3.12 x64 №11322223 · Rust 1.75 x64 №11322224.

Rust checks the two smallest brick dimensions in tenths with an integer inequality for the rotated fit. Rust 1.75 x64, submission 11323284. Time 0.015 → 0.046 s, memory 236 → 52 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1234_geometry.cpp](1234_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB | 11321887 |
| [1234_geometry.go](1234_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1080 KB | 11322221 |
| [1234_geometry.java](1234_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 536 KB | 11322222 |
| [1234_geometry.py](1234_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 420 KB | 11322223 |
| [1234_geometry.rs](1234_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB | 11322224 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1234_geometry_optimized.go](1234_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 308 KB | 11322881 |
| [1234_geometry_optimized.py](1234_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 464 KB | 11318418 |
| [1234_geometry_optimized.java](1234_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 364 KB | 11318424 |
| [1234_geometry_optimized.rs](1234_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 52 KB | 11323284 |

\* The marked versions have room to improve in the ratings.
