# 1262. Pseudo-Roman number

[Timus 1262](https://acm.timus.ru/problem.aspx?space=1&num=1262) · difficulty 391 · strings

Original problem by Alexander Ipatov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Pseudo-Roman digits stand for 1, 5, 10, 50, 100, 500, 1000, and so on
without end. The statement lists rules for writing a number with them,
close to the usual Roman ones: at most three equal powers of ten in a
row and no two equal "fives" in a row; a smaller digit may stand before
a larger one only if it is a power of ten and the larger one is at most
ten times bigger; at most one smaller digit before a digit and at most
one larger after it; and a rule on every three neighbours. A digit
before a larger one is subtracted, otherwise added. Find how many
digits the pseudo-Roman notation of N has (1 ≤ N ≤ 10²⁰⁰³).

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of digits.

## Examples

### Example 1

Input:

```
1939
```

Output:

```
8
```

## Solution

Since the digits go on past M (5000, 10 000, …), every decimal place of
N is written on its own, exactly like the units, tens or hundreds in
usual Roman numerals: the decimal digits 0 to 9 take 0, 1, 2, 3, 2, 1,
2, 3, 4, 2 letters (nothing, I, II, III, IV, V, VI, VII, VIII, IX). The
answer is the sum of these over the decimal digits of N, read as a
string. `O(log N)`.

Pitfalls:

- N has up to 2004 digits, so it must be read as a string;
- the rules as printed also let some numbers be written longer: VIV is
  5 + 4 = 9 and passes all of them. The usual form is the shortest valid
  one, and the sample agrees with it;
- zeros cost nothing, so 10²⁰⁰³ is a single letter (test 03).

A brute force over all digit strings of up to seven letters with values
up to 10 000, checked against the rules, found the usual form to be the
shortest valid one for every N below 4000.

## Language notes

- All languages sum a table over the characters of the input.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1262_strings.cpp](1262_strings.cpp) | G++ 13.2 x64 | strings | O(log N) | AC | 0.031 s | 384 KB |
| [1262_strings.go](1262_strings.go) | Go 1.14 x64 | strings | O(log N) | AC | 0.031 s | 1096 KB |
| [1262_strings.java](1262_strings.java) | Java 1.8 | strings | O(log N) | AC | 0.078 s | 456 KB |
| [1262_strings.py](1262_strings.py) | Python 3.12 x64 | strings | O(log N) | AC | 0.078 s | 400 KB |
| [1262_strings.rs](1262_strings.rs) | Rust 1.75 x64 | strings | O(log N) | AC | 0.015 s | 240 KB |
