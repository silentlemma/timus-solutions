# 1823. Ideal Gas

[Timus 1823](https://acm.timus.ru/problem.aspx?space=1&num=1823) · difficulty 348 · math

Original problem credited to Benoît Paul Émile Clapeyron and Dmitri Mendeleev, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The ideal gas law pV = nRT links pressure p, amount of gas n, volume V
and temperature T, with R = 8.314. Three of the four values are given;
find the fourth. Volume and temperature must be positive. Print
"error" if the data contradict each other and "undefined" if the value
is not determined uniquely.

## Input

Three lines "X = value" for three different quantities X among p, n, V
and T, each value a non-negative integer up to 1000. The given V and T
are positive.

## Output

"X = value" with absolute or relative error at most 10⁻⁶, or "error",
or "undefined".

## Examples

### Example 1

Input:

```
p = 1
n = 1
V = 1
```

Output:

```
T = 0.120279
```

## Solution

Solve pV = nRT for the missing value; the given values are integers,
so every zero test is exact.

- p = nRT/V and n = pV/(RT): V and T are given and positive, so the
  result is always defined, possibly 0.
- V = nRT/p: if p = 0 the equation reads 0 = nRT, which holds for every
  V when n = 0 ("undefined") and for none when n > 0 ("error"). If
  p > 0 and n = 0, V would be 0, which is not allowed ("error").
- T = pV/(nR) works the same way with n in place of p.

Use R = 8314/1000 to keep each result as an exact integer fraction a/b.
Round a/b to six decimal places using integer arithmetic, rounding ties
up, then print the integer and six-digit fractional parts with a literal
decimal point. Java uses `Locale.ROOT` for the digits. The absolute
rounding error is at most 0.0000005, and all intermediate values fit in
signed 64-bit integers under the input bounds.

`O(1)`.

In the example T = 1·1/(1·8.314) ≈ 0.120279.

Pitfalls:

- zero pressure or zero gas is allowed and is a valid answer when p or
  n is the unknown;
- a computed volume or temperature of zero is an error, not an answer;
- the lines may come in any order;
- numeric output must be independent of the system locale: test 15
  exposes Java's default formatting, which can print `0,000000` instead
  of `0.000000`.

## Optimized solutions

Go and Rust index p, V, n and T in four fixed slots and use 1000pV = 8314nT to isolate the missing value with integer arithmetic. A zero numerator and denominator give undefined. A zero denominator, or a forced zero volume or temperature, gives error. Otherwise round the rational value to six decimal places using 64-bit integers.

The accepted base implementations [1823_math.cpp](1823_math.cpp), [1823_math.java](1823_math.java), [1823_math.py](1823_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1823_math.cpp](1823_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11298045 |
| [1823_math.go](1823_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1116 KB | 11298046 |
| [1823_math.java](1823_math.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 1736 KB | 11298047 |
| [1823_math.py](1823_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 572 KB | 11298048 |
| [1823_math.rs](1823_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 432 KB | 11298049 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1823_math_optimized.go](1823_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 776 KB | 11311181 |
| [1823_math_optimized.rs](1823_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB | 11310736 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
