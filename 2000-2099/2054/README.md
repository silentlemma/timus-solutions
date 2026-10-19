# 2054. Solar altitude from two rotations

[Timus 2054](https://acm.timus.ru/problem.aspx?space=1&num=2054) · difficulty 5873 · geometry

Original problem by Dmitry Ivankov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The Earth is a sphere whose axis keeps a fixed direction tilted by ε =
23.439281° from the normal of its circular orbit; orbiting and spinning
are both counterclockwise seen from the north. A year is exactly 365
days of 24 equal solar hours, and at noon on 21 June, the northern
summer solstice, the Sun is on the observer's meridian. Sunlight is
parallel to the Earth–Sun line. For given moments find the altitude of
the Sun above the horizon at a given latitude, or 0 when it is below.
The limits are 1 second and 64 MB.

## Input

The first line has the latitude l, −89.99 ≤ l ≤ 89.99 with at most two
decimals, and the number of queries n, 1 ≤ n ≤ 8760. Each query is `d m
h`: a valid day of a non-leap year, a month among `jan feb mar apr may
jun jul aug sep oct nov dec`, and a whole hour 0 ≤ h ≤ 23.

## Output

For each query, the altitude of the Sun in degrees, between 0 and 90.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

```
56 3
17 nov 12
17 nov 22
7 jul 12
```

```
14.4968100457
0.0000000000
56.4916089122
```

```
-66.57 1
22 jun 12
```

```
0.0000000000
```

The first example is at northern latitude 56°. On 17 November at noon
the model gives about 14.4968100457°; at 22:00 the Sun is below the
horizon, giving zero. On 7 July at noon it gives about 56.4916089122°.
The second example places the observer at southern latitude −66.57° just
after the northern summer solstice, during the local winter; the scalar
product is negative and the answer is zero.

## Solution

### Orbit and spin in one coordinate system

Use radians inside trigonometric functions. Let `D` be the zero-based
day of the year, obtained from month lengths and `d−1`. The solstice day
is `D₀=171`. Measured in hours from 21 June at noon, `t=24(D−171)+h−12`
and `θ=2πt/8760`. The fractional day in `t` matters: the Earth continues
moving along its orbit between midnight and noon.

Choose the inertial equatorial frame with the north rotation axis along
`z` and the observer's meridian along `x` at the calibration instant.
Choose the positive orbital direction so that the unit vector pointing
from Earth toward the Sun is `S=(cos ε cos θ, sin θ, sin ε cos θ)`. The
vectors multiplying `cos θ` and `sin θ` are perpendicular unit vectors
spanning the tilted orbital plane. At `θ=0`, the Sun has its greatest
northern component, as required at the northern summer solstice.

A solar day describes the spin relative to the moving Earth–Sun
direction. During one orbit the axial rotation makes one extra full turn
relative to an inertial frame: 366 turns in 365 solar days. Thus the
inertial meridian phase is `ψ=2π·366t/8760` modulo a full turn. For
computation use the equivalent small-angle expression `H=2π(h−12)/24`
and `ψ=θ+H`, since the omitted term is a whole number of daily turns.
Keep this orbital contribution to the meridian phase; replacing it with
a meridian freshly aligned to the Sun at every date would be a different
rotation model.

At latitude `φ=lπ/180` the outward unit normal to the local tangent plane is
`N=(cos φ cos ψ, cos φ sin ψ, sin φ)`.
Both vectors now use the same inertial axes, so their scalar product is
`u=cos φ cos ε cos ψ cos θ + cos φ sin ψ sin θ + sin φ sin ε cos θ`.

### Why the formula gives the required angle

For a spherical surface, its radius is perpendicular to the tangent
plane; therefore `N` is exactly the local zenith. The dot product of
unit vectors `N` and `S` is the cosine of the angle from zenith to the
Sun. When the Sun is visible its altitude is the complementary angle, so
its sine is `u`. The unique altitude in `[0,π/2]` is `asin(u)`. A
nonpositive `u` means the Sun is on or below the horizon, and the
required result is zero. This proves that `asin(max(0,u))` gives the
requested angle in every case.

The calendar prefix gives the exact elapsed hours, uniform orbital
motion gives `S`, and uniform axial rotation gives `N`. The dot-product
argument therefore proves the whole algorithm. At the calibration noon,
`u=cos(φ−ε)`; for example latitude 23.44° yields altitude 89.999281°, a
useful near-zenith check.

Do not count a leap day or make June 21 one day late. The origin is
noon, not midnight. Include the hour in orbital motion, preserve the
obliquity's full precision and distinguish inertial spin from daily
solar phase. A formula using declination and a Sun-aligned daily
meridian misses the prescribed rotational phase. Do not take the
absolute value at night. Clamp roundoff before arcsine, especially near
the zenith. Queries may cross month or year boundaries in arbitrary
order; compute each from the common origin.

## Language notes

Precompute the twelve month offsets and the three latitude-dependent
coefficients `cos φ cos ε`, `cos φ` and `sin φ sin ε`. For every query
evaluate `θ`, `ψ` and the displayed scalar product, clamp it to `[0,1]`
against roundoff, take the arcsine and convert back to degrees. Print
ten digits after the decimal point. No simulation with small time steps
or astronomical library is needed.

Each query takes `O(1)` time, so total time is `O(n)`. The mathematical
auxiliary state is `O(1)`, including the fixed calendar. C++ and Go
stream the answers using buffered I/O; Python and Rust retain
input/output tokens and Java accumulates output, using `O(n)` I/O
storage. All ports use double precision, and Python runs under CPython
3.12. Java fixes the decimal locale. Integers suffice for elapsed hours,
including negative hours before the solstice.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2054_geometry.cpp](2054_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 524 KB |
| [2054_geometry.go](2054_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.046 s | 1524 KB |
| [2054_geometry.java](2054_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.171 s | 6556 KB |
| [2054_geometry.py](2054_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.109 s | 2852 KB |
| [2054_geometry.rs](2054_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 668 KB |
