# 1914. Fractional Inputs with Integral Outputs

[Timus 1914](https://acm.timus.ru/problem.aspx?space=1&num=1914) · difficulty 3724 · matrix

Original problem by Alexander Ipatov (prepared by Dmitry Ivankov), from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An integer n×n matrix maps the real rotations of n accessible controls
to the rotations of n protected controls. All controls initially have
integral rotations. Find whether some real input vector x has at least
one noninteger coordinate while every coordinate of Ax is an integer.
Only existence is required. Limits: 2 seconds, 64 MB.

## Input

n, 1≤n≤100, followed by n rows of n integers in [−100,100].
The entry in row j, column i is the protected control j response to
one counterclockwise turn of accessible control i. Negative turns are
clockwise; input rotations may be arbitrary real numbers.

## Output

Print `Power of magic saves lives` if such a vector exists; otherwise
print `Death`.

## Checking

Compare output tokens exactly. No approximate rotation or determinant
is printed.

## Examples

```
3
1 2 0
4 3 0
0 0 0
```

```
Power of magic saves lives
```

## Solution

The answer is `Death` exactly when det(A) is +1 or −1.

If A is singular, choose a nonzero kernel vector and scale it so one
coordinate is strictly between 0 and 1 in absolute value. Its image is
zero, so it works. If det(A)=±1, the adjugate formula makes A⁻¹ integral.
Consequently Ax integral forces x integral, and no required vector exists.
Finally, for an invertible matrix with |det(A)|>1, at least one column
of A⁻¹ is nonintegral: otherwise A⁻¹ would be an integer matrix with
noninteger determinant 1/det(A), a contradiction. That column maps to
an integer unit vector and is a valid input.

### Exact modular certificate

C++, Go, Java and Rust compute determinants modulo distinct fixed primes
p strictly between 2²⁹ and 2³⁰. Gaussian elimination in a prime field
uses row swaps and the inverse pivot a^(p−2) mod p. A missing pivot
gives determinant zero. Normalize negative entries; include every row
swap in the determinant sign.

A true integer determinant ±1 must give the same sign modulo every prime.
Reject the unit property immediately if a residue is neither 1 nor p−1,
or if one prime gives +1 and another gives −1. Using several primes
without a bound would only be a heuristic; here the finite certificate
is deterministic. Each row has norm at most 100√n≤1000<2¹⁰, so Hadamard's
inequality gives |det(A)|<2^(10n). Take
K=ceil((10n+1)/29), at most 35 primes. Their product M is greater than
2^(10n+1). If all residues equal the same sign s, M divides det(A)−s,
whose absolute value is less than M. Therefore det(A)=s exactly.
No Chinese remainder reconstruction or large integer is needed.
Modular products are below 2⁶⁰ and fit 64-bit integers.

### Python: fraction-free determinant

Python instead uses its native arbitrary-precision integers with Bareiss
elimination. With current pivot p and previous pivot q (initially 1),
replace each trailing entry by (aᵢⱼp−aᵢₖaₖⱼ)/q, then zero the pivot
column below p. The minor identity behind Bareiss ensures exact division;
all intermediate values stay integers. Swap a nonzero row into the pivot
position, or declare singularity when no pivot exists. The final diagonal
entry is the determinant up to row-swap sign, which does not affect its
absolute value. This handles n=1 directly as well.

Both arithmetic backends decide the same exact determinant criterion.
The modular versions take `O(n³K + nK log p)` modular operations and
`O(n²)` machine words. Bareiss takes `O(n³)` arbitrary-precision integer
operations and `O(n²)` integers; arithmetic cost depends on their bit length.

The example is singular because its last row is zero, so the required
vector exists. A single zero coefficient also succeeds, while scalar +1
and −1 fail. A nonzero determinant such as 2 succeeds too: half a turn
can produce an integral output.

Invertibility is not the criterion: only determinants ±1 prohibit the
required input. Keep determinant signs consistent between primes, handle
zero/negative pivots and row swaps, and do not stop after a few random
moduli. Floating-point determinants can lose a small integer answer through
cancellation. The matrix/transposed indexing convention cannot change its
determinant, but arbitrary reordering without sign tracking can.

## Language notes

The four modular ports use 64-bit products, exact modular powers and at
most 35 preverified primes. Rust uses unsigned residues; the other ports
normalize into a nonnegative signed type. Java has a byte input reader.
Python performs exact integer division, never floating-point elimination.
Each source is standalone and uses its language's standard library.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1914_matrix.cpp](1914_matrix.cpp) | G++ 13.2 x64 | matrix | O(K n^3) | AC | 0.125 s | 544 KB |
| [1914_matrix.go](1914_matrix.go) | Go 1.14 x64 | matrix | O(K n^3) | AC | 0.156 s | 4660 KB |
| [1914_matrix.java](1914_matrix.java) | Java 1.8 | matrix | O(K n^3) | AC | 0.359 s | 3412 KB |
| [1914_matrix.py](1914_matrix.py) | Python 3.12 x64 | matrix | O(K n^3) | AC | 0.390 s | 2820 KB |
| [1914_matrix.rs](1914_matrix.rs) | Rust 1.75 x64 | matrix | O(K n^3) | AC | 0.140 s | 388 KB |
