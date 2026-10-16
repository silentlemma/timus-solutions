# 1782. Jack's New Word

[Timus 1782](https://acm.timus.ru/problem.aspx?space=1&num=1782) · difficulty 2126 · strings

Original problem by Alex Samsonov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A binary word has no non-empty factor xyxyx with |y| ≤ 2|x|. Starting
from the empty word, three phrases are allowed: add a letter at the
front, add a letter at the back, or replace every 0 by 01 and every 1
by 10 (doubling). Build the word with at most 100 phrases, or report
that it needs more.

## Input

The word, non-empty, at most 10⁵ letters.

## Output

The number of phrases k (1 ≤ k ≤ 100) and the phrases `front c`,
`back c` or `double` in order, or −1. Any fitting description is
accepted.

## Examples

### Example 1

Input:

```
011010011
```

Output:

```
5
back 1
front 0
double
double
back 1
```

## Solution

Read backwards, a description peels a few letters off the ends of the
word, undoes a doubling, peels again, and so on. A word can be undoubled
when its letters pair up as 01 and 10, and then the first letter of
each pair gives the shorter word. Words without the forbidden repeats
have a known structure: apart from at most two letters at each end,
such a word is the double of a shorter word of the same kind. So the
fewest phrases for a word s are found by trying every way to take up to
five letters off each end (two would do, five is a margin) and undo a
doubling of the rest, against simply adding all letters of s one by
one, keeping the cheapest; the results are remembered by word. The
words met at each level are pieces of one another, so only a few dozen
are tried, and halving keeps the levels to about log₂ n.
`O(n log n)`.

The description is then written forwards: the shorter word, the
doubling, the front letters in reverse order and the back letters. If
even the fewest phrases are more than 100, the answer is −1.

In the example 01101001 is the double of 0110, which is the double of
01: two letters, two doublings and a 1 at the back, five phrases.

Pitfalls:

- the letters added at the front come out in reverse order;
- a pair 00 or 11 means the middle part is no doubled word;
- the answer is not unique, so the checker replays the phrases.

The phrase counts equal the fewest found by an independent accepted
implementation, which searches all descriptions breadth first, on 310
words: short words built by random phrases and pieces of the
Thue–Morse word of up to 10⁵ letters.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1782_strings.cpp](1782_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.046 s | 2120 KB |
| [1782_strings.go](1782_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 8736 KB |
| [1782_strings.java](1782_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.171 s | 8444 KB |
| [1782_strings.py](1782_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.156 s | 2592 KB |
| [1782_strings.rs](1782_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.046 s | 2208 KB |
