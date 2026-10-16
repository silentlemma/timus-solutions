# 1803. The Czechs' Rifles

[Timus 1803](https://acm.timus.ru/problem.aspx?space=1&num=1803) · difficulty 717 · math

Original problem by Viktor Kamashev, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Rifle i costs the i-th Fibonacci number of roubles (1, 1, 2, 3, …).
Notes are worth the powers of k, and every rifle is paid with the
fewest notes. Order the rifles by the number of notes paid, breaking
ties by the rifle number.

## Input

k and n (2 ≤ k ≤ 10, 3 ≤ n ≤ 50000).

## Output

The rifle numbers in the required order.

## Examples

### Example 1

Input:

```
10 8
```

Output:

```
1 2 3 4 8 7 5 6
```

## Solution

The fewest notes for an amount is the sum of its digits in base k, so
each rifle costs the digit sum of a Fibonacci number. F(50000) has
about 10⁴ decimal digits, so the numbers are added one from the other,
kept in base k. The compiled solutions store limbs in base k^m, the
largest power of k up to a million. A table gives the digit sum of
every limb, so one addition yields the next number and its digit sum
at once. A stable sort by the digit sum then gives the order.
`O(n² / log B)` for limbs of base B.

The Python solution keeps every base-k digit in a 4-bit field of one
big integer. Each field stores digit + 16 − k, so it overflows exactly
when the base-k digit carries, and an ordinary integer addition passes
the carries along. The fields that did carry are found from the
exclusive or of the operands and the sum, and get the offset back. Bit
counts of the fields' four bit planes then give the digit sum. For
k = 2 the digit sum is simply the number of ones.

In the example the prices are 1, 1, 2, 3, 5, 8, 13, 21 with digit sums
1, 1, 2, 3, 5, 8, 4, 3, which gives 1 2 3 4 8 7 5 6.

Pitfalls:

- the numbers have thousands of digits, far beyond 64 bits;
- equal note counts keep the rifles in increasing order;
- converting big numbers to text in Python is too slow for 50000 of
  them.

The answers agree with an independent accepted implementation for
every base on the largest count and on many smaller ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1803_math.cpp](1803_math.cpp) | G++ 13.2 x64 | math | O(n^2 / log B) | AC | 0.328 s | 4748 KB |
| [1803_math.go](1803_math.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.593 s | 12320 KB |
| [1803_math.java](1803_math.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.531 s | 9896 KB |
| [1803_math.py](1803_math.py) | Python 3.12 x64 | math | O(n^2 / log B) | AC | 1.656 s | 26640 KB |
| [1803_math.rs](1803_math.rs) | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.359 s | 6888 KB |
