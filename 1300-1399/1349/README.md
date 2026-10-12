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

## Language notes

- All five solutions print the three cases directly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1349_math.cpp](1349_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB |
| [1349_math.go](1349_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB |
| [1349_math.java](1349_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB |
| [1349_math.py](1349_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 336 KB |
| [1349_math.rs](1349_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 232 KB |
