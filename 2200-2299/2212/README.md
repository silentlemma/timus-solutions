# 2212. Prefix sums applied Q times as one convolution

[Timus 2212](https://acm.timus.ru/problem.aspx?space=1&num=2212) · difficulty 1647 · math, combinatorics

Original problem by Yackov Malin, from the University Academic School Olympiad in Informatics 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array of N numbers is replaced by its prefix sums Q times in a row.
Print the result modulo 998 244 353. The limits are 2 seconds and
256 MB.

## Input

N and Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁷, then the array with values from 1
to 10⁸.

## Output

The final array modulo 998 244 353.

## Examples

### Example 1

Input:

```
3 2
1 2 3
```

Output:

```
1 4 10
```

## Solution

One prefix sum multiplies the generating function of the array by
1 / (1 − x), so Q of them multiply it by 1 / (1 − x)^Q, whose
coefficients are C(Q + k − 1, k). The answer is the convolution

pᵢ = Σ over j ≤ i of C(Q + i − j − 1, i − j) · vⱼ.

The coefficients follow from each other: the k-th is the previous one
times (Q + k − 1) / k, with modular inverses of 1 … N computed by the
usual linear recurrence.

The convolution is done modulo 998 244 353 with the number theoretic
transform, whose modulus this is. Python instead packs both sequences
into huge decimal numbers, one 23-digit slot per element. Every exact
coefficient of the product is below 10⁵ · 10⁸ · 10⁹, so the slots do not
overflow into each other, and the built-in decimal multiplication does
the fast transform internally; each slot is then reduced modulo
998 244 353.

In the example Q = 2 gives the coefficients 1, 2, 3, so the last value
is 3 · 1 + 2 · 2 + 1 · 3 = 10.

This takes O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2212_math_combinatorics.cpp](2212_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.093 s | 2180 KB |
| [2212_math_combinatorics.go](2212_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.125 s | 9012 KB |
| [2212_math_combinatorics.java](2212_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.500 s | 9564 KB |
| [2212_math_combinatorics.py](2212_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.765 s | 31896 KB |
| [2212_math_combinatorics.rs](2212_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.062 s | 8384 KB |
