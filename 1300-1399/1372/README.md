# 1372. Death Star

[Timus 1372](https://acm.timus.ru/problem.aspx?space=1&num=1372) · difficulty 5382 · geometry

Original problem: idea by Alexander Mironenko, prepared by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A spherical station of radius R has N ≤ 9 engines stuck on, each on a
mast of height h at a given longitude and latitude, each pushing with
the same thrust F in a given direction, also written as a longitude and
latitude. One more engine on the same kind of mast can be put anywhere,
pointed anywhere and given any thrust. Choose it so that the station
stops being spun up, with the least thrust; print its place, its
direction and its thrust to 8 decimal places.

Time limit: 1 second. Memory limit: 64 MB.

## Input

R, the mass of the station and h, then F and N, then N lines: the
longitude and latitude of an engine and of its direction.

## Output

The longitude and latitude of the new engine, those of its direction,
and its thrust. Any answer with the least thrust is accepted.

## Examples

### Example 1

Input:

```
100.3 1000000.45 15.5
156.5 1
0.0 0.0 90.0 0.0
```

Output:

```
0.00 0.00 270.00 0.00 156.50
```

## Solution

The engines spin the station up through their total torque
T = Σ pᵢ × F dᵢ, where pᵢ is the engine's position vector of length
R + h and dᵢ the unit direction of its push. The mass does not matter.
The new engine must add −T.

A force f at a point p gives the torque p × f, and |p × f| ≤ |p| · |f|.
So the thrust is at least |T| / (R + h), and it is exactly that when p is
at right angles to T and f = p × T / |p|²; then p × f = −T. Any point on
the great circle perpendicular to T will do. The solutions take the
coordinate axis least aligned with T, remove its part along T, and use
that as the placement direction. Longitude and latitude come back from
atan2 and asin. `O(N)`.

Pitfalls:

- with no total torque, nothing has to be done: a thrust of 0 (tests 02
  and 04);
- a longitude just under 360 prints as `360.00000000`, so it is folded
  back to 0 (test 09);
- the mass in the input is a decoy;
- longitudes at the poles are arbitrary (test 03).

The tests are judged by a checker that recomputes the torque left and
the least thrust; 400 random stations passed it, many of them with
engines at the poles or along the axes.

## Language notes

- All five solutions use the same vectors; Java reads and prints with
  `Locale.US`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1372_geometry.cpp](1372_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 172 KB |
| [1372_geometry.go](1372_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1096 KB |
| [1372_geometry.java](1372_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2064 KB |
| [1372_geometry.py](1372_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 876 KB |
| [1372_geometry.rs](1372_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 300 KB |
