# 1787. Turn for MEGA

[Timus 1787](https://acm.timus.ru/problem.aspx?space=1&num=1787) · difficulty 25 · simulation

Original problem by Bulat Zaynullin, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A traffic light lets k cars turn each minute. During minute i, aᵢ new
cars arrive at the turn, which was empty at the start. How many cars
are waiting after n minutes?

## Input

k and n (1 ≤ k, n ≤ 100), then a₁, …, aₙ (0 ≤ aᵢ ≤ 100).

## Output

The number of waiting cars.

## Examples

### Example 1

Input:

```
5 3
6 7 2
```

Output:

```
0
```

### Example 2

Input:

```
5 3
20 0 0
```

Output:

```
5
```

## Solution

Follow the jam minute by minute: add the new cars, take k away, and if
that goes below zero the jam is simply empty. `O(n)`.

In the first example the jam is 1, then 3, then 0, since only 5 cars
stand at the light in the last minute. In the second it is 15, 10, 5.

Pitfalls:

- the jam cannot go negative: a quiet minute does not save capacity for
  later, so summing all aᵢ and subtracting n·k is wrong;
- the order matters for the same reason: the first example read
  backwards, 2 7 6, leaves 3 cars instead of 0.

The answers agree with an independent accepted implementation on 150
random cases with any counts and with counts close to k.

## Optimized solutions

The optimized solutions (C++, Java) keep the same queue count. C++ reads
and writes with `scanf` and `printf` instead of `iostream`: 124 KB
instead of 392 KB, with the same time. Java parses the numbers by hand
from a small buffer instead of using `Scanner`: 364 KB instead of
1680 KB, with the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1787_simulation.cpp](1787_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 392 KB | 11303509 |
| [1787_simulation.go](1787_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1076 KB | 11289817 |
| [1787_simulation.java](1787_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 1680 KB | 11289820 |
| [1787_simulation.py](1787_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 420 KB | 11289819 |
| [1787_simulation.rs](1787_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.046 s | 248 KB | 11303511 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1787_simulation_optimized.cpp](1787_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 124 KB | 11303637 |
| [1787_simulation_optimized.java](1787_simulation_optimized.java) \* | Java 1.8 | simulation | O(n) | AC | 0.125 s | 364 KB | 11303638 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
