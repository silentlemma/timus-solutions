# 1297. Palindrome

[Timus 1297](https://acm.timus.ru/problem.aspx?space=1&num=1297) · difficulty 82 · strings

Original problem by Evgeny Krokhalev, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A line of at most 1000 Latin letters is given. Print its longest
substring that reads the same in both directions; if there are several,
print the leftmost one. Upper and lower case letters are different.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The line.

## Output

The longest palindromic substring.

## Examples

### Example 1

Input:

```
Kazak
```

Output:

```
aza
```

## Solution

Every palindrome has a centre: a letter for odd lengths, the gap
between two letters for even ones. A line of n letters has 2n − 1
centres. From each, expand outwards while the letters on both sides
match. The longest palindrome around a centre is what the expansion
reaches, and the shorter ones around it start further right, so they
never win.

The best palindrome is the longest one; among equals, the one with the
smallest start. `O(n²)` in the worst case (a line of one letter), only
about 500 000 comparisons for n = 1000.

Manacher's algorithm would do it in `O(n)`, but it is not needed at
this size.

Pitfalls:

- letters are compared exactly, so `K` and `k` differ (tests 01, 04
  and 10);
- with no two equal neighbours the answer is the first letter
  (test 03);
- ties go to the leftmost palindrome (tests 05 and 06);
- even-length palindromes need their own centres (tests 05 and 08).

The answers were compared with checking every substring on 300 random
lines.

## Language notes

- The line is read whole, and stray whitespace such as a final `\r` is
  dropped before the search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1297_strings.cpp](1297_strings.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 364 KB |
| [1297_strings.go](1297_strings.go) | Go 1.14 x64 | strings | O(n^2) | AC | 0.015 s | 1088 KB |
| [1297_strings.java](1297_strings.java) | Java 1.8 | strings | O(n^2) | AC | 0.125 s | 444 KB |
| [1297_strings.py](1297_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.171 s | 452 KB |
| [1297_strings.rs](1297_strings.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.046 s | 244 KB |
