# 1560. Elementary Symmetric Functions

[Timus 1560](https://acm.timus.ru/problem.aspx?space=1&num=1560) · difficulty 931 · fenwick

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array of N ≤ 80000 integers gets M ≤ 100000 queries of two kinds:
`I i d` adds d to A[i], and `C l r K` (1 ≤ K ≤ 4) asks for the
elementary symmetric polynomials S(0), …, S(K) of A[l..r], where S(j) is
the sum of the products of all j-element subsets. The answers are taken
modulo a prime 1000 ≤ P ≤ 10⁹. Initial values and changes are at most 10⁵ in
absolute value.

Time limit: 4 seconds. Memory limit: 64 MB.

## Input

N, M and P, then the array, then the queries.

## Output

For each `C` query, S(0) … S(K) as residues modulo P on one line.

## Examples

### Example 1

Input:

```
7 6 1237
0 0 1 1 1 1 1
C 3 3 1
C 1 6 4
I 1 -1235
C 1 7 3
I 4 1
C 2 5 4
```

Output:

```
1 1
1 4 6 4 1
1 7 20 30
1 4 5 2 0
```

## Solution

The power sums p(j) = Σ a^j over an interval are easy to keep: four
Fenwick trees hold them for j = 1…4, an update changes each by
new^j − old^j, and a query takes a difference of two prefix sums. The
elementary polynomials follow from Newton's identities,
k·S(k) = S(k−1)·p(1) − S(k−2)·p(2) + S(k−3)·p(3) − …, with S(0) = 1.
P is a prime above 4, so dividing by k ≤ 4 is a multiplication by its
inverse modulo P.

The tree nodes keep their sums unreduced: each starts as a sum of at
most N residues and each update adds a difference of two residues, so
they stay below about 2·10¹⁴ and fit in 64 bits; they are reduced only
when a query reads them. Every query takes O(K log N) time, O((N + M)
log N) in all. The results were checked against a direct product
over the interval on random small tests.

Pitfalls:

- values and changes may be negative, while the answers must be
  residues from 0 to P − 1 (tests 03, 04);
- a fourth power of a value near 10⁹ overflows 64 bits unless every
  multiplication is reduced (test 05);
- P may be smaller than the values, so the values are reduced first
  (test 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1560_fenwick.cpp](1560_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + M) log N) | AC | 0.406 s | 4136 KB |
| [1560_fenwick.go](1560_fenwick.go) | Go 1.14 x64 | fenwick | O((N + M) log N) | AC | 0.156 s | 9028 KB |
| [1560_fenwick.java](1560_fenwick.java) | Java 1.8 | fenwick | O((N + M) log N) | AC | 0.250 s | 15908 KB |
| [1560_fenwick.py](1560_fenwick.py) | Python 3.12 x64 | fenwick | O((N + M) log N) | AC | 2.156 s | 48580 KB |
| [1560_fenwick.rs](1560_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + M) log N) | AC | 0.109 s | 10612 KB |
