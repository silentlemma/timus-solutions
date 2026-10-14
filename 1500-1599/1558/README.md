# 1558. Periodical Numbers

[Timus 1558](https://acm.timus.ru/problem.aspx?space=1&num=1558) · difficulty 864 · math

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A periodical number (a₁…aₖ)b₁…bₘ has infinitely many digits to the left:
the block a₁…aₖ repeated forever, followed by b₁…bₘ at the low end. Add
two such numbers given with periods of the same length k ≤ 9 and no
non-periodic part, digit by digit from the low end with carries as
usual. Print the sum with the shortest period and, among those, the
shortest non-periodic part.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines, each with a number of the form (a₁…aₖ).

## Output

The sum in the same notation.

## Examples

### Example 1

Input:

```
(234)
(342)
```

Output:

```
(576)
```

## Solution

Read both periods as k-digit numbers A and B and add them, S = A + B.
If S < 10ᵏ, no block ever carries and the sum is S repeated, written
with k digits. Otherwise the lowest block is S − 10ᵏ and passes a carry
on; every block above it receives that carry, equals S + 1 − 10ᵏ, and
passes a carry on as well. So the sum is the block P = S + 1 − 10ᵏ
repeated forever above the single block S − 10ᵏ.

What is left is the shortest form. The shortest period of the infinite
part is the smallest divisor d of k for which P is made of k/d copies of
its first d digits. Then the non-periodic part is cut from the top:
going down from the first block of P, a digit still belongs to the
periodic part while it equals the digit d places above it. The digits
that remain below form the shortest non-periodic part, and the period is
read off just above them, which may turn the block: 999909 + 099000
gives (100989)09 (test gen4). The results were checked against a direct
addition over 200 digits on 1500 random pairs.

Pitfalls:

- the non-periodic part can shrink: (111) + (999) is (1)0, and
  (5) + (5) is (1)0 as well (tests 09, 02);
- leading zeros are part of the period, as in (0100) (test 10);
- a sum of all nines, such as (454545) + (545454), has no carry at all
  and is just (9) (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1558_math.cpp](1558_math.cpp) | G++ 13.2 x64 | math | O(k^2) | AC | 0.015 s | 380 KB |
| [1558_math.go](1558_math.go) | Go 1.14 x64 | math | O(k^2) | AC | 0.031 s | 1036 KB |
| [1558_math.java](1558_math.java) | Java 1.8 | math | O(k^2) | AC | 0.109 s | 468 KB |
| [1558_math.py](1558_math.py) | Python 3.12 x64 | math | O(k^2) | AC | 0.093 s | 556 KB |
| [1558_math.rs](1558_math.rs) | Rust 1.75 x64 | math | O(k^2) | AC | 0.046 s | 220 KB |
