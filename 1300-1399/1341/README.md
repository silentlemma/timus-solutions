# 1341. Device

[Timus 1341](https://acm.timus.ru/problem.aspx?space=1&num=1341) · difficulty 1130 · geometry

Original problem by Stanislav Vasiliev, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A device flies at a fixed distance of 6400 km from the center of the
Earth. Starting at latitude W and longitude L, it flies a "square": a
given distance north, the same distance east, then south, then west. It
never reaches a pole. Print the latitude and longitude where it ends,
with three digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W, L and the side of the square in kilometers, one per line.

## Output

The final latitude and longitude, one per line.

## Examples

### Example 1

Input:

```
56.846841
53.36673
1124.427
```

Output:

```
56.847
60.631
```

## Solution

North and south run along meridians, each changing the latitude by the
same angle a = side / 6400 in radians, so the device comes back to
latitude W. East and west run along parallels: at latitude φ a parallel
has radius 6400 · cos φ, so a flight of the side's length turns the
longitude by a / cos φ. The eastward leg flies along the parallel at
W + a, the westward one along the parallel at W. So the longitude changes
by a / cos(W + a) − a / cos(W), turned into degrees and brought back
into (−180, 180]. `O(1)`.

In the northern hemisphere the eastward leg is nearer the pole and turns
further, so the device ends east of the start; in the southern one the
eastward leg is nearer the equator and the device ends west of it.

Pitfalls:

- the final longitude can cross the 180th meridian in either direction
  (tests 04 and 05);
- a start in the southern hemisphere moves the device west (test 02);
- small values must not print as `-0.000`.

## Language notes

- All five solutions use the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1341_geometry.cpp](1341_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1341_geometry.go](1341_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1096 KB |
| [1341_geometry.java](1341_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1944 KB |
| [1341_geometry.py](1341_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 416 KB |
| [1341_geometry.rs](1341_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 264 KB |
