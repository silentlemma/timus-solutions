# 1786. Sandro's Biography

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · difficulty 110 · strings

Original problem by Olga Soboleva, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of Latin letters must be changed so that it contains the word
"Sandro". Replacing a letter by another letter of the same case costs
5 coins, and so does changing the case of a letter. Find the smallest
cost.

## Input

The text, from 6 to 200 letters.

## Output

The smallest number of coins.

## Examples

### Example 1

Input:

```
MyNameIsAlexander
```

Output:

```
20
```

## Solution

Try every place for the six letters of the name. A letter costs 5 if
its case is wrong and 5 more if it is the wrong letter, so a letter
that is wrong in both ways costs 10. Sum the six costs at each place
and take the smallest sum. The scan takes `O(n)` time, but Python copies
the suffix `text[start:]` at each place, so that implementation takes
`O(n^2)` time. All implementations use `O(n)` memory including the input;
the maximum input length is only 200.

In the example the best place is "xander": x needs a new letter and an
uppercase, 10, while e → r and r → o cost 5 each, 20 in all.

Pitfalls:

- a wrong letter of the wrong case costs both fees;
- test 03, `sANDRO`, has all six cases wrong, so it costs 30;
- the name may start at the very first or end at the very last letter.

The Python answers agree with an independent operation-graph oracle on
2,000 random small texts, 592 directed cases, all 8 stored tests and 64
generated cases.

## Optimized solutions

The optimized C++ solution reads the text with `scanf` into a buffer of
201 bytes, enough for 200 letters and the terminating zero, instead of
`std::cin` and `std::string`, and since the text has only Latin letters
it tells the case by comparing with `'Z'` and lowers a letter by adding
`'a' − 'A'` instead of calling `isupper` and `tolower`:
{1786_strings_optimized.cpp}.

The optimized Java solution reads the text character by character
straight from `System.in` instead of creating a `Scanner`, and since the
text has only Latin letters it tells the case by comparing with `'Z'`
and lowers a letter by adding `'a' − 'A'` instead of calling
`Character.isUpperCase` and `Character.toLowerCase`:
{1786_strings_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1786_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +68.42%; base: `1786_strings.cpp`.

- `1786_strings_optimized.java`: time reduction +28.44%; memory
  reduction +75.13%; base: `1786_strings.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1786_strings.go](1786_strings.go).
- [1786_strings.rs](1786_strings.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 380 KB | 11304047 |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB | 11289804 |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1576 KB | 11304048 |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.109 s | 408 KB | 11304049 |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB | 11289809 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings_optimized.cpp](1786_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 120 KB | 11304276 |
| [1786_strings_optimized.java](1786_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.078 s | 392 KB | 11304277 |
