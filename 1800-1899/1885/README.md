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

## Checking

Compare two real values with absolute or relative tolerance 1e-6. The new Python passed 6953 target-runtime cases including repository boundaries; exact rounding bounds justify all inputs.

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

## Optimized solutions

Keep the same minimum/supremum formulas as the teaching versions. Compute their numerators exactly and round nonnegative divisions to six decimal places using scale `S=10^6`: `floor((a*S+floor(b/2))/b)`. The error is at most half a decimal unit, `0.5·10^-6`, within the required tolerance. Clip the minimum at zero and the maximum at t. Emit integer and padded fractional fields directly, avoiding floating-point conversion, the general percent formatter and a concatenated output string. All input-bound intermediates fit signed 64 bits; the Python file was accepted under PyPy 3.10. This changes the arithmetic and formatting implementation, not the mathematical answer. The short floating-point bases remain available. Time and extra space stay constant.

- `1885_math_optimized.py`: 0.109 s / 272 KB; base `1885_math.py`: 0.078 s / 392 KB; relative change: time +39.7%, memory -30.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1885_math.cpp`; covering source `1885_math.cpp`; time/memory places 1/4, other-author entries 106/106.

- Go: preferred teaching base `1885_math.go`; covering source `1885_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1885_math.java`; covering source `1885_math.java`; time/memory places 1/1, other-author entries 1/1.

- Python/PyPy: preferred teaching base `1885_math.py`; covering source `1885_math_optimized.py`; time/memory places 13/1, other-author entries 23/23.

- Rust: preferred teaching base `1885_math.rs`; covering source `1885_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1885_math.cpp](1885_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB | 11308434 |
| [1885_math.go](1885_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB | 11291093 |
| [1885_math.java](1885_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1788 KB | 11291097 |
| [1885_math.py](1885_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB | 11291095 |
| [1885_math.rs](1885_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 248 KB | 11308435 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1885_math_optimized.py](1885_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 272 KB | 11309564 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
