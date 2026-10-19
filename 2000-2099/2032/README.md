# 2032. Realizing three lengths on the integer lattice

[Timus 2032](https://acm.timus.ru/problem.aspx?space=1&num=2032) · difficulty 788 · geometry

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given three positive integer lengths, find three integer-coordinate points whose
three pairwise distances equal those lengths in any order. Lengths are at most
`10000000` and satisfy the triangle inequality. Every coordinate must have
absolute value at most `100000000`. Limits: 1 second, 64 MB.

## Input

One line with the three side lengths.

## Output

Any three integer coordinate pairs separated by whitespace, or `-1` if no
lattice realization exists. The vertex order is arbitrary.

## Checking

A checker compares the three squared distances exactly and verifies the
coordinate bound; `-1` is accepted only when no lattice triangle exists.
Any valid placement is accepted.

## Examples

```
4 3 5
```

```
0 0
3 4
3 0
```

```
10 17 21
```

```
0 0
0 21
-8 15
```

```
100 100 100
```

```
-1
```

## Solution

Sort lengths `r ≤ b ≤ a`. Put `A=(0,0)`, `B=(x,y)`, `C=(u,v)`, with
`|B|=r`, `|C|=b` and `|C-B|=a`. The dot product is `D=(r²+b²-a²)/2`.
An odd numerator rules out integer coordinates. The cross product must be an
integer `K` with `K²=r²b²-D²`. Reject a negative value or a nonsquare using an
exact integer square root. The dot product may be negative.

For any lattice point `B` on radius `r`, solve the dot/cross linear system:
`u=(Dx-Ky)/r²`, `v=(Dy+Kx)/r²`. Return it only if both divisions are exact.

Enumerate all first-quadrant `B`. Try axes first. Dividing nonzero legs by
their gcd `t` gives a primitive Pythagorean triangle with hypotenuse `d=r/t`,
a divisor of `r`. Euclid's parametrization gives legs `m²-k²,2mk` and
`m²+k²=d`, where `m>k≥1`, the parameters are coprime and of opposite parity.
Factor `r` by trial division and generate every divisor. For odd `d≥5`,
try `m` from `floor(sqrt(d/2))+1` to `floor(sqrt(d-1))`, take
`k=isqrt(d-m²)` and check square, gcd and parity. Scale the legs by `r/d`
and test both coordinate orders immediately, without storing a circle.

Why is the search complete? Any lattice embedding can be translated to `A=0`.
Reflect the whole triangle if necessary to make the cross product nonnegative,
then rotate the whole triangle by a multiple of 90 degrees to place `B` in the
closed first quadrant. These operations preserve integer coordinates. Axis cases
and the complete primitive parametrization visit this `B`; the linear system
recovers its unique `C`. Therefore exhaustion proves impossibility. A square
cross product is a necessary precheck, not a substitute for the complete search.

For soundness, the constructed dot and cross give
`|C|²=(D²+K²)/r²=b²` and `|C-B|²=b²+r²-2D=a²`.
Exact divisibility makes coordinates integral. Their absolute values are bounded
by their distances `r,b≤10000000` from the origin, satisfying the output bound.

The first sample has squared distances `25,9,16`, hence lengths `5,3,4`.
The second has `441,289,100`, hence `21,17,10`; negative coordinates are legal.
For the equilateral side 100, `D=5000` and `K²=75000000` is not a square,
explaining the final `-1`.

Let `d(r)` denote divisor count and `M` the largest input side. At most
`O(d(r) sqrt(r))` parameter candidates are visited. The exact binary roots,
including the larger cross-product root, give the common upper bound
`O(d(r) sqrt(r) log(M+1))` time and `O(d(r))` working space.
All intermediate values, including square-root bounds, fit signed 128 bits.

Pitfalls:

- An integer realization need not have a side on an axis.
- Check every divisor, both leg orders, gcd and parity.
- Do not round coordinate divisions or square roots.
- Keep negative dot products and negative coordinates.
- Products reach `10^28`; widen before multiplying.

## Language notes

C++ uses signed `__int128` and Rust `i128`, with exact binary roots.
Go uses `math/big.Int.Sqrt`; Java 8 uses `BigInteger` and an exact integer
Newton iteration because that version has no built-in square root.
Their small binary roots receive values at most `10000000`.
Python uses exact integers and `math.isqrt`. No floating-point geometry is used.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2032_geometry.cpp](2032_geometry.cpp) | G++ 13.2 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.015 s | 404 KB |
| [2032_geometry.go](2032_geometry.go) | Go 1.14 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.031 s | 1236 KB |
| [2032_geometry.java](2032_geometry.java) | Java 1.8 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.140 s | 788 KB |
| [2032_geometry.py](2032_geometry.py) | Python 3.12 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.093 s | 736 KB |
| [2032_geometry.rs](2032_geometry.rs) | Rust 1.75 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.046 s | 244 KB |
