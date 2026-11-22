# 1723. Sandro's Book

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · difficulty 62 · strings

Original problem by Ivan Burmistrov (prepared by Olga Soboleva), from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every substring of a given word is a spell, and its strength is the
number of times it occurs in the word, overlaps included. Print a
strongest spell.

## Input

A nonempty word of at most 50 lowercase Latin letters.

## Output

Any strongest spell.

## Examples

### Example 1

Input:

```
tebidohtebidoh
```

Output:

```
tebidoh
```

## Solution

Each occurrence of a spell begins with an occurrence of its first
letter, and different occurrences begin at different places. So no
spell is stronger than its first letter alone, and a most frequent
letter is a strongest spell. `O(n)`.

In the example every letter occurs twice, so `t` is as strong as
`tebidoh`.

Pitfalls:

- occurrences may overlap: `aba` occurs three times in `abababa`, but
  `a` occurs four times;
- any strongest spell is accepted, so the tests use a checker.

The checker counts the occurrences of the answer, overlaps included,
and compares them with the expected answer's. A most frequent letter
matches an exhaustive search over all substrings on 300 random words.

## Optimized solutions

`1723_strings_optimized.java`. Keep counting the 26 lowercase letters and returning any most frequent letter, which is also a strongest spell. The entire word has at most fifty letters, so signed byte counters cannot overflow. Update the current maximum during the input scan; write the answer letter and newline as two bytes. No stored word, Scanner or final count scan. O(N) time and 26 byte counters plus constant state; a different equally frequent letter is valid.

Exact-source Java 1.8 Accepted #11327830: 0.109 s / 308 KB. Saved 2026-11-20 compiler-cohort comparison: time 36/246, memory 1/246. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303774 was 0.14 s / 348 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1723_strings_optimized.java`: 0.109 s / 308 KB; retained teaching base `1723_strings.java`: 0.125 s / 1556 KB.

The optimized C++ solution counts the letters as they are read with
`getchar`, without storing the string: 84 KB instead of 352 KB.

Count occurrences of each lowercase letter with the built-in byte count and keep the first maximum. Accepted submission 11302183 took 0.078 s and used 392 KB. The simple version took 0.078 s and used 404 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 352 KB | 11303504 |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB | 11289348 |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1556 KB | 11303505 |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB | 11289349 |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB | 11289353 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1723_strings_optimized.cpp](1723_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 84 KB | 11303635 |
| [1723_strings_optimized.java](1723_strings_optimized.java) \* | Java 1.8 | strings | O(N) time; 26 byte counters | AC | 0.109 s | 308 KB | 11327830 |
| [1723_strings_optimized.py](1723_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 392 KB | 11302183 |

\* Accepted; the separate rating target is not yet met: C++ requires top ten or top 15% in both time and memory, and the other language families require first place in both. This marker is separate from the admission criteria; the version may be optimized further.
