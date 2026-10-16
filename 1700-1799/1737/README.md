# 1737. Mnemonics and Palindromes 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · difficulty 254 · strings

Original problem by Alexander Ipatov, from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

List, in alphabetical order, all words of length n over the letters a,
b and c that have no palindromic substring of two or more letters. If
they would take more than 100 000 letters in total, print `TOO LONG`.

## Input

n (1 ≤ n ≤ 20 000).

## Output

The words, one per line, or `TOO LONG`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
ab
ac
ba
bc
ca
cb
```

## Solution

A palindrome of two or more letters has a palindrome of two or three
letters in its middle, so it is enough that no two neighbouring
letters are equal and no two letters one apart are equal. Then any
three letters in a row are a, b and c in some order, and each letter
repeats the one three places back: the word is one of the six orders
of a, b and c repeated. So there are three words for n = 1 and six for
every longer n, and the answer is `TOO LONG` when 6n > 100 000, that is
from n = 16 667 on. `O(n)`.

Pitfalls:

- for n = 1 the six orders give only three different words;
- the limit is on the total length, not on the number of words.

The lists match all words over a, b and c checked one by one for n up
to 9.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 252 KB |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 3052 KB |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.125 s | 1132 KB |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB |
