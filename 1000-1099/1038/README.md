# 1038. Counting capitalisation errors

[Timus 1038](https://acm.timus.ru/problem.aspx?space=1&num=1038) · difficulty 489 · implementation

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

## Optimized solutions

Go/Python preserve the two-flag scan but read bounded 4096-byte chunks instead of retaining the text. Flags persist between chunks, so a split word or pending sentence is handled exactly. Go classifies ASCII letters directly. Python translates each chunk through a 256-byte alphabet-class table and scans the resulting small integer classes; the table describes ASCII, not problem answers. Digits and whitespace end words but only .?! start a new sentence. Time O(L), fixed auxiliary storage; actual judge metrics decide admission, especially for Python where startup can dominate. All simple files remain; C++, Java and Rust reuse their admitted bases.

The accepted Python 3.12 x64 run takes 0.078 s versus 0.109 s for the base and uses 496 KB versus 364 KB.

The accepted base implementations [1038_implementation.cpp](1038_implementation.cpp), [1038_implementation.java](1038_implementation.java), [1038_implementation.rs](1038_implementation.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1038_implementation_parsing_optimized.rs`. Count capitalization errors while consuming native input blocks, carrying only sentence and word state across refills. The original ASCII letter and punctuation rules are unchanged; the full text is not stored. Specialize direct output to the answer types actually used, avoiding generic formatting dispatch and temporary answer strings. Fixed text uses native writes; numeric writers handle the required signed or unsigned magnitudes exactly. Mathematical decisions and archived simple versions are preserved.

Accepted #11329194 (Rust 1.75 x64): **0.015 s / 60 KB**. Archived comparison: `1038_implementation.rs` (Rust 1.75 x64) — 0.031 s / 252 KB (#11278496).

## Language notes

These notes describe the simple implementations.

- All languages read the whole input byte by byte (or as one string) and
  run the same two-flag scan.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1038_implementation.cpp](1038_implementation.cpp) | G++ 13.2 x64 | implementation | O(L) | AC | 0.015 s | 108 KB | 11278488 |
| [1038_implementation.go](1038_implementation.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.031 s | 1052 KB | 11278490 |
| [1038_implementation.java](1038_implementation.java) | Java 1.8 | implementation | O(L) | AC | 0.109 s | 392 KB | 11278493 |
| [1038_implementation.py](1038_implementation.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.109 s | 364 KB | 11278492 |
| [1038_implementation.rs](1038_implementation.rs) | Rust 1.75 x64 | implementation | O(L) | AC | 0.031 s | 252 KB | 11278496 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1038_implementation_optimized.go](1038_implementation_optimized.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.015 s | 292 KB | 11315352 |
| [1038_implementation_optimized.py](1038_implementation_optimized.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.078 s | 496 KB | 11315358 |
| [1038_implementation_parsing_optimized.rs](1038_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(text length) time; O(1) state + bounded I/O buffers | AC | 0.015 s | 60 KB | 11329194 |
