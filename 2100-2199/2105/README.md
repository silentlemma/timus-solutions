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

## Checking

Compare one exact integer token; formatting whitespace is ignored. The new exact Python source passed 13 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

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

## Optimized solutions

Relative distance is monotone: add (speedA+speedB)*T, then subtract speed*duration for every stop of that rider. Nonoverlapping stops make these subtractions exact regardless of their start times. Each new multiple of track length creates one meeting; a stationary interval at an already reached multiple does not create more. Therefore the quotient of total relative distance by track length is the answer. The compact implementations keep only the running total and discard stop records after reading. Python uses the existing text streams and exact integer arithmetic. Preserve all five readable versions.

- `2105_math_optimized.py`: 0.125 s / 264 KB; base `2105_math.py`: 0.062 s / 440 KB; relative change: time +101.6%, memory -40.0%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `2105_math.cpp`; covering source `2105_math.cpp`; time/memory places 1/2, other-author entries 62/61.

- Go: preferred teaching base `2105_math.go`; covering source `2105_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `2105_math.java`; covering source `2105_math.java`; time/memory places 1/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `2105_math.py`; covering source `2105_math_optimized.py`; time/memory places 95/1, other-author entries 101/101.

- Rust: preferred teaching base `2105_math.rs`; covering source `2105_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2105_math.cpp](2105_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 136 KB | 11294747 |
| [2105_math.go](2105_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1084 KB | 11294750 |
| [2105_math.java](2105_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 388 KB | 11309241 |
| [2105_math.py](2105_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.062 s | 440 KB | 11294751 |
| [2105_math.rs](2105_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 196 KB | 11309404 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2105_math_optimized.py](2105_math_optimized.py) \* | PyPy 3.10 x64 | math | O(K) | AC | 0.125 s | 264 KB | 11309678 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
