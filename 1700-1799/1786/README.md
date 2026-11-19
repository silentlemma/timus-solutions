# 1786. Sandro's Biography

[Timus 1786](https://acm.timus.ru/problem.aspx?space=1&num=1786) · difficulty 110 · strings

Original problem by Olga Soboleva, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of Latin letters must be changed so that it contains the word
"Sandro". Replacing a letter by another letter of the same case costs
5 coins, and so does changing the case of a letter. Find the smallest
cost.

## Input

The text, from 6 to 200 letters.

## Output

The smallest number of coins.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
MyNameIsAlexander
```

Output:

```
20
```

## Solution

Try every place for the six letters of the name. A letter costs 5 if
its case is wrong and 5 more if it is the wrong letter, so a letter
that is wrong in both ways costs 10. Sum the six costs at each place
and take the smallest sum. The scan takes `O(n)` time, but Python copies
the suffix `text[start:]` at each place, so that implementation takes
`O(n^2)` time. All implementations use `O(n)` memory including the input;
the maximum input length is only 200.

In the example the best place is "xander": x needs a new letter and an
uppercase, 10, while e → r and r → o cost 5 each, 20 in all.

Pitfalls:

- a wrong letter of the wrong case costs both fees;
- test 03, `sANDRO`, has all six cases wrong, so it costs 30;
- the name may start at the very first or end at the very last letter.

The Python answers agree with an independent operation-graph oracle on
2,000 random small texts, 592 directed cases, all 8 stored tests and 64
generated cases.

## Optimized solutions

`1786_strings_optimized.py`. Keep the cost of changing each ASCII letter and its case to the six letters of Sandro. Build one 256-byte translation table per target position and translate the whole text into six aligned cost streams; then sum each six-cost column. This removes repeated text[start:] suffix copies, which made the simple implementation quadratic in copied characters, as well as per-letter Python cost calls. Time becomes O(L) for the fixed six-letter target, with O(L) cost-stream storage; memory is not constant. There is no forced interpreter exit in this variant. Ranking admits the own Accepted result even without a 30% measurement gain.

Compared with `1786_strings.py`: time 0.109 s → 0.078 s; memory 408 KB → 400 KB.

The optimized C++ solution reads the text with `scanf` into a buffer of
201 bytes, enough for 200 letters and the terminating zero, instead of
`std::cin` and `std::string`, and since the text has only Latin letters
it tells the case by comparing with `'Z'` and lowers a letter by adding
`'a' − 'A'` instead of calling `isupper` and `tolower`:
{1786_strings_optimized.cpp}.

The optimized Java solution reads the text character by character
straight from `System.in` instead of creating a `Scanner`, and since the
text has only Latin letters it tells the case by comparing with `'Z'`
and lowers a letter by adding `'a' − 'A'` instead of calling
`Character.isUpperCase` and `Character.toLowerCase`:
{1786_strings_optimized.java}.

### Measured gains

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1786_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +68.42%; base: `1786_strings.cpp`.

- `1786_strings_optimized.java`: time reduction +28.44%; memory
  reduction +75.13%; base: `1786_strings.java`.

`1786_strings_optimized.rs`. Keep only the last six letters in a ring. For each complete window, sum the independent costs of changing case and changing the letter ignoring case to match Sandro. Six comparisons per position give O(N) time and O(1) auxiliary space without retaining the text or allocating slices. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1786_strings.rs`: time 0.031 s → 0.062 s; memory 216 KB → 64 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1786_strings_optimized.py`: time place 2/32, memory place 7/32 in this comparable sample.

`1786_strings_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings.cpp](1786_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 380 KB | 11304047 |
| [1786_strings.go](1786_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1088 KB | 11289804 |
| [1786_strings.java](1786_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1576 KB | 11304048 |
| [1786_strings.py](1786_strings.py) | Python 3.12 x64 | strings | O(n^2) | AC | 0.109 s | 408 KB | 11304049 |
| [1786_strings.rs](1786_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 216 KB | 11289809 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1786_strings_optimized.cpp](1786_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 120 KB | 11304276 |
| [1786_strings_optimized.java](1786_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.078 s | 392 KB | 11304277 |
| [1786_strings_optimized.rs](1786_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(N) | AC | 0.062 s | 64 KB | 11325109 |
| [1786_strings_optimized.py](1786_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L) time; O(L) space | AC | 0.078 s | 400 KB | 11325470 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
