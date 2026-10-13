# 1407. One-two, One-two

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · difficulty 388 · constructive

Original problem by Sergey Pupyrev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For 1 ≤ N ≤ 100, print a number of at most 10 000 digits, all 1 or 2, that
is divisible by 2ᴺ, or "No solution" if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

Such a number; any one is accepted.

## Examples

### Example 1

Input:

```
2
```

Output:

```
12
```

## Solution

There is always one with exactly N digits, built from the right. Let aₖ
have k digits 1 and 2 and be divisible by 2ᵏ; put the digit d in front:
d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ). As 5ᵏ is odd, exactly one of d = 1 and
d = 2 makes the bracket even, which gives aₖ₊₁ divisible by 2ᵏ⁺¹. Start
from nothing and repeat N times. `O(N²)` in Go/Java, `O(N³)` in Python.

Only the lowest N + 1 bits decide the choice, so C++ and Rust keep the
number in 128 bits and let the sums wrap around; Go and Java use big
integers and look at the lowest set bit.

Pitfalls:

- the answer is never "No solution";
- 2¹⁰⁰ is far past 64 bits (tests 07 to 09).

Every N from 1 to 100 was checked: the number has N digits 1 and 2 and
2ᴺ divides it. The tests are judged by exact comparison, as the N-digit
answer is unique.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB |
| [1407_constructive.java](1407_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB |
| [1407_constructive.py](1407_constructive.py) | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB |
