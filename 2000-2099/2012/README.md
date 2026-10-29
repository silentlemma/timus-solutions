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

The first hour takes 60 minutes, and the 12 − f remaining tasks take
45 minutes each, one after another. The plan fits when
60 + 45 · (12 − f) ≤ 300, that is when f ≥ 7. `O(1)`.

Pitfall: the remaining tasks start only after the whole first hour, even
if the first f are done earlier.

## Optimized solutions

The optimized C++ and Java solutions check the same inequality. C++
reads with `scanf` and prints with `puts` instead of `iostream`: 116 KB
instead of 380 KB, with the same time. Java parses the number by hand
from `System.in` instead of using `Scanner`: 0.078 s instead of 0.125 s
and 432 KB instead of 1532 KB.

The optimized Rust solution writes the answer as bytes in one call
instead of using `println!`: 0.015 s instead of 0.046 s and 220 KB
instead of 236 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2012_math.cpp](2012_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB | 11292500 |
| [2012_math.go](2012_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1080 KB | 11292501 |
| [2012_math.java](2012_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1532 KB | 11303528 |
| [2012_math.py](2012_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 348 KB | 11292502 |
| [2012_math.rs](2012_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB | 11292505 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2012_math_optimized.cpp](2012_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11303657 |
| [2012_math_optimized.java](2012_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 432 KB | 11303529 |
| [2012_math_optimized.rs](2012_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 220 KB | 11303792 |
