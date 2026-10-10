# 1151. Locating radio beacons from distances in the maximum metric

[Timus 1151](https://acm.timus.ru/problem.aspx?space=1&num=1151) · difficulty 1041 · geometry

Original problem from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

At most 10 radio beacons stand at integer points with coordinates from 1
to 200. From `M ≤ 20` control points with known coordinates, distances to
some of the beacons were measured, where the distance between `A` and `B`
is `max(|Ax − Bx|, |Ay − By|)`. For every beacon, in increasing order of
its identifier, print its position if exactly one point of the field
fits all its measurements, and `UNKNOWN` otherwise. The measurements are
consistent.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`M`, then `M` lines of the form `X,Y:ID-R,ID-R,…`: a control point, then
beacon identifiers with their distances.

## Output

One line per beacon: `ID:x,y`, or `ID:UNKNOWN`.

## Examples

### Example 1

Input:

```
2
15,15:16-7,5-3
10,10:5-2,16-2
```

Output:

```
5:12,12
16:UNKNOWN
```

## Solution

In the maximum metric the points at distance exactly `r` from a control
point form the boundary of a square of side `2r` around it, at most `8r`
cells, or the point itself when `r = 0`. Every beacon has at least one
measurement, so its candidates are the cells of the first such square
that lie in the field; each of them is kept only if it is at the right
distance from every other point that measured this beacon. If exactly one
candidate survives it is the answer, otherwise the position is
`UNKNOWN`. With at most 1600 candidates and 20 measurements per beacon
this is tiny.

The input lines mix commas, colons and minus signs; all of them only
separate numbers, so a line is read as the list of its digit runs: the
control point, then pairs of identifier and distance.

Pitfalls:

- the border of the field cuts the square, which is often what makes the
  answer unique;
- a beacon can be measured from several points and a point can measure
  several beacons;
- beacons are printed in increasing order of identifier, not in the
  order they appear;
- a distance of `0` puts the beacon on the control point.

The answers were compared with a check of every cell of the field on
every test and on 80 random inputs.

## Language notes

- All languages filter the same squares. C++, Go and Java pick the digit
  runs out of a line by hand, Python uses a regular expression, and Rust
  splits the line at every non-digit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1151_geometry.cpp](1151_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·R) | AC | 0.015 s | 428 KB |
| [1151_geometry.go](1151_geometry.go) | Go 1.14 x64 | geometry | O(M·R) | AC | 0.031 s | 1868 KB |
| [1151_geometry.java](1151_geometry.java) | Java 1.8 | geometry | O(M·R) | AC | 0.156 s | 3572 KB |
| [1151_geometry.py](1151_geometry.py) | Python 3.12 x64 | geometry | O(M·R) | AC | 0.062 s | 920 KB |
| [1151_geometry.rs](1151_geometry.rs) | Rust 1.75 x64 | geometry | O(M·R) | AC | 0.031 s | 372 KB |
