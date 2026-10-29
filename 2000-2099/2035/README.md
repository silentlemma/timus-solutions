# 2035. Splitting a total under two upper bounds

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · difficulty 78 · math

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given integers `X,Y,C` with `0 ≤ X,Y,C ≤ 1000000000`, find any integers
`A,B` satisfying `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` and `A+B=C`.
Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One line with `X Y C`. There is one instance and no test-count prefix.

## Output

Any valid pair `A B`, or the exact word `Impossible` if no pair exists.
The pair `0 0` is valid when `C=0`.

## Checking

A checker verifies both bounds and the sum; `Impossible` is accepted
only when no pair exists. Any valid pair is accepted.

## Examples

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solution

Take A as large as possible, A = min(X, C), and B = C − A. If B ≤ Y,
the pair works; otherwise no pair does, because any other A is smaller
and only makes B larger. `O(1)`.

Pitfalls:

- A = X alone may exceed C and make B negative;
- zero summands are allowed, and any valid pair is accepted.

## Optimized solutions

The optimized C++ solution parses the three numbers by hand with
`getchar` instead of `iostream`: 100 KB instead of 400 KB, with the same
time.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB | 11293165 |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB | 11293168 |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 492 KB | 11303531 |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11293171 |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11293174 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2035_math_optimized.cpp](2035_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11303670 |
