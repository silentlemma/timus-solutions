# 1725. Sold Out!

[Timus 1725](https://acm.timus.ru/problem.aspx?space=1&num=1725) · difficulty 142 · math

Original problem by Denis Dublennykh (prepared by Oleg Dolgorukov), from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Vasya sits first in a row of n seats, at seat k; the others come one by
one until the row is full. Each enters from the end with fewer people
already sitting between it and their seat, or, on a tie, from the
nearer end. Find the largest number of people who can trip over
Vasya's legs.

## Input

n and k (1 ≤ k ≤ n ≤ 50, n even).

## Output

The largest number of people who trip over Vasya.

## Examples

### Example 1

Input:

```
4 1
```

Output:

```
1
```

## Solution

Call the longer part of the row, beyond Vasya, the far side; it has
max(k − 1, n − k) seats. The answer is that count minus 2, but not
below 0. `O(1)`.

The two seats at the far end never trip. The last seat has nobody
beyond it, and the one before has at most one person beyond it but
Vasya on the other side, and on that tie it is nearer to its own end.

Everyone else on the far side can trip. Seat the two end seats first,
then fill the far side from its end towards Vasya. Each new person
then has only Vasya on the way from Vasya's end and at least two
people on the way from the other end, so they come in past Vasya.

People on the near side can trip too, but only when the near side is
already much fuller than the far side, and then far-side people find
too many people on Vasya's side and stop tripping. This never pays
off.

In the example the far side has three seats, so one person trips: the
one at seat 2, after seats 3 and 4 are taken.

Pitfalls:

- with n = 2 or Vasya in the middle of four seats the answer is 0, not
  a negative number;
- the far side may be on either side of Vasya.

The formula matches an exhaustive search over all arrival orders for
every even n up to 16 and every k.

## Optimized solutions

The optimized C++ solution reads the two numbers with `scanf` and prints
with `printf` instead of `std::cin` and `std::cout`, so the program does
without the `iostream` library and its buffers; the formula is the same:
{1725_math_optimized.cpp}.

The optimized Java solution reads the two numbers byte by byte with
`System.in.read` instead of creating a `Scanner`, so the JVM does not
load the scanner and its regular expressions; the formula is the same:
{1725_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1725_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +74.75%; base: `1725_math.cpp`.

- `1725_math_optimized.java`: time reduction +25.60%; memory reduction
  +77.89%; base: `1725_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1725_math.go](1725_math.go).
- [1725_math.rs](1725_math.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math.cpp](1725_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11289360 |
| [1725_math.go](1725_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11289361 |
| [1725_math.java](1725_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1592 KB | 11289365 |
| [1725_math.py](1725_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 340 KB | 11289363 |
| [1725_math.rs](1725_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 244 KB | 11304071 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1725_math_optimized.cpp](1725_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11304482 |
| [1725_math_optimized.java](1725_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 352 KB | 11304483 |
