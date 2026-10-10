# 1165. Where a digit string first appears in 123456789101112…

[Timus 1165](https://acm.timus.ru/problem.aspx?space=1&num=1165) · difficulty 930 · strings

Original problem by Nikita Shamgunov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`S` is the infinite string of all positive integers written one after
another: `1234567891011121314…`, indexed from 1. Given a string `A` of at
most 200 digits, find the smallest `k` such that `A` occurs in `S` starting
at position `k`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The string `A`.

## Output

The number `k`. It can be about 200 digits long.

## Examples

### Example 1

Input:

```
101
```

Output:

```
10
```

## Solution

The first digit of a `d`-digit number `x` stands at position
`d·x + 1 − R(d)`, where `R(d)` is the repunit `11…1` of `d` ones: the
shorter numbers take `(d − 1)·10^(d−1) − R(d − 1)` digits, and
`10^(d−1) + R(d − 1) = R(d)`.

An occurrence of `A` covers a run of consecutive numbers. There are three
kinds:

1. Some number `x` lies completely inside `A`. Then `x` is a substring of
   `A` without a leading zero, and it fixes everything else: write `x + 1`,
   `x + 2`, … to the right and `x − 1`, `x − 2`, … to the left and compare
   with `A`. There are `O(n²)` such substrings.
2. `A` is the end of `y − 1` followed by the beginning of `y`, neither of
   them complete, with the boundary at some `i`. The beginning of `y` is
   `A[i..]`. Its last `i` digits are the last `i` digits of `y − 1` plus
   one, that is, `A[..i] + 1` cut to `i` digits, even when a carry turns
   `99…9` into `100…0`. The shortest `y` overlaps these two known pieces as
   much as possible, so every overlap is tried and checked as in case 1.
3. `A` lies inside one number but not at its start. The shortest such
   number is `1A`, so `k` is the position of `1A` plus one.

The answer is the smallest position among all candidates that pass the
check. `O(n³)` digit operations, `n ≤ 200`.

Pitfalls:

- `A` may begin with zeros or consist of zeros only: `0` first appears
  inside `10`, at position 11;
- the answer is far beyond 64 bits, so positions need big numbers;
- the number before a power of ten is one digit shorter;
- the walk to the left must stop with a failure if it reaches zero.

The answers were compared with a direct search in `S` on all strings of up
to three digits and on random ones of up to five, 1,708 strings in all,
and on 400 generated strings of up to 200 digits with a separately written
solution.

## Language notes

- Python uses its own big integers throughout.
- Go and Java walk along the neighbours with decimal strings and compute
  positions with `big.Int` and `BigInteger`.
- C++ and Rust keep everything in decimal strings, with small helpers for
  adding one, subtracting one, multiplying by the length and subtracting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1165_strings.cpp](1165_strings.cpp) | G++ 13.2 x64 | strings | O(n³) | AC | 0.015 s | 420 KB |
| [1165_strings.go](1165_strings.go) | Go 1.14 x64 | strings | O(n³) | AC | 0.031 s | 4540 KB |
| [1165_strings.java](1165_strings.java) | Java 1.8 | strings | O(n³) | AC | 0.156 s | 6188 KB |
| [1165_strings.py](1165_strings.py) | Python 3.12 x64 | strings | O(n³) | AC | 0.093 s | 680 KB |
| [1165_strings.rs](1165_strings.rs) | Rust 1.75 x64 | strings | O(n³) | AC | 0.031 s | 260 KB |
