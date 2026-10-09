# 1074. Rewriting a real number with exactly N digits after the point

[Timus 1074](https://acm.timus.ru/problem.aspx?space=1&num=1074) · difficulty 2110 · parsing

Original problem by Alexander Klepinin, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A real number is an optional sign, then digits, `.digits` or
`digits.digits`, then optionally `e` or `E` with an optionally signed
integer. The input has pairs of lines: a line `S` of up to 100 characters
with codes 32–255, and an integer `0 ≤ N ≤ 100`; a line `#` ends the
input. For each pair print `Not a floating point number` if `S` is not a
real number; otherwise print its value with exactly `N` digits after the
point, cut off without rounding, with no leading zeros in the integer
part (a zero integer part is one `0`) and no `+` sign. The answer is
guaranteed to be at most 200 characters long.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Pairs of lines `S` and `N`, then the line `#`.

## Output

One line for each pair.

## Checking

The output is compared line by line; within a line, token by token. The
tests store the lines in UTF-8 and give them to the solutions in latin-1,
one byte for each character from 32 to 255.

## Examples

### Example 1

Input:

```
10.23
0
.04
1
-0.051e0
1
1.1e30
10
-1.1E-30
1
2468097632.1358642324268913e-2
20
e23
3
1 e3
1
#
```

Output:

```
10
0.0
0.0
1100000000000000000000000000000.0000000000
0.0
24680976.32135864232426891300
Not a floating point number
Not a floating point number
```

## Solution

Parse the line by hand, exactly by the grammar: an optional sign, the
digits before the point, then either a point followed by at least one
digit, or no point but at least one digit before it, then an optional
exponent with at least one digit, and nothing else. Any other character,
a space included, makes the line invalid.

Never turn the number into a floating-point value. Glue the digits before
and after the point into one string `D`; the decimal point stands after
`len(before) + exponent` of its digits, a position that may be negative or
beyond the end of `D`. The integer part is the digits of `D` before that
position, padded with zeros on the right, with leading zeros removed (or
`0`); the fraction is the next `N` digits, padded with zeros. Cutting the
digits off is exactly the required truncation. `O(|S| + N)`.

Pitfalls:

- the minus sign stays only if some printed digit is not zero: `-0.051`
  with one digit is `0.0`, and so is `-1.1E-30`;
- with `N = 0` there is no decimal point at all;
- `5.`, `.`, `e5`, `1e`, `1e+`, `1.e5` and an empty line are not numbers;
  `.5`, `+.5` and `-0` are;
- the exponent may have dozens of digits: cap its value at 1000 while
  reading; a larger one either makes the answer zero (with at most 100
  digits in `D`) or is excluded by the 200-character guarantee, unless all
  digits are zero, and then it does not matter;
- characters above 127 must not count as digits or spaces: Python's
  `str.isdigit` accepts `²`, and reading the input as UTF-8 breaks on
  such bytes, so the input is read as bytes or latin-1 and digits are
  checked as `'0' ≤ c ≤ '9'`;
- only a trailing carriage return is removed from a line; spaces are part
  of `S`.

The answers were checked against a regular expression for the grammar
and exact fraction arithmetic for the value, on the hand-made lines and
thousands of random ones.

## Language notes

- C++ reads lines with `std::getline`, which keeps every byte.
- Go and Rust read the whole input as bytes and split it at `\n`.
- Java reads the bytes and decodes them as ISO-8859-1, which maps each
  byte to one character.
- Python decodes `sys.stdin.buffer` as latin-1 for the same reason.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1074_parsing.cpp](1074_parsing.cpp) | G++ 13.2 x64 | parsing | O(len(S) + N) | AC | 0.015 s | 372 KB |
| [1074_parsing.go](1074_parsing.go) | Go 1.14 x64 | parsing | O(len(S) + N) | AC | 0.031 s | 948 KB |
| [1074_parsing.java](1074_parsing.java) | Java 1.8 | parsing | O(len(S) + N) | AC | 0.109 s | 940 KB |
| [1074_parsing.py](1074_parsing.py) | Python 3.12 x64 | parsing | O(len(S) + N) | AC | 0.078 s | 752 KB |
| [1074_parsing.rs](1074_parsing.rs) | Rust 1.75 x64 | parsing | O(len(S) + N) | AC | 0.015 s | 236 KB |
