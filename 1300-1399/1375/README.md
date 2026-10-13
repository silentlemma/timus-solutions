# 1375. Bill Clevers

[Timus 1375](https://acm.timus.ru/problem.aspx?space=1&num=1375) · difficulty 541 · number_theory

Original problem by Den Raskovalov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a prime p ≤ 10⁶ and 0 ≤ k ≤ p − 1, print any x and y from 0 to
p − 1 with x² + y² ≡ k (mod p), or `NO SOLUTION` if there are none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k and p.

## Output

x and y, or `NO SOLUTION`.

## Examples

### Example 1

Input:

```
1 3
```

Output:

```
0 2
```

## Solution

For an odd prime p, the squares take (p + 1) / 2 different values
modulo p, and so do the values k − x². Two sets of (p + 1) / 2 values
among p must meet, so some x² and y² add up to k: there is always an
answer, and `NO SOLUTION` never comes. For p = 2 every k is 0² + 0² or
1² + 0².

To find it, list one square root for every square: for y from 0 to
p − 1, remember y as a root of y² mod p. Then try x = 0, 1, 2, … until
k − x² mod p has a root. About half of all values are squares, so this
ends almost at once. `O(p)`.

Pitfalls:

- k = 0 has the answer 0 0 (test 07);
- k − x² must be taken modulo p as a non-negative number;
- y² can approach 10¹², beyond 32-bit integers.

The answer was checked for every k and every prime below 300, and the
tests are judged by a checker that accepts any pair.

## Language notes

- All five solutions keep the table of roots in one array of p
  numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1375_number_theory.cpp](1375_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p) | AC | 0.031 s | 3656 KB |
| [1375_number_theory.go](1375_number_theory.go) | Go 1.14 x64 | number_theory | O(p) | AC | 0.062 s | 9624 KB |
| [1375_number_theory.java](1375_number_theory.java) | Java 1.8 | number_theory | O(p) | AC | 0.156 s | 5172 KB |
| [1375_number_theory.py](1375_number_theory.py) | Python 3.12 x64 | number_theory | O(p) | AC | 0.359 s | 23992 KB |
| [1375_number_theory.rs](1375_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p) | AC | 0.046 s | 7892 KB |
