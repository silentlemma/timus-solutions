# 1756. One and a Half Diggers

[Timus 1756](https://acm.timus.ru/problem.aspx?space=1&num=1756) · difficulty 179 · math

Original problem by Magaz Asanov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

m diggers dig a trench in exactly d₁ days, all working every day. Plan
how many diggers work on each of d₂ days so that the same trench is
dug in exactly d₂ days with as few diggers hired as possible. A day
with nobody working is allowed.

## Input

m, d₁ and d₂ (1 ≤ m, d₁, d₂ ≤ 10000).

## Output

d₂ numbers: the diggers working on each day. Any best plan is
accepted.

## Examples

### Example 1

Input:

```
3 1 2
```

Output:

```
1 2
```

## Solution

The trench takes W = m·d₁ digger-days. The number of diggers to hire
is the largest daily number, and d₂ days with at most k diggers each
give at most k·d₂ digger-days, so at least ⌈W / d₂⌉ diggers are
needed. That many are enough: with W = q·d₂ + r, put q diggers on
d₂ − r days and q + 1 on the other r. `O(d₂)`.

In the example W = 3 over 2 days: one day with 1 digger and one with 2,
so two diggers are hired, not one and a half.

Pitfalls:

- m·d₁ reaches 10⁸, which is fine in 32 bits but worth noticing;
- when W < d₂ some days have nobody working;
- the daily numbers must add up to W exactly, not just reach it.

The plans pass a checker that tests the sum and the busiest day, on
small, random and near-limit inputs; an independent accepted
implementation prints the same days in another order.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1756_math.cpp](1756_math.cpp) | G++ 13.2 x64 | math | O(d2) | AC | 0.015 s | 128 KB |
| [1756_math.go](1756_math.go) | Go 1.14 x64 | math | O(d2) | AC | 0.031 s | 1060 KB |
| [1756_math.java](1756_math.java) | Java 1.8 | math | O(d2) | AC | 0.109 s | 1996 KB |
| [1756_math.py](1756_math.py) | Python 3.12 x64 | math | O(d2) | AC | 0.125 s | 1148 KB |
| [1756_math.rs](1756_math.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.015 s | 620 KB |
