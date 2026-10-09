# 1089. Fixing one-letter typos with a dictionary

[Timus 1089](https://acm.timus.ru/problem.aspx?space=1&num=1089) · difficulty 840 · strings

Original problem by Anton Botov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dictionary of up to 100 lowercase words (up to 8 letters each) ends
with a line `#`; after it comes a text of up to 1000 words. A word is a
maximal run of letters `a`–`z`. Every word of the text that is not in the
dictionary but differs from a dictionary word in exactly one letter (same
length, one position) must be replaced by that dictionary word; the
dictionary is such that there is at most one choice. Print the corrected
text, keeping everything else exactly as it was, and then the number of
corrections.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The dictionary, one word per line, the line `#`, then the text.

## Output

The corrected text, then the number of corrections on its own line.

## Checking

The output must be equal to the expected text; only trailing whitespace at
the very end is ignored.

## Examples

### Example 1

Input:

```
country
occupies
surface
covers
russia
largest
europe
part
about
world
#
the rushia is the larjest cauntry in the vorld.
it ockupies abaut one-seventh of the earth's surfase.
it kovers the eastern park of yurope and the northern park of asia.
```

Output:

```
the russia is the largest country in the world.
it occupies about one-seventh of the earth's surface.
it covers the eastern part of europe and the northern part of asia.
11
```

## Solution

Walk through the text character by character. Everything that is not a
letter is copied as it is; a run of letters is a word. A word found in the
dictionary is kept. Otherwise compare it with every dictionary word of the
same length, and if one of them differs in exactly one position, write
that word instead and count a correction. `O(T · W · L)` for `T` text
words, `W` dictionary words and length `L ≤ 8`.

Pitfalls:

- only a changed letter is a correctable typo: a missing or an extra
  letter is not, so `aple` and `appple` stay as they are;
- a word already in the dictionary is correct even if another dictionary
  word is one letter away from it;
- digits, apostrophes and hyphens split words: `one-seventh` is two words;
- spaces, punctuation and empty lines must be kept exactly.

The answers were checked with a regular expression substitution over runs
of letters that asserts the uniqueness of every correction.

## Language notes

- Python uses `re.sub` with a function that keeps the running count.
- C++ and Java read the text line by line; Go, Python and Rust read it
  whole and split it at line breaks, dropping carriage returns.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1089_strings.cpp](1089_strings.cpp) | G++ 13.2 x64 | strings | O(T · W · L) | AC | 0.015 s | 416 KB |
| [1089_strings.go](1089_strings.go) | Go 1.14 x64 | strings | O(T · W · L) | AC | 0.015 s | 1244 KB |
| [1089_strings.java](1089_strings.java) | Java 1.8 | strings | O(T · W · L) | AC | 0.125 s | 700 KB |
| [1089_strings.py](1089_strings.py) | Python 3.12 x64 | strings | O(T · W · L) | AC | 0.109 s | 496 KB |
| [1089_strings.rs](1089_strings.rs) | Rust 1.75 x64 | strings | O(T · W · L) | AC | 0.031 s | 464 KB |
