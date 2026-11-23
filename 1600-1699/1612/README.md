# 1612. Tram Forum

[Timus 1612](https://acm.timus.ru/problem.aspx?space=1&num=1612) · difficulty 152 · strings

Original problem by Alexander Ipatov, prepared by Denis Musin, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A forum message of at most 10000 characters, small Latin letters,
spaces, line breaks and the marks `. , - : ! ?`, is written by a tram
driver if the word `tram` occurs in it more often than `trolleybus`, by
a trolleybus driver if the other way round, and by a bus driver
otherwise. Words are runs of letters. Who wrote it?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The message.

## Output

`Tram driver`, `Trolleybus driver` or `Bus driver`.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
of course, tram is the best transport
in the world!
```

Output:

```
Tram driver
```

### Example 2

Input:

```
yes, yekaterinburg trams are the
best trams in the world, but
i like my trolleybus too.
```

Output:

```
Trolleybus driver
```

### Example 3

Input:

```
read forum.tr.ru every day!
you can learn much about tram 
drivers and trolleybus drivers.
```

Output:

```
Bus driver
```

## Solution

Split the message into words at every character that is not a letter,
count the words equal to `tram` and to `trolleybus`, and compare the
two counts: `O(n)`. The answers were compared with an independent
implementation on generated messages.

Pitfalls:

- only whole words count: `trams`, `tramway` or the `tr` in
  `forum.tr.ru` are not the word `tram` (examples 2 and 3);
- marks also separate words, so `tram-tram` holds two trams and
  `tram,trolleybus` one of each (tests 06 and 07);
- equal counts, zero included, mean a bus driver.

## Optimized solutions

`1612_strings_optimized.go`. Recognize tram and trolleybus using two streaming word states. Only lowercase ASCII letters form a word; separators and EOF finalize it. Avoid the full input string and FieldsFunc token list, retaining the same whole-word semantics. O(I) time for I input bytes and constant auxiliary storage. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1612_strings.go`: time 0.031 s → 0.015 s; memory 1124 KB → 296 KB.

The optimized C++ solution collects a word in a fixed `char` array of
11 bytes instead of a `std::string`: only words of at most 10 letters,
the length of `trolleybus`, can match, so letters after the tenth are
only counted, not stored. It tests letters with a range check instead of
`islower`: {1612_strings_optimized.cpp}.

The optimized Java solution reads the bytes from a 4 KB buffer instead
of collecting the whole message in a `StringBuilder` and splitting it
with a regular expression. For the current word it only keeps its length
and whether it is still a prefix of `tram` and of `trolleybus`, so no
word is ever stored: {1612_strings_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1612_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +56.41%; base: `1612_strings.cpp`.

- `1612_strings_optimized.java`: time reduction +14.68%; memory
  reduction +51.90%; base: `1612_strings.java`.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1612_strings_optimized.py`. Use a byte translation table to separate ASCII words instead of regular expressions, preserving the original word boundaries. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328576 (Python 3.12 x64): **0.078 s / 732 KB**. Archived comparison: `1612_strings.py` (Python 3.12 x64) — 0.093 s / 444 KB (#11288253).

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1612_strings.go](1612_strings.go).
- [1612_strings.rs](1612_strings.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1612_strings.cpp](1612_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 156 KB | 11288250 |
| [1612_strings.go](1612_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1124 KB | 11288251 |
| [1612_strings.java](1612_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 840 KB | 11288255 |
| [1612_strings.py](1612_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 444 KB | 11288253 |
| [1612_strings.rs](1612_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 232 KB | 11288257 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1612_strings_optimized.cpp](1612_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 68 KB | 11305846 |
| [1612_strings_optimized.java](1612_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 404 KB | 11305849 |
| [1612_strings_optimized.go](1612_strings_optimized.go) | Go 1.14 x64 | strings | O(I) time; O(1) space | AC | 0.015 s | 296 KB | 11328278 |
| [1612_strings_optimized.py](1612_strings_optimized.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 732 KB | 11328576 |
