# 1000. Sum of two integers

[Timus 1000](https://acm.timus.ru/problem.aspx?space=1&num=1000) · difficulty 16 · math

Original problem by Pavel Atnashev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two integers `a` and `b` are given. Output their sum `a + b`.

The original problem does not state bounds for `a` and `b`; the fixed-width
solutions use 64-bit integers, so both operands and their sum must fit in a
signed 64-bit integer.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two integers `a` and `b`, separated by whitespace (a space or a line break).

## Output

One integer: `a + b`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 3
```

Output:

```
5
```

### Example 2

Input:

```
2000000000 2000000000
```

Output:

```
4000000000
```

## Solution

Read the two numbers and print their sum. Time and memory are `O(1)`.

Pitfalls:

- the sum of two values that fit in 32 bits may not fit in 32 bits, so a
  64-bit type is used for both operands and the result;
- the numbers are read as whitespace-separated tokens, so it does not matter
  whether they are on one line or on two.

## Optimized solutions

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 0.046 s instead of 0.078 s and
336 KB instead of 1548 KB.

## Language notes

- **C++**: `long long` and `scanf("%lld %lld")`.
- **Go**: `int64` with `fmt.Scan`, which skips any whitespace.
- **Python**: integers have arbitrary precision; reading all tokens with
  `sys.stdin.read().split()` copes with any line layout.
- **Java**: the simple solution uses `long` and `Scanner`.
- **Rust**: read the whole input into a `String`, split on whitespace and parse
  `i64`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1000_math.cpp](1000_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303840 |
| [1000_math.go](1000_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB | 11277409 |
| [1000_math.java](1000_math.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 1548 KB | 11277412 |
| [1000_math.py](1000_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 132 KB | 11277410 |
| [1000_math.rs](1000_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.001 s | 228 KB | 11303841 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1000_math_optimized.java](1000_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.046 s | 336 KB | 11303693 |
