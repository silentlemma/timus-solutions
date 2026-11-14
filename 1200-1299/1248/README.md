# 1248. Adding numbers to 19 significant digits

[Timus 1248](https://acm.timus.ru/problem.aspx?space=1&num=1248) · difficulty 658 · math

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
input is a whole multiple of 10⁻³⁰⁰ (19 digits near 10⁻¹⁰⁰ reach
10⁻¹¹⁸), so it becomes an exact integer once multiplied by 10³⁰⁰: the
mantissa's digits times a power of ten. The integers are added exactly,
the sum is cut to its 19 leading digits, rounding half up on the rest,
and printed with the exponent `(number of digits − 1) − 300`. If
rounding turns the 19 digits into 10¹⁹, the mantissa becomes 1 followed
by zeros and the exponent grows by one. `O(N · L)` with L ≈ 400 digits.

Pitfalls:

- terms past the 19th digit can still affect rounding: test 04 sits
  exactly on a tie, test 05 just below it;
- two numbers below 10¹⁰⁰ can have a rounded sum of 2·10¹⁰⁰ (test 03);
  rounding can carry into a new power of ten (test 08);
- the exponent is printed bare, `e3` and `e-100`, without a plus sign or
  leading zeros.

## Language notes

- Python uses its exact integers and Go `math/big`; Java adds
  `BigDecimal`s and rounds with `MathContext(19, HALF_UP)`; C++ and Rust
  keep one signed digit sum per power of ten and settle the carries at
  the end.

## Optimized solutions


Java caches the scaling factors and accumulates the scaled terms as BigIntegers. Java 1.8, submission 11318438. Time 0.109 → 0.109 s, memory 1696 → 1932 KB.

Rust accumulates the decimal inputs in fixed-size blocks, propagates carries, and rounds the leading 19 digits. Rust 1.75 x64, submission 11323295. Time 0.015 → 0.015 s, memory 280 → 68 KB.


**Timus submissions for the simple versions**

G++ 13.2 x64 №11321870 · Go 1.14 x64 №11322253 · Java 1.8 №11322254 · Python 3.12 x64 №11322255 · Rust 1.75 x64 №11322256.

Go adds signed digits in decimal columns and propagates carries once after reading all terms. Go 1.14 x64, submission 11322027. Time 0.015 → 0.015 s, memory 2076 → 908 KB.

Python reads one term at a time and scales to the smallest possible decimal place. Python 3.12 x64, submission 11322028. Time 0.078 → 0.078 s, memory 468 → 512 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1248_math.cpp](1248_math.cpp) | G++ 13.2 x64 | math | O(N · L) | AC | 0.015 s | 388 KB | 11321870 |
| [1248_math.go](1248_math.go) | Go 1.14 x64 | math | O(N · L) | AC | 0.015 s | 2076 KB | 11322253 |
| [1248_math.java](1248_math.java) | Java 1.8 | math | O(N · L) | AC | 0.109 s | 1696 KB | 11322254 |
| [1248_math.py](1248_math.py) | Python 3.12 x64 | math | O(N · L) | AC | 0.078 s | 468 KB | 11322255 |
| [1248_math.rs](1248_math.rs) | Rust 1.75 x64 | math | O(N · L) | AC | 0.015 s | 280 KB | 11322256 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1248_math_optimized.java](1248_math_optimized.java) \* | Java 1.8 | math | O(N · L) | AC | 0.109 s | 1932 KB | 11318438 |
| [1248_math_optimized.rs](1248_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N · L) | AC | 0.015 s | 68 KB | 11323295 |
| [1248_math_optimized.go](1248_math_optimized.go) \* | Go 1.14 x64 | math | O(N · L) | AC | 0.015 s | 908 KB | 11322027 |
| [1248_math_optimized.py](1248_math_optimized.py) | Python 3.12 x64 | math | O(N · L) | AC | 0.078 s | 512 KB | 11322028 |

\* The marked versions have room to improve in the ratings.
