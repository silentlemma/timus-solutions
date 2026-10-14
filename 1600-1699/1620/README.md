# 1620. Clever House

[Timus 1620](https://acm.timus.ru/problem.aspx?space=1&num=1620) · difficulty 1551 · probability

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
E · (1 − 2/N) + 1. Its fixed point is N/2, and the distance to it shrinks
by the factor (N − 2)/N each time:

E_K = N/2 + (M − N/2) · ((N − 2)/N)^K = (N^(K+1) + (2M − N)(N − 2)^K) / (2 N^K).

The numbers reach about 9 000 digits. Python, Go and Java use their big
integers. A gcd of two such numbers is slow in Java, and C++ and Rust
have no big integers, so these keep the numerator as base-10⁹ digits and
cancel only the primes of 2N — no other prime divides the denominator
2N^K — by dividing by each one while it fits. `O(K²)` digit operations.

Pitfalls:

- the result can be 0, printed as `0/1` (the first example);
- N = 1 makes N − 2 negative, and N = 2 makes it zero (tests 03, 05);
- K = 0 leaves the answer M/1 (test 04);
- Python 3.12 limits integer printing to 4 300 digits unless the limit
  is lifted.

The answers match an independent accepted implementation on 300 random
inputs, many with N a power of two or with many small prime factors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1620_math.cpp](1620_math.cpp) | G++ 13.2 x64 | math | O(K²) | AC | 0.031 s | 324 KB |
| [1620_math.go](1620_math.go) | Go 1.14 x64 | math | O(K²) | AC | 0.031 s | 1432 KB |
| [1620_math.java](1620_math.java) | Java 1.8 | math | O(K²) | AC | 0.156 s | 5720 KB |
| [1620_math.py](1620_math.py) | Python 3.12 x64 | math | O(K²) | AC | 0.062 s | 472 KB |
| [1620_math.rs](1620_math.rs) | Rust 1.75 x64 | math | O(K²) | AC | 0.031 s | 344 KB |
