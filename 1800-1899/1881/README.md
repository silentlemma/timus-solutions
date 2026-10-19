# 1881. Long problem statement

[Timus 1881](https://acm.timus.ru/problem.aspx?space=1&num=1881) · difficulty 62 · simulation

Original problem by Fedor Fominykh, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A page has h lines of w characters. Words on a line are separated by
single spaces, and a word that does not fit on the current line starts
a new one; words are never split. How many pages does a text of n
words take?

## Input

h, w and n (1 ≤ h, w ≤ 100, 1 ≤ n ≤ 10 000), then n words, one per line,
each at most w characters long; their total length is at most 10 000.

## Output

The number of pages.

## Examples

### Example 1

Input:

```
3 5 6
To
be
or
not
to
be
```

Output:

```
2
```

## Solution

Fill the lines greedily. Keep the number of characters used on the
current line; a word needs its length plus one space unless it starts
the line. If it does not fit, start a new line with it. Starting the
count at −1 makes the first word of a line need no space. The answer
is the number of lines divided by h, rounded up. `O(n)`.

In the example the lines are "To be", "or", "not" and "to be": "or not"
and "not to" are one character too long. Four lines on pages of three
lines take two pages.

Pitfalls:

- a word exactly filling the rest of the line, space included, still
  fits;
- the space goes only between words, never at the start of a line;
- the page count rounds up.

The counts agree with an independent accepted implementation on 100
random texts.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB |
