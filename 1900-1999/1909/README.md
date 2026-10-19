# 1909. First Contact Without Square Roots

[Timus 1909](https://acm.timus.ru/problem.aspx?space=1&num=1909) · difficulty 3960 · geometry

Original problem by Pavel Atnashev, prepared by Daniil Ayzenshteyn, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two distinct points A,B move with the same nonzero constant velocity v.
Their connecting segment is monitored against a fixed solid sphere with
center C and positive radius R. Initially the entire segment is clear.
At its first contact with the sphere, both points stop immediately.
Determine whether that contact includes an endpoint, lies strictly inside
the segment, or never occurs. Tangency counts as contact. An endpoint
contact tied with segment contact is a collision. Limits: 1 second, 64 MB.

## Input

Four lines: Cx Cy Cz R; Ax Ay Az; Bx By Bz; vx vy vz.
All 13 values are integers of absolute value at most 100 000. R>0,
A≠B and v≠0. The initial segment, including both endpoints, does not
intersect or touch the sphere.

## Output

Print `Crash` for endpoint contact, `Warning` for a first contact strictly
inside the segment, or `False alarm` if there is no contact. Later endpoint
intersections along the original trajectories do not cause a collision
if an earlier interior contact has already stopped both points.

## Checking

The exact, case-sensitive outcome is checked token by token.

## Examples

```
0 0 0 1
2 0 0
3 0 0
-1 0 0
```

```
Crash
```

```
0 0 0 1
2 0 0
0 2 0
-1 -1 0
```

```
Warning
```

```
0 0 0 1
2 0 0
3 -1 0
1 1 0
```

```
False alarm
```

## Solution

Translate the sphere center to the origin. Use dot and cross products:

```text
w0 = A-C, w1 = B-C, u = w1-w0, U = dot(u,u)
n = cross(u,v), j = cross(u,w0)
a = dot(n,n), b = dot(j,n), c = dot(j,j)-R²U
q(t) = at²+2bt+c
K = R²a-dot(w0,n)²
```

The squared distance from the origin to the moving supporting line,
minus R², is q(t)/U. An interior first contact requires this line to enter
the sphere from outside. Thus a>0, c>0, b<0 and its discriminant must be
nonnegative. If the line is initially inside but the segment is clear,
first segment contact can only be at an endpoint. A later exit tangency
strictly inside the segment would imply an earlier intersection by continuity.
If a=0, movement is along the line and again first contact is at an endpoint.

Do not form D=b²−ac in a 128-bit implementation. The Lagrange identity
gives D=U·K. Since U>0, K gives its sign and detects a double root.
When a>0,c>0,b<0,K≥0, the first line contact is at the positive time
t₀=(−b−√D)/a. Its closest point lies strictly inside the segment exactly
when u·(w0+vt₀)<0 and u·(w1+vt₀)>0. If both inequalities hold, return
`Warning`: no endpoint can contact earlier than its supporting line.

We can test those signs without evaluating t₀. For either endpoint w,
put x=u·w, y=u·v. If y=0, the sign is simply sign(x). Otherwise let
z=−x/y=num/den with den>0 and H=a·num+b·den. H compares z with the
quadratic vertex −b/a. If H≥0, sign(t₀−z)=−1, except H=0,K=0 gives zero.
If H<0, z lies left of the vertex and sign(t₀−z)=sign(q(z)).
At z the endpoint is perpendicular to u, so this last sign equals
the sign of E=||w·y−v·x||²−R²y², because q(z)y²/U=E.
Finally sign(x+yt₀)=sign(y)·sign(t₀−z). Equality in either endpoint test
belongs to `Crash`, hence the strict interior inequalities.

If no interior first contact exists, test both forward endpoint rays.
For offset w, let p=w·v and V=v·v. The initial point is outside the sphere,
so its ray hits exactly when p<0 and p²≥V(w·w−R²). Equality is tangency.
If either ray hits, return `Crash`; otherwise return `False alarm`.
No earlier interior contact remains to stop these rays.

The number of arithmetic operations and auxiliary space are O(1).
Coordinate offsets and u have components at most 2·10⁵; v has components
at most 10⁵. Bounding these products gives |H|≤1.152·10³³ and
|E|≤1.728·10³³, so every computed intermediate fits signed 128 bits.
The unused full D may exceed that range, which is why K is essential.

## Language notes

C++ and Rust use signed 128-bit values throughout the vector operations;
64-bit multiplication followed by a cast is unsafe. Go 1.14 uses math/big,
Java 8 uses immutable BigInteger values, and Python 3.12 uses exact integers.
Go helpers allocate their results so inputs are never mutated by aliasing.
Production uses no square root, division, floating point or tolerance.
Keep the first-event rule: checking possible endpoint collisions first
would misclassify a trajectory stopped by an earlier beam contact.

The answers agree with a high-precision search for the first contact on
6957 cases, among them 32 exact cases for tangency, ties at an endpoint,
one-unit shifts and nearly parallel directions; an independent accepted
implementation agrees on 48 more.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1909_geometry.cpp](1909_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 440 KB |
| [1909_geometry.go](1909_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1216 KB |
| [1909_geometry.java](1909_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1756 KB |
| [1909_geometry.py](1909_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 764 KB |
| [1909_geometry.rs](1909_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 220 KB |
