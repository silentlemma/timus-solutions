# 1953. Maximum-Area Ellipse from Three Sides

[Timus 1953](https://acm.timus.ru/problem.aspx?space=1&num=1953) · difficulty 2527 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (idea by Pavel Ageev).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given the side lengths of a nondegenerate triangle, find the ellipse of
maximum area contained in it. An ellipse is the set of points whose sum
of distances to two foci is at most 2R. Report the distance between the
foci and R, the major semiaxis. The requested pair is unique; a circle
has coincident foci. Limits: 1 second, 64 MB.

## Input

One line of integers a,b,c with 1≤a≤b≤c≤1000 and c<a+b.

## Output

Two real numbers: focal distance, then R. Each may have absolute or
relative error at most 10⁻⁶. Print twelve digits after the decimal point.

## Checking

Both numbers are compared with absolute or relative error 10⁻⁶.

## Examples

```
1 1 1
```

```
0.000000 0.288675
```

## Solution

The maximal ellipse is the Steiner inellipse: center at the centroid,
tangent at the three side midpoints. Here is an area proof, so its use
does not require a geometry lookup. Map any candidate ellipse affinely
to the unit disk. Its containing triangle has area at least 3√3. Indeed,
move its three sides inward parallel until tangent to the disk; this
cannot increase area. For a tangent triangle of inradius 1, area equals
semiperimeter, namely cot(A/2)+cot(B/2)+cot(C/2). The function cot is
strictly convex on (0,π/2); since the half-angles sum to π/2, the sum is
at least 3cot(π/6)=3√3, with equality only for an equilateral triangle.
Thus ellipse area divided by triangle area is at most π/(3√3). The
affine image of an equilateral triangle's incircle attains this ratio.
Affine maps preserve centroids and side midpoints, proving the description
and equality case.

Let p₁,p₂,p₃ be vertex vectors and g their centroid. Write the ellipse as
g+Q^(1/2)u, |u|≤1. Its shape matrix is
Q=(1/6)Σ(pᵢ−g)(pᵢ−g)ᵀ. For an equilateral triangle this is exactly its
incircle's radius squared times the identity; an affine map transforms
both sides as Q→TQTᵀ. Therefore the formula holds for every triangle.
Its eigenvalues λ₊≥λ₋>0 are the squared semiaxes. With S=a²+b²+c² and
triangle area Δ, trace Q=S/18 and det Q=Δ²/27. Consequently
λ₊=(S+√D)/36 and λ₊−λ₋=√D/18, where D=S²−48Δ².

Avoid computing an area or subtracting close floating-point values.
Using Heron's identity gives the exact nonnegative integer expression
D=2[(a²−b²)²+(b²−c²)²+(c²−a²)²]. Set q=√D. The two answers are
sqrt(2q)/3 and sqrt(S+q)/6. This also handles an equilateral triangle:
D=0 gives focal distance zero without any tolerance or special case.

O(1) time and space: integer arithmetic and three square roots.

R is a semiaxis, while the first answer is the full distance between
foci: 2sqrt(λ₊−λ₋). The triangle's incircle is optimal only for an
equilateral triangle. Avoid integer overflow before converting to double,
and avoid S²−48Δ² in floating point near a circle. Thin valid triangles
still have positive area and a genuine ellipse.

## Language notes

Form side squares and squared differences in signed 64-bit integers in
C++, Go, Java and Rust; Python integers are unbounded. A conservative
bound is D<6·10¹²<2⁴³, so all integer operations fit, and conversion to
binary64 is exact. Only then take square roots in double/f64. The positive
sum S+q has no cancellation, and D=0 is represented exactly. Twelve
fractional digits contribute at most 5·10⁻¹³ printing error. All five
programs use only the standard library; Java specifies Locale.US.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1953_geometry.cpp](1953_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [1953_geometry.go](1953_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1104 KB |
| [1953_geometry.java](1953_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1840 KB |
| [1953_geometry.py](1953_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 540 KB |
| [1953_geometry.rs](1953_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 252 KB |
