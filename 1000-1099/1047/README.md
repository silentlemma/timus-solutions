# 1047. The first unknown term of a second-order recurrence

[Timus 1047](https://acm.timus.ru/problem.aspx?space=1&num=1047) · difficulty 303 · math

Original problem by Dmitry Filimonenkov, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence `a0, a1, …, aN+1` (`1 ≤ N ≤ 3000`, `−2000 ≤ ai ≤ 2000`)
satisfies `ai = (ai−1 + ai+1) / 2 − ci` for every `i = 1 … N`. Given
`a0`, `aN+1` and `c1 … cN`, all with two decimals, find `a1`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `a0`, then `aN+1`, then `c1 … cN`, one number per line.

## Output

`a1` with two decimals.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1
50.50
25.50
10.15
```

Output:

```
27.85
```

### Example 2

Input:

```
2
0.00
9.00
1.00
1.00
```

Output:

```
1.00
```

## Solution

Rewrite the relation with the differences `d[i] = a[i] − a[i−1]`:

```text
a[i+1] − 2·a[i] + a[i−1] = 2·c[i]   →   d[i+1] = d[i] + 2·c[i]
```

So `d[k] = d[1] + 2·(c[1] + … + c[k−1])`, and summing all the
differences from `d[1]` to `d[N+1]`, each `c[i]` appears `N + 1 − i`
times:

```text
a[N+1] − a[0] = (N + 1)·d[1] + 2 · Σ (N + 1 − i)·c[i]
a[1] = a[0] + d[1] = (N·a[0] + a[N+1] − 2 · Σ (N + 1 − i)·c[i]) / (N + 1)
```

`O(N)`. To avoid rounding trouble, the solutions work in hundredths: all
inputs become integers, the numerator stays below about `10^12`, and the
division by `N + 1` is exact for a consistent input (it is rounded to the
nearest hundredth just in case).

Pitfalls:

- floating-point summation of 3000 terms can drift, and the output must
  show exactly two decimals; integers in hundredths avoid both;
- negative answers between −1 and 0 must print as `-0.35`, not `0.35`
  or `-0.-35`.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: 64-bit integers in hundredths.
- **Python**: exact `Fraction`s parsed from the decimal strings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1047_math.cpp](1047_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 156 KB |
| [1047_math.go](1047_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1140 KB |
| [1047_math.java](1047_math.java) | Java 1.8 | math | O(N) | AC | 0.093 s | 1460 KB |
| [1047_math.py](1047_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.109 s | 1068 KB |
| [1047_math.rs](1047_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 264 KB |
