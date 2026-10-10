# 1179. The base in which a text contains the most numbers

[Timus 1179](https://acm.timus.ru/problem.aspx?space=1&num=1179) · difficulty 295 · strings

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of up to 1 MB consists of digits, capital Latin letters, spaces and
line breaks; letters are digits from `A = 10` to `Z = 35`. In base `K`, a
number is a maximal run of characters that are digits of base `K`. Find
the base `K` from 2 to 36 in which the text has the most numbers, the
smallest such base on a tie, and that count.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The text.

## Output

`K` and the number of numbers.

## Examples

### Example 1

Input:

```
01234B56789
AZA
```

Output:

```
11 4
```

## Solution

Give every character a value: its digit value, or 36 for a space or a
line break, which is too large to be a digit in any base. Put such a
separator before the text too. In base `K`, a number starts at every
character whose value is below `K` while the value before it is at least
`K`. So a neighbouring pair with values `(left, right)` and
`right < left` starts one number in each base from `right + 1` to `left`
(and from 2 at the least).

Count how often each of the 37 × 37 pairs occurs, then spread each count
over its range of bases with a difference array and pick the best base.
`O(L + 37²)` for a text of length `L`.

Pitfalls:

- the first character also starts a number, which the separator put in
  front takes care of;
- an empty text, or one with no digits, gives `2 0`;
- in base 36 every letter, including `Z`, is a digit.

The answers were compared with a separately written solution, which
tracks every base character by character, on 200 random texts and on
every test.

## Language notes

- Python avoids a loop over a megabyte: it maps the text to values with
  one `translate` and counts each two-byte pair with `bytes.count`. A pair
  of two different bytes cannot overlap another copy of itself, so this
  count is exact. The other languages count the pairs in one pass.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1179_strings.cpp](1179_strings.cpp) | G++ 13.2 x64 | strings | O(L + 37²) | AC | 0.031 s | 116 KB |
| [1179_strings.go](1179_strings.go) | Go 1.14 x64 | strings | O(L + 37²) | AC | 0.015 s | 3160 KB |
| [1179_strings.java](1179_strings.java) | Java 1.8 | strings | O(L + 37²) | AC | 0.125 s | 588 KB |
| [1179_strings.py](1179_strings.py) | Python 3.12 x64 | strings | O(L + 37²) | AC | 0.640 s | 3100 KB |
| [1179_strings.rs](1179_strings.rs) | Rust 1.75 x64 | strings | O(L + 37²) | AC | 0.015 s | 2124 KB |
