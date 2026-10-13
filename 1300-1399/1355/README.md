# 1355. Bald Spot Revisited

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · difficulty 212 · number_theory

Original problem by Aleksandr Bikbaev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Taverns are numbered by positive integers, and from tavern n one may go
only to a tavern whose number is a multiple of n. A walk starts at
tavern a and must end at tavern b, with a mug of ale in every tavern on
the way, a and b included. For each of T ≤ 20 pairs with
1 ≤ a, b ≤ 10⁹, print the largest number of mugs, or 0 if b cannot be
reached.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with a and b.

## Output

T lines with the answers.

## Examples

### Example 1

Input:

```
5
30 89
2 16
3 243
1 1
2 2
```

Output:

```
0
4
5
1
1
```

## Solution

Every number on the walk divides the next one, so b is reachable only
when a divides b. Then each step multiplies the number by some factor
greater than 1, and the product of all the factors is q = b / a. To
visit as many taverns as possible, each factor should be a single
prime, so the number of steps is Ω(q), the count of prime factors of q
with repetition. The answer is 1 + Ω(q), counting tavern a itself.

Trial division up to √q ≤ 31 623 finds Ω(q). `O(T · √(b / a))`.

Pitfalls:

- a = b gives one mug, not zero (example);
- b smaller than a, or not a multiple of it, gives 0 (test 04);
- T can be 0, and then no answers are printed (test 02);
- q = 2²⁹ gives the most steps, 30 mugs (test 03).

## Language notes

- Python divides out 2 first and then tries only odd divisors, which
  halves the loop on large primes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB |
