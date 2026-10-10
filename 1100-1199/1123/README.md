# 1123. The smallest palindrome not below a long number

[Timus 1123](https://acm.timus.ru/problem.aspx?space=1&num=1123) · difficulty 122 · strings

Original problem by Leonid Volkov and Oleg Kats, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a non-negative integer of up to 2001 digits, print the smallest
palindrome (a number that reads the same from both ends) that is greater
than or equal to it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number on one line.

## Output

The palindrome.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
12341321
```

Output:

```
12344321
```

## Solution

First remove leading zeroes, keeping one zero if all digits are zero.
The answer has the same number of digits as this normalized number: the
number made of nines only is a palindrome. A palindrome of this length is
fixed by its left half together with the middle digit, and a larger left
half always gives a larger palindrome. So copy the left half backwards
onto the right half;
if the result is not below the number, it is the answer. Otherwise add
one to the left half (with its middle digit) and mirror again: that is
the next possible left half, so the next palindrome. The addition cannot
overflow, because a left half of nines mirrors to the largest number of
this length, which is never too small. Strings of equal length compare
like the numbers, so no big integers are needed. `O(L)` time and `O(L)`
auxiliary space, where `L` is the input length.

Pitfalls:

- the carry of the addition can run through a long block of nines (1999
  becomes 2002);
- with an odd length the middle digit belongs to the left half;
- leading zeroes must be removed before mirroring (`01` must give `1`,
  test `11`); an all-zero input must give `0`;
- the number has up to 2001 digits, far beyond any integer type.

The answers were checked by counting up to the next palindrome for all
numbers from 0 through 9999 and 3000 seeded random inputs with up to six
significant digits, including leading zeroes. An independent digit-state
dynamic program checked longer inputs by assigning symmetric digits and
tracking comparison with the input. Stored tests, generator cases and
boundary cases up to 2001 digits, including long carries, agreed.

## Language notes

- All languages work on the digit string directly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1123_strings.cpp](1123_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.001 s | 360 KB |
| [1123_strings.go](1123_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 1152 KB |
| [1123_strings.java](1123_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 436 KB |
| [1123_strings.py](1123_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 448 KB |
| [1123_strings.rs](1123_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 204 KB |
