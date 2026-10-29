# 2111. Delivery cost that does not depend on the order

[Timus 2111](https://acm.timus.ru/problem.aspx?space=1&num=2111) · difficulty 74 · math

Original problem by Anna Khanova, from the University Academic Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities are joined to the capital by roads of lengths dᵢ, and city i
needs dᵢ tons of cargo. A truck loaded once in the capital visits the
cities in any order, always along the roads; carrying m tons over l
kilometres costs m · l. Find the smallest total cost. The limits are
1 second and 256 MB.

## Input

1 ≤ n ≤ 10⁵, then d₁ … dₙ with 1 ≤ dᵢ ≤ 10⁴.

## Output

The smallest cost.

## Examples

### Example 1

Input:

```
3
1 2 3
```

Output:

```
36
```

## Solution

Every visit goes from the capital to a city and back. With load L on the
way there, the visit costs L·d and then (L − d)·d on the way back, that
is (2L − d)·d. Here L is d plus the demand of the cities still to visit.
Summing over the visits, each city contributes d² twice minus once, and
each pair of cities contributes 2·dᵢ·dⱼ whichever of them comes first.
So every order costs (Σ dᵢ)², which reaches 10¹⁸ and needs 64-bit
integers.

In the example (1 + 2 + 3)² = 36.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from 8 KB blocks
read with `fread` instead of calling `scanf` for each: 0.015 s instead
of 0.078 s and 104 KB instead of 140 KB. The formula is the same.

The optimized Python solution reads the input in 16 KB blocks and parses
it lazily, so the list of all distances is never built: 916 KB instead
of 7368 KB, with the same time. The optimized Rust solution parses the
numbers by hand from the locked standard input instead of reading the
whole input into a string: 216 KB instead of 2140 KB, with the same
time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2111_math.cpp](2111_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.078 s | 140 KB | 11294774 |
| [2111_math.go](2111_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.062 s | 2776 KB | 11294777 |
| [2111_math.java](2111_math.java) | Java 1.8 | math | O(n) | AC | 0.156 s | 488 KB | 11303535 |
| [2111_math.py](2111_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 7368 KB | 11294779 |
| [2111_math.rs](2111_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 2140 KB | 11294783 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2111_math_optimized.cpp](2111_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 104 KB | 11303673 |
| [2111_math_optimized.py](2111_math_optimized.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 916 KB | 11303800 |
| [2111_math_optimized.rs](2111_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 216 KB | 11303801 |
