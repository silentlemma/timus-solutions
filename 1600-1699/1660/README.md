# 1660. The Island of Bad Luck

[Timus 1660](https://acm.timus.ru/problem.aspx?space=1&num=1660) · difficulty 5926 · geometry

Original problem by Alexander Kokovin (prepared by Alexander Ipatov), from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A circle of radius R is drawn, and inside it a circle of radius r whose
centre is d away. The first player draws a circle touching the big one
from inside and the small one from outside. Then, one after another,
each next circle must touch both given circles and the circle drawn just
before it, without crossing any other circle (touching the very first
one is allowed). When a step can go two ways, the first player decides.
Once no circle fits, the distance between the first and the last circle
is measured. Find the smallest distance the first player can achieve.

## Input

Integers R, r and d, with 0 < r < R − d, d ≥ 0, all at most 100.

## Output

The distance, with at least 5 digits after the decimal point.

## Examples

### Example 1

Input:

```
3 1 0
```

Output:

```
0.00000
```

## Solution

The circles form a Steiner chain. Inverting the plane around a limit
point of the two given circles (one of the two points that are mirror
images of each other in both circles at once) makes the two circles
concentric. The limit point inside the small circle is

p = 2·d·R² / (b + √(b² − 4·d²·R²)), with b = R² + d² − r²,

measured from the big centre towards the small one; for d = 0 it is the
common centre, so no special case is needed. Inversion keeps touching
and crossing as they are, and in the concentric picture every chain
circle has the same radius w and the same distance m from the centre,
so each new circle is the previous one turned by the same angle
α = 2·asin(w / m). The chain therefore always has n = ⌊2π / α⌋ circles,
and the last one sits (n − 1)·α away from the first, whatever the start.

The only freedom left is where the first circle starts (the other
direction is just a mirror image). Mapping the first and the last circle
back gives their distance |c₁ − c₂| − r₁ − r₂ as a function of the start
angle. The best start is always symmetric: the first and last circles
mirror each other across the centre line (any diameter if d = 0), with
the gap centred on either ray. This was checked on all 166 650 valid
inputs against a scan of 20 000 start angles refined by ternary search;
the two agree within 10⁻¹⁰. In practice the gap on the narrow side of
the ring wins; the solution simply takes the smaller of the two. `O(1)`.

Pitfalls:

- when the chain closes exactly the answer is 0, so the count needs a
  little slack against rounding (tests 01 and 05);
- with only two circles the last one touches the first (test 06);
- written as above, the limit point needs no subtraction of nearly equal
  numbers, which keeps thin rings accurate (tests 02–04).

The answers match an independent accepted implementation on all 166 650
inputs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1660_geometry.cpp](1660_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 156 KB |
| [1660_geometry.go](1660_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1128 KB |
| [1660_geometry.java](1660_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1812 KB |
| [1660_geometry.py](1660_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 584 KB |
| [1660_geometry.rs](1660_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 264 KB |
