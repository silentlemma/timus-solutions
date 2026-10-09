# 1095. Rearranging digits to get a multiple of 7

[Timus 1095](https://acm.timus.ru/problem.aspx?space=1&num=1095) · difficulty 580 · number_theory

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
number is `r · 10⁴ + p` modulo 7 for the order `p` of the key digits, and
the 24 orders of 1, 2, 3, 4 leave all seven remainders modulo 7
(`1234 ≡ 2`, `1243 ≡ 4`, `1324 ≡ 1`, `2134 ≡ 6`, `2143 ≡ 1`,
`3124 ≡ 2`, `3241 ≡ 0`, `4123 ≡ 0`, `1342 ≡ 5`, …). So one of them always
works, and 0 is never the answer. `O(N · L)` for `L` digits.

Pitfalls:

- a 20-digit number does not fit 64-bit integers, so the remainder is
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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1095_number_theory.cpp](1095_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.031 s | 668 KB |
| [1095_number_theory.go](1095_number_theory.go) | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.031 s | 4712 KB |
| [1095_number_theory.java](1095_number_theory.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.140 s | 7436 KB |
| [1095_number_theory.py](1095_number_theory.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.171 s | 2740 KB |
| [1095_number_theory.rs](1095_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.046 s | 944 KB |
