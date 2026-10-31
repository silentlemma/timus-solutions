# 1336. Problem of Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · difficulty 123 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write a whole number n, 1 ≤ n ≤ 10⁹, as the ratio of a square to a cube:
find whole numbers m and k from 1 to 10¹⁰⁰ with m² = k³ · n. Any such
pair is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

m on the first line and k on the second.

## Checking

The checker accepts any m and k from 1 to 10¹⁰⁰ with m² = k³ · n.

## Examples

### Example 1

Input:

```
18
```

Output:

```
12
2
```

### Example 2

Input:

```
1
```

Output:

```
1
1
```

## Solution

Take k = n and m = n². Then m² = n⁴ = n³ · n. So a pair always exists,
which is also why the problem always has a solution. `O(1)`.

Pitfalls:

- m reaches 10¹⁸, which needs a 64-bit integer (test 03);
- the first sample shows a smaller pair; any correct one is accepted.

## Optimized solutions

The optimized Java solution reads n byte by byte from `System.in`
instead of creating a `Scanner`, whose regular expressions and locale
data are the main cost of a program that does one multiplication; n²
still fits in `long`, since it is at most 10¹⁸:
{1336_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1336_math_optimized.java`: time reduction +0.00%; memory reduction
  +77.24%; base: `1336_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1336_math.cpp](1336_math.cpp).
- [1336_math.go](1336_math.go).
- [1336_math.rs](1336_math.rs).

- All five solutions print n² and n.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285033 |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11285034 |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11285036 |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB | 11285035 |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11285038 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math_optimized.java](1336_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11304378 |
