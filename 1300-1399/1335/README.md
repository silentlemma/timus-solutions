# 1335. White Thesis

[Timus 1335](https://acm.timus.ru/problem.aspx?space=1&num=1335) · difficulty 182 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N, 2 ≤ N ≤ 30 000, find three different whole numbers A, B and C
between N² and (N + 1)² inclusive such that A² + B² is divisible by C,
or print `No solution` if there are none. Any such triple is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

A, B and C, or `No solution`.

## Checking

The checker accepts any three different numbers in the range with
A² + B² divisible by C. A triple always exists, so `No solution` is
never accepted.

## Examples

### Example 1

Input:

```
2
```

Output:

```
8 6 4
```

### Example 2

Input:

```
1000
```

Output:

```
1000000 1000756 1000976
```

## Solution

Take C = N² + 1, A = N² and B = N² + N + 1. Modulo C the first number
is −1 and the second is N, so A² + B² ≡ 1 + N², which is C itself, and
the sum is divisible by C. All three lie between N² and (N + 1)², since
N² + N + 1 < N² + 2N + 1, and they are different for every N ≥ 1. So
the answer always exists and `No solution` never happens. `O(1)`.

The triple was found by listing all solutions with A = N² for small N
and noticing (N² + N + 1, N² + 1) among them every time.

Pitfalls:

- the numbers reach about 9 · 10⁸, and the squares, which only a
  checker needs, reach 8 · 10¹⁷, more than 32 bits hold;
- the samples show other triples; any correct one is accepted.

## Language notes

- All five solutions print the same triple.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1335_math.cpp](1335_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1335_math.go](1335_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB |
| [1335_math.java](1335_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB |
| [1335_math.py](1335_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB |
| [1335_math.rs](1335_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 244 KB |
