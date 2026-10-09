# 1070. The time zone shift between two airports from a round trip

[Timus 1070](https://acm.timus.ru/problem.aspx?space=1&num=1070) · difficulty 662 · bruteforce

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1070_bruteforce.cpp](1070_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.001 s | 128 KB |
| [1070_bruteforce.go](1070_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1080 KB |
| [1070_bruteforce.java](1070_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1552 KB |
| [1070_bruteforce.py](1070_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 368 KB |
| [1070_bruteforce.rs](1070_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.015 s | 208 KB |
