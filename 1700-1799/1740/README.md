# 1740. Deer is Better!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · difficulty 138 · math

Original problem by Sergey Pupyrev (prepared by Daniil Ayzenshteyn), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The way to the polling station is l km long. The deer may run any way
they like, as long as every stretch of k km takes exactly h hours. Find
the shortest and the longest possible time for the whole way.

## Input

Integers l, k and h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

## Output

The shortest and the longest time, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
30 10 1
```

Output:

```
3.00000000 3.00000000
```

## Solution

Let t(x) be the time to reach kilometre x. Every stretch of k km takes h
hours, so t(x + k) = t(x) + h: t grows by h per k km plus a part that
repeats every k km. With l = nk + r, the whole way takes nh + t(r), and
t(r) lies between t(0) = 0 and t(k) = h. The deer can spend almost no
time on the first r km of every stretch, or almost all of it, so the
answers are nh and, if r > 0, (n + 1)h. `O(1)`.

In the example 30 km is three stretches of 10 km, 3 hours either way.

Pitfalls:

- when k divides l both answers are the same;
- the times are whole numbers; the code prints eight decimal
  places.

## Optimized solutions

The optimized C++ solution reads the three numbers with `scanf` instead
of `std::cin`, so the program does not carry the `iostream` machinery at
all; the computation and the output are the same:
{1740_math_optimized.cpp}.

The optimized Java solution reads the numbers with a `StreamTokenizer`
instead of a `Scanner` and does not format floating-point numbers at
all: both answers are whole numbers up to 1000 · 1000 = 10⁶, so it
computes them in `int` and appends `.00000000` to each, instead of
calling `printf` with `%.8f`, whose formatter and locale data cost more
than the rest of the program: {1740_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1740_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +72.28%; base: `1740_math.cpp`.

- `1740_math_optimized.java`: time reduction +0.00%; memory reduction
  +75.89%; base: `1740_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1740_math.go](1740_math.go).
- [1740_math.rs](1740_math.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB | 11289483 |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB | 11289484 |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1792 KB | 11304069 |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11289486 |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB | 11304070 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math_optimized.cpp](1740_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11304455 |
| [1740_math_optimized.java](1740_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.140 s | 432 KB | 11304456 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
