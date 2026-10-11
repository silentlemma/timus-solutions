# 1226. Every word written backwards

[Timus 1226](https://acm.timus.ru/problem.aspx?space=1&num=1226) · difficulty 114 · strings

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The statement leaves the transformation for the reader to guess from the
example: a text of up to 1000 lines of up to 255 printable characters
each must be reproduced with the letters of every word in reverse order.
A word is a maximal run of Latin letters, upper or lower case; every
other character stays where it is.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The text.

## Output

The text with every word reversed.

## Examples

### Example 1

Input:

```
This is an example of a simple test. If you did not 
understand the ciphering algorithm yet, then write the 
letters of each word in the reverse order. By the way, 
"reversing" the text twice restores the original text.
```

Output:

```
sihT si na elpmaxe fo a elpmis tset. fI uoy did ton 
dnatsrednu eht gnirehpic mhtirogla tey, neht etirw eht 
srettel fo hcae drow ni eht esrever redro. yB eht yaw, 
"gnisrever" eht txet eciwt serotser eht lanigiro txet.
```

## Solution

Read the whole input at once and walk through it: whenever a run of
letters starts, find where it ends and reverse it in place. Digits,
punctuation, spaces and line breaks are left untouched, so the text keeps
its exact layout. `O(L)` for `L` characters.

Pitfalls:

- the lines may end with spaces, and they must stay, so the text is not
  split into words and joined again;
- a word ends at any non-letter, including a digit or an underscore:
  `abc123` becomes `cba123`;
- the last line may lack a line break, and none must be added.

The output was compared character by character with the expected text on
every test, including 1000 lines of random printable characters.

## Language notes

- Python reverses every match of a regular expression over the raw bytes;
  the other languages walk the bytes by hand.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 444 KB |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB |
