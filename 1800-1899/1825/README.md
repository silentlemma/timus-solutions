# 1825. Ifrit Bomber 2

[Timus 1825](https://acm.timus.ru/problem.aspx?space=1&num=1825) · difficulty 927 · geometry

Original problem by Alexander Belits, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of two bottles destroys a ring: everything at distance from r to R
of its drop point. The drop points are d apart. Find the total area
destroyed by both bottles.

## Input

d, r₁, R₁, r₂, R₂ (0 ≤ d ≤ 15000, 1 ≤ rᵢ < Rᵢ ≤ 15000).

## Output

The area of the union of the two rings, with absolute or relative
error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
200 100 300 200 300
```

Output:

```
353992.933435
```

## Solution

The union is the sum of the ring areas π(R² − r²) minus their overlap.
A ring is a disc minus a smaller disc inside it, so with L(a, b) the
area common to discs of radii a and b around the two points,

overlap = L(R₁, R₂) − L(r₁, R₂) − L(R₁, r₂) + L(r₁, r₂)

by inclusion and exclusion. L itself is the usual lens: 0 when
d ≥ a + b, π·min(a, b)² when d ≤ |a − b|, and otherwise
a²α + b²β minus the area of the kite through both centres and both
crossing points, where α and β are the half-angles of the lens seen
from the centres, from the law of cosines, and the kite is half of
√((−d+a+b)(d+a−b)(d−a+b)(d+a+b)). The case tests use exact integers,
and strictly inside the lens case the cosines stay away from ±1.
`O(1)`.

In the example L(r₁, R₂) is the whole first inner disc, since a disc
of radius 100 at distance 200 lies inside one of radius 300; the other
three pairs are true lenses.

Pitfalls:

- with d = 0 both lens formulas divide by zero; the containment case
  catches it first;
- a ring can sit entirely inside the other's hole, where the overlap is
  0 even though the outer discs overlap;
- distinguish crossing from tangency: test 06 crosses the larger ring's
  outer circle (distances 8 to 12 versus radius 10), while test 07 is
  externally tangent (7 = 5 + 2) and has zero overlap;
- the areas reach about 10⁹, so a relative error is what matters.

The example agrees with a fine grid count, and all answers agree with
an independent accepted implementation on about 400 random and
touching cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1825_geometry.cpp](1825_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 160 KB |
| [1825_geometry.go](1825_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1076 KB |
| [1825_geometry.java](1825_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1852 KB |
| [1825_geometry.py](1825_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 508 KB |
| [1825_geometry.rs](1825_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 248 KB |
