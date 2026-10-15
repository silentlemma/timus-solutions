# 1732. Ministry of Truth

[Timus 1732](https://acm.timus.ru/problem.aspx?space=1&num=1732) · difficulty 458 · strings

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1732_strings.cpp](1732_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.046 s | 2676 KB |
| [1732_strings.go](1732_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 3296 KB |
| [1732_strings.java](1732_strings.java) | Java 1.8 | strings | O(L) | AC | 0.156 s | 6484 KB |
| [1732_strings.py](1732_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.156 s | 6320 KB |
| [1732_strings.rs](1732_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.031 s | 2184 KB |
