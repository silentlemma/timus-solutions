# 1732. Ministry of Truth

[Timus 1732](https://acm.timus.ru/problem.aspx?space=1&num=1732) · difficulty 558 · strings

Original problem by Alex Samsonov (prepared by Dmitry Ivankov), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Erase some letters of a saying, each erased letter turning into a
space, so that it reads as another given saying once runs of spaces
are squeezed into one and the ends are trimmed. Show which letters to
erase.

## Input

The source saying and the wanted one, each up to 100 000 characters:
words of Latin letters separated by single spaces. The two differ.

## Output

The source with the erased letters replaced by `_`, or
`I HAVE FAILED!!!` if it cannot be done. Any fitting answer is
accepted.

## Examples

### Example 1

Input:

```
Preved to Medved
Preved Me
```

Output:

```
Preved __ Me____
```

### Example 2

Input:

```
this is impossible
im possible
```

Output:

```
I HAVE FAILED!!!
```

## Solution

Each wanted word must be a run of letters inside one source word, and
two wanted words inside the same source word need at least one erased
letter between them. Spaces of the source cannot be removed, so a
wanted word never spans two source words.

Go through the source words in order and place the wanted words
greedily: each one at its earliest occurrence in the current word, at
least two positions after the end of the previous one there. If it
does not occur in what is left of the word, move on to the next word.
An earliest placement leaves the most room for what follows, so if the
greedy runs out of source words, nothing can work. Every letter not
kept becomes `_`.

Searching with a library `find` can be quadratic, for example a word of
100 000 a's against a wanted word of a's ending in b. The search runs
on the prefix function of the current wanted word instead, which is
rebuilt only when that word changes, and every search starts where the
last one stopped, so each source letter is scanned once. `O(L)`.

In the first example `Preved` keeps itself, `to` is erased, and `Me`
is the start of `Medved`.

Pitfalls:

- `abab` cannot become `ab ab`: the space has to come from an erased
  letter, and for the same reason `impossible` cannot give
  `im possible` in the second example;
- letters are case sensitive;
- a wanted word may not join two source words: `to Me` never gives
  `toMe`.

The checker verifies that only letters became underscores and that the
result reads as the wanted saying. The answers match an exhaustive
search over all erasures on 300 short sayings, and an independent
accepted implementation on long ones.

## Optimized solutions

The Python variant searches the entire byte string using CPython’s substring search. A word
cannot match across an original space. After a match, skipping one byte leaves a separator
before the next match. The output starts with every letter erased, then restores each
matched span. The search advances through the input and the buffer uses O(L) memory.
Submission 11316946 took 0.093 s and 2168 KB versus 0.156 s and 6212 KB for the base.

The C++ variant runs KMP over the full source. An original space breaks any partial word
match. It reuses the prefix table for successive target words and masks each gap directly in
the source string. Both passes together take O(L) time and O(L) memory. Submission 11316951
took 0.031 s and 1000 KB, down from 0.046 s and 2676 KB.

Rust runs KMP over one input byte buffer and erases the gaps in place. It reuses a 32-bit prefix table and writes the resulting slice directly. Submission 11317256 took 0.031 s and used 1096 KB, versus 0.046 s and 2188 KB for the base.

Go also edits the source in place and grows the reusable 32-bit prefix table only when necessary. Submission 11317266 took 0.031 s and used 1836 KB, versus 0.031 s and 3248 KB for the base.

Java uses one byte buffer for both input lines, erases gaps in place, and reuses the KMP prefix table. Submission 11317268 took 0.125 s and used 1036 KB, versus 0.125 s and 6420 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11318250 · Java 1.8 №11318255 · Rust 1.75 x64 №11318260.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1732_strings.cpp](1732_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.046 s | 2660 KB | 11318250 |
| [1732_strings.go](1732_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 3248 KB | 11322033 |
| [1732_strings.java](1732_strings.java) | Java 1.8 | strings | O(L) | AC | 0.125 s | 6420 KB | 11318255 |
| [1732_strings.py](1732_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.156 s | 6212 KB | 11322034 |
| [1732_strings.rs](1732_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.046 s | 2188 KB | 11318260 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1732_strings_optimized.cpp](1732_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.031 s | 1000 KB | 11316951 |
| [1732_strings_optimized.go](1732_strings_optimized.go) \* | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 1836 KB | 11317266 |
| [1732_strings_optimized.java](1732_strings_optimized.java) \* | Java 1.8 | strings | O(L) | AC | 0.125 s | 1036 KB | 11317268 |
| [1732_strings_optimized.py](1732_strings_optimized.py) | Python 3.12 x64 | strings | O(L) | AC | 0.093 s | 2168 KB | 11316946 |
| [1732_strings_optimized.rs](1732_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(L) | AC | 0.031 s | 1096 KB | 11317256 |

\* The saved ratings have no comparable Go or Rust submissions from other authors. Java ranks second by time and first by memory in the saved rating.
