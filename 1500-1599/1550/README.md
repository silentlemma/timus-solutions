# 1550. Dean's Pyramid 3

[Timus 1550](https://acm.timus.ru/problem.aspx?space=1&num=1550) · difficulty 594 · geometry

Original problem by Evgeny Krokhalev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A regular square pyramid of height H and base side W (both below 10⁴)
has a vertical cylindrical hole of radius R through it, centred over the
point (X, Y) of the base, with the origin at the centre of the base and
the axes along its sides. The hole meets no edge of the pyramid. Find
the volume of the pyramid with the hole, within 10⁻³.

Time limit: 1 second. Memory limit: 64 MB.

## Input

H and W, then X and Y, then R.

## Output

The volume.

## Examples

### Example 1

Input:

```
3.0 3.0
-1.00 -0.70
0.1
```

Output:

```
8.96858
```

## Solution

The solid pyramid has volume H·W²/3. Over a point (x, y) of the base
its height is H·(1 − max(|x|, |y|)/(W/2)). Since the hole meets no edge,
its disc lies inside one triangle of the base under a single face, where
the height is a linear function of (x, y). The integral of a linear
function over a disc is its value at the centre times the area, so the
hole removes πR²·H·(1 − max(|X|, |Y|)/(W/2)). `O(1)`.

Pitfalls:

- the numbers may come without a decimal point (test 02);
- the volume reaches about 3·10¹¹, which double precision still holds
  to well under 10⁻³ (test 04);
- C++ has no standard M_PI, and the judge's compiler lacks it, so the
  C++ solution uses acos(−1).

## Optimized solutions

The optimized C++ version uses the same formula with a compile-time constant for π and C input and output. It keeps the calculation in long double and prints five decimal places. Submission 11317021 took 0.015 s and used 136 KB. The simple version took 0.015 s and used 444 KB.

Java uses the same volume formula, with direct decimal parsing and fixed-precision output. Submission 11318321 took 0.093 s and used 464 KB, versus 0.093 s and 1964 KB for the simple version.

Go computes the same volume formula and uses small buffers for decimal input and fixed-precision output. Go 1.14 x64, submission 11322933. Time 0.031 → 0.015 s, memory 1080 → 320 KB.

Python reads the five values as bytes and computes the height fraction from the distance to the nearest base edge. Python 3.12 x64, submission 11322022. Time 0.093 → 0.109 s, memory 444 → 452 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322273 · Go 1.14 x64 №11322275 · Java 1.8 №11322277 · Python 3.12 x64 №11322278 · Rust 1.75 x64 №11322279.

Rust keeps the volume formula and uses fixed buffers for ordinary inputs and five-place output. Rust 1.75 x64, submission 11323247. Time 0.015 → 0.031 s, memory 244 → 68 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1550_geometry.cpp](1550_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB | 11322273 |
| [1550_geometry.go](1550_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1080 KB | 11322275 |
| [1550_geometry.java](1550_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1964 KB | 11322277 |
| [1550_geometry.py](1550_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 444 KB | 11322278 |
| [1550_geometry.rs](1550_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 244 KB | 11322279 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1550_geometry_optimized.cpp](1550_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 136 KB | 11317021 |
| [1550_geometry_optimized.go](1550_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 320 KB | 11322933 |
| [1550_geometry_optimized.java](1550_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 464 KB | 11318321 |
| [1550_geometry_optimized.py](1550_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 452 KB | 11322022 |
| [1550_geometry_optimized.rs](1550_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 68 KB | 11323247 |

\* The Go rating target remains open.
