# 1283. Dwarf

[Timus 1283](https://acm.timus.ru/problem.aspx?space=1&num=1283) · difficulty 115 · math

Original problem by Leonid Volkov (prepared by Ivan Dashkevich), from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dwarf has G units of gold, and every year a bank keeps p percent of
it as a fee (1 ≤ p ≤ 99), so the gold shrinks to (100 − p)/100 of
itself. Once the gold is at most L, the dwarf gives up. G and L are at
most 2³¹ − 1. How many years are left?

Time limit: 1 second. Memory limit: 64 MB.

## Input

G, L and p.

## Output

The number of years.

## Examples

### Example 1

Input:

```
19 10 50
```

Output:

```
1
```

### Example 2

Input:

```
1000 1 1
```

Output:

```
688
```

## Solution

After k years the gold is exactly G · ((100 − p)/100)^k, and the answer
is the first k with that at most L. In whole numbers the test is

```text
G · (100 − p)^k ≤ L · 100^k
```

so both sides are multiplied each year, by 100 − p and by 100, until
the left one is no longer larger. The loop runs at most about 2140
times, for G = 2³¹ − 1, L = 1 and p = 1, and the numbers grow to a few
thousand digits. `O(Y²)` digit operations for Y years.

Pitfalls:

- the gold can land exactly on the limit, and floating point then
  misses it: 300 · 0.81 comes out as 243.00000000000003, one year too
  many for L = 243 (test 05), and ln(9801/10000) / ln(0.99) rounds up to
  three years instead of two (test 06);
- if the gold is already at most L, the answer is 0 (tests 03, 04).

## Language notes

- Python, Go and Java use their big integers; C++ and Rust keep a
  number as digits in base 10⁹ and only multiply by small factors and
  compare.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O(Y²) | AC | 0.015 s | 204 KB |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O(Y²) | AC | 0.031 s | 1276 KB |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 5600 KB |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O(Y²) | AC | 0.078 s | 480 KB |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O(Y²) | AC | 0.015 s | 232 KB |
