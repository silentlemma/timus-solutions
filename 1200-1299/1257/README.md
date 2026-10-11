# 1257. Hyphenation

[Timus 1257](https://acm.timus.ru/problem.aspx?space=1&num=1257) · difficulty 1740 · implementation

Original problem by Den Raskovalov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Lay out a text on a page 40 characters wide using hyphenation rules.
A word is a run of Latin letters; every other character separates
words. A rule `s1-s2` (up to 100 rules, |s1| + |s2| ≤ 40) says that a
word ending in s1s2, in any letter case, may be broken before s2: the
head goes on the current line followed by `-`, and s2 starts the next
line. No output line may be longer than 40 characters, counting the
`-`. When several rules apply, the one carrying the fewest letters over
wins; when none fits, the whole word moves to the next line. Spaces,
punctuation and the line breaks already in the text are kept.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N rules, one per line, then the text: at most 450 lines of at
most 250 characters, words at most 40 letters long.

## Output

The laid-out text.

## Examples

### Example 1

Input:

```
12
un-usual
for-ced
re-al
sum-mer
N-ED
home-work
sec-ret
ho-lidays
Wi-zard
th-Er
L-so
Holi-days
Harry Potter was a highly unusual boy in many ways. 
For one thing, he hated the summer holidays more than any 
other time of year. For another, he really 
 wanted to do his homework but was forced to do it in 
secret, in the dead of night. And he also happened 
to be a wizard.
```

Output:

```
Harry Potter was a highly unusual boy in
 many ways. 
For one thing, he hated the summer holi-
days more than any 
other time of year. For another, he 
really 
 wanted to do his homework but was for-
ced to do it in 
secret, in the dead of night. And he al-
so happened 
to be a wizard.
```

## Solution

Walk through the text keeping the current column:

- a line break is copied and resets the column;
- any other separator is copied, but if the line already holds 40
  characters a line break goes first;
- a word that fits is copied;
- otherwise, among the rules whose s1s2 ends the word (compared in
  lower case) and whose head plus `-` still fits, take the one with the
  shortest s2: print the head, `-`, a line break and s2; with no such
  rule, print a line break and the word.

Every word is at most 40 letters, so it always fits on a fresh line.
`O(L · N · 40)` for a text of L characters.

Pitfalls:

- separators carry over too: a space after a full line starts the next
  one (in the example, ` many ways.`), and so do dots (test 02);
- a line break in the input right after a full line is the only break
  there, not a second one (tests 03, 10);
- the text may end without a line break (test 04);
- a rule must match the end of the word, not the first place where its
  letters occur (test 05);
- rules ignore case (test 06), and the shortest carried part counts only
  among the rules whose head fits (tests 07, 12);
- a rule that carries one letter never applies: its head with the `-` is
  as long as the whole word, which would have fitted.

The solutions were compared with an independent implementation on 450
random texts.

## Language notes

- All languages read the input as bytes, drop `\r` and walk the text
  once.
- Java decodes and prints the bytes as ISO-8859-1, so every byte stays
  one character.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1257_implementation.cpp](1257_implementation.cpp) | G++ 13.2 x64 | implementation | O(L · N · 40) | AC | 0.046 s | 768 KB |
| [1257_implementation.go](1257_implementation.go) | Go 1.14 x64 | implementation | O(L · N · 40) | AC | 0.031 s | 1876 KB |
| [1257_implementation.java](1257_implementation.java) | Java 1.8 | implementation | O(L · N · 40) | AC | 0.156 s | 5152 KB |
| [1257_implementation.py](1257_implementation.py) | Python 3.12 x64 | implementation | O(L · N · 40) | AC | 0.140 s | 1740 KB |
| [1257_implementation.rs](1257_implementation.rs) | Rust 1.75 x64 | implementation | O(L · N · 40) | AC | 0.015 s | 600 KB |
