# 1820. Ural Steaks

[Timus 1820](https://acm.timus.ru/problem.aspx?space=1&num=1820) · difficulty 25 · math

Original problem by Magaz Asanov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cook must fry both sides of n steaks, one minute per side, on a pan
that holds at most k steaks at a time. Find the least number of
minutes.

## Input

n and k (1 ≤ n, k ≤ 1000).

## Output

The least number of minutes.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 2
```

Output:

```
3
```

## Solution

There are 2n sides and each minute fries at most k of them, so at
least ⌈2n/k⌉ minutes are needed; and a steak cannot have both sides
fried in the same minute, so at least 2. The answer is
max(2, ⌈2n/k⌉), and it is reachable: list the sides as front 1, …,
front n, back 1, …, back n and fry the next k of them each minute. For
n ≥ k the two sides of a steak are n apart in the list and never share
a minute; for n < k both sides fit in two minutes anyway. `O(1)`.

In the example: fronts 1 and 2, then back 1 with front 3, then backs 2
and 3: three minutes.

Pitfalls:

- frying whole batches of k steaks for two minutes each wastes the
  pan: 3 steaks on a pan for 2 take 3 minutes, not 4;
- when k ≥ 2n the bound ⌈2n/k⌉ is 1, but a steak still needs two
  minutes.

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 348 KB instead of 1608 KB, with
the same time.

`1820_math_optimized.cpp`. Retain max(2,ceil(2N/K)): a steak needs two distinct minutes and at most K of the 2N sides fit per minute. Explicit C byte conversion replaces formatted integer scanning/printing; signed 64-bit intermediates compute the ceiling exactly. Time and auxiliary state remain O(1).

Compared with `1820_math.cpp`: time 0.031 s → 0.015 s; memory 124 KB → 72 KB.

`1820_math_optimized.go`. Keep the same frying bound and construction. Portable os.File byte streams and bounded input/output buffers replace fmt scanning and printing; the ceiling uses int64 arithmetic. Only the two inputs and the answer are retained, so the algorithm uses O(1) time and fixed auxiliary storage.

Compared with `1820_math.go`: time 0.046 s → 0.031 s; memory 1076 KB → 808 KB.

`1820_math_optimized.py`. Use the same exact frying formula on raw byte tokens, avoiding the decoded input string and the main-function wrapper. Flush the printed answer before exiting without normal interpreter teardown. Under the stated bounded integer inputs, time and auxiliary storage remain O(1).

Compared with `1820_math.py`: time 0.093 s → 0.125 s; memory 348 KB → 216 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1820_math.cpp](1820_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 124 KB | 11303517 |
| [1820_math.go](1820_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1076 KB | 11290244 |
| [1820_math.java](1820_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB | 11290247 |
| [1820_math.py](1820_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 348 KB | 11290246 |
| [1820_math.rs](1820_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11303518 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1820_math_optimized.java](1820_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.125 s | 348 KB | 11303779 |
| [1820_math_optimized.cpp](1820_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 72 KB | 11325061 |
| [1820_math_optimized.go](1820_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 808 KB | 11325052 |
| [1820_math_optimized.py](1820_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 216 KB | 11324829 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
