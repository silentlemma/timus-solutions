# 1675. Lunar Code 2

[Timus 1675](https://acm.timus.ru/problem.aspx?space=1&num=1675) · difficulty 1793 · combinatorics

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the M × N matrices of zeros and ones with exactly K rows and
exactly L columns made only of zeros, modulo 10⁹ + 7.

## Input

M, N, K, L (1 ≤ M, N ≤ 100000; 0 ≤ K ≤ M; 0 ≤ L ≤ N).

## Output

The count modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
2 2 0 0
```

Output:

```
7
```

### Example 2

Input:

```
2 3 1 1
```

Output:

```
6
```

## Solution

Choose which K rows and which L columns are the zero ones, C(M, K) ·
C(N, L) ways. The ones then all lie in the remaining a × b block, with
a = M − K and b = N − L, and every row and every column of that block
must contain a one.

Count the a × b matrices with no zero row and no zero column by
inclusion–exclusion over the columns forced to be zero: if j given
columns are zero, each of the a rows is any of the 2^(b − j) − 1 nonzero
patterns on the others, so

f(a, b) = Σⱼ (−1)ʲ C(b, j) (2^(b − j) − 1)^a.

The formula is symmetric in a and b, so the sum runs over the shorter
side. Factorials and their inverses up to max(M, N) give the binomial
coefficients. `O(max(M, N) + min(a, b) log max(a, b))`.

Pitfalls:

- if all rows are zero, so are all columns: K = M forces L = N (tests 06
  and 07); the formula handles it, as with a = 0 the sum is
  Σ (−1)ʲ C(b, j), which is 1 for b = 0 and 0 otherwise;
- 0⁰ counts as 1 in that sum.

The answers match a count over every matrix up to 4 × 4 for every K and
L, and an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1675_combinatorics.cpp](1675_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.015 s | 1760 KB |
| [1675_combinatorics.go](1675_combinatorics.go) | Go 1.14 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 2696 KB |
| [1675_combinatorics.java](1675_combinatorics.java) | Java 1.8 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.218 s | 3132 KB |
| [1675_combinatorics.py](1675_combinatorics.py) | Python 3.12 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.500 s | 8372 KB |
| [1675_combinatorics.rs](1675_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(max(M, N) + min(a, b) log max(a, b)) | AC | 0.031 s | 1792 KB |
