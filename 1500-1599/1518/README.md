# 1518. Jedi Riddle 3

[Timus 1518](https://acm.timus.ru/problem.aspx?space=1&num=1518) · difficulty 1045 · math

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The keys K1 … KN (1 ≤ N ≤ 100, each from 0 to 100) are given, and every
later key follows
Ki = (Ki−1·CN + Ki−2·CN−1 + … + Ki−N·C1) mod Y, with shifts Ci equal to 0
or 1 and 2 ≤ Y < 2²⁸. Find KX for N < X < 2²⁸.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

N, X and Y, then the N keys, then the N shifts.

## Output

KX.

## Examples

### Example 1

Input:

```
3 6 73
12 91 65
1 1 0
```

Output:

```
22
```

## Solution

Counting from K1, the key KX is term X − 1 of a linear recurrence. Its
characteristic polynomial is P(x) = x^N − Σ x^(N−j) over the j with
C(N+1−j) = 1. Compute x^(X−1) modulo P(x) and Y by repeated squaring:
multiply two polynomials of degree below N, then fold every term x^d
with d ≥ N back by replacing x^N with the sum above. If
x^(X−1) ≡ r0 + r1·x + … + r(N−1)·x^(N−1), then
KX = r0·K1 + r1·K2 + … + r(N−1)·KN mod Y. Each product costs `O(N²)`,
and about 2·28 products give `O(N² log X)`, about 10⁶ operations; a
100 × 100 matrix power would need about 6·10⁷ multiplications.

Pitfalls:

- X reaches 2²⁸ − 1, so stepping through the keys one by one is far too
  slow (gen5);
- products stay below 2⁵⁶; 64-bit versions reduce each, Python later
  (test 05, gen5);
- the given keys can reach Y and have to be reduced too (test 07);
- N = 1 makes the polynomial linear: x is replaced by C1
  (tests 02, 03);
- with every shift 0 all later keys are 0 (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1518_math.cpp](1518_math.cpp) | G++ 13.2 x64 | math | O(N^2 log X) | AC | 0.015 s | 204 KB |
| [1518_math.go](1518_math.go) | Go 1.14 x64 | math | O(N^2 log X) | AC | 0.031 s | 1200 KB |
| [1518_math.java](1518_math.java) | Java 1.8 | math | O(N^2 log X) | AC | 0.140 s | 3120 KB |
| [1518_math.py](1518_math.py) | Python 3.12 x64 | math | O(N^2 log X) | AC | 0.109 s | 544 KB |
| [1518_math.rs](1518_math.rs) | Rust 1.75 x64 | math | O(N^2 log X) | AC | 0.046 s | 244 KB |
