# 1769. Old Ural Legend

[Timus 1769](https://acm.timus.ru/problem.aspx?space=1&num=1769) · difficulty 206 · strings

Original problem by Daniil Ayzenshteyn, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a non-empty line of decimal digits, find the smallest positive
integer whose decimal notation does not occur in the line.

## Input

The line, at most 10⁵ digits.

## Output

That integer.

## Examples

### Example 1

Input:

```
10123456789
```

Output:

```
11
```

## Solution

A line of n digits has at most n pieces of each length, while there are
9·10⁵ numbers of six digits, so some six-digit number is always
missing and the answer has at most six digits. Every piece of one to
six digits that does not start with a zero is the notation of a number;
marking them all and then counting up from 1 to the first unmarked
number gives the answer. `O(6n)`.

In the example 1 to 9 and 10 occur, but 11 does not.

Pitfalls:

- pieces starting with 0 are not notations of numbers, though the
  number after the zero still occurs one digit later;
- a line of zeros misses 1;
- searching the line for each number in turn can be slow on long
  lines with a large answer.

The answers agree with a search of the line for 1, 2, 3 and so on on 90
random lines and with an independent accepted implementation on 20
long ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1769_strings.cpp](1769_strings.cpp) | G++ 13.2 x64 | strings | O(6n) | AC | 0.015 s | 632 KB |
| [1769_strings.go](1769_strings.go) | Go 1.14 x64 | strings | O(6n) | AC | 0.031 s | 2740 KB |
| [1769_strings.java](1769_strings.java) | Java 1.8 | strings | O(6n) | AC | 0.140 s | 2144 KB |
| [1769_strings.py](1769_strings.py) | Python 3.12 x64 | strings | O(6n) | AC | 0.328 s | 23756 KB |
| [1769_strings.rs](1769_strings.rs) | Rust 1.75 x64 | strings | O(6n) | AC | 0.031 s | 1472 KB |
