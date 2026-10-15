# 1668. Death Star 2

[Timus 1668](https://acm.timus.ru/problem.aspx?space=1&num=1668) · difficulty 5684 · math

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A station in N-dimensional space has M fixed engines. Feeding X units of
energy to engine i adds X · A_ij to coordinate j of the thrust, and X may
be negative. Choose X₁ … X_M so that the total thrust is as close as
possible to a target vector b, and among such choices, the one with the
smallest sum of squares of X.

## Input

N and M (1 ≤ N, M ≤ 100), then M rows of N integers A_ij, then the N
integers of b; all of absolute value at most 100.

## Output

X₁ … X_M with five digits after the decimal point.

## Examples

### Example 1

Input:

```
4 3
2 3 -2 1
-1 2 1 3
4 2 3 -2
3 13 -9 13
```

Output:

```
4.00000 2.00000 -1.00000
```

## Solution

The thrust is Σ Xᵢ aᵢ, where aᵢ is row i of A. This is the least squares
problem for the matrix with columns aᵢ, and the shortest of its solutions
(the pseudoinverse answer) is unique: it is the one solution lying in
the span of the vectors cⱼ = (A₁ⱼ, …, A_Mⱼ), the columns of A, because
any part orthogonal to them changes nothing in the thrust and only adds
length.

1. Pick a maximal independent set among the cⱼ. Doing this in floating
   point needs a threshold for "almost dependent"; instead the elimination
   runs on the integers modulo the prime 10⁹ + 7, which is exact. A set
   independent modulo the prime is independent over the rationals; the
   rank modulo the prime could only come out lower if the prime divided
   every r × r minor, which takes a matrix built against that prime.
2. Turn the chosen vectors into an orthonormal basis q₁ … q_r with
   Gram–Schmidt, projecting every new vector out twice; the second pass
   restores orthogonality lost to rounding.
3. With X = Σ w_k q_k, the thrust is K w for K_jk = cⱼ · q_k, and K has
   full column rank. A second QR of K, again by Gram–Schmidt, gives the
   least squares w by back substitution, and X follows.

Neither step forms AᵀA, so the condition number is never squared.
`O(N · M · min(N, M))`.

Pitfalls:

- with dependent engines the best thrust is reached by many X, and only
  the shortest is right (tests 03 and 05);
- a dead engine gets 0, and an all-zero matrix gives all zeros (test
  02);
- tiny negative results print as `-0.00000`, so values below 5 · 10⁻⁶
  are set to zero.

The answers match an exact computation in fractions on about 300 small
inputs and an independent accepted implementation on large ones.

## Language notes

- Python runs under PyPy: CPython takes 0.2–0.4 s here on 100 × 100
  inputs against a limit of 0.5 s, too close for the judge, and PyPy
  about 0.1 s. The CPython version still keeps Q transposed so that each
  projection is one pass of built-in sums per row.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1668_math.cpp](1668_math.cpp) | G++ 13.2 x64 | math | O(N M min(N, M)) | AC | 0.031 s | 632 KB |
| [1668_math.go](1668_math.go) | Go 1.14 x64 | math | O(N M min(N, M)) | AC | 0.046 s | 2060 KB |
| [1668_math.java](1668_math.java) | Java 1.8 | math | O(N M min(N, M)) | AC | 0.109 s | 1788 KB |
| [1668_math.py](1668_math.py) | PyPy 3.10 x64 | math | O(N M min(N, M)) | AC | 0.250 s | 6936 KB |
| [1668_math.rs](1668_math.rs) | Rust 1.75 x64 | math | O(N M min(N, M)) | AC | 0.031 s | 1000 KB |
