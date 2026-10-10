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

The answer has the same number of digits: the number made of nines only
is a palindrome. A palindrome of this length is fixed by its left half
together with the middle digit, and a larger left half always gives a
larger palindrome. So copy the left half backwards onto the right half;
if the result is not below the number, it is the answer. Otherwise add
one to the left half (with its middle digit) and mirror again: that is
the next possible left half, so the next palindrome. The addition cannot
overflow, because a left half of nines mirrors to the largest number of
this length, which is never too small. Strings of equal length compare
like the numbers, so no big integers are needed. `O(L)`.

Pitfalls:

- the carry of the addition can run through a long block of nines (1999
  becomes 2002);
- with an odd length the middle digit belongs to the left half;
- the number has up to 2001 digits, far beyond any integer type.

The answers were checked by counting up to the next palindrome for
numbers of up to six digits, and for longer ones by building, with big
integers, the palindromes of the left half `p` and of `p + 1` and taking
the smaller one not below the number; 400 random numbers and the long
tests, with carries through hundreds of nines, agreed.

## Language notes

- All languages work on the digit string directly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1123_strings.cpp](1123_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 360 KB |
| [1123_strings.go](1123_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.015 s | 1116 KB |
| [1123_strings.java](1123_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 452 KB |
| [1123_strings.py](1123_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 376 KB |
| [1123_strings.rs](1123_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 204 KB |
