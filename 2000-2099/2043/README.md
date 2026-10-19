# 2043. Serpentine traversal with south-boundary refills

[Timus 2043](https://acm.timus.ru/problem.aspx?space=1&num=2043) · difficulty 4147 · math

Original problem by Ilya Kuchumov (Prepared by Kirill Borozdin), from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid has `n` columns from west to east and `m` rows from south to
north. Process its cells in a vertical serpentine order: start in the
southwest cell, go north through the first column, move east once, go
south through the second, and keep alternating. The starting cell costs
no movement step. Moving to a side-adjacent cell costs one step.

A container initially holds `k` units, and processing a cell uses one.
After every `k` processed cells, unless the last cell has just been
processed, refill as follows: walk straight south to the bottom cell of
the current column, step outside the grid, refill, step back into that
same bottom cell, then reach the next cell of the processing order by a
shortest Manhattan path. The outside-and-back portion costs two steps.
Refill travel does not advance the processing order or consume units.
Stop immediately after processing the last cell. Find the total movement
cost modulo `1000000007`.

## Input

The first line contains `1≤t≤10`. Each of the next `t` lines contains
`n,m,k`, where `1≤n,m≤10^12`, `1≤k≤10^18` and `min(n,m)≤10^6`. In
particular, the area `N=nm≤10^18`. Width and height have different roles
and must not be interchanged. Time limit: 4 seconds; memory limit: 64
MB.

## Output

Print one integer modulo `1000000007` per case, in input order. Answers
are compared as integer tokens.

## Checking

Outputs are compared token by token.

## Examples

```
1
5 3 5
```

```
20
```

There are `15` cells, so the ordinary traversal costs `14` steps.
Refills occur after cells `5` and `10`. At the first, the current and
next heights above the south row are `1` and `0`; its route costs
`1+2+0=3` instead of one step, adding `2`. At the second they are `2`
and `1`, adding `2+2+1-1=4`. The result is `14+2+4=20`; no refill occurs
after cell `15`.

## Solution

### Turn a refill into an extra cost

Use zero-based coordinates with southern height zero. If a refill is
made after ordinal `j`, the current cell is `(x,y)` and the next is
`(u,v)`. Its route costs `y+2+v+|u-x|`, replacing a single ordinary
step. This extra is always even; denote half by `f(j)`. There are
exactly `F=(N-1)//k` refills, so the answer is `N-1+2Σ f(ik)` for
`1≤i≤F`. The `N-1` bound excludes refilling at the final cell even when
`k` divides `N`.

Write `j=qm+r` with `0≤r<m`. If `r>0`, an upward column has `f(j)=r` and
a downward one has `f(j)=m-r`, according to even or odd `q`. At a column
boundary `r=0`, odd `q` gives a top transition of cost `f=m`; even `q`
gives a bottom transition of cost `f=1`. Thus, for `P=2m` and `z=j mod
P`, `f(j)=min(z,P-z)` except that `z=0` has value `1` rather than zero.

### Sum by columns

For zero-based column `c`, take refill ordinals in
`(cm,min((c+1)m,N-1)]`. Their multiplier indices are `a=cm//k+1` through
`b=min((c+1)m,N-1)//k`. If `a>b`, there are none. Otherwise let
`C=b-a+1`.

In an upward column the half-costs form an arithmetic progression from
`ak-cm` to `bk-cm`. In a downward column they run from `(c+1)m-ak` to
`(c+1)m-bk`. Sum each progression as `C(first+last)/2`. If a downward
progression ends at zero, add one for that bottom transition. These
ordinal intervals partition all refills exactly, proving this `O(n)`
method.

### Sum a short prefix of a residue period

Let `g=gcd(k,2m)` and `L=2m/g`. The residues of `ki` have period `L` and
visit exactly `0,g,2g,...,(L-1)g` once each. Put `h=L//2`. Summing the
two sides of the triangular function gives `g h(L-h)`, whether `L` is
even or odd. The zero residue contributes the additional one, so a full
period sums to `C=g h(L-h)+1`.

Write `F=qL+r`. Full periods give `qC`. For nonzero period indices,
`f(ki)=f(k(L-i))`, hence `prefix(r)+prefix(L-r-1)=C-1`. Compute only
`W=min(r,L-r-1)` initial terms. If the complementary prefix is shorter,
subtract it from `C-1`. Generate residues by adding `k mod 2m` and
subtracting `2m` once when needed. These are proper prefixes, so none of
their residues is zero; its special one has already been handled in the
full-period and complement formulas.

Since `W≤floor((L-1)/2)≤m/g≤m`, choose the column method when `n<W` and
the residue method otherwise. The number of iterations is at most
`min(n,m)≤10^6`. The partition of refills proves the column sum, while
the residue permutation and symmetry prove the other sum; choosing
either therefore preserves the answer.

### Short full-column periods in Python

Python can also group full columns by `T=2k/gcd(m,k)`. Advancing `c` by
`T` preserves its parity and `cm mod k`, so its complete-column cost
repeats. `T` is even and `k` divides `Tm`. The existing `columns(T,m,k)`
omits the final bottom refill, so add one to obtain a complete cycle. A
partial group of `R` columns is reconstructed similarly: add its omitted
terminal cost only if `k` divides `Rm`; that cost is `m` for odd `R` and
one for even `R`. After combining cycles and the partial group, subtract
the actual final-cell refill if `k` divides `N`.

This shortcut is selected only when `2T<min(n,W)`. Computing one cycle
and its partial prefix visits fewer than `2T` columns, so it never
worsens the original iteration bound. All calculations remain exact
modulo the answer modulus.

Per case, time is `O(min(n,m)+log(max(k,m)))` and auxiliary arithmetic
storage is `O(1)`. The gcd computations account for the logarithmic
term. The complete input has at most ten cases.

Area, relevant ordinal products and the selected short residue sum fit
64 bits: the latter is at most `m·10^6≤10^18`. Whole progression and
cycle sums may reach roughly `10^30`. C++ and Rust use 128-bit
intermediates. Go, Java and Python divide an even progression factor by
two before reducing factors modulo the modulus; the reduced product is
below `MOD²<2^63`. Go and Java also reduce the full-cycle factors before
multiplication. These reductions preserve the final residue and avoid
overflow.

Do not rotate the grid, refill after the last cell, or charge an initial
movement step. The zero triangular residue costs one. A complementary
prefix has length `L-r-1`, including the subtraction of the period's
final special one. Preserve the top/bottom correction at column
endpoints. Divide the progression's even factor before modular
multiplication, and do not build the grid or enumerate all refills.

## Language notes

All versions use integer gcd and scalar loops. C++ and Rust retain exact
large sums with 128-bit integers; Go 1.14 and Java 8 keep modular 64-bit
sums. Java uses buffered integer input. Python uses the extra
full-column period and bounded modular accumulation and is selected for
PyPy 3.10. Buffers hold only the at-most-ten cases and their answers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2043_math.cpp](2043_math.cpp) | G++ 13.2 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.187 s | 440 KB |
| [2043_math.go](2043_math.go) | Go 1.14 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.328 s | 1108 KB |
| [2043_math.java](2043_math.java) | Java 1.8 | math | O(min(n,m)+log(max(k,m))) | AC | 1.218 s | 552 KB |
| [2043_math.py](2043_math.py) | PyPy 3.10 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.171 s | 2328 KB |
| [2043_math.rs](2043_math.rs) | Rust 1.75 x64 | math | O(min(n,m)+log(max(k,m))) | AC | 0.218 s | 248 KB |
