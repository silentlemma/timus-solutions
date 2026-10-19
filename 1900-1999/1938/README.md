# 1938. An Equilateral Triangle on Three Lines

[Timus 1938](https://acm.timus.ru/problem.aspx?space=1&num=1938) · difficulty 4558 · geometry

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose one point on each of three distinct infinite straight lines so
that the three points form an equilateral triangle. A suitable answer
is guaranteed to exist. Limits: 1 second, 64 MB.

## Input

Three lines, each containing x₁,y₁,x₂,y₂ for two different points on
one straight line. All coordinates are integers in [−1000,1000].
The three represented lines are pairwise distinct. They may be parallel
or concurrent; the given segments do not restrict the allowed positions.

## Output

Three coordinate pairs, one per line. Point i belongs to input line i.
Every coordinate has absolute value at most 10⁸. Point-to-line distance
must be at most 10⁻⁶, every pair separation at least 10⁻⁶, and the largest
and smallest of the three pairwise distances must differ by at most 10⁻⁶.
All tolerances are absolute. Any qualifying points are valid.

## Checking

A checker verifies the three conditions above with the stated
tolerances; any such triangle is accepted.

## Examples

```
0 -1 1 0
0 -1 -1 0
0 -1 0 1
```

```
1 0
-1 0
0 1.7320508
```

```
3 1 4 1
-2 -1 -4 -1
-4 0 4 0
```

```
0 1
0 -1
1.7320508 0
```

## Solution

Write lines 2 and 3 as Q+t·u and Z+s·v. Choose a base point A on line 1.
For a rotation R by either +60° or −60°, the desired relation is
P₃−A=R(P₂−A). Rotate line 2 about A: its anchor is T=A+R(Q−A) and
direction D=Ru. Intersect that line with line 3. With Δ=Z−T and
det=cross(D,v), the parameters are

t=cross(Δ,v)/det, s=cross(Δ,D)/det.

Return A,Q+t·u,Z+s·v. Each is explicitly on its assigned line, and
P₃−A=R(P₂−A) proves equal side lengths: a 60° rotation preserves the
base length and its chord has that same length.

Two choices make this construction uniformly safe. First, choose the
given endpoint of line 1 with larger |cross(u,endpoint−Q)|, evaluated
with integers. Both values cannot be zero because lines 1 and 2 differ.
Thus A is outside line 2. The nonzero integer area has magnitude at least 1,
so |P₂−A|≥1/|u|≥1/(2000√2)>10⁻⁶. The triangle cannot collapse.

Second, try both rotation directions and use the larger |cross(Ru,v)|.
If θ is the angle from u to v, their normalized determinants are
sin(θ−60°),sin(θ+60°). Their mean square is
¼sin²θ+¾cos²θ=¼+½cos²θ≥¼. The chosen magnitude is therefore at least
|u||v|/2, preventing a nearly parallel intersection in every configuration.

The output bound also follows directly. Let M=1000. Input anchors have
norm≤√2M, so |T|≤3√2M and |Δ|≤4√2M. The determinant bound gives
|t||u|≤2|Δ| and |s||v|≤2|Δ|. Both constructed points have norm≤9√2M
<13000, far below 10⁸. These bounds also keep double-precision errors
small under the absolute tolerance. Print 15 fractional digits.

O(1) time and space: the input always consists of three lines, and the
algorithm uses a fixed number of integer and floating-point operations.

A first input endpoint can be a common intersection; taking it blindly
can produce a zero triangle. Testing just one rotation can lead to a
nearly zero denominator and oversized coordinates. The output order
must preserve line association. Reversing input endpoint order must not
change validity. The lines extend infinitely beyond their defining points.

## Language notes

Endpoint selection uses exact integer cross products before conversion:
C++ long long, Go int64, Java long, Rust i64 and Python integers.
Rotations and intersection parameters use double/float64/f64. Java
specifies Locale.US, and every implementation prints three lines with
two coordinates and a final newline. No numerical search is required.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1938_geometry.cpp](1938_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 448 KB |
| [1938_geometry.go](1938_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1132 KB |
| [1938_geometry.java](1938_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 988 KB |
| [1938_geometry.py](1938_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 848 KB |
| [1938_geometry.rs](1938_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 280 KB |
