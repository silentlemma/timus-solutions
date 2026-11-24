# 1095. Rearranging digits to get a multiple of 7

[Timus 1095](https://acm.timus.ru/problem.aspx?space=1&num=1095) · difficulty 583 · number_theory

Original problem by Dmitry Filimonenkov, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N` positive integers (`1 ≤ N ≤ 10000`, up to 20 digits) contains
each of the digits 1, 2, 3 and 4. Rearrange the digits of each number so
that the result is divisible by 7, or print 0 if that is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` numbers, one per line.

## Output

A multiple of 7 made of the digits of each number, one per line.

## Checking

Any suitable rearrangement is accepted. The checker verifies that every
answer uses exactly the digits of its number, does not start with 0 and
is divisible by 7.

## Examples

### Example 1

Input:

```
2
1234
531234
```

Output:

```
3241
531342
```

## Solution

Take one 1, one 2, one 3 and one 4 out of the number. Write the other
nonzero digits first in any order, then the four key digits in some
order, then all the zeros. The zeros at the end multiply the number by a
power of 10, which does not change divisibility by 7, and the number
cannot start with a zero. For a head with remainder `r` modulo 7, the
number before the zeros is `r · 10⁴ + p` modulo 7 for the order `p` of the
key digits, and the 24 orders of 1, 2, 3, 4 leave all seven remainders modulo 7
(`1234 ≡ 2`, `1243 ≡ 4`, `1324 ≡ 1`, `2134 ≡ 6`, `2143 ≡ 1`,
`3124 ≡ 2`, `3241 ≡ 0`, `4123 ≡ 0`, `1342 ≡ 5`, …). So one of them always
works, and 0 is never the answer. `O(N · L)` for `L` digits.

Pitfalls:

- a 20-digit number may not fit 64-bit integers, so the remainder is
  computed digit by digit (Python simply uses big integers);
- zeros in the head could put a zero first when the head is empty, which
  is why all zeros go to the end;
- only one copy of each key digit is taken out; the others stay in the
  head.

The checker verifies the digits and the divisibility of every answer with
big integers.

## Language notes

- C++ lists the orders with `std::next_permutation`; Go, Java and Rust
  build them recursively; Python uses `itertools.permutations`.

## Optimized solutions

The C++ version precomputes one order of 1, 2, 3 and 4 for each remainder modulo 7. A single pass over each number reserves the four digits, counts the zeros and computes the remainder of the remaining nonzero digits. That remainder gives the required order by table lookup. The time stays O(N·L) and the version uses fixed-size buffers. Metrics for this version come from submission 11316960.

Python submission 11317754 took 0.125 s and used 436 KB. The simple version took 0.171 s and used 2676 KB.

Go submission 11317765 took 0.031 s and used 1276 KB. The simple version took 0.046 s and used 4660 KB.

Rust submission 11317775 took 0.015 s and used 192 KB. The simple version took 0.031 s and used 936 KB.

Java submission 11317780 took 0.093 s and used 1240 KB. The simple version took 0.171 s and used 7408 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322115 · Go 1.14 x64 №11322116 · Java 1.8 №11322117 · Python 3.12 x64 №11322118 · Rust 1.75 x64 №11322119.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1095_number_theory.cpp](1095_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.015 s | 648 KB | 11322115 |
| [1095_number_theory.go](1095_number_theory.go) | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.046 s | 4660 KB | 11322116 |
| [1095_number_theory.java](1095_number_theory.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.171 s | 7408 KB | 11322117 |
| [1095_number_theory.py](1095_number_theory.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.171 s | 2676 KB | 11322118 |
| [1095_number_theory.rs](1095_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.031 s | 936 KB | 11322119 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1095_number_theory_optimized.cpp](1095_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.015 s | 112 KB | 11316960 |
| [1095_number_theory_optimized.py](1095_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.125 s | 436 KB | 11317754 |
| [1095_number_theory_optimized.go](1095_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.031 s | 1276 KB | 11317765 |
| [1095_number_theory_optimized.rs](1095_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.015 s | 192 KB | 11317775 |
| [1095_number_theory_optimized.java](1095_number_theory_optimized.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.093 s | 1240 KB | 11317780 |
