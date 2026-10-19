# 1853. Laser Technologies

[Timus 1853](https://acm.timus.ru/problem.aspx?space=1&num=1853) · difficulty 6453 · geometry

Original problem by Denis Dublennykh, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A laser source and its receiver sit on the border of a convex polygon,
d apart along the border, and the beam always runs straight from one to
the other. Both move along the border at the same constant speed in the
same direction until they are back where they started. Glass turns
cloudy where two consecutive pulses cross, so the beam draws a curve:
find the total length of all the lines it draws.

## Input

n (3 ≤ n ≤ 10 000) and the vertices counter-clockwise, integers of
absolute value at most 10⁶; then the integer d, larger than the longest
side and at most half the perimeter.

## Output

The total length, with absolute or relative error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
3
-1 0
1 0
0 10
11
```

Output:

```
22.3730148246
```

### Example 2

Input:

```
4
0 0
10 0
10 10
0 10
11
```

Output:

```
56.1255583559
```

## Solution

Consecutive pulses cross at the point where the moving beam touches its
envelope, so the drawing is the envelope of the family of beams. Cut
the motion at the moments when the source or the receiver passes a
vertex; there are at most 2n of them, found by walking both points
along the border together. Between two such moments the source moves as
A + t·u_A and the receiver as B + t·u_B with unit directions of their
sides, so the beam vector is D(t) = D₀ + tV with V = u_B − u_A, and
M = D × V stays constant.

The touching point is E = A + λD, where the line through it does not
move sideways: (u_A + λV) × D = 0 gives λ = (u_A × D)/M, linear in t.
E′ runs along the beam, so its speed is |E′·D|/|D|, which works out to
|R(t)|/√Q(t) for Q = |D|² and a quadratic R. Writing R = αQ + βQ′ + γ
turns the integral into √Q terms and ∫dt/√Q = asinh((Q′/2)/|M|)/√a,
where a = |V|² and the discriminant of Q is −4M²; the asinh form avoids
the cancellation of the usual logarithm. R changes sign at its
roots, where the curve has cusps, so each stretch is cut there too.

Going counter-clockwise, the source and the receiver always move to
opposite sides of the beam, so the touching point lies between them,
inside the glass. `O(n)`.

When d is exactly half the perimeter of a square, every beam passes
through the centre, so the drawing is a single point and the answer is
0.

Pitfalls:

- the two endpoints cross vertices at different moments: walk them
  together instead of looking positions up by floating-point distance;
- M is positive for a convex polygon and zero only when the beam lies
  along a side, where nothing is drawn;
- ln(2at + b + 2√(aQ)) can lose precision when 2at + b is negative and
  large; asinh avoids this cancellation.

The answers agree with an independent accepted implementation to within
10⁻⁷ on two hundred random polygons, among them circles of 9000
vertices, thin needles and d at both of its limits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1853_geometry.cpp](1853_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.046 s | 312 KB |
| [1853_geometry.go](1853_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 2016 KB |
| [1853_geometry.java](1853_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 6176 KB |
| [1853_geometry.py](1853_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.218 s | 4076 KB |
| [1853_geometry.rs](1853_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 776 KB |
