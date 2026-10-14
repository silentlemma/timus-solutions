# 1605. Devil's Sequence

[Timus 1605](https://acm.timus.ru/problem.aspx?space=1&num=1605) · difficulty 611 · math

Original problem by Alexander Ipatov, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

x₀ = 0, x₁ = 1 and xₙ = (xₙ₋₁ + xₙ₋₂)/2. For 2 ≤ n ≤ 100000, how many
sixes does the decimal expansion of xₙ start with after the point? For
example, x₁₀ = 0.666015625 starts with three.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n.

## Output

The number of leading sixes.

## Examples

### Example 1

Input:

```
10
```

Output:

```
3
```

## Solution

The recurrence has the characteristic roots 1 and −1/2, and the starting
values give xₙ = 2/3 − (−1)ⁿ·(2/3)·2⁻ⁿ. Since 2/3 = 0.666…, everything
depends on how far xₙ is from it and on which side.

A number starts with k sixes exactly when it lies in
[0.6…6, 0.6…6 + 10⁻ᵏ) with k sixes, that is between 2/3 − (2/3)·10⁻ᵏ and
2/3 + (1/3)·10⁻ᵏ. For even n, xₙ is below 2/3 by (2/3)·2⁻ⁿ, so it keeps k
sixes while 10ᵏ ≤ 2ⁿ. For odd n, xₙ is above by the same amount, so it
keeps them while 2·10ᵏ < 2ⁿ, that is 10ᵏ ≤ 2ⁿ⁻¹ (equality is impossible
for n ≥ 2). In both cases the answer is ⌊m·log₁₀ 2⌋ for m = n or n − 1,
one less than the number of decimal digits of 2ᵐ: `O(1)`.

The formula was checked against the decimal expansion of the exact
fractions for n < 200 and against the digit count of 2ᵐ.

Pitfalls:

- the side matters: x₃ = 0.75 has no six while x₄ = 0.625 has one, so
  odd n use 2ⁿ⁻¹ instead of 2ⁿ;
- m·log₁₀ 2 can come close to an integer, but for n up to 10⁵ never
  closer than 1.5·10⁻⁵ (n = 28738), far more than the rounding error of a
  double (tests 08 to 10);
- simulating xₙ in floating point loses the gap to 2/3 after about 50
  steps, long before n = 100000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1605_math.cpp](1605_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1605_math.go](1605_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1072 KB |
| [1605_math.java](1605_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1620 KB |
| [1605_math.py](1605_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [1605_math.rs](1605_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 248 KB |
