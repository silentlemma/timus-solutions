# 1428. Jedi Riddle

[Timus 1428](https://acm.timus.ru/problem.aspx?space=1&num=1428) · difficulty 498 · math

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given A, B and C (1 ≤ A, B, C ≤ 32) such that C − 1 is divisible by both
A and B, find whole numbers X, Y and Z from 1 to 10⁵⁰ with
X^A + Y^B = Z^C. Any such triple will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C.

## Output

X, Y and Z, one per line.

## Examples

### Example 1

Input:

```
2 2 3
```

Output:

```
10
5
5
```

## Solution

Two equal halves make a whole: 2^(C−1) + 2^(C−1) = 2^C. Since A and B
divide C − 1, take X = 2^((C−1)/A) and Y = 2^((C−1)/B), so that
X^A = Y^B = 2^(C−1), and Z = 2. The numbers are at most 2³¹, far below
10⁵⁰, and fit in 64 bits. `O(1)`.

Pitfalls:

- C = 1 gives X = Y = 1 and 1 + 1 = 2¹ (tests 03, 08);
- the example prints another triple, so the tests use a checker with
  big integers (test 01).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1428_math.cpp](1428_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1428_math.go](1428_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB |
| [1428_math.java](1428_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1600 KB |
| [1428_math.py](1428_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 408 KB |
| [1428_math.rs](1428_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 208 KB |
