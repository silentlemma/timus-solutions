# 1986. Expand recursive mixtures exactly

[Timus 1986](https://acm.timus.ru/problem.aspx?space=1&num=1986) · difficulty 1176 · matrix

Original problem by Pavel Klimov, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each named mixture is defined by integer percentages of other named
components. A component with its own recipe is a mixture; every other
component is a base ingredient. Expand every recipe into percentages of
all base ingredients, including zeros, in lexicographic order. Recipes
may refer to themselves or form cycles. A unique expansion is
guaranteed.

There are at most `n=10` recipes and `m=10` base ingredients. Names
contain 1–10 lowercase Latin letters. Each listed percentage is an
integer from 1 to 100, and the percentages of each input recipe sum to
100. Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

Read recipe lines until EOF; there is no initial count. A line has the
form `name : component percentage component percentage ...`. Recipes and
components within a recipe are listed lexicographically.

## Output

For each recipe, print `name : base percentage ...`, with recipe names
and all global base names in lexicographic order. Include an explicit
zero for absent bases. Each resulting recipe totals 100 percent.

## Checking

A checker solves the equations exactly and compares every percentage
with absolute or relative error 10⁻³; it also checks the names, their
order and the totals.

## Examples

Input 1:

```
razduv : cucumber 30 razgon 50 tomato 20
razgon : bread 40 cucumber 20 razduv 40
```

Output 1:

```
razduv : bread 25.0 cucumber 50.0 tomato 25.0
razgon : bread 50.0 cucumber 40.0 tomato 10.0
```

Input 2:

```
razduv : cucumber 100
razgon : tomato 100
```

Output 2:

```
razduv : cucumber 100.0 tomato 0
razgon : cucumber 0 tomato 100.0
```

## Solution

Collect and sort recipe names. A component absent from this name set is
a base; sort the union of those names too. Let `P[i,j]` be the input
percentage of recipe `j` in recipe `i`, and `b[i]` the direct input
percentage of a chosen base. Let `x[i]` be its final fraction, between
zero and one. The equations are `A x=b`, where `A=100I−P`. The
right-hand side is the input percentage, not that percentage multiplied
by another 100.

The guaranteed unique valid expansion gives a nonsingular system.
Compute `d=det(A)` and, for every recipe position `i` and base,
`dᵢ=det(A with column i replaced by b)`. Cramer's rule gives
`x[i]=dᵢ/d`. All operations until decimal formatting are integers. This
avoids loss of accuracy in recipes that repeatedly return to the start
and escape to bases only after many rare transitions.

### Fraction-free determinants

Use Bareiss elimination on a copy of the integer matrix. The previous
pivot starts at 1. At stage `k`, find a nonzero entry in column `k` at
or below the diagonal, swap that row into place, and track the
determinant sign. If no pivot exists, this determinant is zero, which is
valid for an absent ingredient. For each `i,j>k`, replace the entry by
`(a[i,j]·pivot−a[i,k]·a[k,j])/previous`, then zero the eliminated
column. The division is exact. Save the current pivot as the previous
pivot. The last diagonal entry, adjusted for row swaps, is the
determinant.

Why does signed 128-bit arithmetic suffice? Each row of `[A | −b]` is a
weighted sum of vectors `eᵢ−eⱼ` or `eᵢ`, with nonnegative integer
weights summing to 100. Restrict any chosen rows and columns. A matrix
of these incidence vectors has determinant zero or ±1: expand a column
with at most one nonzero; if there is no such column, every row and
column has two nonzeros and the row sums are zero. By multilinearity,
every minor of order `k` has absolute value at most `100ᵏ`. A
replaced-column matrix has the same bound, up to changing a column's
sign. Bareiss entries are minors. With at most ten rows, the largest
predivision subtraction combines two products of order-nine minors,
bounded by `2·100¹⁸=2·10³⁶<2¹²⁷`. Final determinants are at most `10²⁰`.
The integer types used here therefore cannot overflow.

### Decimal output with an exact total

Use `S=10⁶` units per percentage point. For one recipe compute
`u[b]=floor(100S·d_b/d)`. The fractions are nonnegative and sum to one,
so their floors total at most `100S`. Add the missing units to a
component with the largest numerator. Fewer than `m≤10` units are
missing. Print each integer unit count with exactly six fractional
digits. Every row totals exactly 100; every component's absolute error
is less than `10⁻⁵` percentage points, below the required `10⁻³`. The
formatting product is at most `10²⁸`, also safe in 128 bits.

In the first example, substituting the second equation into the first
gives 25% bread, 50% cucumber and 25% tomato for `razduv`; substitution
back gives 50%, 40%, 10% for `razgon`. In the second example the recipes
already use bases, but each output still includes the other global base
with zero percentage.

There are at most `nm+1` determinants, each taking `O(n³)` integer
operations. Time is `O((nm+1)n³)`; auxiliary matrix and numerator
storage is `O(n²+nm)`. Integer magnitudes are bounded as above for the
stated constraints.

Pitfalls:

- Read to EOF and classify components only after collecting every recipe name.
- Forward references, self references and cycles require equations
  rather than recursive substitution.
- Solve for fractions with `A=100I−P`; convert to percentages once, at
  the output step.
- A zero replaced-column determinant means a zero component, not an
  invalid input system.
- Track row-swap signs and the previous Bareiss pivot; do not use
  floating-point division.
- Print every base in every recipe, even when its contribution is zero.

## Language notes

Python uses arbitrary-precision integers. Go and Java use `math/big.Int`
and `BigInteger`. C++ uses signed `__int128_t`, Rust uses `i128`; the
proof above covers their intermediates. All versions format integer
micropercent units directly, so no locale-dependent decimal conversion
is needed. Equal largest components may receive the rounding remainder
differently while satisfying the same error bound.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1986_matrix.cpp](1986_matrix.cpp) | G++ 13.2 x64 | matrix | O((n*m+1)*n^3) | AC | 0.015 s | 496 KB |
| [1986_matrix.go](1986_matrix.go) | Go 1.14 x64 | matrix | O((n*m+1)*n^3) | AC | 0.031 s | 6384 KB |
| [1986_matrix.java](1986_matrix.java) | Java 1.8 | matrix | O((n*m+1)*n^3) | AC | 0.140 s | 5616 KB |
| [1986_matrix.py](1986_matrix.py) | Python 3.12 x64 | matrix | O((n*m+1)*n^3) | AC | 0.093 s | 828 KB |
| [1986_matrix.rs](1986_matrix.rs) | Rust 1.75 x64 | matrix | O((n*m+1)*n^3) | AC | 0.015 s | 300 KB |
