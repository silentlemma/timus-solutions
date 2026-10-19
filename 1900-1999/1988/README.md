# 1988. Meet a surface traveler without crossing the sphere

[Timus 1988](https://acm.timus.ru/problem.aspx?space=1&num=1988) · difficulty 1154 · geometry

Original problem by Mikhail Rubinchik, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sphere centered at the origin has radius `R=|A|>0`. A traveler starts
at `A` on its surface and moves along the surface at speed at most 1. A
second traveler starts at `S`, with `|S|>R`, and moves outside the
sphere or on its surface at speed at most `v`. Find the earliest time
they can meet. Either traveler may wait.

The coordinates of `A` and `S` are integers of absolute value at most
100, `1≤v≤100` is an integer, and `0<|A|²<|S|²`. Time limit: 0.5
seconds; memory limit: 64 MB.

## Input

Three coordinates of `A`, then three coordinates of `S`, then the speed
`v`, on three lines.

## Output

One real number: the minimum meeting time.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
-1 1 -1
10 10 10
1
```

Output:

```
15.588457
```

## Solution

Let `D=|S|`, and let `θ` be the angle between `A` and `S`. Measure a
surface point's angle `β` from the direction of `S`. For a fixed `β`,
the shortest surface distance from `A` is `R|θ−β|`, attained on a great
circle through both starting directions. This follows from the spherical
triangle inequality. Points with `β>θ` are dominated by the initial
surface point: they require no shorter flight and a positive surface
trip. It suffices to search `0≤β≤θ` along the short great-circle arc
toward the point directly below `S`.

### Shortest flight around the obstacle

Write `h=√(D²−R²)` and `α=atan2(h,R)`, the angular radius of the visible
cap. For a destination at angle `β`, the shortest legal flight length is

- `L(β)=√((D−R)²+4DR sin²(β/2))` if `β≤α`: the straight segment is visible;
- `L(β)=h+R(β−α)` if `β>α`: a tangent segment followed by a surface arc.

The second expression is a lower bound for every exterior path, not just
a convenient route. Any path reaching angular distance `β>α` must first
cross the cone of angular distance `α`. At that crossing its radius
`ρ≥R`, and its distance from `S` is at least `√((ρ−R)²+D²−R²)≥h`, since
`D cos α=R`. The remaining path has length at least `R(β−α)`: radial
projection of an exterior path onto the sphere cannot increase length.
The tangent and great-circle arc attain both bounds. For `β≤α`, the
visible chord attains the ordinary Euclidean distance lower bound.

### Balance the arrival times

The surface traveler needs `R(θ−β)` time and the exterior traveler needs
`L(β)/v`. They can wait, so the meeting time at that point is the
maximum of the two, not their sum. The first is decreasing in `β`; the
second is increasing and continuous.

If `Rθ≤(D−R)/v`, both can meet at `β=0` in time `(D−R)/v`. This is
globally minimal because every flight to the sphere has length at least
`D−R`. Otherwise the two arrival times cross exactly once inside
`(0,θ)`. Bisect this angle interval 80 times. If the surface arrival
time is larger, increase the lower angle bound; otherwise decrease the
upper bound. Evaluate the maximum of both arrival times at the final
midpoint.

### Stable evaluation and correctness

Compute dot products, cross products, and `Δ=|S|²−|A|²` as integers. Use
`θ=atan2(|A×S|,A·S)`, which handles parallel and antiparallel starts
without division by a cross product. Compute the radial gap as `Δ/(D+R)`
instead of subtracting two nearly equal square roots. For the visible
flight use `hypot(D−R,2√(DR) sin(β/2))`, avoiding subtraction of nearly
equal squared distances.

Both arrival-time functions are `R`-Lipschitz on the searched interval
because `v≥1`. The exact-arithmetic bisection interval after 80 steps
gives a time error at most `Rπ/2⁸⁰<5·10⁻²²`. Double precision and ten
printed decimal places leave ample margin for the required `10⁻⁶`
tolerance; independent high-precision checks cover the floating-point
evaluation. Integer squared norms are at most 30,000. Since their
difference is a positive integer, the radial gap is at least
`1/(2√30000)`, so the minimum time is positive even at speed 100.

In the example, `R=√3` and `D=10√3`. The surface traveler can reach the
point below `S` before the radial flight arrives, so the optimum is
`9√3≈15.5884572681`, matching the printed output within tolerance.

There are 80 constant-size iterations: `O(B)` time for `B=80`, hence
`O(1)` under the problem constraints, and `O(1)` memory.

Pitfalls:

- A chord to an invisible point crosses the sphere and is forbidden.
- The meeting time is the maximum of the arrival times; either traveler
  can wait.
- Surface distances are great-circle arc lengths, not straight chords.
- Include the boundary optimum directly below the exterior start.
- Use radians and stable dot/cross angle evaluation at collinear configurations.
- Preserve the strict input condition `|S|²>|A|²>0` when generating tests.

## Language notes

All five versions use the same 80-step angle search and double-precision
geometry. Integer dot and cross products use wide integer types in
compiled versions; Python uses exact integers. Each language provides
`atan2` and `hypot`. Java fixes the output locale to use a decimal
point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1988_geometry.cpp](1988_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 480 KB |
| [1988_geometry.go](1988_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1120 KB |
| [1988_geometry.java](1988_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1816 KB |
| [1988_geometry.py](1988_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 736 KB |
| [1988_geometry.rs](1988_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 264 KB |
