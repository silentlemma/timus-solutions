# 1457. Heating Main

[Timus 1457](https://acm.timus.ru/problem.aspx?space=1&num=1457) · difficulty 69 · math

Original problem by Nikita Rybak, Dmitry Kovalioff and Ilya Grebnov, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A straight heating main passes under N places (1 ≤ N ≤ 1000) at
positions P[i] (0 ≤ P[i] ≤ 10⁶). The effort of walking a distance is
proportional to its square. Find the point of the main where the average
effort of reaching the places is smallest, with at least six digits
after the decimal point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N positions.

## Output

The best point.

## Examples

### Example 1

Input:

```
3
7 4 5
```

Output:

```
5.333333
```

## Solution

The average of (x − P[i])² is a parabola in x whose derivative
2 (x − mean) vanishes at the arithmetic mean of the positions, so the
answer is the sum divided by N. The sum is at most 10⁹ and fits in any
integer type. `O(N)`.

Pitfalls:

- rounding to six digits may differ between languages when the mean
  ends exactly in a five, as 1/128 does (test 05); any answer within the
  required precision is accepted.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1457_math.cpp](1457_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 144 KB |
| [1457_math.go](1457_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1120 KB |
| [1457_math.java](1457_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 2612 KB |
| [1457_math.py](1457_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 504 KB |
| [1457_math.rs](1457_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 252 KB |
