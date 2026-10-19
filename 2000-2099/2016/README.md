# 2016. Fast Portions of Three Spatial Circular Arcs

[Timus 2016](https://acm.timus.ru/problem.aspx?space=1&num=2016) · difficulty 6173 · geometry

Original problem by Denis Dublennykh, prepared by Eugene Kurpilyansky, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A point starts at rest at the origin. A constant acceleration `(0,0,a)`
acts upward, together with a constraint force perpendicular to the
motion, which does no work. The point first moves upward along a circle
centered at `C1`. At its first visit to the point of that circle nearest
`C2`, the center changes to `C2`, preserving the current tangent
velocity. Repeat this rule to switch from `C2` to `C3`, then follow one
full circle around `C3`. Find the total traveled length where speed is
at least `v`.

Each new circle passes through the switching point and has the incoming
velocity as its tangent. Both nearest points are unique, differ from the
respective arc starts, and are reached before a full revolution.
Switching points differ from the new centers. Speed never becomes zero
after the initial instant. These conditions define a valid directed
trajectory, including possible horizontal circles.

## Input

First `t`, `1 ≤ t ≤ 1000`. Each experiment gives integers `v a`, `1 ≤ v
≤ 50,000`, `1 ≤ a ≤ 1000`, followed by the three center vectors. Every
coordinate is an integer in `[-10^6,10^6]`, and `C1.x²+C1.y²>0`. A
horizontal traveled arc never has speed exactly `v`. Time limit 1
second, memory 64 MB.

## Output

Print one total length per experiment, in input order. An absolute or
relative error of at most `10^-6` is accepted; the tests use
`float:1e-6` judging. Isolated threshold-equality points contribute no
length.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

```
1
10 100
4 0 -3
4 16 2
21 16 2
```

```
35.3929206868
```

The first arc has radius 5 and angle `asin(0.8)`, ending at `(4,0,2)`.
The next is a horizontal quarter-circle of radius 16, ending at
`(20,16,2)`. The last is a horizontal full circle of radius 1. The speed
threshold becomes height `0.5`; the qualifying part of the first arc
plus the two complete horizontal arcs gives the output.

## Solution

### Reduce speed to height

The constraint force is perpendicular to velocity and does no work. Per
unit mass, the upward acceleration contributes work `a·Δz`; starting at
height zero with speed zero gives `speed²=2az`. Thus the desired parts
are exactly those with `z≥h`, where `h=v²/(2a)`. There is no need to
integrate time or simulate acceleration along an arc. The positive-speed
guarantee fixes the direction of motion throughout.

### Represent a directed circle

Store center `C`, radius `R`, unit radial vector `A` at the arc start,
and unit forward tangent `B`, with `A·B=0`. Its point at positive
angular displacement `θ` is `C+R(A cosθ+B sinθ)`. Let `N=A×B` be its
unit normal. Initially `R=|C1|`, `A=−C1/R`, and `B` is the normalized
projection of the upward unit vector onto the plane perpendicular to
`A`. Equivalently, use the oriented raw normal `(-C1.y,C1.x,0)` and set
`B=unit(N×A)`; the nonzero horizontal component guarantees that this
tangent exists and points upward.

For the next center let `q=Cnext−C`, `d=q·N` and `ρ=|q−dN|`. The nearest
radial direction is `U=(q−dN)/ρ`. Indeed, squared distance to `Cnext`
equals `R²+|q|²−2R·q·U`; among unit directions in the circle plane it is
minimized precisely by the normalized projection. Uniqueness guarantees
`ρ>0`. The endpoint angle is `atan2(U·B,U·A)`, increased by `2π` if
nonpositive. The first-visit and different-start guarantees put it
strictly between zero and `2π`. Its forward tangent is `T=N×U`.

### Transfer the circle without cancellation

At the switch, the new radial vector is `R·U−q = δ·U−d·N`, where
`δ=R−ρ`. Hence the new radius is `hypot(δ,d)`, and the new unit radial
vector is `(δU−dN)/Rnew`. Its oriented normal is proportional to
`δN+dU`, because `(δU−dN)×T=δN+dU`. Normalize its cross product with the
new radial vector to recover the forward tangent. On the third circle
use angle `2π` instead of finding another switch.

Computing a world-coordinate endpoint and subtracting the next center
can lose the tiny new radial vector, corrupting the following circle's
plane. Instead calculate

`δ = (R²−|q|²+d²)/(R+ρ)`.

This is the rationalized difference of the radii, since `ρ²=|q|²−d²`.
Use compensated sums. Obtain `T=unit(Nraw×q)` and `U=unit(T×N)` to avoid
subtracting nearly parallel projections. When `d=0`, preserve the
original raw normal and reverse its sign only if `δ<0`; repeatedly
normalizing it could destroy exact coplanarity. Initial integer products
fit exactly within the floating-point integer range. Retain
`Rnew²=δ²+d²` for the next transfer. Do not classify a tiny positive
radius as zero with an arbitrary tolerance.

### Measure each arc above the height

The vertical coordinate is `Cz+R(Az cosθ+Bz sinθ)`. Set
`F=R·hypot(Az,Bz)` and `φ=atan2(Bz,Az)`. For `F=0`, the entire arc
qualifies or none does according to its constant height. Otherwise put
`u=(h−Cz)/F`. If `u≤−1`, count the entire arc; if `u≥1`, count zero
length. For `−1<u<1`, let `α=acos(u)`. The allowed angles form intervals
`[φ−α+2πk,φ+α+2πk]`. Intersect them with `[0,L]`, where `L` is the
traveled angle, sum the intersection widths, and multiply by `R`. With
`L≤2π`, `φ∈[-π,π]` and `α<π`, checking shifts `k=-2..2` suffices. These
intervals do not overlap except at endpoints.

The energy identity proves the height condition. The projection and
tangent construction reproduce each prescribed directed arc, and the
interval intersections count exactly the angles satisfying that
condition. Multiplying by radius converts angle to traveled length, so
summing the three contributions gives the required answer.

## Language notes

There are three arcs and a fixed number of interval intersections per
experiment: total time `O(t)`, auxiliary geometry space `O(1)` per
experiment. Whole-input or output buffering uses up to `O(t)` space.
Speed must be converted to floating point before squaring in a 32-bit
language. Centers can have negative coordinates; use the directed first
angle, not the shorter unoriented arc. Handle horizontal circles
separately and include a full final revolution. C++ uses `long double`;
Go, Java, Rust and Python use double precision with compensated
three-term sums. Stable radius and plane updates are essential even when
the final printed length is large.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2016_geometry.cpp](2016_geometry.cpp) | G++ 13.2 x64 | geometry | O(t) | AC | 0.062 s | 544 KB |
| [2016_geometry.go](2016_geometry.go) | Go 1.14 x64 | geometry | O(t) | AC | 0.031 s | 1292 KB |
| [2016_geometry.java](2016_geometry.java) | Java 1.8 | geometry | O(t) | AC | 0.156 s | 3624 KB |
| [2016_geometry.py](2016_geometry.py) | Python 3.12 x64 | geometry | O(t) | AC | 0.171 s | 2084 KB |
| [2016_geometry.rs](2016_geometry.rs) | Rust 1.75 x64 | geometry | O(t) | AC | 0.015 s | 544 KB |
