# 2117. Sums of two square roots equal to a given root

[Timus 2117](https://acm.timus.ru/problem.aspx?space=1&num=2117) · difficulty 543 · number_theory

Original problem by Pavel Klimov, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For an integer C count the pairs of non-negative integers A ≤ B with
√A + √B = √C. The limits are 1 second and 256 MB.

## Input

C, 0 ≤ C ≤ 10¹⁸.

## Output

The number of pairs.

## Examples

### Example 1

Input:

```
9
```

Output:

```
2
```

### Example 2

Input:

```
3
```

Output:

```
1
```

## Solution

Write C = s² q with q square-free. Squaring √A = √C − √B shows that √(BC)
is an integer, and from there that A and B are a² q and b² q with
a + b = s; conversely every such split works. So the answer is the
number of pairs a ≤ b with a + b = s, that is ⌊s/2⌋ + 1 (C = 0 has the
single pair 0, 0).

It remains to find s, the root of the largest square dividing C. Trial
division by d up to 10⁶ (the cube root of 10¹⁸) removes d² as long as it
divides and then one more d if present, multiplying s by d for every d²
removed. What is left has only prime factors above 10⁶, and at most two
of them because 10¹⁸ < (10⁶)³, so it contains a square factor only when
it is itself the square of a prime; then s gains that prime. The work is
at most 10⁶ divisions.

In the first example 9 = 3² · 1, so s = 3 and the pairs are 0 + 9 and
1 + 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(C^(1/3)) | AC | 0.031 s | 136 KB |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(C^(1/3)) | AC | 0.046 s | 1096 KB |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(C^(1/3)) | AC | 0.140 s | 1604 KB |
| [2117_number_theory.py](2117_number_theory.py) | Python 3.12 x64 | number_theory | O(C^(1/3)) | AC | 0.500 s | 472 KB |
| [2117_number_theory.rs](2117_number_theory.rs) | Rust 1.75 x64 | number_theory | O(C^(1/3)) | AC | 0.062 s | 232 KB |
