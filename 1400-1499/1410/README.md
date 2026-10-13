# 1410. Crack

[Timus 1410](https://acm.timus.ru/problem.aspx?space=1&num=1410) · difficulty 386 · dp

Original problem by Den Raskovalov (idea by Magaz Asanov), from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A phrase is given: words are runs of Latin letters and every other
character separates them; no word repeats, ignoring case. Arthur
answers with the same phrase after deleting some words, keeping the
order. A word may last at most as many seconds as it has letters, and
no two words that stood next to each other in the phrase may both stay.
How many seconds can the answer last at most?

Up to 10 000 words of up to 100 letters, at most 512 KB of input.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The phrase.

## Output

The longest possible answer, in seconds.

## Examples

### Example 1

Input:

```
You have come a long way
```

Output:

```
11
```

In the example the answer is "You come long".

## Solution

Two words become a forbidden pair in the answer exactly when they were
neighbours in the phrase, so the task is to pick words with no two
neighbours and the largest total length. Go through the words keeping
two numbers: the best total with the last word kept and with it
dropped. A new word of length w gives kept' = dropped + w and
dropped' = max(kept, dropped). The words are cut out while reading,
without storing the phrase. `O(size of input)`.

Pitfalls:

- the phrase may span several lines (test 02);
- any non-letter separates words, including apostrophes, digits and
  `=`, and runs of separators give no empty words (tests 04, 05, gen4);
- the input may hold no words at all, and then the answer is 0 (tests
  03 and 06);
- taking the longest word first is wrong: in "tiny Enormous small" the
  two short words win (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1410_dp.cpp](1410_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.015 s | 108 KB |
| [1410_dp.go](1410_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 3180 KB |
| [1410_dp.java](1410_dp.java) | Java 1.8 | dp | O(L) | AC | 0.109 s | 568 KB |
| [1410_dp.py](1410_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.078 s | 2012 KB |
| [1410_dp.rs](1410_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 1240 KB |
