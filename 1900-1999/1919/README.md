# 1919. A Rectangular Patch from a Cylinder

[Timus 1919](https://acm.timus.ru/problem.aspx?space=1&num=1919) · difficulty 2080 · geometry

Original problem by Dmitry Ivankov, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rectangular opening has sides w and h. For each available cylinder,
decide whether one connected piece can be cut from its lateral wall,
flattened without stretching, and placed over the whole opening.
The piece may follow a spiral around the cylinder. Rotation is allowed;
the top and bottom disks provide no material. The cylinder is described
by its height H and its circumference L, not its diameter.
Limits: 1 second, 64 MB.

## Input

The first line contains w,h, the next line n. Each of the next n lines
contains H,L for one cylinder, in that order. Every length is an integer
from 1 to 1,000,000; 1≤n≤1000.

## Output

For each cylinder, in input order, print exactly `Block the hole` if it
can supply the patch, or `Too small` otherwise. Equality is sufficient:
the patch can touch the cylinder's ends or the cut seam.

## Checking

Compare the output as whitespace-separated tokens, including capitalization.
The phrases are printed on separate lines.

## Examples

```
314 314
4
314 314
314 313
600 500
234 3456
```

```
Block the hole
Too small
Block the hole
Too small
```

## Solution

Unroll the cylinder into a plane whose horizontal coordinate is periodic
with period L, inside a vertical strip of height H. A rectangular patch
in this plane must have vertical extent at most H. No horizontal section
may be longer than L: otherwise two interior points a distance L apart
would represent the same material. Conversely, if every section has length
at most L, periodic projection identifies no interior points, so the
connected rectangle can be cut out. A larger covering piece may be trimmed
to the rectangle, so checking rectangles suffices.

The full horizontal projection is irrelevant: different heights may use
different turns of the cylinder. For example, a 1×1000 opening can be
covered using H=11,L=100, though an ordinary 100×11 sheet would fail.

Let θ∈[0,π/2] be the angle of the w-side to the horizontal. With
c=cos θ,s=sin θ, the vertical extent is Y=w s+h c. The longest horizontal
section passes through the center, by symmetry and convexity, and has
length min(w/c,h/s); a zero denominator means an infinite bound.
Thus the circumference condition is

```text
w ≤ L cos θ  OR  h ≤ L sin θ.
```

Each branch permits a closed angle interval touching 0 or π/2.
On either interval Y is concave, since Y''=−Y<0. Its minimum is at an
endpoint. Consequently it is enough to examine the aligned positions
and the positions where one horizontal chord constraint is tight.

Consider both ordered pairs (A,B)=(w,h),(h,w). The branch with
A≤L cos θ exists only if A≤L. One endpoint is aligned and works when
B≤H. At the other endpoint cos θ=A/L, and the required height is

```text
A (B + sqrt(L²−A²)) / L.
```

Set T=HL−AB. After the previous checks this endpoint fits exactly when
T≥0 and T²≥A²(L²−A²). The sign check is mandatory before squaring.
All comparisons are inclusive and use integers only. If either ordered
pair works, print the positive phrase. The interval argument proves
that a rejected pair of branches leaves no possible rotation.

O(n) bounded-integer operations and O(1) geometric working space.
The implementations that buffer the complete input or output use O(n)
total storage.

Only the opening's sides may be exchanged: H and L have different roles.
L is already the circumference. Area alone does not decide feasibility;
for example 3×11 fails for H=7,L=5. A bounding-box test incorrectly rejects
spiral patches. Preserve the sign of T before multiplication and allow
equality, including A=L where the radical is zero.

## Language notes

HL,AB,A²,L² fit 64 bits, but the squared comparison can reach 10²⁴.
C++ widens before multiplication to `__int128`; Rust uses `u128`, with
an explicit subtraction guard. Go 1.14 uses `math/bits.Mul64` and compares
the high and then low words of the unsigned 128-bit products.
Java 8 uses `BigInteger` for the final products; Python uses exact integers.
There are no floating-point angles, square roots or tolerances in a solution.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1919_geometry.cpp](1919_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 432 KB |
| [1919_geometry.go](1919_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1112 KB |
| [1919_geometry.java](1919_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 960 KB |
| [1919_geometry.py](1919_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 616 KB |
| [1919_geometry.rs](1919_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 260 KB |
