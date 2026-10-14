# 1592. Chinese Clocks

[Timus 1592](https://acm.timus.ru/problem.aspx?space=1&num=1592) · difficulty 588 · math

Original problem by Andrey Demidov, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n ≤ 50000 clocks with 12-hour dials, each showing a time
h:mm:ss. The hands can only be wound forward, and the effort is the
total time the hands are moved. Choose one time to set on all clocks
with the least total effort.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the time of each clock as h:mm:ss with 1 ≤ h ≤ 12.

## Output

The chosen time in the same format.

## Examples

### Example 1

Input:

```
3
11:30:00
12:10:01
6:10:18
```

Output:

```
12:10:01
```

## Solution

Count seconds from 12 o'clock, so a time is a number t from 0 to 43199.
Winding a clock from time a to time t costs (t − a) mod 43200 seconds of
hand movement. For a target t, the clocks showing at most t cost t − a,
and the clocks showing a later time cost a full cycle more, so the total
is n·t − Σa + 43200·(number of clocks after t). Moving t back to the
nearest clock time does not increase the total effort, so the best
target is one of the clock times. After sorting, a pointer keeps the
count while t goes through the clock times: `O(n log n)`.

The statement does not say which time to print when several are equally
good; the solutions print the earliest one counting from 12 o'clock.
The results were checked against trying all 43200 times on small
inputs.

Pitfalls:

- 12 o'clock is the start of the dial: it is 0 seconds, and an answer of
  0 seconds is printed as 12:00:00;
- the total effort reaches about 50000·43200 ≈ 2·10⁹, beyond 32-bit
  integers;
- minutes and seconds are printed with two digits, the hour without a
  leading zero.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1592_math.cpp](1592_math.cpp) | G++ 13.2 x64 | math | O(n log n) | AC | 0.062 s | 584 KB |
| [1592_math.go](1592_math.go) | Go 1.14 x64 | math | O(n log n) | AC | 0.046 s | 5708 KB |
| [1592_math.java](1592_math.java) | Java 1.8 | math | O(n log n) | AC | 0.109 s | 6124 KB |
| [1592_math.py](1592_math.py) | Python 3.12 x64 | math | O(n log n) | AC | 0.156 s | 6344 KB |
| [1592_math.rs](1592_math.rs) | Rust 1.75 x64 | math | O(n log n) | AC | 0.046 s | 1268 KB |
