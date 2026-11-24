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

`1885_math_optimized.java`. Java keeps the same minimum and upper-limit formulas, max(0,h-t*x)/(v-x) and min(t,h/x), using exact integer numerators and denominators. Long division emits twelve fractional digits directly into a 64-byte output buffer instead of double conversion, Locale.US or general formatting. Truncation error is below 1e-12, within the 1e-6 tolerance. Here x<v makes the first denominator positive; denominators are at most 99, each remainder times ten is below 1000, and each answer is at most t<=1200, so the two results fit the buffer. Fixed input bounds and twelve digits give O(1) time and auxiliary space. The floating-point teaching versions and the separate Rust implementation remain unchanged.

Exact-source Java 1.8 Accepted #11327530: 0.078 s / 336 KB. Saved 2026-11-20 compiler-cohort comparison: time 2/41, memory 1/41. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324784 was 0.125 s / 976 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1885_math_optimized.java`: 0.078 s / 336 KB; retained teaching base `1885_math.java`: 0.109 s / 1788 KB.

`1885_math_optimized.rs`. Keep exactly the same extremal formulas: max(0,h-t*x)/(v-x) and min(t,h/x), with double arithmetic and six fractional digits. Rust reads four doubles directly through checked C scanf calls and prints through printf, avoiding the input String, parsed vector and Rust formatting machinery. The static C formats match live f64 pointers and promoted double arguments; no variable format strings are used. This is an I/O/runtime improvement, not a new mathematical algorithm; both time and auxiliary storage remain O(1). The condition x<v keeps the denominator positive, and the existing 1e-6 numeric tolerance applies.

Compared with `1885_math.rs`: time 0.046 s → 0.046 s; memory 248 KB → 104 KB.

Keep the same minimum/supremum formulas as the teaching versions. Compute their numerators exactly and round nonnegative divisions to six decimal places using scale `S=10^6`: `floor((a*S+floor(b/2))/b)`. The error is at most half a decimal unit, `0.5·10^-6`, within the required tolerance. Clip the minimum at zero and the maximum at t. Emit integer and padded fractional fields directly, avoiding floating-point conversion, the general percent formatter and a concatenated output string. All input-bound intermediates fit signed 64 bits; the Python file was accepted under PyPy 3.10. This changes the arithmetic and formatting implementation, not the mathematical answer. The short floating-point bases remain available. Time and extra space stay constant.

- `1885_math_optimized.py`: 0.109 s / 272 KB; base `1885_math.py`: 0.078 s / 392 KB; relative change: time +39.7%, memory -30.6%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1885_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1885_math_optimized.java](1885_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 336 KB | 11327530 |
| [1885_math_optimized.rs](1885_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 104 KB | 11325115 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
