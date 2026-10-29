# 1297. Palindrome

[Timus 1297](https://acm.timus.ru/problem.aspx?space=1&num=1297) · difficulty 82 · strings, greedy

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
- if all letters are distinct, the answer is the first letter (test 03);
  no equal neighbours rules out even-length palindromes, but odd-length
  ones such as `aba` are still possible (test 06);
- ties go to the leftmost palindrome (tests 05 and 06);
- even-length palindromes need their own centres (tests 05 and 08).

The answers were compared with checking every substring on 300 random
lines.

## Optimized solutions

The optimized C++ solution reads the letters one by one with `getchar`
instead of reading a whole line, into a fixed array for the at most 1000
letters, stopping at the first whitespace. It writes the answer straight
from that array instead of building a string: 92 KB instead of 364 KB,
with the same time. The optimized Rust solution reads and writes the
letters as bytes, with no UTF-8 string in between: 0.015 s instead of
0.046 s and 208 KB instead of 244 KB. The search from every centre is
the same.

**Growing the best palindrome** (Python). A palindrome ending at the
next letter is at most 2 longer than the best one so far: cut off its
ends and a palindrome remains that ends one letter earlier. So for each
letter only the two candidates of lengths best + 2 and best + 1 ending
there are checked, by comparing the slice with its reverse, which Python
does in C: 0.109 s instead of 0.171 s, although the memory grows from
452 KB to 464 KB.

## Language notes

- The simple solutions read the line whole, and stray whitespace such
  as a final `\r` is dropped before the search.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1297_strings.cpp](1297_strings.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 364 KB | 11284682 |
| [1297_strings.go](1297_strings.go) | Go 1.14 x64 | strings | O(n^2) | AC | 0.015 s | 1088 KB | 11284689 |
| [1297_strings.java](1297_strings.java) | Java 1.8 | strings | O(n^2) | AC | 0.125 s | 444 KB | 11284696 |
| [1297_strings.py](1297_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.171 s | 452 KB | 11284694 |
| [1297_strings.rs](1297_strings.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.046 s | 244 KB | 11284699 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1297_greedy.py](1297_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.109 s | 464 KB | 11303737 |
| [1297_strings_optimized.cpp](1297_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n^2) | AC | 0.015 s | 92 KB | 11303962 |
| [1297_strings_optimized.rs](1297_strings_optimized.rs) | Rust 1.75 x64 | strings | O(n^2) | AC | 0.015 s | 208 KB | 11303738 |
