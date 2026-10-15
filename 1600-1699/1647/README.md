# 1647. Divide an Island!

[Timus 1647](https://acm.timus.ru/problem.aspx?space=1&num=1647) · difficulty 836 · geometry

Original problem by Vladislav Isenbaev (prepared by Alexander Ipatov), from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An island is a non-degenerate triangle. Find two points S and T on its
coast such that the segment ST splits the island into two parts of
equal area and equal coast length, or report that there are none.

## Input

Six integers x₁ y₁ x₂ y₂ x₃ y₃, at most 2000 in absolute value.

## Output

`YES` and the coordinates of S and T with precision 10⁻⁹, or `NO`. Any
valid segment is accepted.

## Examples

### Example 1

Input:

```
0 0 10 0 0 10
```

Output:

```
YES
0 0
5 5
```

### Example 2

Input:

```
0 3 4 0 3 4
```

Output:

```
YES
1.741248277008306 3.580416092336102
3.445803840397070 0.415647119702198
```

## Solution

Walk around the coast by arc length. Put S at arc position s and T half
a perimeter further, so the coast is always split evenly; let f(s) be
the area on the side from S to T minus half of the triangle. Moving S
by half a perimeter swaps the two parts, so f(s + P/2) = −f(s), and f
is continuous: it has a root in [0, P/2]. Hence the answer is always
`YES` (such lines are exactly the ones through the incentre), and
bisection finds a root.

The area of a part is the shoelace formula over S, the corners passed
on the way to T, and T, with the corners listed at their arc positions
twice round so that the wrap past the first corner needs no special
case. Two hundred halvings leave the interval far below double
precision. `O(1)` with a constant of a few thousand operations.

Pitfalls:

- `NO` is never the answer, though the statement allows it;
- the chord may start or end at a corner, as in the first example; the
  arc parametrisation handles that without special cases;
- a checker accepts any valid chord, since there may be up to three.

The program's chords pass the checker on all tests, as do those of an
independent accepted implementation on 180 random triangles.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1647_geometry.cpp](1647_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 216 KB |
| [1647_geometry.go](1647_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1116 KB |
| [1647_geometry.java](1647_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1988 KB |
| [1647_geometry.py](1647_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 848 KB |
| [1647_geometry.rs](1647_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 276 KB |
