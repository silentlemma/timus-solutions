# 1243. What is left after seven dwarfs share

[Timus 1243](https://acm.timus.ru/problem.aspx?space=1&num=1243) · difficulty 49 · math

Original problem by Stanislav Vasilyev, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Seven dwarfs share N equal things (1 ≤ N ≤ 10⁵⁰) equally, and whatever
cannot be shared goes to Snow White. How many things does Snow White get?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

N mod 7.

## Examples

### Example 1

Input:

```
123456123456
```

Output:

```
1
```

## Solution

The answer is the remainder of N divided by 7, but N has up to 51
digits, far beyond 64 bits. Reading N as a string and keeping only the
remainder of its prefix gives it digit by digit:
`rest = (rest · 10 + digit) mod 7`. `O(len N)`.

Pitfalls:

- even 20 digits already overflow a 64-bit integer (test gen4).

## Language notes

- Python's integers hold N exactly, so it just takes `int(N) % 7`; the
  other languages fold the digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1243_math.cpp](1243_math.cpp) | G++ 13.2 x64 | math | O(len N) | AC | 0.015 s | 380 KB |
| [1243_math.go](1243_math.go) | Go 1.14 x64 | math | O(len N) | AC | 0.046 s | 1060 KB |
| [1243_math.java](1243_math.java) | Java 1.8 | math | O(len N) | AC | 0.078 s | 400 KB |
| [1243_math.py](1243_math.py) | Python 3.12 x64 | math | O(len N) | AC | 0.046 s | 328 KB |
| [1243_math.rs](1243_math.rs) | Rust 1.75 x64 | math | O(len N) | AC | 0.046 s | 216 KB |
