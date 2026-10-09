# 1024. The order of a permutation

[Timus 1024](https://acm.timus.ru/problem.aspx?space=1&num=1024) · difficulty 321 · math

Original problem by Nikita Shamgunov, from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A permutation `P` of `1..N` (`1 ≤ N ≤ 1000`) is given by `P(1), ..., P(N)`.
Its powers are `P^1 = P` and `P^k(n) = P(P^(k-1)(n))`. Find the smallest
`k ≥ 1` for which `P^k` is the identity. The answer does not exceed `10^9`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then the `N` numbers `P(1), ..., P(N)`.

## Output

The smallest such `k`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
2 3 1 5 4
```

Output:

```
6
```

### Example 2

Input:

```
1
1
```

Output:

```
1
```

## Solution

Every permutation splits into disjoint **cycles**: start at an element,
apply `P` until you come back. On a cycle of length `c` the permutation is a
rotation, so `P^k` is the identity on it exactly when `c` divides `k`.
`P^k` is the identity everywhere when this holds for every cycle, and the
smallest such `k` is the **least common multiple** of the cycle lengths.

Walk the cycles with a `seen` array (every element is visited once, `O(N)`)
and fold the lengths with `lcm(a, b) = a / gcd(a, b) · b` — dividing first
keeps the intermediate value small.

Pitfalls:

- the product of the cycle lengths is not the answer: lengths 4 and 6 give
  12, not 24;
- computing powers of `P` one by one can take up to `10^9` steps;
- the lcm fits in `10^9` by the statement, but `a · b` before the division
  may not fit in 32 bits — use 64-bit integers.

## Language notes

The same cycle walk everywhere; C++ (`std::lcm`) and Python (`math.lcm`)
have the lcm in the standard library.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1024_math.cpp](1024_math.cpp) | G++ 13.2 x64 | math | O(N log N) | AC | 0.015 s | 200 KB |
| [1024_math.go](1024_math.go) | Go 1.14 x64 | math | O(N log N) | AC | 0.015 s | 1100 KB |
| [1024_math.java](1024_math.java) | Java 1.8 | math | O(N log N) | AC | 0.140 s | 2400 KB |
| [1024_math.py](1024_math.py) | Python 3.12 x64 | math | O(N log N) | AC | 0.078 s | 524 KB |
| [1024_math.rs](1024_math.rs) | Rust 1.75 x64 | math | O(N log N) | AC | 0.046 s | 224 KB |
