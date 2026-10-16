# 1808. Chapaev at the Planet Ocean

[Timus 1808](https://acm.timus.ru/problem.aspx?space=1&num=1808) · difficulty 1855 · geometry

Original problem by Alexander Mironenko, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A planet is a water disk of radius r centred at the origin, with
refractive index η. Two observers outside it look along given vectors
and each sees a man somewhere in the water. Could they see the same
man?

## Input

r (1 ≤ r ≤ 1000) and η (1 ≤ η ≤ 100, at most two decimals), then for
each observer the position and the direction of the look, integers up
to 1000 in absolute value. Both observers are outside the planet and
see points strictly inside. If the answer is "Yes", the common point is
at least 10⁻⁴ away from the shore.

## Output

"Yes" or "No".

## Examples

### Example 1

Input:

```
10 2.0
5 10 0 -1
-5 10 0 -1
```

Output:

```
Yes
```

### Example 2

Input:

```
10 1.5
5 10 0 -1
-5 10 0 -1
```

Output:

```
No
```

## Solution

An observer can see any point of the refracted ray inside the water,
which is a chord of the disk. The line of sight first meets the circle
at the smaller root of |P + tD|² = r². At that point split the unit
direction into its part along the inward normal and its tangential
part, of length sin α. Snell's law divides the tangential part by η,
and the normal part becomes √(1 − sin²β), which gives the direction v
inside. From the entry point E the chord has length −2·(E·v). The two
chords share a point exactly when they cross at parameters strictly
between 0 and 1, or when they lie on one line, which happens for two
looks along the same diameter. `O(1)`.

In the examples both look straight down at x = ±5. With η = 2 the rays
bend towards the centre enough to cross on the axis inside the planet;
with η = 1.5 they would meet only beyond its far side.

Pitfalls:

- the refracted ray bends towards the normal, so the tangent part
  shrinks, not the normal part;
- two looks along one diameter give the same chord, which counts as a
  common man;
- the line of sight has to be followed to the first crossing, the root
  with the minus sign.

The answers agree with an independent accepted implementation on 300
random cases with small and large planets and indices, including cases
built to give No, all chosen away from touching or parallel chords.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1808_geometry.cpp](1808_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 144 KB |
| [1808_geometry.go](1808_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1160 KB |
| [1808_geometry.java](1808_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1844 KB |
| [1808_geometry.py](1808_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 800 KB |
| [1808_geometry.rs](1808_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
