# 2211. Counting triangles with integer sides and a given integer area

[Timus 2211](https://acm.timus.ru/problem.aspx?space=1&num=2211) · difficulty 1875 · number_theory

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the triangles with integer side lengths and area exactly S, where
triangles with the same multiset of sides are the same. The limits are
0.5 seconds and 256 MB.

## Input

S, 1 ≤ S ≤ 10⁹.

## Output

The number of triangles.

## Examples

### Example 1

Input:

```
6
```

Output:

```
1
```

## Solution

Heron's formula gives S² = p(p − a)(p − b)(p − c) for the semiperimeter
p. A triangle with integer sides and integer area always has an even
perimeter and an area divisible by 6, so for S not divisible by 6 the
answer is 0. Otherwise x = p − a, y = p − b and z = p − c are positive
integers, the sides are y + z, x + z and x + y, and

xyz(x + y + z) = S².

Distinct triangles correspond to solutions with x ≤ y ≤ z. Both x and y
divide S², so the solution lists the divisors of S² from the
factorization of S. For each x with 3x⁴ ≤ S², the candidates y ≥ x run
up to the largest one with y²(x + 2y) ≤ S² / x, which keeps z ≥ y and is
found by binary search. When xy divides S², z is the positive root of
z² + (x + y)z − S² / (xy) = 0, which must be an integer: the
discriminant (x + y)² + 4S² / (xy) has to be a perfect square of the
right parity.

In the example S² = 36 = 1 · 2 · 3 · 6, so x, y, z = 1, 2, 3 and the
sides are 5, 4 and 3.

The work is bounded by pairs of divisors of S² with small x and y,
fast enough for every S up to 10⁹.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2211_number_theory.cpp](2211_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.031 s | 852 KB |
| [2211_number_theory.go](2211_number_theory.go) | Go 1.14 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 2740 KB |
| [2211_number_theory.java](2211_number_theory.java) | Java 1.8 | number_theory | O(d(S²) log d(S²)) | AC | 0.250 s | 3296 KB |
| [2211_number_theory.py](2211_number_theory.py) | PyPy 3.10 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.500 s | 7688 KB |
| [2211_number_theory.rs](2211_number_theory.rs) | Rust 1.75 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 892 KB |
