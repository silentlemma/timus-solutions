# 2105. Meetings of two riders going opposite ways

[Timus 2105](https://acm.timus.ru/problem.aspx?space=1&num=2105) · difficulty 206 · math

Original problem by Nikita Sivukhin, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two kids ride around a circular path of length L in opposite directions
with speeds v_A and v_B, starting together, for T seconds; sometimes one
of them stops for a while. A meeting is a moment when they are at the
same point after not being there just before. Count the meetings. The
limits are 1 second and 64 MB.

## Input

L ≤ 10⁹, T ≤ 10⁶, v_A, v_B ≤ 10³, then n ≤ 10⁵ stops: who, start,
duration; any two stops of one kid intersect in at most one point.

## Output

The number of meetings.

## Examples

### Example 1

Input:

```
10 10 2 1
3
1 1 1
1 2 2
2 2 1
```

Output:

```
2
```

## Solution

Going opposite ways, the two are at the same point exactly when the
distance they have ridden together is a multiple of L. That distance
never decreases and starts at 0, so every multiple kL with k ≥ 1 up to
the final distance is reached once and counts as one meeting, even if
both stand still there for a while; the start itself does not count.
Any two stops of one kid intersect in at most one point, so each kid rides T minus the sum
of their stop durations, and the answer is
⌊(v_A · ride_A + v_B · ride_B) / L⌋, using 64-bit integers (arbitrary precision in Python).

In the example Alice rides 7 seconds and Bob 9, together 2 · 7 + 9 = 23
metres on a path of 10: two meetings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2105_math.cpp](2105_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 136 KB |
| [2105_math.go](2105_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1084 KB |
| [2105_math.java](2105_math.java) | Java 1.8 | math | O(n) | AC | 0.171 s | 472 KB |
| [2105_math.py](2105_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.062 s | 440 KB |
| [2105_math.rs](2105_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 216 KB |
