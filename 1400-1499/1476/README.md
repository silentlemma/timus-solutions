# 1476. Lunar Code

[Timus 1476](https://acm.timus.ru/problem.aspx?space=1&num=1476) · difficulty 1263 · dp

Original problem by Alexander Ipatov (idea by Alexander Toropov), from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the M × N matrices of zeros and ones (1 ≤ M, N ≤ 40) in which,
for every pair of neighbouring columns i and i + 1, at most K rows
(0 ≤ K ≤ M) have a 0 in column i and a 1 in column i + 1.

Time limit: 1 second. Memory limit: 64 MB.

## Input

M, N and K.

## Output

The number of such matrices.

## Examples

### Example 1

Input:

```
2 1 0
```

Output:

```
4
```

### Example 2

Input:

```
2 2 1
```

Output:

```
15
```

## Solution

Fill the matrix column by column. Whether the next column is allowed
depends on which rows of the current one hold zeros, but the number of
ways to continue depends only on how many ones the column has. From a
column with c ones, a next column with d ones arises by turning t ≤ K
of the M − c zeros into ones and keeping s = d − t of the c ones:
step(c, d) = Σ C(M − c, t)·C(c, d − t) over t ≤ K. These counts are at
most 2⁴⁰. The first column with c ones can be chosen in C(M, c) ways;
each further column multiplies the vector of counts by the step table,
and the answer is the sum after N columns. `O(M²(K + N))` arithmetic
operations on numbers of up to M·N + 1 bits.

Pitfalls:

- with K = M every matrix counts, and 2¹⁶⁰⁰ needs big integers (test 03);
- one row with K = 0 means the row never goes from 0 to 1: N + 1
  matrices (test 05);
- one column has no pairs to check: 2^M matrices (tests 01, 06).

## Language notes

- C++ and Rust keep the counts in base 10⁹ limbs, using 128-bit
  arithmetic for multiplication by 64-bit step counts and addition.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1476_dp.cpp](1476_dp.cpp) | G++ 13.2 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.031 s | 492 KB |
| [1476_dp.go](1476_dp.go) | Go 1.14 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.046 s | 2104 KB |
| [1476_dp.java](1476_dp.java) | Java 1.8 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.125 s | 6228 KB |
| [1476_dp.py](1476_dp.py) | Python 3.12 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.093 s | 540 KB |
| [1476_dp.rs](1476_dp.rs) | Rust 1.75 x64 | dp | O(M^2(K + N)) arithmetic operations | AC | 0.031 s | 516 KB |
