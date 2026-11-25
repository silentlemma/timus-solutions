# 1070. The time zone shift between two airports from a round trip

[Timus 1070](https://acm.timus.ru/problem.aspx?space=1&num=1070) · difficulty 665 · bruteforce

Original problem by Magaz Asanov and Stanislav Vasiliev, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A flight goes from one airport to another and a second flight comes back.
For each flight the departure and the arrival are given in the local time
of the airport where they happen. The clocks of the two airports differ by
a whole number of hours, at most 5; every flight takes at most 6 hours, and
the two flights differ in duration by at most 10 minutes. Find the
difference between the clocks.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines, one per flight, each with the departure and arrival times as
`HH.MM`.

## Output

The difference in hours, a non-negative integer.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
23.42 00.39
08.10 17.11
```

Output:

```
4
```

## Solution

Let the second airport be `k` hours ahead of the first. Then the real
duration of the first flight is its clock difference minus `k` hours, and
that of the second flight is its clock difference plus `k` hours, both
taken modulo a day, since a flight may land "before" it leaves by the
clock. Try every `k` from −5 to 5 and keep the one where both durations
are at most 6 hours and differ by at most 10 minutes. Print `|k|`. `O(1)`.

Only one `k` passes: a step of one hour changes the difference of the two
durations by two hours, and with durations of at most 6 hours the
wrap-around of the day cannot produce a second match.

Pitfalls:

- a flight can cross midnight, and with the shift a flight can even land
  earlier on the clock than it leaves, so the durations are taken modulo
  24 hours;
- `HH.MM` is not a decimal fraction: read hours and minutes separately
  rather than as a real number.

The answers were checked another way: trying every real duration of the
first flight up to six hours, deriving the shift from it and checking the
return flight, with the shift found to be unique.

## Language notes

- C++ reads each time with `scanf("%d.%d")`; the other languages split the
  token at the dot.
- Python, Java (`Math.floorMod`) and Rust (`rem_euclid`) have a modulo
  that is never negative; C++ and Go add a day before the second `%`.

## Optimized solutions

Subtract the two clock differences and wrap the result into the interval from −12 to 12 hours. It equals twice the time-zone shift plus the difference in flight durations, which is at most ten minutes in magnitude. Round the absolute value to the nearest multiple of two hours.

Java submission 11317998 took 0.093 s and used 324 KB. The simple version took 0.093 s and used 1540 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322403 · Go 1.14 x64 №11322484 · Python 3.12 x64 №11322478 · Rust 1.75 x64 №11322445 · Java 1.8 №11322489.

Go 1.14 x64, submission 11322471. Time 0.015 → 0.015 s, memory 1072 → 276 KB.

The PyPy version reduces the difference of the two local durations to the interval around zero and rounds it to the nearest multiple of two hours. PyPy 3.10 x64, submission 11322490. Time 0.062 → 0.14 s, memory 352 → 240 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1070_bruteforce.cpp](1070_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 112 KB | 11322403 |
| [1070_bruteforce.go](1070_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1072 KB | 11322484 |
| [1070_bruteforce.java](1070_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.093 s | 1540 KB | 11322489 |
| [1070_bruteforce.py](1070_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.062 s | 352 KB | 11322478 |
| [1070_bruteforce.rs](1070_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.015 s | 204 KB | 11322445 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1070_math.java](1070_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 324 KB | 11317998 |
| [1070_math.go](1070_math.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 276 KB | 11322471 |
| [1070_math.py](1070_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 240 KB | 11322490 |

\* The marked solutions can improve their target rankings.
