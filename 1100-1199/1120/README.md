# 1120. The longest run of consecutive positive integers with a given sum

[Timus 1120](https://acm.timus.ru/problem.aspx?space=1&num=1120) · difficulty 86 · math

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `1 ≤ S ≤ 10^9`, find positive integers `A` and `N` with
`S = A + (A + 1) + … + (A + N − 1)` and `N` as large as possible.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`S`.

## Output

`A N`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
14
```

Output:

```
2 4
```

## Solution

The run sums to `N·A + N(N − 1)/2`, so for a given `N` the start is
`A = (S − N(N − 1)/2) / N`, which must be a positive integer. `A ≥ 1`
means `N(N + 1)/2 ≤ S`, so `N` is at most about `√(2S) ≈ 44721`. Try `N`
downwards from that bound and stop at the first one that divides; `N = 1`
always works. `O(√S)`.

Pitfalls:

- a square root may round up: start from `⌊√(2S)⌋` and lower `N` while
  `N(N + 1)/2 > S`;
- `N(N + 1)/2` for `N ≈ 44721` is about `10^9` and fits in 32 bits, but the
  solutions use 64 bits throughout;
- a power of two has no odd divisor, so only `N = 1` works.

The answers were checked against trying every start and length for
`S ≤ 3000`, and for larger `S` against the divisor view: a run of length
`N` exists exactly when `N` divides `2S` and `2S/N − N + 1` is positive
and even.

## Language notes

- All languages run the same descending loop.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1120_math.cpp](1120_math.cpp) | G++ 13.2 x64 | math | O(√S) | AC | 0.015 s | 128 KB |
| [1120_math.go](1120_math.go) | Go 1.14 x64 | math | O(√S) | AC | 0.031 s | 1064 KB |
| [1120_math.java](1120_math.java) | Java 1.8 | math | O(√S) | AC | 0.109 s | 1640 KB |
| [1120_math.py](1120_math.py) | Python 3.12 x64 | math | O(√S) | AC | 0.078 s | 444 KB |
| [1120_math.rs](1120_math.rs) | Rust 1.75 x64 | math | O(√S) | AC | 0.046 s | 220 KB |
