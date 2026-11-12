# 1828. Approximation by a Progression

[Timus 1828](https://acm.timus.ru/problem.aspx?space=1&num=1828) · difficulty 478 · math

Original problem by Alexey Samsonov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given integers a₁, …, aₙ, find the arithmetic progression b₁, …, bₙ,
not necessarily of integers, that minimises Σ(aᵢ − bᵢ)².

## Input

n (2 ≤ n ≤ 10⁴), then a₁, …, aₙ, each at most 10⁴ in absolute value.

## Output

The first term and the common difference, with absolute or relative
error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
4
0 6 10 15
```

Output:

```
0.400 4.900
```

### Example 2

Input:

```
4
-2 -2 -2 -2
```

Output:

```
-2 0
```

## Solution

A progression is bᵢ = b + d·xᵢ with xᵢ = i − 1, so this is the least
squares line fitted to the points (xᵢ, aᵢ). Setting the derivatives in b
and d to zero gives the normal equations, whose solution is

d = (n·Σxa − Σx·Σa) / (n·Σx² − (Σx)²),  b = (Σa − d·Σx) / n.

All four sums are integers that fit in 64 bits (n·Σxa stays below
10¹⁶). C++, Go, Java and Rust then use floating point; Python keeps
exact fractions until output. The denominator is n²(n² − 1)/12, never 0
for n ≥ 2. `O(n)`.

For the first example x̄ = 1.5 and ā = 7.75; Σ(x − x̄)(a − ā) = 24.5 and
Σ(x − x̄)² = 5, so d = 4.9 and b = 7.75 − 4.9·1.5 = 0.4.

Pitfalls:

- the progression is fitted to positions 0 … n − 1, not to the values
  alone: the mean is not enough;
- Σx² is about 3·10¹¹ and n·Σx² about 3·10¹⁵, beyond 32 bits;
- the first term is b₁, the value at the first position, not the
  intercept at some other origin.

## Optimized solutions

New C++/Go/Java/Rust stream only A=Σaᵢ and B=Σ(i−1)aᵢ. Simplifying the same normal equations gives first=((4n−2)A−6B)/(n(n+1)) and step=(12B−6(n−1)A)/(n(n²−1)). Thus no Σx² accumulator or subtraction of rounded floating-point coefficients is needed. Numerators have magnitude below10¹³, denominators below10¹² under the input bounds. Exact integer long division generates nine decimal digits and rounds using twice the final remainder; each remainder-times-ten is below 10¹³, so all arithmetic fits signed64 bits. Output rounding error is at most0.5·10⁻⁹. Time O(n), auxiliary space O(1), bounded I/O without floating-point formatters. All bases remain; Python reuses its admitted base.

The accepted base implementations [1828_math.py](1828_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1828_math.cpp](1828_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 144 KB | 11290408 |
| [1828_math.go](1828_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1256 KB | 11290410 |
| [1828_math.java](1828_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1004 KB | 11290421 |
| [1828_math.py](1828_math.py) \* | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 1824 KB | 11290418 |
| [1828_math.rs](1828_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 540 KB | 11290425 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1828_math_optimized.cpp](1828_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 68 KB | 11315311 |
| [1828_math_optimized.go](1828_math_optimized.go) \* | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 332 KB | 11315314 |
| [1828_math_optimized.java](1828_math_optimized.java) \* | Java 1.8 | math | O(n) | AC | 0.109 s | 388 KB | 11315307 |
| [1828_math_optimized.rs](1828_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 44 KB | 11315315 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
