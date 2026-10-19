# 2050. Map two spatial lines by a bounded half-turn

[Timus 2050](https://acm.timus.ru/problem.aspx?space=1&num=2050) · difficulty 2874 · geometry

Original problem by Egor Shchelkonogov (idea by Dmitry Ivankov), from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Points A, B define a target line and C, D a source line in space. Find a
rotation about some axis that maps the whole source line onto the target
line. The limits are 1 second and 64 MB.

## Input

Four lines with the integer coordinates of A, B, C and D, each between
−1000 and 1000; A ≠ B and C ≠ D.

## Output

Two points P and Q of the axis, each coordinate within [−2000, 2000] and
at least 1 apart, and then the angle in degrees in [0, 360],
counterclockwise when looking from P towards Q. A rotation always
exists, but `Impossible` is allowed when there is none.

## Checking

A checker rotates the source line and accepts the answer when A and B
are within 10⁻⁵ of its image; any valid rotation is accepted.

## Examples

```
0 0 0
0 1 0
0 0 0
1 0 0
```

```
0 0 1
0 0 0
90
```

```
1 0 1
1 0 0
0 1 1
0 1 0
```

```
0 0 1
0 0 0
270
```

In the first example the source is the x-axis and the target is the
y-axis; the displayed axis and quarter-turn give that line. In the
second example the source and target are parallel to z, through
`(0,1,0)` and `(1,0,0)`. The displayed 270-degree rotation moves the
entire offset line correctly. Our answer may instead use a different
axis and 180 degrees.

## Solution

### Construction

Normalize `B-A` and `D-C` to unit vectors `u,v`. If their dot product is
negative, replace `v` by `-v`: a line has no preferred direction. Thus
`u·v≥0`. Set `m=(A+C)/2` and `s=C-A`.

For `w=u+v,z=u-v` define `H=m+z(s·w)/(2|w|²)`. Take the axis through `H`
in direction `w` and use 180 degrees. A second candidate interchanges
`w,z`. The second is needed only when the directions are not parallel.

The half-turn's linear action is `R(x)=2e(e·x)-x`, with `e=w/|w|`. For
the first candidate it sends `v` to `u`. Let `δ=s·(u+v)/(1+u·v)`. The
two points `C-δv/2` and `A+δu/2` have midpoint `H`, and their difference
is perpendicular to `w`. The half-turn therefore exchanges them, while
mapping their line directions. Hence it maps the complete source line
onto the target. The second candidate is the same argument with `v`
replaced by `-v`. For parallel directions the first candidate has
`z=0,H=m` and works directly.

### Why the axis can fit the coordinate bounds

We must prove the output bounds, not merely find an unbounded axis. For
nonparallel directions put `e=(u+v)/|u+v|`, `f=(u-v)/|u-v|` and choose a
unit vector `g` perpendicular to both. These form an orthonormal basis.
Let `t=|u-v|/|u+v|∈(0,1]` and `d=(C-A)/2`. Components below refer to
this basis.

The closest-to-origin points on the two candidate axes are `P_+=(0,m_f+t
d_e,m_g)` and `P_-=(m_e+d_f/t,0,m_g)`. Cauchy–Schwarz gives `(m_f+t
d_e)²≤(1+t²)(m_f²+d_e²)` and `(t m_e+d_f)²≤(1+t²)(m_e²+d_f²)`.
Consequently
`|P_+|²+t²|P_-|²≤(1+t²)(|m|²+|d|²-d_g²)≤(1+t²)(|A|²+|C|²)/2≤(1+t²)·3·1000²`.
Their weighted average proves at least one candidate has norm at most
`1000√3<1733`. In the parallel case the first candidate is the
perpendicular projection of `m` and has that bound as well.

Compute the first candidate, project `H` onto the plane perpendicular to
its unit direction to obtain its closest point `P=H-e(e·H)`, and accept
it if `|P|≤1900`. Otherwise use the second candidate, whose norm is at
most `1000√3` by the proof. Output `Q=P+2e`. Thus `|P-Q|=2` and both
point norms are below 1902, so every coordinate is strictly inside the
allowed 2000 bound. No legal input requires `Impossible`.

Use double precision and fifteen digits after the decimal point. Compute
the denominator as `2|w|²`; subtracting nearly equal numbers in `1-u·v`
is unnecessary. The first direction always has norm at least `√2`. If
its closest point exceeds 1900, the estimate `|P_+|≤1000√3(1+t)` implies
`t>1900/(1000√3)-1>0.09`, so the selected second direction is also well
conditioned. Parallel or nearly parallel lines need no unstable
intersection computation.

There are always twelve input coordinates and a fixed number of vector
operations: time and auxiliary space are `O(1)`. All five versions
implement the same formulas. Java uses a fixed-size input and US decimal
formatting; Python uses double-precision floats.

Rotate `CD` into `AB`, not the other way round, and check both target
points. Lines are infinite and unoriented; endpoint lengths need not
match. A bisector axis through an arbitrary midpoint is usually wrong:
include the correction term in `H`. A valid geometric axis can lie
outside the output bounds, so consider the second bisector when
required. A separation of two avoids rounding below the required one.
For arbitrary sample answers the angle sense follows the view from `P`
to `Q`; our half-turn has the same action in either sense.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2050_geometry.cpp](2050_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 484 KB |
| [2050_geometry.go](2050_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1140 KB |
| [2050_geometry.java](2050_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1864 KB |
| [2050_geometry.py](2050_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 836 KB |
| [2050_geometry.rs](2050_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 260 KB |
