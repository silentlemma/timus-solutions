# 1797. Summit Online Judge. Version 2

[Timus 1797](https://acm.timus.ru/problem.aspx?space=1&num=1797) · difficulty 4736 · number_theory

Original problem by Xie Lingxi, based on problem 1720 by Alex Samsonov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every contest has either x or y problems. A volume size is correct if
some contests, at least one, hold exactly that many problems together.
Count the correct sizes from l to r. There are up to 100 cases.

## Input

The number of cases, then x, y, l, r for each (1 ≤ x, y, l, r ≤ 10¹⁸,
l ≤ r).

## Output

For each case, the number of correct sizes.

## Examples

### Example 1

Input:

```
1
4 5 7 13
```

Output:

```
5
```

## Solution

Count the sizes a·x + b·y (a, b ≥ 0, not both zero) up to a limit N;
the answer is the count up to r minus the count up to l − 1. Dividing
x, y and N by g = gcd(x, y) makes x and y coprime. Then every
reachable size has exactly one form with 0 ≤ b < x, so the count up to
N is the sum over b from 0 to B = min(x − 1, ⌊N/y⌋) of
⌊(N − b·y)/x⌋ + 1, minus one for zero. Writing i = B − b turns the sum
into Σ ⌊(y·i + (N − y·B))/x⌋ for i from 0 to B, a floor sum, which the
Euclid-like reduction computes in O(log) steps: take out the whole
parts of the slope and the offset, then swap the roles of the slope
and the modulus. All intermediate results stay below the final count,
except the product slope × count + offset, which needs 128 bits.
`O(log max(x, y))` per case.

In the example 8, 9, 10, 12 and 13 can be made of 4s and 5s, while 7
and 11 cannot.

Pitfalls:

- x and y may share a factor, and then only multiples of it count;
- B and the range reach 10¹⁸, so the sum over b cannot be walked term
  by term;
- the product inside the floor sum overflows 64 bits; the Java
  solution uses BigInteger, the Go one bits.Mul64 and bits.Div64;
- zero, the empty set of contests, is not a size.

The answers agree with a direct count of reachable sizes on 3000 small
cases, and with an independent accepted implementation on 4500 large
ones, including shared factors, sizes of 1 and equal sizes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1797_number_theory.cpp](1797_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 408 KB |
| [1797_number_theory.go](1797_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 1092 KB |
| [1797_number_theory.java](1797_number_theory.java) | Java 1.8 | number_theory | O(log max(x, y)) per case | AC | 0.109 s | 2492 KB |
| [1797_number_theory.py](1797_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(x, y)) per case | AC | 0.078 s | 440 KB |
| [1797_number_theory.rs](1797_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 236 KB |
