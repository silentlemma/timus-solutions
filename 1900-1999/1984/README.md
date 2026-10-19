# 1984. An enclosing circle touched by every unit disk

[Timus 1984](https://acm.timus.ru/problem.aspx?space=1&num=1984) · difficulty 214 · geometry

Folklore problem, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place `n` disks of radius 1 inside a circle, with disjoint interiors, so
that every disk touches the enclosing boundary internally. Find the
smallest possible enclosing radius. The input is an integer with
`1≤n≤10`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One integer `n`.

## Output

The minimum radius, as a real number.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
2
```

Output:

```
2
```

## Solution

With one disk the answer is 1. For `n≥2`, write the outer radius as `R`
and let `r=R−1>0`. Internal tangency forces every disk center to lie on
the circle of radius `r` around the enclosing center. Distinct disk
centers must be at least distance 2 apart.

Sort the centers by polar angle. The `n` cyclic angular gaps sum to
`2π`, so one gap `α` is at most `2π/n≤π`. That pair has distance `2r
sin(α/2)≤2r sin(π/n)`. Non-overlap requires this distance to be at least
2; therefore `R≥1+1/sin(π/n)`.

This lower bound is attainable: put the centers at the vertices of a
regular `n`-gon on the circle with radius `1/sin(π/n)`. Adjacent centers
are exactly distance 2 apart, and every other pair is at least that far
apart. Each unit disk reaches outer radius `R=r+1`, so all required
internal tangencies hold. Thus the minimum is `1+1/sin(π/n)` for `n≥2`.

For the example `n=2`, the centers are opposite on a radius-1 circle.
Two unit disks fit inside a radius-2 circle and touch each other, giving
output 2.

The formula uses a constant number of operations: `O(1)` time and `O(1)`
memory. Double precision and ten digits after the decimal point are
sufficient for the required tolerance over this input range.

Pitfalls:

- Every disk must touch the outer boundary; unrestricted disk packing is
  a different optimization problem.
- The centers lie at radius `R−1`, not at radius `R`.
- Handle one disk geometrically before evaluating the formula, which
  would divide by `sin(π)`.
- The angle is `π/n` in radians.
- Interior overlap is forbidden, but tangency between small disks is allowed.

## Language notes

All five versions evaluate the same formula in double precision. C++
obtains π with `acos(-1)`; Python, Go, Java and Rust use their standard
π constants. Java fixes the output locale to use a decimal point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1984_geometry.cpp](1984_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB |
| [1984_geometry.go](1984_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1100 KB |
| [1984_geometry.java](1984_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1820 KB |
| [1984_geometry.py](1984_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 396 KB |
| [1984_geometry.rs](1984_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB |
