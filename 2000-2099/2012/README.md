# 2012. Finishing Twelve Tasks Before the Deadline

[Timus 2012](https://acm.timus.ru/problem.aspx?space=1&num=2012) · difficulty 17 · math

Original problem by Alexander Ipatov, prepared by Olga Soboleva, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A five-hour session contains twelve tasks. Exactly `f` tasks are
completed during the first hour. Even if this work ends earlier, the
next task starts only after that whole hour. Each remaining task takes
exactly 45 minutes, and tasks are done sequentially. Decide whether all
twelve finish by the end of the session.

## Input

A single integer `f`, `1 ≤ f ≤ 11`. Time limit 1 second, memory 64 MB.

## Output

Print uppercase `YES` if the plan finishes on time; otherwise print
`NO`. The unique answer is compared token by token.

## Checking

Outputs are compared token by token.

## Examples

```
7
```

```
YES
```

```
5
```

```
NO
```

For `f=7`, five tasks remain: the total time is `60+5·45=285` minutes,
within 300. For `f=5`, seven tasks remain and the total is
`60+7·45=375`, exceeding the deadline.

## Solution

Convert all durations to minutes. The first phase consumes 60 minutes,
and there are `12−f` remaining tasks. The finishing time is therefore
`T=60+45·(12−f)`. Return `YES` exactly when `T≤300`.

This is both necessary and sufficient. The fixed first hour and the
consecutive remaining tasks require exactly that much time, so a larger
total cannot meet the deadline. If the total is at most 300, performing
the remaining tasks immediately after minute 60 finishes within the
session. No spare time from inside the first hour is available to move
that starting point earlier.

Equivalently, 240 minutes remain after the first hour. Only
`floor(240/45)=5` further tasks fit, so `12−f≤5`, or `f≥7`. The programs
use the duration expression with named constants rather than an
unexplained threshold. Both forms include equality at the deadline.

Time is `O(1)` and extra space is `O(1)`. For valid input the total is
at most `60+11·45=555`; ordinary signed integers suffice. No
floating-point arithmetic or rounding is needed.

## Language notes

Reserve the full first hour, count the tasks still unsolved, and keep
hours and minutes consistent. The output is `YES`/`NO`, not mixed case.
Java 8's scanner is sufficient for one integer; the other ports use
their standard input readers. CPython is sufficient for the
constant-size calculation. All five implementations use the same exact
integer inequality.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2012_math.cpp](2012_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB |
| [2012_math.go](2012_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1080 KB |
| [2012_math.java](2012_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1564 KB |
| [2012_math.py](2012_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 348 KB |
| [2012_math.rs](2012_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
