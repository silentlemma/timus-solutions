# 1531. Zones on a Plane

[Timus 1531](https://acm.timus.ru/problem.aspx?space=1&num=1531) · difficulty 1427 · math

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Zone 1 is a square made of two isosceles right triangles. Zone n + 1
comes from zone n: on each leg of each of its triangles, as a
hypotenuse, build two isosceles right triangles, then drop every triangle
that is part of an earlier zone. Count the simple polygons that zone n
consists of (1 ≤ n ≤ 2000).

Time limit: 1 second. Memory limit: 64 MB.

## Input

n.

## Output

The number of polygons.

## Examples

### Example 1

Input:

```
1
```

Output:

```
1
```

### Example 2

Input:

```
2
```

Output:

```
4
```

### Example 3

Input:

```
3
```

Output:

```
8
```

### Example 4

Input:

```
4
```

Output:

```
12
```

## Solution

The first 16 zones can be constructed exactly on a lattice: scale the
square by 2^16, so that all vertex coordinates stay integral,
keep the new triangles whose centre is not covered by an
earlier triangle, and join the triangles of a zone that share an edge.
For the first 16 zones this gives 1, 4, 8, 12, 20, 28, 44, 60, 92, 124,
188, 252, 380, 508, 764, 1020. From zone 3 on the increments are 4, 4, 8,
8, 16, 16, …, doubling every two zones, so for n ≥ 2

- an even n = 2k gives 2^(k+2) − 4;
- an odd n = 2k + 1 gives 3·2^(k+1) − 4.

The solutions print these numbers, which reach about 10³⁰¹, so C++ and
Rust double a decimal number digit by digit and Go and Java use their big
integers. `O(n²)` digit operations at most.

Pitfalls:

- zone 1 is the only exception: the odd formula would give 2, but the
  square is one polygon (test 01);
- over 300 digits for n = 2000, 1999 (tests 06, 07);
- the formula rests on the counts of the first 16 zones and was checked
  by the judge; the derivation above does not prove it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1531_math.cpp](1531_math.cpp) | G++ 13.2 x64 | math | O(n^2) | AC | 0.015 s | 188 KB |
| [1531_math.go](1531_math.go) | Go 1.14 x64 | math | O(n^2) | AC | 0.015 s | 1160 KB |
| [1531_math.java](1531_math.java) | Java 1.8 | math | O(n^2) | AC | 0.093 s | 1700 KB |
| [1531_math.py](1531_math.py) | Python 3.12 x64 | math | O(n^2) | AC | 0.093 s | 380 KB |
| [1531_math.rs](1531_math.rs) | Rust 1.75 x64 | math | O(n^2) | AC | 0.046 s | 232 KB |
