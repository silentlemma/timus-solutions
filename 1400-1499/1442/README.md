# 1442. Floo Powder

[Timus 1442](https://acm.timus.ru/problem.aspx?space=1&num=1442) · difficulty 3004 · geometry

Original problem by Anton Botov (author) and Stanislav Vasiliev (text), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Floo powder was poured into a chest 1 m long, 50 cm wide and 50 cm high
through a hole in the middle of the lid, and formed a right circular
cone of radius r and height h (1 ≤ r ≤ 25, 1 ≤ h ≤ 50). A thin straight
slit runs across the bottom at distance d from the centre of the base
(1 ≤ d ≤ 25). Where the base meets the slit, powder pours out, leaving
flat slopes along the slit with the same angle of repose as the cone.
Find, in cubic centimetres and accurate to four decimal places, how
much powder remains.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

Integers r, d and h, one per line, in centimetres.

## Output

The remaining volume.

## Examples

### Example 1

Input:

```
10
5
2
```

Output:

```
151.704483
```

## Solution

Put the centre of the base at the origin and the slit on the line
x = d. With the slope k = h / r, the cone surface over a point at
distance ρ from the centre has height k (r − ρ), and the slopes along
the slit have height k |x − d|; the powder that remains lies under the
lower of the two. If d ≥ r the slit touches the base or misses it, and
the answer is the whole cone π r² h / 3. Otherwise subtract the lost volume, the
integral of k ((r − ρ) − |x − d|) where that is positive.

Slice the base along the slit. For a fixed x let a = r − |x − d|; the
loss is positive where ρ < a, which is |y| < Y = √(a² − x²), and the
integral over y has a closed form, so the slice loses
k (a Y − x² ln((a + Y) / |x|)) (k a² at x = 0). Slices
exist only for (d − r) / 2 < x < (d + r) / 2. The remaining integral
over x uses adaptive Simpson quadrature, split at x = 0 (logarithmic
limit) and x = d (kink); the square root at the ends is what makes the
adaptive steps worth having. N counts visited subintervals.

Pitfalls:

- when the slit touches the base or misses it, nothing is lost (tests
  02, 06, 10);
- the slit next to the centre removes the most (tests 03, 09);
- accuracy to four decimal places is required, so plain Simpson with a
  few hundred steps is not quite enough near the ends.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1442_geometry.cpp](1442_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 156 KB |
| [1442_geometry.go](1442_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1100 KB |
| [1442_geometry.java](1442_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1772 KB |
| [1442_geometry.py](1442_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 700 KB |
| [1442_geometry.rs](1442_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 252 KB |
