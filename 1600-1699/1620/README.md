# 1620. Clever House

[Timus 1620](https://acm.timus.ru/problem.aspx?space=1&num=1620) · difficulty 1539 · probability, math

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N light bulbs (1 ≤ N ≤ 10⁹), M of them on. K times (K ≤ 1000) a virus
picks a uniformly random bulb and flips it. Print the expected number of
bulbs that are on at the end as an irreducible fraction p/q.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, M and K.

## Output

The expectation as `p/q`.

## Examples

### Example 1

Input:

```
1 1 9
```

Output:

```
0/1
```

### Example 2

Input:

```
5 4 3
```

Output:

```
353/125
```

## Solution

If E bulbs are on in expectation, a flip turns one off with chance E / N
and one on with chance (N − E) / N, so the next expectation is
E · (1 − 2/N) + 1. Its fixed point is N/2, and the signed difference
E − N/2 is multiplied by (N − 2)/N each time:

E_K = N/2 + (M − N/2) · ((N − 2)/N)^K = (N^(K+1) + (2M − N)(N − 2)^K) / (2 N^K).

The numbers reach about 9 000 digits. Python, Go and Java use their big
integers; C++ and Rust use base-10⁹ digits. A gcd of two such numbers is
slow in Java, so Java, C++ and Rust cancel only the primes of 2N — no other
prime divides the denominator 2N^K — up to their exponents in the denominator.

Pitfalls:

- the result can be 0, printed as `0/1` (the first example);
- N = 1 makes N − 2 negative (test 05), and N = 2 makes it zero (test 03);
- K = 0 leaves the answer M/1 (test 04);
- Python 3.12 limits integer printing to 4 300 digits unless the limit
  is lifted.

The answers match an independent accepted implementation on 300 random
inputs, many with N a power of two or with many small prime factors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1620_math.cpp](1620_math.cpp) | G++ 13.2 x64 | math | O(K² + √N) | AC | 0.031 s | 324 KB |
| [1620_math.go](1620_math.go) | Go 1.14 x64 | math | O(K²) | AC | 0.031 s | 1432 KB |
| [1620_math.java](1620_math.java) | Java 1.8 | math | O(K² + √N) | AC | 0.156 s | 5720 KB |
| [1620_math.py](1620_math.py) | Python 3.12 x64 | math | O(K²) | AC | 0.062 s | 472 KB |
| [1620_math.rs](1620_math.rs) | Rust 1.75 x64 | math | O(K² + √N) | AC | 0.031 s | 344 KB |
