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
Words are nonempty and contain only uppercase and lowercase English
letters and the punctuation marks `.,!?`.

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

## Optimized solutions

The optimized C++ solution never stores a word: it reads each word
character by character with `getchar` and keeps only its length, which
is all the line breaking needs. It takes 128 KB instead of 404 KB, with
the same time.

The optimized Java solution reads the input in 1 KB blocks and only
measures each word, byte by byte, instead of joining the lines and
splitting them into strings: 408 KB instead of 1336 KB, with the same
time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB | 11291031 |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB | 11291032 |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB | 11291035 |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB | 11291034 |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB | 11291036 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1881_simulation_optimized.cpp](1881_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 128 KB | 11303646 |
| [1881_simulation_optimized.java](1881_simulation_optimized.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 408 KB | 11303783 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
