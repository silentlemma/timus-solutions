# 1532. Lost in Translation

[Timus 1532](https://acm.timus.ru/problem.aspx?space=1&num=1532) · difficulty 1976 · hashing

Original problem by Sergey Pupyrev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A list holds K distinct words (1 ≤ K ≤ 5000) of 1 to 15 lowercase English
letters. Some of them are misspellings of others: a misspelled word has
at most two mistakes, each a missing letter, an extra letter or a wrong
letter, and the correct spelling of every word is on the list. Print, in
lexicographic order, every word that occurs more than once together with
its misspellings.

Time limit: 4 seconds. Memory limit: 64 MB.

## Input

K, then the K words, one per line.

## Output

The number of such words, then the words, one per line.

## Examples

### Example 1

Input:

```
7
lomba
pella
palpa
papa
moina
morna
sin
```

Output:

```
5
moina
morna
palpa
papa
pella
```

## Solution

Since the correct spellings are all on the list, a word belongs to the
answer exactly when some other word is at most two edits away from it.
Take an optimal alignment of two such words: every substitution deletes
a letter from both words, every extra letter deletes a letter from one
of them, and what is left is the same string, the rest. So each word
deletes at most two letters. Conversely, if deleting letters from two
words leaves the same rest, record for each deleted letter its gap: the
number of letters of the rest before it. Inside one gap, the letters
deleted from the two words can be matched up by substitutions and the
surplus inserted, so the words are at most the sum, over the gaps, of
the larger of the two counts apart.

For two words that share a rest, with c and d deleted letters, that sum
is at most two in these cases:

- c + d ≤ 2;
- c = 2 and d = 1, with the single gap one of the two gaps;
- c = d = 2, with the same two gaps.

Each word gives at most 1 + 15 + 105 = 121 keys: the rest, packed into
an integer with 5 bits per letter (Python takes its bytes), the word number, the number of deleted
letters and their gaps. One word never gives the same gaps twice. After
sorting, each group of equal rests is checked: if the
rest is itself a word, everybody in the group is close to it; two words
that each lost one letter are close; a word that lost two letters is
close to a word that lost two in the same gaps or one in one of its
gaps. With 5-bit packing, a rest takes up to 75 bits, so C++ and Rust use
128-bit keys, Go uses two 64-bit fields, and Java replaces the first 12
letters by their rank among all heads. `O(K·L²·(L + log(K·L)))` with L ≤ 15.

Pitfalls:

- sharing a rest is not enough: abcde and bcdxy both give bcd after
  two deletions, but in different gaps, and they are three edits apart
  (test 05);
- a swap of two neighbouring letters is two edits (test 03);
- lengths that differ by three or more never match (test 07);
- the answer can be empty; print 0 (tests 02, 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1532_hashing.cpp](1532_hashing.cpp) | G++ 13.2 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.109 s | 17484 KB |
| [1532_hashing.go](1532_hashing.go) | Go 1.14 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.375 s | 35180 KB |
| [1532_hashing.java](1532_hashing.java) | Java 1.8 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.421 s | 27344 KB |
| [1532_hashing.py](1532_hashing.py) | Python 3.12 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 1.953 s | 39528 KB |
| [1532_hashing.rs](1532_hashing.rs) | Rust 1.75 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.093 s | 17732 KB |
