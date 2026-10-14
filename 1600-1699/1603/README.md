# 1603. Erudite

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · difficulty 255 · implementation

Original problem by Vladimir Yakovlev, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 4 × 4 grid holds lowercase letters. A word can be written in it along a
path of horizontally or vertically neighbouring cells that may turn at
right angles anywhere but never uses a cell twice. For each of up to 100
words of 1 to 16 letters, say whether it can be found.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Four rows of the grid, then n and the words.

## Output

`word: YES` or `word: NO` for each word.

## Examples

### Example 1

Input:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

Output:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## Solution

Search depth-first from every cell holding the first letter, stepping to
an unused neighbouring cell with the next letter. The cells used so far
form a 16-bit mask. Repeated letters can make the search revisit the
same situation many times: the same set of used cells ending in the
same cell, with the same rest of the word ahead. So a failed pair
(mask, cell) is remembered and never searched again; at most 16·2¹⁶
such pairs exist, and in practice far fewer are reachable. A quick check
first rejects a word that needs more of some letter than the grid has.

The results were compared with an independent implementation on
generated grids, including grids of one repeated letter with long words.

Pitfalls:

- without the memory of failed states, a grid of fifteen equal letters
  and a 16-letter word that cannot be placed makes the search walk
  through every self-avoiding path (tests 04 and 07);
- such a NO can come from parity alone: the grid is coloured like a
  chessboard, a path of 16 cells always ends on the other colour, so a
  word starting and ending in cells of one colour cannot use all 16
  cells (test 07);
- a cell must not be used twice, and steps are only horizontal or
  vertical (test 03).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB |
