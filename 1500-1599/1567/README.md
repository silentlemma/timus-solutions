# 1567. SMS-spam

[Timus 1567](https://acm.timus.ru/problem.aspx?space=1&num=1567) · difficulty 41 · implementation

Original problem by Denis Musin, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya types a slogan of at most 1000 characters on a phone without
predictive input and charges one rouble per key press. A character
costs as many presses as its place on its key:

| key | characters |
|-----|------------|
| 1 | a b c |
| 2 | d e f |
| 3 | g h i |
| 4 | j k l |
| 5 | m n o |
| 6 | p q r |
| 7 | s t u |
| 8 | v w x |
| 9 | y z |
| 0 | . , ! |
| # | space |

The slogan holds lowercase words, spaces, commas, points and
exclamation marks. Print its price.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The slogan on one line.

## Output

The number of presses.

## Examples

### Example 1

Input:

```
pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi!
```

Output:

```
114
```

## Solution

A table maps every character to its place on its key, counted from 1,
and the answer is the sum over the line. The line is read whole, since
spaces cost a press too. `O(n)`.

Pitfalls:

- the key 9 holds only y and z, so z costs 2 (test 03);
- the space is a character of its own on the key #, one press each,
  also when two spaces stand together (test 05);
- reading word by word loses the spaces.

## Optimized solutions

`1567_implementation_optimized.py`. Derive a 256-byte weight map at startup from the keypad groups in the statement: position in a group is the number of presses. One native bytes.translate pass maps the line to press counts, then native sum adds them, replacing repeated full-line counts. CR/LF map to zero; the allowed letters, punctuation and space retain their exact weights. This is a rule-derived character map, not a precomputed answer table. O(L+256) time/space with an O(L) translated temporary; flush before direct exit. The readable per-character source remains.

Exact-source CPython 3.12 Accepted #11327006: 0.046 s / 604 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 1/167, memory rank 129/167. Below 1024 KB, strict admission uses time only.

- `1567_implementation_optimized.py`: 0.046 s / 604 KB; retained teaching base `1567_implementation.py` (Python 3.12 x64): 0.078 s / 380 KB; time change -41.0%; memory change +58.9%.

The optimized C++ solution turns the keys into a table of 256 entries
that gives the number of presses for every byte, so each character is
looked up once instead of searching all the keys, and reads the line
with `getchar` instead of `getline`: 100 KB instead of 376 KB, with the
same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1567_implementation.cpp](1567_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 376 KB | 11287740 |
| [1567_implementation.go](1567_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1048 KB | 11287743 |
| [1567_implementation.java](1567_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 424 KB | 11287747 |
| [1567_implementation.py](1567_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 380 KB | 11287745 |
| [1567_implementation.rs](1567_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 224 KB | 11287750 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1567_implementation_optimized.cpp](1567_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303623 |
| [1567_implementation_optimized.py](1567_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n) | AC | 0.046 s | 604 KB | 11327006 |

\* The marked solutions can improve their target rankings.
