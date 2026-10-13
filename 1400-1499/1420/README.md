# 1420. Integer-Valued Complex Division

[Timus 1420](https://acm.timus.ru/problem.aspx?space=1&num=1420) · difficulty 1809 · math

Original problem by Evgeny Krokhalev, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For complex numbers with integer parts, a division of a by b with
remainder is any pair (q, r) of such numbers with b·q + r = a and
|r| < |b|. Given a and b (all parts at most 10⁶ by absolute value),
count the possible results.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The real and imaginary parts of a on the first line, of b on the second.

## Output

The number of results.

## Examples

### Example 1

Input:

```
12 0
0 5
```

Output:

```
2
```

## Solution

The remainder is fixed by q, so the task counts the integer complex
numbers q with |a − b·q| < |b|. If b = 0 nothing is shorter than 0 and
the answer is 0. Otherwise dividing by |b| gives |a / b − q| < 1: q lies
in the open unit disk around a / b, so it is one of the 3 × 3 points
around (⌊Re a/b⌋, ⌊Im a/b⌋), at most four of which can fit.

With a / b = (x + y·i) / |b|², where x = Re a·Re b + Im a·Im b and
y = Im a·Re b − Re a·Im b, floor division gives the centre exactly. Each
candidate is tested as |a − b·q|² < |b|² in 64-bit integers: the parts
of the remainder stay within a few times |b|, so nothing overflows and
no floating point is needed. `O(1)`.

Pitfalls:

- division by zero has no result at all (tests 04, 05);
- a quotient at distance exactly 1 does not count, so an integer a / b
  gives only one result (tests 02, 07);
- floor division must round towards minus infinity for negative parts
  (tests 10, 11, 12).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1420_math.cpp](1420_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1420_math.go](1420_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [1420_math.java](1420_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1568 KB |
| [1420_math.py](1420_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 416 KB |
| [1420_math.rs](1420_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 216 KB |
