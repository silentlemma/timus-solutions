# 1586. Threeprime Numbers

[Timus 1586](https://acm.timus.ru/problem.aspx?space=1&num=1586) · difficulty 144 · dp

Original problem by Denis Musin, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number is threeprime when every three neighbouring digits form a
three-digit prime. Count the n-digit threeprime numbers
(3 ≤ n ≤ 10000) modulo 10⁹ + 9.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n.

## Output

The count modulo 10⁹ + 9.

## Examples

### Example 1

Input:

```
4
```

Output:

```
204
```

## Solution

Whether a digit can follow depends only on the last two digits, so
count the numbers by them. For n = 3 every three-digit prime counts
once, under its last two digits. Each further digit c appends to a
number ending in ab exactly when abc is a three-digit prime, and the
new number ends in bc. The 143 three-digit primes give 143 transitions
per digit: `O(143·n)`. The results were checked against testing every
number of up to six digits.

Pitfalls:

- a three-digit prime cannot start with 0, so no window may start with a
  zero digit either; counting by the primes themselves takes care of it;
- the count overflows quickly and is taken modulo 10⁹ + 9, not
  10⁹ + 7.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1586_dp.cpp](1586_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 204 KB |
| [1586_dp.go](1586_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 6456 KB |
| [1586_dp.java](1586_dp.java) | Java 1.8 | dp | O(n) | AC | 0.171 s | 6072 KB |
| [1586_dp.py](1586_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.390 s | 488 KB |
| [1586_dp.rs](1586_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.015 s | 240 KB |
