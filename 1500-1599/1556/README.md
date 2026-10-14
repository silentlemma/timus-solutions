# 1556. Multishot in the Secret Cow Level

[Timus 1556](https://acm.timus.ru/problem.aspx?space=1&num=1556) · difficulty 8165 · geometry

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Vasya stands at a point of the plane among N cows (N ≤ 50000), discs of
one radius R (0.4 ≤ R ≤ 2) that touch neither Vasya nor each other.
Vasya picks a main direction and shoots K arrows at once (2 ≤ K ≤ 16);
arrow i (from 0) flies along a ray at the angle Aᵢ = arctan(i/(K − 1) − 1/2)
to the main direction. A ray that crosses or touches a cow hits it.
After each hit the arrow flies on with probability P % (0 ≤ P ≤ 100) and
stops otherwise, and it stops for sure after the fifth hit. Find a main
direction with the largest expected total number of hits.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

N, K, P and R, then the coordinates of Vasya, then those of the N cow
centres; all coordinates are real numbers of absolute value at most 25000.

## Output

The line `The best shot at (x;y) gives Vasya E average hits.`, where
(x, y) is the main direction as a unit vector with at least 10 digits
and E is the expectation with 4 digits.

## Examples

### Example 1

Input:

```
3 5 40 1.0
-2.0 1
0 2.0
3 2.0
4 -3
```

Output:

```
The best shot at (0.8944271910;0.4472135955) gives Vasya 5.8000 average hits.
```

## Solution

Move Vasya to the origin. A ray at the angle θ meets a cow with centre at
distance d and direction c exactly when θ lies within asin(R/d) of c, ends
included. Arrow i flies at φ + Aᵢ for the main direction φ, so it meets
the cow when φ lies in the same interval turned back by Aᵢ. Every hit
has the same chance to pass on, so only the number m of cows on the ray
matters: the arrow scores 1 + q + … + q^(min(m, 5) − 1) with q = P/100.

The sum over the arrows changes only at the 2NK ends of these intervals.
The ends are sorted once; each arrow sees the same sorted list rotated,
so the K lists are merged in one sweep around the circle (with a heap in
Python, by comparing the K heads elsewhere), starting from the intervals
that already hold φ = 0. Each event angle is a candidate where the
entering intervals already count and the leaving ones still do, and each
open stretch between events is a candidate with the counts after the
update; ties go to the middle of a stretch, which is safer to print than
a tangent direction. Ends closer than 10⁻¹² count as one event.

The scores are kept as integers in units of 1/100⁴, so the comparisons
are exact. The sweep takes O(N log N + NK²) time, about 2.6·10⁷ steps.
A checker accepts any direction that scores the best expectation within
10⁻⁴; the results were checked against an independent program.

Pitfalls:

- the formula for Aᵢ is a picture in the original statement, and the
  example confirms arctan(i/(K − 1) − 1/2); the offsets are symmetric,
  so the side they are measured to does not matter;
- touching counts, so the best shot may be a single tangent direction:
  in the example 5.8 is reached only there, with 4.4 and 4.8 on either
  side;
- intervals around the direction of the x axis wrap past 2π
  (tests 02, 06);
- an arrow scores at most five hits however many cows lie on the ray
  (test 03), and with P = 0 every arrow scores 1 at most (test 04);
- a cow at the far corner of the square is only about 10⁻⁵ wide in angle
  (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1556_geometry.cpp](1556_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N + N K^2) | AC | 0.718 s | 2044 KB |
| [1556_geometry.go](1556_geometry.go) | Go 1.14 x64 | geometry | O(N log N + N K^2) | AC | 0.843 s | 5792 KB |
| [1556_geometry.java](1556_geometry.java) | Java 1.8 | geometry | O(N log N + N K^2) | AC | 0.484 s | 15164 KB |
| [1556_geometry.py](1556_geometry.py) | Python 3.12 x64 | geometry | O(N log N + N K^2) | AC | 3.671 s | 25528 KB |
| [1556_geometry.rs](1556_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N + N K^2) | AC | 0.281 s | 7480 KB |
