# 1820. Ural Steaks

[Timus 1820](https://acm.timus.ru/problem.aspx?space=1&num=1820) · difficulty 25 · math

Original problem by Magaz Asanov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cook must fry both sides of n steaks, one minute per side, on a pan
that holds at most k steaks at a time. Find the least number of
minutes.

## Input

n and k (1 ≤ n, k ≤ 1000).

## Output

The least number of minutes.

## Examples

### Example 1

Input:

```
3 2
```

Output:

```
3
```

## Solution

There are 2n sides and each minute fries at most k of them, so at
least ⌈2n/k⌉ minutes are needed; and a steak cannot have both sides
fried in the same minute, so at least 2. The answer is
max(2, ⌈2n/k⌉), and it is reachable: list the sides as front 1, …,
front n, back 1, …, back n and fry the next k of them each minute. For
n ≥ k the two sides of a steak are n apart in the list and never share
a minute; for n < k both sides fit in two minutes anyway. `O(1)`.

In the example: fronts 1 and 2, then back 1 with front 3, then backs 2
and 3: three minutes.

Pitfalls:

- frying whole batches of k steaks for two minutes each wastes the
  pan: 3 steaks on a pan for 2 take 3 minutes, not 4;
- when k ≥ 2n the bound ⌈2n/k⌉ is 1, but a steak still needs two
  minutes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1820_math.cpp](1820_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1820_math.go](1820_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1076 KB |
| [1820_math.java](1820_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB |
| [1820_math.py](1820_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 348 KB |
| [1820_math.rs](1820_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
