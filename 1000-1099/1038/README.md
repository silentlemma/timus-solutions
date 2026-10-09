# 1038. Counting capitalisation errors

[Timus 1038](https://acm.timus.ru/problem.aspx?space=1&num=1038) · difficulty 487 · implementation

Original problem by Alexander Galperin, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of at most 10000 characters consists of Latin letters, digits,
the punctuation marks `. , ; : - ! ?` and whitespace. A word is a maximal
run of letters; any other character, a line break included, ends it. A
sentence ends at `.`, `?` or `!`; the text starts a sentence too. Count the
errors of two kinds:

- the first letter of a sentence is lowercase;
- a capital letter is not the first letter of its word (each such letter
  is a separate error).

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The text, possibly on several lines.

## Output

The number of errors.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
This sentence iz correkt! -It Has,No mista;.Kes et oll.
But there are two BIG mistakes in this one!
and here is one more.
```

Output:

```
3
```

### Example 2

Input:

```
hello. World? yes!
OK, fine.
```

Output:

```
3
```

## Solution

One pass over the characters with two flags:

- `new_sentence` — no letter has been seen since the start of the text or
  since the last `.`, `?`, `!`;
- `in_word` — the previous character was a letter.

For a letter: if it is lowercase and `new_sentence` is set, it is an error
of the first kind; if it is uppercase and `in_word` is set, it is an error
of the second kind. Then `new_sentence` is cleared and `in_word` set. Any
other character clears `in_word`, and a sentence end sets `new_sentence`.
`O(L)` for a text of length `L`.

Pitfalls:

- the first letter of a sentence need not start the sentence: digits,
  spaces or other punctuation may come before it (`2nd place.` has an
  error at `n`);
- a digit is not a letter, so `3Rd` is a word `Rd` that starts with a
  capital — no error;
- the whole input is the text: read it to the end, line breaks included.

## Language notes

- All languages read the whole input byte by byte (or as one string) and
  run the same two-flag scan.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1038_implementation.cpp](1038_implementation.cpp) | G++ 13.2 x64 | implementation | O(L) | AC | 0.015 s | 108 KB |
| [1038_implementation.go](1038_implementation.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.031 s | 1052 KB |
| [1038_implementation.java](1038_implementation.java) | Java 1.8 | implementation | O(L) | AC | 0.109 s | 392 KB |
| [1038_implementation.py](1038_implementation.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.109 s | 364 KB |
| [1038_implementation.rs](1038_implementation.rs) | Rust 1.75 x64 | implementation | O(L) | AC | 0.031 s | 252 KB |
