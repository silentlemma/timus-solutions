# 1845. Integer-valued Complex Determinant

[Timus 1845](https://acm.timus.ru/problem.aspx?space=1&num=1845) · difficulty 4252 · number_theory

Original problem by Dmitry Poletaev and Ivan Burmistrov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Gaussian integer is a complex number with integer real and imaginary
parts. If a = bq + r for Gaussian integers with |r| < |b|, then r is a
remainder of a modulo b. Given an n × n matrix of Gaussian integers and
a nonzero Gaussian integer p, find a remainder of the determinant of the
matrix modulo p.

## Input

n (1 ≤ n ≤ 50), then the n rows of the matrix, each entry as its real
and imaginary part, and finally p in the same way. All parts are at
most 10 000 in absolute value.

## Output

The real and imaginary part of a remainder. Any remainder is accepted.

## Examples

### Example 1

Input:

```
2
2 0 -7 0
1 0 0 -1
3 1
```

Output:

```
3 0
```

## Solution

The determinant itself can have hundreds of digits, so the compiled
solutions never build it. Determinants survive replacing every entry by
its remainder modulo p, and they survive adding a multiple of one row
to another. The Gaussian integers have a division with remainder:
rounding both parts of x / y to the nearest integers gives a quotient q
with |x − qy|² ≤ |y|² / 2. So each column can be cleared below the
diagonal by the Euclidean algorithm on rows: subtract q times the lower
row from the pivot row, swap them (flipping the sign) and repeat until
the lower entry is zero. The entries of the column only shrink, while
every other changed entry is reduced modulo p again, so all numbers stay
below about 2·10⁸ and fit in 64 bits. The determinant is the product of
the diagonal, reduced modulo p after every factor. `O(n³ log |p|)`.

The Python solution takes the other road: it computes the exact
determinant by Bareiss elimination, where every entry is updated as
(a·c − b·d) / previous pivot and the division is always exact, and
reduces it once at the end. Python's big integers handle the few
hundred digits quickly.

In the example the determinant is 2·(−i) − (−7)·1 = 7 − 2i. Since
(3 + i)(1 − i) = 4 − 2i, the remainder can be 3; since
(3 + i)(2 − i) = 7 − i, it can also be −i, which is what the solutions
print.

Pitfalls:

- the remainder is not unique, so the answers are judged by a checker;
- a unit p leaves only the remainder 0;
- rounding must be a floor of (2x + n) / 2n, not a truncation, for
  negative parts.

The remainders pass a checker that computes the exact determinant and
tests the divisibility, on random matrices up to 50 × 50 with zero
pivots, equal rows, units and composite moduli.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1845_number_theory.cpp](1845_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^3 log p) | AC | 0.015 s | 264 KB |
| [1845_number_theory.go](1845_number_theory.go) | Go 1.14 x64 | number_theory | O(n^3 log p) | AC | 0.031 s | 1156 KB |
| [1845_number_theory.java](1845_number_theory.java) | Java 1.8 | number_theory | O(n^3 log p) | AC | 0.125 s | 4096 KB |
| [1845_number_theory.py](1845_number_theory.py) | Python 3.12 x64 | number_theory | O(n^3 log p) | AC | 0.250 s | 1880 KB |
| [1845_number_theory.rs](1845_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^3 log p) | AC | 0.046 s | 308 KB |
