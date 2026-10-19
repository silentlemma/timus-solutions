# 1885. Passenger Comfort

[Timus 1885](https://acm.timus.ru/problem.aspx?space=1&num=1885) · difficulty 186 · math

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A plane must climb to h metres within the first t seconds and then keep
that height. It climbs at most v metres per second and may not descend
before reaching h. Passengers' ears are blocked exactly while the plane
climbs faster than x metres per second. Find the least and the greatest
possible time with blocked ears.

## Input

h, t, v, x (5000 ≤ h ≤ 12 000, 50 ≤ t ≤ 1200, 1 ≤ x < v ≤ 100,
h ≤ t·v).

## Output

The least and the greatest time, each with absolute or relative error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
10000 500 50 10
```

Output:

```
125.0 500.0
```

## Solution

Least: every second at speed x or less is free, and each such second
gains at most x metres. If t·x ≥ h, the plane climbs at x and the ears
never block. Otherwise it should climb at x for all but τ seconds and
at v for τ, with τ·v + (t − τ)·x = h, so τ = (h − t·x)/(v − x).
Spending the fast seconds at any speed below v only makes them longer.

Greatest: the ears are blocked only while climbing, so at most t
seconds and at most h/x seconds. Climbing at a speed slightly above x
approaches the latter limit, or, if h/x > t,
the plane climbs at h/t > x for all t seconds. The answer is
min(t, h/x). `O(1)`.

In the example t·x = 5000 < 10 000, so the plane needs
5000/40 = 125 seconds at 50 m/s, and climbing at h/t = 20 > 10 m/s for
all 500 seconds keeps the ears blocked the whole time.

Pitfalls:

- the greatest time is a limit: climbing at exactly x does not block
  the ears, but any speed above it does, so min(t, h/x) is the answer;
- when t·x ≥ h the least time is 0;
- climbs below x are free, so mixing slower speeds never beats one
  climb at x.

The answers agree with an independent accepted implementation on all
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1885_math.cpp](1885_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1885_math.go](1885_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB |
| [1885_math.java](1885_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1788 KB |
| [1885_math.py](1885_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB |
| [1885_math.rs](1885_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 264 KB |
