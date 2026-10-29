# 1349. Farm

[Timus 1349](https://acm.timus.ru/problem.aspx?space=1&num=1349) · difficulty 51 · math

Original problem credited to Pierre Fermat, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n, 0 ≤ n ≤ 100, find three different integers a, b, c from 1 to
100 with aⁿ + bⁿ = cⁿ, the one with the smallest a, then the smallest
b, then the smallest c, or print −1 if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

a, b and c, or −1.

## Examples

### Example 1

Input:

```
0
```

Output:

```
-1
```

### Example 2

Input:

```
1
```

Output:

```
1 2 3
```

## Solution

- n = 0: every power is 1, and 1 + 1 is never 1, so there is no answer.
- n = 1: a + b = c, and the smallest choice with three different numbers
  is 1 2 3.
- n = 2: the smallest Pythagorean triple, 3 4 5, is the first in the
  required order.
- n ≥ 3: by Fermat's last theorem aⁿ + bⁿ = cⁿ has no solution in positive
  integers.

`O(1)`.

Pitfalls:

- n = 0 has no answer even though every power is equal (test 01);
- the numbers must be different, which rules out answers like 1 1 2 for
  n = 1.

A search over all triples up to 100 for n from 0 to 5 gave the same
answers.

## Optimized solutions

The optimized solutions print the same three answers. Java parses the
exponent by hand with `System.in.read` instead of `Scanner`: 0.062 s
instead of 0.125 s and 316 KB instead of 1612 KB. Rust writes the answer
as a byte string with `write_all` instead of `println!`: 0.031 s instead
of 0.062 s and 212 KB instead of 232 KB.

## Language notes

- All solutions print the three cases directly.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1349_math.cpp](1349_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11285147 |
| [1349_math.go](1349_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB | 11285150 |
| [1349_math.java](1349_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285153 |
| [1349_math.py](1349_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 336 KB | 11285152 |
| [1349_math.rs](1349_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 232 KB | 11285154 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1349_math_optimized.java](1349_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.062 s | 316 KB | 11303601 |
| [1349_math_optimized.rs](1349_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 212 KB | 11303602 |
