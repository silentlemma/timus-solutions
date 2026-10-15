# 1723. Sandro's Book

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · difficulty 62 · strings

Original problem by Ivan Burmistrov (prepared by Olga Soboleva), from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every substring of a given word is a spell, and its strength is the
number of times it occurs in the word, overlaps included. Print a
strongest spell.

## Input

A nonempty word of at most 50 lowercase Latin letters.

## Output

Any strongest spell.

## Examples

### Example 1

Input:

```
tebidohtebidoh
```

Output:

```
tebidoh
```

## Solution

Each occurrence of a spell begins with an occurrence of its first
letter, and different occurrences begin at different places. So no
spell is stronger than its first letter alone, and a most frequent
letter is a strongest spell. `O(n)`.

In the example every letter occurs twice, so `t` is as strong as
`tebidoh`.

Pitfalls:

- occurrences may overlap: `aba` occurs three times in `abababa`, but
  `a` occurs four times;
- any strongest spell is accepted, so the tests use a checker.

The checker counts the occurrences of the answer, overlaps included,
and compares them with the expected answer's. A most frequent letter
matches an exhaustive search over all substrings on 300 random words.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 356 KB |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1572 KB |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB |
