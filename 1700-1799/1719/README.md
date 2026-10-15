# 1719. Kill the Shaitan-Boss

[Timus 1719](https://acm.timus.ru/problem.aspx?space=1&num=1719) · difficulty 1462 · geometry

Original problem by Alexander Ipatov, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A player stands at the origin, and four bosses stand at given points,
no three on a line. A shot fires along a whole line in both
directions and kills every boss on it. With only two shots left, find
the shortest walk that lets the player kill all four.

## Input

Four lines with the integer coordinates of the bosses, up to 10000 in
absolute value.

## Output

The shortest walk, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
-2 0
2 0
-2 4
2 4
```

Output:

```
2.0000000000
```

## Solution

No three bosses share a line, so each shot kills exactly two. That
gives three ways to split the bosses into the two lines L₁ and L₂, and
two orders of shooting. The player walks to some point P on L₁, shoots
along it, then walks straight to L₂, the nearest point on that line,
and shoots again.

Put P = A + t·u on L₁, with u the unit direction. The walk is then
f(t) = √((t − t₀)² + h²) + |k·t + m|. Here t₀ is where the origin
projects onto L₁ and h is its distance to L₁. The second term is the
distance from P to L₂: k = n·u for the unit normal n of L₂, with
|k| ≤ 1. Both terms are convex, so the minimum is at a kink or where
the slope vanishes:

- t₀, when L₂ is parallel to L₁ (k = 0);
- the crossing point of the lines, t = −m/k, where the second term
  bends;
- t₀ ± k·h/√(1 − k²), where the slope of the first term, which runs
  from −1 to 1, cancels ±k.

Evaluating f at these few points and taking the least gives the exact
minimum, with no search. `O(1)`.

Pitfalls:

- the player may stand on a boss, or start on one of the lines: the
  answer can be 0 (test 02);
- for perpendicular lines |k| = 1 and the slope never cancels, so the
  kink is the answer;
- the shot goes both ways along the line, so the player need not stand
  beyond the bosses.

The answers match an independent accepted implementation, which uses a
ternary search, on 900 random cases. These include nearly parallel
lines far from the origin.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1719_geometry.cpp](1719_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 204 KB |
| [1719_geometry.go](1719_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1136 KB |
| [1719_geometry.java](1719_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1808 KB |
| [1719_geometry.py](1719_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 720 KB |
| [1719_geometry.rs](1719_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 276 KB |
