# 1409. Two Gangsters

[Timus 1409](https://acm.timus.ru/problem.aspx?space=1&num=1409) · difficulty 15 · math

Original problem by Den Raskovalov, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

At most 10 cans stand in a row. Harry shoots them one by one from the
left, Larry from the right, and both hit the same last can at once.
Given how many cans each of them shot, find how many cans Harry did not
shoot and how many Larry did not shoot.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The numbers of cans shot by Harry and by Larry.

## Output

The numbers of cans not shot by Harry and by Larry.

## Examples

### Example 1

Input:

```
4 7
```

Output:

```
6 3
```

## Solution

The shared can is counted in both numbers, so there were H + L − 1
cans. Harry missed the other L − 1 of Larry's cans and Larry missed
H − 1, so the answer is L − 1 and H − 1. `O(1)`.

Pitfalls:

- the answer for Harry comes from Larry's count and the other way
  round, so the order is easy to swap (test 03);
- a single can gives 0 0 (test 02).

## Optimized solutions

The optimized C++ solution reads and writes with `scanf` and `printf`
instead of `iostream`, which needs less memory: 124 KB instead of
400 KB, with the same time.

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 336 KB instead of 1560 KB, with
the same time.

Read the two counts through a small byte buffer and append both results directly to the output bytes. Accepted submission 11303745 took 0.015 s and used 912 KB. The simple version took 0.031 s and used 1080 KB.

Read the two counts and subtract one from each before printing them in the required order. Accepted submission 11324298 took 0.093 s and used 248 KB. The simple version took 0.046 s and used 360 KB. The recorded runtime is higher than for the simple version.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1409_math.cpp](1409_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB | 11286064 |
| [1409_math.go](1409_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB | 11286066 |
| [1409_math.java](1409_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1560 KB | 11286070 |
| [1409_math.py](1409_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 360 KB | 11286068 |
| [1409_math.rs](1409_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 212 KB | 11286072 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1409_math_optimized.cpp](1409_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 124 KB | 11303605 |
| [1409_math_optimized.java](1409_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 336 KB | 11303746 |
| [1409_math_optimized.go](1409_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 912 KB | 11303745 |
| [1409_math_optimized.py](1409_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.093 s | 248 KB | 11324298 |

\* The marked solutions can improve their target rankings.
