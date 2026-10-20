# 2191. Writing a polyline as a signed sum of exactly N absolute values

[Timus 2191](https://acm.timus.ru/problem.aspx?space=1&num=2191) · difficulty 2298 · math, constructive

Original problem by Valentin Zuev and Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A piecewise linear function is given by N vertices (xᵢ, yᵢ) with
increasing xᵢ. Write it on [x₁, x_N] as ±|a₁x + b₁| ± … ± |a_N x + b_N|
with exactly N terms, in the format of the examples. The limits are
3 seconds and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then the N vertices with integer coordinates up to 10⁵
in absolute value.

## Output

The expression on one line.

## Examples

### Example 1

Input:

```
2
1 0
2 1
```

Output:

```
|1x-1|+|0x+0|
```

### Example 2

Input:

```
2
0 1
1 2
```

Output:

```
|1x-0|+|0x+1|
```

### Example 3

Input:

```
3
-1 1
0 -1
1 0
```

Output:

```
|1.5x-0|-|0.5x+0.5|-|0x+0.5|
```

## Solution

Let sᵢ be the slope of the i-th segment. At an inner vertex xᵢ the
slope turns from sᵢ₋₁ to sᵢ, and the term cᵢ |x − xᵢ| with
cᵢ = (sᵢ − sᵢ₋₁) / 2 makes exactly that turn, since its slope jumps by
2cᵢ there. The N − 2 inner vertices use N − 2 terms, and on [x₁, x_N]
what is left is a linear function, written with the remaining two:

- α |x − x₁| equals α(x − x₁) on the interval. Left of every kink the
  kink terms have slope −Σcᵢ = −(s_last − s₁) / 2, so α = (s₁ + s_last) / 2
  restores the first slope.
- A constant β, written as |0x + β| with the sign of β in front, fixes
  the value at x₁: β = y₁ − Σ cᵢ (xᵢ − x₁).

That sum looks like a mix of many fractions, but summation by parts
turns Σ (sᵢ − sᵢ₋₁)(xᵢ − x₁) into
s_last (x_{N−1} − x₁) − (y_{N−1} − y₁), because each sⱼ times the width
of its segment is just its rise. So every coefficient is one fraction
whose numerator and denominator are products of at most two coordinate
differences, and with |xᵢ| up to 10⁵ even bᵢ = −cᵢ xᵢ fits in 64 bits.

Each fraction is printed exactly by long division with 18 decimals and
trailing zeros removed, so the expression is off by at most about
10⁻¹⁸ per coefficient. Rounding the slopes first would instead let the
errors build up along the line.

In the third example the slopes are −2 and 1, so the kink at 0 is
1.5|x|, α = −0.5 and β = 1 − 1.5 = −0.5.

This takes O(N) with 18 digits per number.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2191_math_constructive.cpp](2191_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(N) | AC | 0.234 s | 5020 KB |
| [2191_math_constructive.go](2191_math_constructive.go) | Go 1.14 x64 | math, constructive | O(N) | AC | 0.093 s | 14532 KB |
| [2191_math_constructive.java](2191_math_constructive.java) | Java 1.8 | math, constructive | O(N) | AC | 0.218 s | 22016 KB |
| [2191_math_constructive.py](2191_math_constructive.py) | Python 3.12 x64 | math, constructive | O(N) | AC | 0.593 s | 28096 KB |
| [2191_math_constructive.rs](2191_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(N) | AC | 0.062 s | 9732 KB |
