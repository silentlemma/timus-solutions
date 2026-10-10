# 1113. The least fuel for a one-way trip with fuel depots

[Timus 1113](https://acm.timus.ru/problem.aspx?space=1&num=1113) · difficulty 264 · math

Original problem from the Bulgarian National Olympiad in Informatics, Day 2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A vehicle must cross `N` km of desert, burning one litre per kilometre.
It carries at most `M` litres, with `M < N ≤ 5M` and `N < 32000`. The
start has unlimited fuel, and the vehicle may leave any amount of fuel at
any point on the way and pick it up later. Find the least total amount
of fuel, in litres, needed to reach the target, rounded up to an integer.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N M` on one line.

## Output

The least amount of fuel, rounded up.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1000 500
```

Output:

```
3837
```

## Solution

This is the one-way jeep problem. Work backwards from the target. The
last `M` km take one full load. To bring two loads to the start of that
stretch, a stretch of `M/3` km before it is crossed three times (there,
back, there), costing exactly one extra load; in general a stretch of
`M/(2k − 1)` km carries `k` loads at the price of one more. So add
stretches `M, M/3, M/5, …` until they reach the start; if `k` loads are
needed and the stretches before the last one cover `s` km, the fuel is
`(k − 1)·M + (N − s)·(2k − 1)`. With `5M ≥ N` there are at most about
3000 stretches. `O(k)`.

Pitfalls:

- the rounding up must be exact: the fuel is often an integer, and the
  floating-point sum of `M/(2i − 1)` lands just above it, adding one
  litre too many (for example `N = 59, M = 35` gives exactly 143, but a
  plain `double` computation prints 144);
- the stretches shrink only like the odd harmonic series, so `N = 5M`
  needs about 3000 of them, and the exact fraction grows to some
  thousands of digits.

The answers were checked against a separate formulation with exact
fractions: the distance reachable with `F` litres,
`M · Σ_{i≤q} 1/(2i − 1) + (F − qM)/(2q + 1)` with `q = ⌊F/M⌋`, and a
binary search for the least integer `F` reaching `N`; the 12 hand-made
trips and 150 random ones, many with capacities divisible by
`3 · 5 · 7 · 9`, agreed.

## Language notes

- Python keeps the stretches as exact fractions.
- C++, Rust, Java and Go find `k` in floating point (an error near the
  boundary does not change the result) and then compute the fractional
  part of the fuel exactly as one fraction over the least common multiple
  of the odd denominators: in their own small big-number arithmetic for
  C++ and Rust, with `BigInteger` and `math/big` for Java and Go. Adding
  plain fractions with a `gcd` of big numbers at each of the 3000 steps
  is too slow for the half-second limit in Java and Go.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1113_math.cpp](1113_math.cpp) | G++ 13.2 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.031 s | 616 KB |
| [1113_math.go](1113_math.go) | Go 1.14 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.046 s | 3364 KB |
| [1113_math.java](1113_math.java) | Java 1.8 | math | O(k), k ≤ 3000 stretches | AC | 0.125 s | 6344 KB |
| [1113_math.py](1113_math.py) | Python 3.12 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.125 s | 908 KB |
| [1113_math.rs](1113_math.rs) | Rust 1.75 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.062 s | 536 KB |
