# 1131. Copying a program to N computers with K cables, one copy per cable per hour

[Timus 1131](https://acm.timus.ru/problem.aspx?space=1&num=1131) · difficulty 77 · math

Original problem by Stanislav Vasiliev and Alexander Mironenko, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A program is on one of `N` computers. In one hour a computer that has it
can copy it to one other computer over a cable, and there are `K` cables.
Find the least number of hours until all `N` computers have the program,
for `1 ≤ N, K ≤ 10⁹`.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N` and `K` on one line.

## Output

The least number of hours.

## Examples

### Example 1

Input:

```
8 3
```

Output:

```
4
```

## Solution

In an hour, `min(have, K, N − have)` new computers get the program, where
`have` is the number of computers that already have it; copying as much
as possible every hour is clearly best. While `have < min(N, K)`, double
`have` and count one hour. If this reaches or exceeds `N`, all remaining
computers can receive the program in that hour, so stop; the counter may
overshoot `N` without changing the answer. This takes at most 30 hours.
Otherwise, once `have ≥ K`, each hour adds up to `K` computers, so the
remaining `N − have` computers need `⌈(N − have) / K⌉` more hours.
`O(log min(N, K))`.

Pitfalls:

- `N = 1` needs no hours;
- with `K = 1` and `N = 10⁹` the answer is almost `10⁹`, so the hours after
  the doubling must be computed by division, not one by one;
- the last hour can copy to fewer than `K` computers (test 11), so use
  ceiling division;
- the doubling counter can exceed `N` (test 05), but reaches at most
  `2³⁰`; 64-bit integers are safe, though signed 32-bit integers suffice.

The answers were compared with a binary search over the number of hours on
every test and with an hour-by-hour simulation for all `N < 200` and
`K < 70`.

## Optimized solutions

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
344 KB instead of 1592 KB.

## Language notes

- All languages use the same loop and division.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1131_math.cpp](1131_math.cpp) | G++ 13.2 x64 | math | O(log min(N, K)) | AC | 0.015 s | 128 KB | 11279375 |
| [1131_math.go](1131_math.go) | Go 1.14 x64 | math | O(log min(N, K)) | AC | 0.015 s | 1076 KB | 11279376 |
| [1131_math.java](1131_math.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.125 s | 1592 KB | 11279379 |
| [1131_math.py](1131_math.py) | Python 3.12 x64 | math | O(log min(N, K)) | AC | 0.078 s | 424 KB | 11279378 |
| [1131_math.rs](1131_math.rs) | Rust 1.75 x64 | math | O(log min(N, K)) | AC | 0.046 s | 216 KB | 11279381 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1131_math_optimized.java](1131_math_optimized.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.093 s | 344 KB | 11303712 |
