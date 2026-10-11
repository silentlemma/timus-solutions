# 1248. Adding numbers to 19 significant digits

[Timus 1248](https://acm.timus.ru/problem.aspx?space=1&num=1248) · difficulty 659 · math

Original problem by Alexander Klepinin, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Add up to 1000 numbers given in exponential notation with 19 significant
digits each, all between 10⁻¹⁰⁰ and 10¹⁰⁰, and print the sum in
exponential notation with 19 correct significant digits.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N numbers, one per line.

## Output

The sum, as `d.ddddddddddddddddddeE`.

## Examples

### Example 1

Input:

```
2
1.5e3
1.5e-3
```

Output:

```
1.500001500000000000e3
```

## Solution

A double holds only 15–17 digits, and even an 80-bit long double loses
the small terms next to large ones, so the sum is done exactly. Every
input is a whole multiple of 10⁻³⁰⁰ (19 digits below 10⁻¹⁰⁰ reach about
10⁻¹¹⁹), so it becomes an exact integer once multiplied by 10³⁰⁰: the
mantissa's digits times a power of ten. The integers are added exactly,
the sum is cut to its 19 leading digits, rounding half up on the rest,
and printed with the exponent `(number of digits − 1) − 300`. If
rounding turns the 19 digits into 10¹⁹, the mantissa becomes 1 followed
by zeros and the exponent grows by one. `O(N · L)` with L ≈ 400 digits.

Pitfalls:

- small numbers matter only past the 19th digit, but they can still move
  it by rounding: test 04 sits exactly on a tie, test 05 just below it;
- the sum of two numbers below 10¹⁰⁰ can reach 2·10¹⁰⁰, and rounding can
  carry into a new power of ten (test 03);
- the exponent is printed bare, `e3` and `e-100`, without a plus sign or
  leading zeros.

## Language notes

- Python uses its exact integers and Go `math/big`; Java adds
  `BigDecimal`s and rounds with `MathContext(19, HALF_UP)`; C++ and Rust
  keep one signed digit sum per power of ten and settle the carries at
  the end.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1248_math.cpp](1248_math.cpp) | G++ 13.2 x64 | math | O(N · L) | AC | 0.015 s | 404 KB |
| [1248_math.go](1248_math.go) | Go 1.14 x64 | math | O(N · L) | AC | 0.015 s | 2084 KB |
| [1248_math.java](1248_math.java) | Java 1.8 | math | O(N · L) | AC | 0.125 s | 1716 KB |
| [1248_math.py](1248_math.py) | Python 3.12 x64 | math | O(N · L) | AC | 0.093 s | 536 KB |
| [1248_math.rs](1248_math.rs) | Rust 1.75 x64 | math | O(N · L) | AC | 0.031 s | 252 KB |
