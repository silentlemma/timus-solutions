# 1269. Obscenity filter

[Timus 1269](https://acm.timus.ru/problem.aspx?space=1&num=1269) · difficulty 832 · strings

Original problem by Pavel Atnashev, from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n ≤ 10 000 forbidden words (any bytes except 0, 10 and 13, at
most 10 000 each, at most 100 KB in all) and a text of m lines (at most
900 KB), find where a forbidden word first occurs as a substring: the
line number and the position of the word's first character in it. If
there is none, print `Passed`. The memory limit is only 8 MB.

Time limit: 1 second. Memory limit: 8 MB.

## Input

n, the n words one per line, m, then the m lines of the text.

## Output

The line and the position, or `Passed`.

## Examples

### Example 1

Input:

```
5
dear
sweetie
angel
dream
baby
8
Had I the heavens' embroidered cloths, 
Enwrought with golden and silver light, 
The blue and the dim and the dark cloths 
Of night and light and the half-light, 
I would spread the cloths under your feet: 
But I, being poor, have only my dreams; 
I have spread my dreams under your feet; 
Tread softly because you tread on my dreams.
```

Output:

```
6 33
```

## Solution

Build an Aho–Corasick automaton of the words. At each node keep the
length of the longest word that ends there, counting the words reached
through failure links. Read each line through the automaton. After the
i-th byte the longest word ending there starts at i − longest + 1, the
earliest start among the words ending at i. The answer for the line is
the least such start over the whole line. The first line with any match
gives the answer.

A table of 256 children per node would not fit into 8 MB for 100 000
nodes. Instead the trie is first built with child and sibling lists,
then renumbered in breadth-first order, so that the children of every
node get consecutive numbers. A child is then found by scanning one
short run of bytes (`memchr`, `bytes.IndexByte`, `bytearray.find`), and
the failure links are computed in the same order, every failure node
coming earlier. With W bytes of words, T bytes of text and at most
σ = 253 children per node, trie insertion and failure-link construction
cost O(W · σ), and matching costs O(T · σ). Python first sorts the n
words, adding O(W log n) byte-comparison work, and builds a bounded
transition cache. Total time is O((W + T) · σ) in the other languages
and O(W log n + (W + T) · σ) in Python.

Pitfalls:

- the earliest start is wanted, not the earliest end: in `xabcdefx` the
  word `abcdef` at 2 comes before `cd` at 4 (test 02);
- words may contain spaces, tabs and punctuation, so lines must not be
  split into tokens (tests 03, 07);
- failure links represent shorter suffixes. A nonterminal node can still
  have a terminal suffix; keep the longest matching suffix to get its
  earliest start;
- internal carriage returns in text are data: count them in positions
  and reset the automaton, since words cannot contain them. Dropping
  them shifts matches or joins bytes into false matches (test 09);
- lines may be empty, and one line can hold almost the whole text
  (test 06, gen7).

The answers were compared with searching every word in every line on
60 generated cases.

## Language notes

- All languages build the same renumbered trie in flat arrays and read
  the text line by line.
- Java builds the trie straight from the input bytes and scans each
  line of text without storing it: strings of the words and lines would
  not fit in 8 MB. Python reads bytes and keeps the arrays in `array`
  and `bytearray` to stay within the memory limit.
- The Python solution runs on CPython and keeps a cache of about 2 MB of
  automaton transitions; an earlier version without it exceeded the time
  limit on the judge's test 13. PyPy is no way out, as its runtime alone
  needs more than the 8 MB allowed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1269_strings.cpp](1269_strings.cpp) | G++ 13.2 x64 | strings | O((W + T) · σ) | AC | 0.046 s | 6004 KB |
| [1269_strings.go](1269_strings.go) | Go 1.14 x64 | strings | O((W + T) · σ) | AC | 0.078 s | 6352 KB |
| [1269_strings.java](1269_strings.java) | Java 1.8 | strings | O((W + T) · σ) | AC | 0.203 s | 3560 KB |
| [1269_strings.py](1269_strings.py) | Python 3.12 x64 | strings | O(W log n + (W + T) · σ) | AC | 0.562 s | 7048 KB |
| [1269_strings.rs](1269_strings.rs) | Rust 1.75 x64 | strings | O((W + T) · σ) | AC | 0.109 s | 6072 KB |
