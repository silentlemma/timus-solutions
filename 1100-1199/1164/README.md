# 1164. Which letters are left after finding all words of a fillword

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · difficulty 206 · strings

Original problem by Alex Selivanov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid of `N×M` capital letters (`2 ≤ N, M ≤ 10`) hides `P ≤ 100` words.
Each word occupies a path of side-adjacent cells, and no cell belongs to
two words or twice to the same word. A valid placement always exists.
Print the letters of the cells not used by any word, in alphabetical
order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M` and `P`, then `N` rows of the grid, then the `P` words.

## Output

The leftover letters, sorted, on one line.

## Examples

### Example 1

Input:

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

Output:

```
EEG
```

## Solution

There is no need to find the words at all. Every placement uses each
letter of each word in exactly one cell, so whichever placement is chosen,
the cells left over hold the letters of the grid minus the letters of the
words, counted with multiplicity. Count the 26 letters over the grid,
subtract their counts over the words and print each letter as many times
as it remains. `O(N·M + total length of the words)`.

Pitfalls:

- the search looks necessary but is not: the placement may be ambiguous,
  as in the example, yet the multiset of leftover letters never is;
- if the words cover the whole grid, the answer is an empty line.

## Language notes

- All languages read the input as whitespace-separated tokens, so line
  breaks do not matter.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 380 KB |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N·M + total word length) | AC | 0.031 s | 1184 KB |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N·M + total word length) | AC | 0.109 s | 1640 KB |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N·M + total word length) | AC | 0.078 s | 436 KB |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N·M + total word length) | AC | 0.015 s | 220 KB |
