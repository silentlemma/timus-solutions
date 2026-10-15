# 1698. Square Country 5

[Timus 1698](https://acm.timus.ru/problem.aspx?space=1&num=1698) · difficulty 640 · number_theory

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the positive integers of at most n digits, without leading zeros,
whose square ends with the number itself, like 76² = 5776.

## Input

n (1 ≤ n ≤ 2000).

## Output

The count.

## Examples

### Example 1

Input:

```
1
```

Output:

```
3
```

## Solution

A d-digit number x qualifies when x² ≡ x (mod 10ᵈ), that is when
x(x − 1) is divisible by both 2ᵈ and 5ᵈ. As x and x − 1 are coprime,
each prime power divides one of them, which gives four residues
modulo 10ᵈ: 0, 1, and the two mixed ones. The mixed residues are the
last d digits of two endless 10-adic numbers, …890625 and …109376.
Their digits other than the last add up to 9 place by place, because
the two numbers sum to 1 (mod 10ᵈ).

So for every length d the candidates are 1 (only when d = 1) and the
two endings of length d, which count when their leading digit, the
d-th digit of the endless number, is not 0. Writing the 5-ending one
as x = Σ xᵢ 10ⁱ, digit d of x² is the sum of xᵢ·xⱼ over i + j = d, plus
the carry from below. A new digit c enters that sum as 2·5·c, a
multiple of 10, so c must be (the other products + carry) mod 10, and
the next carry follows. The 6-ending number has digit 9 − c there, which
counts when c ≠ 9. `O(n²)` digit products, without big integers.

Pitfalls:

- 1 counts (1² = 1), but 0 is not positive;
- endings with a leading zero, like 0625 for d = 4, do not count
  (test 04);
- the two endless numbers are tied: one is 1 minus the other, so the
  same digit decides both.

The answers match an independent accepted implementation for every
tested n up to 2000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1698_number_theory.cpp](1698_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n²) | AC | 0.015 s | 204 KB |
| [1698_number_theory.go](1698_number_theory.go) | Go 1.14 x64 | number_theory | O(n²) | AC | 0.031 s | 1168 KB |
| [1698_number_theory.java](1698_number_theory.java) | Java 1.8 | number_theory | O(n²) | AC | 0.125 s | 1600 KB |
| [1698_number_theory.py](1698_number_theory.py) | Python 3.12 x64 | number_theory | O(n²) | AC | 0.296 s | 436 KB |
| [1698_number_theory.rs](1698_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n²) | AC | 0.015 s | 236 KB |
