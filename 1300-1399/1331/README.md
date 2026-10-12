# 1331. Vladislava

[Timus 1331](https://acm.timus.ru/problem.aspx?space=1&num=1331) · difficulty 988 · geometry

Original problem by Alexander Bikbaev, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A spherical planet of radius R ≤ 1000 has M ≤ 5000 landing pads and
N ≤ 5000 artifacts, each given by latitude and longitude in degrees. For
every artifact print the distance along the surface to the nearest pad,
with two digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then R, then M lines with the pads and N lines with the
artifacts, each as latitude and longitude.

## Output

N lines with the distances.

## Examples

### Example 1

Input:

```
1 2
1
0 0
1 1
0 0
```

Output:

```
0.00
```

### Example 2

Input:

```
2 1
1
0 0
0 90
0 45
```

Output:

```
1.57
0.79
```

## Solution

Put every place on the unit sphere as a point in space:
(cos φ cos λ, cos φ sin λ, sin φ). The surface distance grows with the
straight chord between two points, so the nearest pad is the one with
the shortest chord, found by trying all pads. Comparing squared chords
needs no roots or trigonometry inside the loop. The distance is then
R · 2 · asin(chord / 2). This keeps its precision for close points,
unlike R · acos of the dot product, which loses digits there.
`O(N · M)`, 25 million pairs.

Pitfalls:

- at the poles the longitude does not matter (test 04);
- longitudes −179.5 and 179.5 are one degree apart across the date line,
  not 359 (test 05);
- opposite points are π · R apart, and rounding can push chord / 2 a
  little above 1, so it is capped (test 03).

The distances were compared with the haversine formula on 300 random
small cases.

## Language notes

- CPython needs about 2 seconds for the 25 million pairs, so the Python
  solution is submitted under PyPy 3.10, where it takes about 0.1
  seconds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1331_geometry.cpp](1331_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·M) | AC | 0.125 s | 408 KB |
| [1331_geometry.go](1331_geometry.go) | Go 1.14 x64 | geometry | O(N·M) | AC | 0.078 s | 1572 KB |
| [1331_geometry.java](1331_geometry.java) | Java 1.8 | geometry | O(N·M) | AC | 0.359 s | 6312 KB |
| [1331_geometry.py](1331_geometry.py) | PyPy 3.10 x64 | geometry | O(N·M) | AC | 0.296 s | 5412 KB |
| [1331_geometry.rs](1331_geometry.rs) | Rust 1.75 x64 | geometry | O(N·M) | AC | 0.046 s | 672 KB |
