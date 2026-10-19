# 2022. A Projectile Through a Thick Horizontal Opening

[Timus 2022](https://acm.timus.ru/problem.aspx?space=1&num=2022) · difficulty 3530 · geometry

Original problem by Nick Burlakov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A moving launch point starts at ground position `(0,0)` with velocity
`(vx,vy)` under downward gravity `g=10`. A wall occupies horizontal positions
`L ≤ X ≤ L+l`. Its opening has floor height `h` and ceiling height `h+d`.
At some time while the launch point is airborne and before the wall, it may
release a point projectile with **absolute** velocity `(ux,uy)`. Gravity is
the only acceleration for both objects. Find any release time whose projectile
crosses the entire opening without touching its floor or ceiling.

The eight integers `L,h,l,d,vx,vy,ux,uy` are all between 1 and 1,000.
Distances are in meters, velocities in meters per second, and the x-axis
points toward the wall. Time starts when the moving point leaves the ground.
The reported time must remain wall-clear if shifted by `ε=10⁻⁶` seconds
in either direction. The input guarantees such a robust answer whenever
a feasible answer exists. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `L h l d`; the second contains `vx vy ux uy`.

## Output

Print any valid release time with absolute or relative error at most `10⁻⁶`,
meeting the robustness requirement. If no answer exists, print `-1`.

## Checking

A checker verifies that the projectile clears the whole opening for
every release time within 10⁻⁶ of the answer, and that `-1` is printed
only when no time works; any such time is accepted.

## Examples

```
4 2 2 4
1 1 5 10
```

```
0.1
```

```
30 15 5 5
10 10 20 10
```

```
-1
```

## Solution

At release time `t`, the launch point is `(vx t, vy t−5t²)`. At wall
position `X`, the projectile has flown for `τ=(X−vx t)/ux`, so its
height is `Y(t,X)=vy t−5t²+uy τ−5τ²`. The release domain is
`0<t<T=min(2vy/10,L/vx)`. The speed is absolute: do not add the launch
point's velocity.

For fixed `t`, height is a concave quadratic in `X`, so the lowest point
inside the wall is at one of its two faces. Enforce `Y(t,L)>h` and
`Y(t,L+l)>h`. Clearing the positive denominator gives
`ux²(Y(t,X)−H)=−At²+Bt+C`, where `A=5(ux²+vx²)`, `B=vy ux²−uy vx ux+10X
vx`, `C=uy X ux−5X²−H ux²`. Each floor inequality is true in the open
interval between its two real roots; a double root merely touches the
floor and is insufficient. Intersect these intervals with `(0,T)`,
obtaining one open interval `I`.

Ceiling clearance needs the highest point, which may be **inside** the wall.
The projectile's apex is at `X*=vx t+ux uy/10`. The maximum height is:

- `Y(t,L)` when `X*≤L`;
- `vy t−5t²+uy²/20` when `L≤X*≤L+l`;
- `Y(t,L+l)` when `X*≥L+l`.

These pieces change at `(10L−ux uy)/(10vx)` and
`(10(L+l)−ux uy)/(10vx)`. For each piece, solve where its quadratic is
**at least** `h+d` and intersect with its piece domain and `I`.
This is a closed forbidden interval, possibly a single tangent point.

Why can all forbidden pieces be united into one interval? The physical
function is jointly concave in `(t,X)`: it is linear terms minus `5t²`
and minus `5((X−vx t)/ux)²`. Given maximizing positions for two times,
their convex combination remains inside the fixed wall interval. Joint
concavity shows that the maximum height at the mixed time is at least the
same mixture of the two maxima. Thus `F(t)=max_X Y(t,X)` is concave, and
its superlevel set `F(t)≥h+d` is an interval or a point. Take the smallest
left and greatest right forbidden endpoints, then subtract this **closed**
set from `I`. At most two open feasible intervals remain.

Choose the widest remaining component and its midpoint. A width greater
than `2ε` gives more than `ε` clearance in time from both boundaries,
including a forbidden tangent point. The promise ensures an eligible
component when an answer exists. Never combine the two feasible components
across their forbidden middle. All operations involve a constant number
of quadratics, so time and auxiliary space are both `O(1)`.

For stable roots of `−At²+Bt+C`, compute the discriminant `D=B²+4AC`
as an exact integer first. For `D>0`, use
`q=(B+copysign(sqrt(D),B))/2` and the roots `q/A`, `−C/q`, avoiding subtraction
of nearly equal numbers. Handle `D=0` explicitly. Under the input limits,
`A≤10⁷`, `|B|≤1.02·10⁹`, `|C|≤2.02·10⁹`, and
`|D|≤1.1212·10¹⁸`, so signed 64-bit intermediate arithmetic suffices.
Retain the chosen time's round-trip precision when printing.

In the first sample, at `t=0.1` the face heights are 4.808 and 4.888,
and the interior apex is 5.05, all strictly between 2 and 6. In the second,
even the moving point's maximum height plus the projectile's additional
rise is only 10, below the floor at 15, so no time works.

Pitfalls:

- `h` is the floor height; the ceiling is `h+d`.
- Test the interior apex for the ceiling, not only the two wall faces.
- Keep a zero-width forbidden interval at an exact ceiling tangency.
- Compute integer products in 64 bits before converting to floating point.
- Use one feasible component's midpoint and preserve the full ±ε time margin
  (tests 072–073). Generators must reject feasible inputs with no component wider
  than `2ε`: integer bounds alone do not ensure the input promise. For example,
  `random_full` seed 452071 originally produced only a 1.256-microsecond component.

## Language notes

C++, Go, Java and Rust use signed 64-bit polynomial coefficients and
discriminants; Python uses arbitrary-precision integers. All five use
binary64 roots with the stable formula and print enough digits to preserve
the selected value. No time grid, iterative search or simulation step is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2022_geometry.cpp](2022_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [2022_geometry.go](2022_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1108 KB |
| [2022_geometry.java](2022_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 648 KB |
| [2022_geometry.py](2022_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 816 KB |
| [2022_geometry.rs](2022_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB |
