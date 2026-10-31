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

Walk through the text: whenever a run of letters starts, find where it
ends and reverse it. Digits, punctuation, spaces and line breaks are
left untouched, so the text keeps its exact layout. `O(L)` for `L`
characters.

Pitfalls:

- the lines may end with spaces, and they must stay, so the text is not
  split into words and joined again;
- a word ends at any non-letter, including a digit or an underscore:
  `abc123` becomes `cba123`;
- the last line may lack a line break, and none must be added.

The output was compared character by character with the expected text on
every test, including 1000 lines of random printable characters.

## Optimized solutions

The optimized C++ solution reads the text with `getchar` and keeps only
the current word, in a buffer of 255 bytes, which is enough since a word
cannot cross a line and a line has at most 255 characters; it prints the
word backwards as soon as a non-letter ends it, instead of collecting
the whole text in a `std::string`: {1226_strings_optimized.cpp}.

The optimized Java solution reads the whole input as bytes in 64 KB
blocks and reverses the runs of letters in place in that byte array,
instead of decoding characters through a reader and a writer and making
a string for every word: {1226_strings_optimized.java}.

The optimized Python solution handles one line at a time in a
`bytearray` and reverses the runs of letters by slicing, instead of
importing the regular expression module and substituting over the whole
text; a word cannot cross a line, so this is safe. It saves memory, but
the loop over every character runs in Python and costs time:
{1226_strings_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1226_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +46.15%; base: `1226_strings.cpp`.

- `1226_strings_optimized.java`: time reduction +0.00%; memory reduction
  +35.00%; base: `1226_strings.java`.

- `1226_strings_optimized.py`: time reduction +0.00%; memory reduction
  +33.10%; base: `1226_strings.py`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1226_strings.rs](1226_strings.rs).

- Python reverses every match of a regular expression over the raw
  bytes; C++, Go and Rust read the whole input and reverse the runs of
  letters in place; Java reads the text character by character in
  Latin-1, which keeps every byte as it is, and prints each word
  reversed when a non-letter ends it.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB | 11283715 |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB | 11283716 |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 720 KB | 11304343 |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB | 11283717 |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB | 11283719 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings_optimized.cpp](1226_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 84 KB | 11304344 |
| [1226_strings_optimized.java](1226_strings_optimized.java) \* | Java 1.8 | strings | O(L) | AC | 0.093 s | 468 KB | 11304346 |
| [1226_strings_optimized.py](1226_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 380 KB | 11304345 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
