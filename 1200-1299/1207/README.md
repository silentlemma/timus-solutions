# 1207. A line through two points that halves the rest

[Timus 1207](https://acm.timus.ru/problem.aspx?space=1&num=1207) · difficulty 117 · geometry

Original problem by Pavel Atnashev, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are an even number `4 ≤ N ≤ 10000` of points with integer
coordinates up to `10⁶` in absolute value, no three on a line. Choose two
of them so that the line through them splits the other points into two
halves of equal size.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` on the first line, then `N` lines, each with the coordinates `x y`
of one point.

## Output

The numbers of the two chosen points.

## Checking

Many pairs work, so any two different points are accepted if their line
leaves `(N − 2)/2` points on each side.

## Examples

### Example 1

Input:

```
4
0 0
1 0
0 1
1 1
```

Output:

```
1 4
```

## Solution

Take the lowest point, the leftmost if two share the lowest height. All
the other points lie above it or to its right on the same height, within
half a turn, so they can be sorted by the angle around it using only the
sign of the cross product, with no floating point. In that order every
point before the `k`-th lies on one side of the line from the lowest
point to the `k`-th, and every point after it on the other side. With
`N − 1` other points, the one at index `(N − 2)/2` from zero has
`(N − 2)/2` before and after it. `O(N log N)`.

Pitfalls:

- with an arbitrary pivot, the rays can span more than half a turn
  and break the order;
- the cross products reach `4·10¹²`, beyond 32 bits;
- a comparator must return "equal" for an element compared with itself,
  or some sorting routines reject it.

Every answer was checked by counting the points on each side, and a
separately written solution passes the same checker on every test.

## Optimized solutions

The optimized Java solution keeps the coordinates in `int` arrays, since
they are at most `10⁶` in absolute value, sorts an array of primitive
indices with a hand-written heapsort instead of sorting boxed `Integer`
indices with a lambda, computes the cross products in `long`, and parses
the input by hand from 4 KB blocks instead of `BufferedReader` and
`StringTokenizer`: {1207_geometry_optimized.java}.

The optimized Python solution gives every point an integer key once and
sorts by the keys instead of calling a Python comparator `O(N log N)`
times. The key is `−dx/dy` multiplied by `2⁴²` and rounded down, with
`dx`, `dy` the offsets from the pivot; `−dx/dy` grows with the angle
seen from the pivot. The offsets are at most `2·10⁶` in absolute value,
so two different fractions differ by at least `1/(2·10⁶)²`, and `2⁴²`
exceeds `(2·10⁶)²`, so the rounded keys stay distinct and in the same
order; points at the height of the pivot get a key below all others.
The coordinates are read line by line into arrays of 32-bit integers:
{1207_geometry_optimized.py}.

The optimized Rust solution reads the input line by line instead of
keeping the whole text and a vector of all its numbers, stores each
point as two `i32` coordinates and its number in one struct, since the
coordinates are at most `10⁶` in absolute value, shifts the points once
so that the pivot is the origin, and sorts them with `sort_unstable_by`
and cross products in `i64`: {1207_geometry_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1207_geometry_optimized.java`: time reduction +36.26%; memory
  reduction +88.53%; base: `1207_geometry.java`.

- `1207_geometry_optimized.py`: time reduction +33.57%; memory reduction
  +49.37%; base: `1207_geometry.py`.

- `1207_geometry_optimized.rs`: time reduction -48.39%; memory reduction
  +56.39%; base: `1207_geometry.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1207_geometry.cpp](1207_geometry.cpp).

- Python sorts with `functools.cmp_to_key`; Java sorts boxed indices with
  a lambda that uses `Long.compare`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry.cpp](1207_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 296 KB | 11283603 |
| [1207_geometry.go](1207_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.046 s | 1512 KB | 11283604 |
| [1207_geometry.java](1207_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 5544 KB | 11283609 |
| [1207_geometry.py](1207_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.140 s | 3516 KB | 11283608 |
| [1207_geometry.rs](1207_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 908 KB | 11283610 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry_optimized.java](1207_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.109 s | 636 KB | 11304352 |
| [1207_geometry_optimized.py](1207_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(N log N) | AC | 0.093 s | 1780 KB | 11304354 |
| [1207_geometry_optimized.rs](1207_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 396 KB | 11304353 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
