# 1605. Devil's Sequence

[Timus 1605](https://acm.timus.ru/problem.aspx?space=1&num=1605) · difficulty 606 · math

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

A number starts with at least k sixes exactly when it lies in
[0.6…6, 0.6…6 + 10⁻ᵏ) with k sixes, that is between 2/3 − (2/3)·10⁻ᵏ and
2/3 + (1/3)·10⁻ᵏ. For even n, xₙ is below 2/3 by (2/3)·2⁻ⁿ, so it keeps k
sixes while 10ᵏ ≤ 2ⁿ. For odd n, xₙ is above by the same amount, so it
keeps them while 2·10ᵏ < 2ⁿ, that is 10ᵏ ≤ 2ⁿ⁻¹ (equality is impossible
for n ≥ 2). In both cases the answer is ⌊m·log₁₀ 2⌋ for m = n or n − 1,
one less than the number of decimal digits of 2ᵐ: `O(1)`.

The formula was checked against the decimal expansion of the exact
fractions for n < 200 and against the digit count of 2ᵐ.

Pitfalls:

- the side matters: x₃ = 0.75 has zero leading sixes and x₄ = 0.625 has one, so
  odd n use 2ⁿ⁻¹ instead of 2ⁿ;
- m·log₁₀ 2 can come close to an integer, but for n up to 10⁵ never
  closer than 1.5·10⁻⁵ (n = 28738), far more than the rounding error of a
  double (tests 08 to 10);
- simulating xₙ in floating point loses the gap to 2/3 after about 50
  steps, long before n = 100000.

## Optimized solutions

Java uses a fixed-point approximation of log₁₀ 2 and integer arithmetic. The approximation gives the exact floor for every allowed input. Submission 11318297 took 0.109 s and used 316 KB.

The approximation truncates log₁₀ 2 to 12 decimal places. Multiplication by m ≤ 10⁵ introduces an error below 10⁻⁷, smaller than the distance to the nearest integer given above.

Python uses a fixed-point approximation of log₁₀ 2 and integer arithmetic. The approximation gives the exact floor for every allowed input. Submission 11318410 took 0.078 s and used 404 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321853 · Go 1.14 x64 №11322280 · Java 1.8 №11322281 · Python 3.12 x64 №11322282 · Rust 1.75 x64 №11322283.

Go uses a fixed-point approximation of the logarithm that preserves the floor over the full input range. It reuses the input buffer to write the answer. Go 1.14 x64, submission 11322854. Time 0.031 → 0.031 s, memory 1060 → 284 KB.

Rust reads the decimal as a scaled integer and uses integer arithmetic for the final floor. Rust 1.75 x64, submission 11323310. Time 0.015 → 0.031 s, memory 244 → 48 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1605_math.cpp](1605_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11321853 |
| [1605_math.go](1605_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11322280 |
| [1605_math.java](1605_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1572 KB | 11322281 |
| [1605_math.py](1605_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 444 KB | 11322282 |
| [1605_math.rs](1605_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 244 KB | 11322283 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1605_math_optimized.java](1605_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 316 KB | 11318297 |
| [1605_math_optimized.py](1605_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11318410 |
| [1605_math_optimized.go](1605_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 284 KB | 11322854 |
| [1605_math_optimized.rs](1605_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 48 KB | 11323310 |

\* The Java rating target remains open. The Python rating target remains open.
