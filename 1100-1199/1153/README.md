# 1153. Recovering N from the sum 1 + 2 + … + N with up to 600 digits

[Timus 1153](https://acm.timus.ru/problem.aspx?space=1&num=1153) · difficulty 336 · math

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A computer added up the integers from 1 to `N`, `0 < N < 10³⁰⁰`, and
printed the sum `S`, but `N` is lost. Given `S`, which is always such a
sum, find `N`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`S`.

## Output

`N`.

## Examples

### Example 1

Input:

```
28
```

Output:

```
7
```

## Solution

`S = N(N + 1)/2`, so `8S + 1 = 4N² + 4N + 1 = (2N + 1)²` is a perfect
square, and `N = (√(8S + 1) − 1) / 2`. The only difficulty is size: `S`
has up to 600 digits, so the square root needs big integers.

The long-hand method from school works digit by digit and needs only
multiplication by small numbers, addition, comparison and subtraction.
Split `8S + 1` into pairs of digits from the right. Keep the root found
so far, `r`, and a remainder. For each next pair, append it to the
remainder (multiply by 100 and add), then find the largest digit `x` with
`(20r + x)·x` not above the remainder, subtract that product, and append
`x` to the root. After the last pair the root is `2N + 1`; subtract one
and halve it from the top digit down. With about 300 pairs and at most
nine tries each over numbers of 600 digits, this is a few million digit
operations.

Pitfalls:

- `S` does not fit in any machine integer, nor does `N`;
- `8S + 1` may have an odd number of digits; a leading zero makes the
  pairs line up;
- `N = 1` gives `S = 1`, and the root of `9` is `3`.

The answers were checked on every test by computing `N(N + 1)/2` back
with Python integers.

## Language notes

- Python uses `math.isqrt` on its built-in integers and Go uses
  `big.Int.Sqrt`.
- Java 8 has no `BigInteger.sqrt`, so it runs Newton's method,
  `x ← (x + D/x)/2`, from a power of two above the root.
- C++ and Rust have no big integers in the standard library and run the
  long-hand square root on decimal digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1153_math.cpp](1153_math.cpp) | G++ 13.2 x64 | math | O(L²) | AC | 0.015 s | 504 KB |
| [1153_math.go](1153_math.go) | Go 1.14 x64 | math | O(L²) | AC | 0.031 s | 1212 KB |
| [1153_math.java](1153_math.java) | Java 1.8 | math | O(L²) | AC | 0.140 s | 1676 KB |
| [1153_math.py](1153_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.093 s | 480 KB |
| [1153_math.rs](1153_math.rs) | Rust 1.75 x64 | math | O(L²) | AC | 0.046 s | 456 KB |
