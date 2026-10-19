# 1973. Expected Triangle Area from an Anchored Convex Polygon

[Timus 1973](https://acm.timus.ru/problem.aspx?space=1&num=1973) · difficulty 4770 · geometry

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fix the first vertex A of a convex polygon. Choose B and C independently
and uniformly by area from its strict interior. Find the expected unsigned
area of triangle ABC. The polygon has 3≤n≤1000 vertices in counterclockwise
order, integer coordinates between −10⁶ and 10⁶ inclusive, and no three
vertices on one line. Limits: 1 second, 64 MB.

## Input

n followed by n pairs x,y in boundary order. The first pair is the fixed
anchor A; changing the starting vertex would change the question.

## Output

One real number: the expected area. Absolute or relative error at most
10⁻⁶ is accepted; satisfying either bound is sufficient.

## Checking

A checker compares the number with error at most 10⁻⁶ · max(1,
|answer|).

## Examples

```
4
0 0
1 0
1 1
0 1
```

```
0.120370370
```

## Solution

Translate A to the origin. Write v₁,…,vₙ₋₁ for the remaining vertices.
The fan triangles Tᵢ=(0,vᵢ,vᵢ₊₁), i=1,…,n−2, have positive areas sᵢ
and partition the polygon apart from boundaries of probability zero.
Let S be the polygon area, dᵢ=2sᵢ=cross(vᵢ,vᵢ₊₁), tᵢ=vᵢ+vᵢ₊₁ and D=Σdᵢ.
For vectors x,y, cross(x,y)=xₓyᵧ−xᵧyₓ. The centroid of Tᵢ is cᵢ=tᵢ/3.

### Two points in different fan triangles

For i<j, every ray in Tᵢ precedes every ray in Tⱼ around the anchor.
The entire angular range is less than π, by convexity, so cross(B,C)≥0
when B lies in Tᵢ and C in Tⱼ. Conditional independence gives expected
cross product cross(cᵢ,cⱼ). The area contributes half that value.
The two possible orders (i,j) and (j,i) have total probability
2sᵢsⱼ/S², so their combined contribution is

sᵢsⱼ·cross(cᵢ,cⱼ)/S².

### Two points in the same triangle

Inside T=(0,u,v), write a uniform point as r((1−t)u+tv). The directional
parameter t is uniform on [0,1], independent of r, whose density is 2r.
Thus E[r]=2/3. For two independent points with parameters (r,t),(q,z),
their anchored triangle area is area(T)·r·q·|t−z|. Since E|t−z|=1/3,
the conditional expected area is (4/27)·area(T).

Weight this by (sᵢ/S)² and add the different-triangle cases:

E = [(4/27)Σsᵢ³ + Σᵢ<ⱼ sᵢsⱼ·cross(tᵢ,tⱼ)/9] / S².

Substituting dᵢ=2sᵢ and D=2S yields

E = [2Σdᵢ³ + 3Σᵢ<ⱼ dᵢdⱼ·cross(tᵢ,tⱼ)] / (27D²).

### Replace the pair sum by a prefix

Before processing j, keep the exact vector P=Σᵢ<ⱼ dᵢtᵢ. Then
Σᵢ<ⱼ dᵢdⱼ·cross(tᵢ,tⱼ)=dⱼ·cross(P,tⱼ). Add
2dⱼ³+3dⱼ·cross(P,tⱼ) to the numerator, update P by dⱼtⱼ and D by dⱼ.
This computes the derived expectation in one scan. Every accumulated
term is nonnegative. The conditioning covers every pair of sampled
points, proving the formula and the prefix implementation correct.

There are `O(n)` arithmetic operations and `O(n)` stored input points,
with `O(1)` additional accumulators. Integer sizes are bounded by the
coordinate and vertex limits.

### Preserve exact differences before rounding

After translation, coordinates are at most 2·10⁶ in magnitude, dᵢ≤8·10¹²
and tᵢ coordinates at most 4·10⁶. Even a loose bound gives prefix
coordinates below 3.2·10²² and |cross(P,tᵢ)| below 2.56·10²⁹, fitting
signed 128 bits. Compute that difference exactly: nearly parallel rays
can make two large products almost cancel. The final numerator can
exceed 128 bits, so C++ and Rust convert the positive terms before
cubing or multiplying by dᵢ. Their positive-term floating sum has no
cancellation. The other versions retain the whole rational numerator
with arbitrary-size integers and round only at the final division.

In the sample d₁=d₂=1, t₁=(2,1), t₂=(1,2), cross(t₁,t₂)=3 and D=2.
The numerator is 2(1+1)+3·3=13; the denominator is 27·4=108. Thus the
answer is 13/108≈0.12037037037, matching the printed value.

Points are uniform by area, so fan triangles must be weighted by their
areas. Keep the first vertex fixed. The expectation of the signed cross
product of two identically distributed points is zero; the unsigned
area requires the angular conditioning above. Do not omit the same-fan
term or replace its factor 4/27 by an unrelated random-triangle formula.
Protect prefix subtraction with exact wide integers, and convert before
forming cubes or squaring D if the target type can overflow.

## Language notes

Python, Go 1.14 math/big and Java 8 BigInteger keep the whole fraction
exact. C++ uses __int128 prefixes and long double accumulation; Rust
uses i128 prefixes and f64 accumulation. All emit twelve decimal places.
Only standard libraries and the selected compiler integer types are used.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1973_geometry.cpp](1973_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 492 KB |
| [1973_geometry.go](1973_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1676 KB |
| [1973_geometry.java](1973_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 4604 KB |
| [1973_geometry.py](1973_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 776 KB |
| [1973_geometry.rs](1973_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 312 KB |
