# 1462. Uncle Scrooge's Gold

[Timus 1462](https://acm.timus.ru/problem.aspx?space=1&num=1462) · difficulty 846 · math

Original problem by Alexander Ipatov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Uncle Scrooge has one gold bar for every string of 0 and 1 of length
2N − 2 with no two zeros in a row, and one safe for every such string
of length N − 2 (3 ≤ N ≤ 70000). Every safe gets the same number of
bars, and the bars left over, fewer than the safes, go to charity. Find
how many bars lie in each safe.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of bars in each safe.

## Examples

### Example 1

Input:

```
3
```

Output:

```
4
```

## Solution

Strings of length k with no two zeros in a row are counted by Fibonacci
numbers: a string ends in 1 after a string one letter shorter, or in 10
after one two letters shorter, so there are F(k + 2) of them with F(1) = F(2) = 1.
There are F(2N) bars and F(N) safes, and the identity
F(2N) = F(N) · L(N), with the Lucas numbers L(0) = 2, L(1) = 1,
L(k + 1) = L(k) + L(k − 1), shows that the bars divide evenly: the
answer is L(N) and nothing goes to charity.

L(70000) has 14630 digits, so it is built by repeated addition of long
numbers: Python and Java have big integers, Go has math/big, and in C++
and Rust the numbers are kept in limbs of 18 decimal digits.
`O(N²)` limb operations in total, a few tens of millions.

Pitfalls:

- the answer outgrows signed 64-bit integers at N = 91 and unsigned
  ones at N = 93 (tests 06, 07);
- Python 3.12 refuses to print integers of more than 4300 digits unless
  the limit is lifted (tests 09, 10).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1462_math.cpp](1462_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.156 s | 444 KB |
| [1462_math.go](1462_math.go) | Go 1.14 x64 | math | O(N^2) | AC | 0.046 s | 2400 KB |
| [1462_math.java](1462_math.java) | Java 1.8 | math | O(N^2) | AC | 0.375 s | 6220 KB |
| [1462_math.py](1462_math.py) | Python 3.12 x64 | math | O(N^2) | AC | 0.125 s | 4672 KB |
| [1462_math.rs](1462_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.093 s | 4272 KB |
