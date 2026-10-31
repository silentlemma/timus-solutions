# 1354. Palindrome. Again Palindrome

[Timus 1354](https://acm.timus.ru/problem.aspx?space=1&num=1354) · difficulty 138 · strings

Original problem by Denis Nazarov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a word S1 of up to 10 000 Latin letters, find the shortest
non-empty word S2 such that S1S2 is a palindrome, and print S1S2.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The word S1 on one line.

## Output

The word S1S2.

## Examples

### Example 1

Input:

```
No
```

Output:

```
NoN
```

### Example 2

Input:

```
OnLine
```

Output:

```
OnLineniLnO
```

### Example 3

Input:

```
AbabaAab
```

Output:

```
AbabaAababA
```

## Solution

If S1S2 is a palindrome and S2 is no longer than S1, then S2 is the
reverse of some prefix of S1, and the rest of S1 after that prefix must
itself be a palindrome. So the shortest S2 comes from the longest
palindromic suffix of S1 that starts at position 1 or later: S2 has to
be non-empty, so S1 itself never counts, even if it is a palindrome.

A suffix X of the tail T = S1 without its first letter is a palindrome
exactly when X is also a prefix of reverse(T). Running the prefix
function over reverse(T) + `#` + T, its last value is the length L of
the longest such suffix, and the answer is S1 followed by the first
|S1| − L letters of S1 reversed. `O(|S1|)`.

Pitfalls:

- a palindrome still needs a letter: `abcba` gives `abcbabcba`
  (test 05);
- one letter is doubled, since the empty tail counts as a palindrome
  (test 04);
- upper and lower case are different letters (tests 03 and 07);
- checking every suffix directly can take 10⁸ steps on long runs of one
  letter (generated test 4).

The answers were compared with trying every prefix length directly on
300 random words of up to 12 letters, and the generated tests were
checked for being palindromes with no shorter addition.

## Optimized solutions

The optimized C++ solution never builds the string reverse(T) + `#` + T
of about 2·|S1| letters. It computes the prefix function of reverse(S1)
alone, reading the letters through reversed indices of S1, and then runs
the matching phase of Knuth–Morris–Pratt with T as the text: the length
matched after the last letter is L. The table takes `unsigned short`,
two bytes per entry, since a matched length is at most 9999 for a word
of at most 10 000 letters. Instead of `iostream`, the word is read with
`scanf` into a fixed array and printed with `fputs`, and the added
letters go out one by one with `putchar`: {1354_strings_optimized.cpp}.

The optimized Go solution never builds the string reverse(T) + `#` + T
of about 2·|S1| letters. It computes the prefix function of reverse(S1)
alone, reading the letters through reversed indices of S1, and then runs
the matching phase of Knuth–Morris–Pratt with T as the text: the length
matched after the last letter is L. The table takes `uint16`, two bytes
per entry, since a matched length is at most 9999 for a word of at most
10 000 letters, and the answer is written through a `bufio.Writer`
without building it as a string: {1354_strings_optimized.go}.

The optimized Java solution never builds the string reverse(T) + `#` + T
of about 2·|S1| letters. It computes the prefix function of reverse(S1)
alone, reading the letters through reversed indices of S1, and then runs
the matching phase of Knuth–Morris–Pratt with T as the text: the length
matched after the last letter is L. The table is a `char[]`, two bytes
per entry, since a matched length is at most 9999 for a word of at most
10 000 letters, and the answer is written through a `BufferedWriter`
without building it as a string: {1354_strings_optimized.java}.

The optimized Python solution never builds the string reverse(T) + `#` +
T of about 2·|S1| letters. It computes the prefix function of
reverse(S1) alone and then runs the matching phase of Knuth–Morris–Pratt
with T as the text: the length matched after the last letter is L. It
works on `bytes`, and the table is an `array("H")` of two-byte entries
instead of a list of integer objects, since a matched length is at most
9999 for a word of at most 10 000 letters: {1354_strings_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1354_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +67.68%; base: `1354_strings.cpp`.

- `1354_strings_optimized.go`: time reduction +0.00%; memory reduction
  +37.66%; base: `1354_strings.go`.

- `1354_strings_optimized.java`: time reduction +26.90%; memory
  reduction +30.42%; base: `1354_strings.java`.

- `1354_strings_optimized.py`: time reduction +0.00%; memory reduction
  +57.57%; base: `1354_strings.py`.

## Language notes

- All five solutions use the same prefix function on bytes or
  characters.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1354_strings.cpp](1354_strings.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 396 KB | 11285248 |
| [1354_strings.go](1354_strings.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 1540 KB | 11285253 |
| [1354_strings.java](1354_strings.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.171 s | 960 KB | 11285261 |
| [1354_strings.py](1354_strings.py) | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 1216 KB | 11285257 |
| [1354_strings.rs](1354_strings.rs) | Rust 1.75 x64 | strings | O(len(S1)) | AC | 0.031 s | 336 KB | 11285267 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1354_strings_optimized.cpp](1354_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 128 KB | 11304449 |
| [1354_strings_optimized.go](1354_strings_optimized.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 960 KB | 11304450 |
| [1354_strings_optimized.java](1354_strings_optimized.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.125 s | 668 KB | 11304452 |
| [1354_strings_optimized.py](1354_strings_optimized.py) \* | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 516 KB | 11304453 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
