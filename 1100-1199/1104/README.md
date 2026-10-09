# 1104. The smallest base in which a number is divisible by the base minus one

[Timus 1104](https://acm.timus.ru/problem.aspx?space=1&num=1104) · difficulty 95 · number_theory

Original problem by Igor Goldberg, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number is written with the digits `0`–`9` and the letters `A`–`Z`
(`A` = 10, …, `Z` = 35), at most `10^6` of them. Find the smallest base
`k`, `2 ≤ k ≤ 36`, in which this string is a valid number divisible by
`k − 1`. Print `No solution.` if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One line with the digits.

## Output

`k` in decimal, or `No solution.`

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
A1A
```

Output:

```
22
```

## Solution

Since `k ≡ 1 (mod k − 1)`, every power of `k` is 1 modulo `k − 1`, and a
number in base `k` has the same remainder as the sum of its digits, the
same rule as divisibility by 9 in decimal. So compute the digit sum `S`
and the largest digit `m` once, then try `k` from `max(m + 1, 2)` up to
36 and print the first one for which `k − 1` divides `S`. `O(L)` for `L`
digits.

Pitfalls:

- the base must exceed every digit, so the search starts at `m + 1`;
- base 2 divides everything by 1, so a number of zeros and ones always
  has the answer 2, including a single `0`;
- the digit sum is at most `35 · 10^6` and fits in 32 bits.

The answers were checked by converting the whole string in every base
with Python's big integers and taking the remainder directly.

## Language notes

- Python and Java read each digit as a base-36 digit with `int(ch, 36)`
  and `Character.digit`; Rust uses `to_digit(36)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1104_number_theory.cpp](1104_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L) | AC | 0.093 s | 2640 KB |
| [1104_number_theory.go](1104_number_theory.go) | Go 1.14 x64 | number_theory | O(L) | AC | 0.031 s | 6608 KB |
| [1104_number_theory.java](1104_number_theory.java) | Java 1.8 | number_theory | O(L) | AC | 0.109 s | 5448 KB |
| [1104_number_theory.py](1104_number_theory.py) | Python 3.12 x64 | number_theory | O(L) | AC | 0.265 s | 17808 KB |
| [1104_number_theory.rs](1104_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L) | AC | 0.015 s | 7048 KB |
