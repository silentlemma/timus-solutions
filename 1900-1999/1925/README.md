# 1925. One Final Value to Match an Aggregate

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Original problem by Pavel Ageev, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence of n past rounds is known. In round i, a displayed value bᵢ
had intended input bᵢ−2, but the actual input was gᵢ. The current round
displays k. Only the total over all n+1 rounds is checked: actual inputs
must sum to the sum of intended inputs. Choose a nonnegative integer
for the current round, or report that none exists. Past rounds need not
be individually correct. Limits: 1 second, 64 MB.

## Input

n,k with 1≤n,k≤100, followed by n pairs bᵢ,gᵢ, each in 0..100.

## Output

Print the required nonnegative integer, including zero if appropriate.
There is no upper bound of 100 on this output. If impossible, print
exactly `Big Bang!`, with its space, capitalization and exclamation mark.

## Checking

Compare whitespace-separated tokens exactly: either the integer or
the two tokens `Big` and `Bang!`.

## Examples

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solution

Let x be today's input. The check compares the sums over all n + 1
rounds: g₁ + … + gₙ + x = (b₁ − 2) + … + (bₙ − 2) + (k − 2). So
x = k − 2 + Σ(bᵢ − gᵢ − 2); if it is negative, no input works and the
answer is `Big Bang!`. `O(n)`.

Pitfalls:

- the running total may become negative in the middle and still end
  nonnegative, so decide only at the end;
- zero is a valid answer;
- every round, today's included, subtracts 2.

## Optimized solutions

The optimized C++ solution reads the pairs with `scanf` instead of
`iostream` and adds them up at once instead of storing the history:
124 KB instead of 428 KB.

The optimized Java solution reads the input in 1 KB blocks and parses it
by hand instead of using `Scanner`, and adds the readings up as they are
read instead of storing them: 0.078 s instead of 0.140 s and 364 KB
instead of 1796 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB | 11291544 |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB | 11291551 |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB | 11291560 |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB | 11291556 |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11291566 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1925_math_optimized.cpp](1925_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 124 KB | 11303650 |
| [1925_math_optimized.java](1925_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 364 KB | 11303789 |
