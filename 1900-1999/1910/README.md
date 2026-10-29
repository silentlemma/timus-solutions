# 1910. The Strongest Consecutive Triple

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a sequence of positive values, find the three consecutive elements
with the largest sum. Report that sum and the 1-based position of the
middle element. The maximizing triple is guaranteed to be unique.
Limits: 1 second and 64 MB.

## Input

First n, 3≤n≤1000, then n integers aᵢ with 1≤aᵢ≤10⁶.
Whitespace and line breaks are interchangeable separators.

## Output

Print the maximum sum followed by the 1-based middle position.

## Checking

Two exact integers, checked token by token.

## Examples

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solution

Try every section from the second to the next to last as the middle of
the three: add it to its two neighbours and keep the largest sum with
its number. The statement promises that the best triple is unique, so a
strict comparison is enough. `O(n)`; a sum is at most 3·10⁶ and fits a
32-bit integer.

Pitfalls:

- the answer is the number of the middle section, counted from 1;
- with n = 3 there is only one triple.

## Optimized solutions

The optimized C++ solution does not store the sections: it reads them
one by one with `scanf` and keeps only the two before the current one,
which is all a triple needs: 128 KB instead of 192 KB, with the same
time.

The optimized Java solution keeps only the two sections before the
current one, as the C++ one does, and parses the input by hand instead
of using `Scanner`: 0.125 s instead of 0.156 s and 380 KB instead of
2372 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.125 s | 380 KB | 11303787 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
