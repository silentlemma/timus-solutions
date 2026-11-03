# 1179. The base in which a text contains the most numbers

[Timus 1179](https://acm.timus.ru/problem.aspx?space=1&num=1179) · difficulty 295 · strings

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of up to 1 MB consists of digits, capital Latin letters, spaces and
line breaks; letters are digits from `A = 10` to `Z = 35`. In base `K`, a
number is a maximal run of characters that are digits of base `K`. Find
the base `K` from 2 to 36 in which the text has the most numbers, the
smallest such base on a tie, and that count.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The text.

## Output

`K` and the number of numbers.

## Checking

Compare the two integer tokens. All seven new sources have 13 repository and 159 additional saved target executions each, including chunk boundaries and maximum-size texts. Each Python source additionally has 62403 host executions against an independent regular-expression run counter: all 37-value pairs/triples, short exhaustive texts and random whitespace. Those Python counts are not native execution totals.

## Examples

### Example 1

Input:

```
01234B56789
AZA
```

Output:

```
11 4
```

## Solution

Try each base `k=2..36` separately. Scan the text, remembering whether
the previous character was a digit in that base. A number starts exactly
at a digit preceded by a separator. This counts each maximal run once,
including a run starting at the first character. Keep the first base with
the maximum count to resolve ties toward the smaller base. Time is
`O(35L)` and storage `O(L)` for the saved text.

Python performs the same scan through native byte operations: prepend a
separator, translate characters to zero (separator) or one (digit), then
count `01`. This two-byte pattern cannot overlap itself. Extend the digit
table as the base grows. Empty input or text with no digits gives `2 0`.
Line endings and spaces separate runs; `Z` becomes a digit in base 36.

## Optimized solutions

Give a separator value 36 and imagine one before the text. A pair of
adjacent values `(left,right)` starts a number in base `k` exactly when
`right<k≤left`. If `right<left`, this is the interval
`max(2,right+1)..left`. Accumulate interval endpoints in a difference array,
then take prefix sums over the 35 bases. Each run has exactly one starting
pair, proving the count. The retained native implementations first count
the 37×37 pairs; the new Java/Python implementations add events directly
while reading bounded chunks and carry the last value between chunks.
Time is `O(L+37²)` for the pair-table native versions and `O(L+36)` for the
streamed versions; streamed storage is bounded by the input block and small
tables, independent of L.

The retained Python pair counter maps the whole text and performs a fixed
number of C-level byte-pattern counts: `O(37²L)` time, not `O(L+37²)` when
the alphabet size is explicit, and `O(L)` memory. It remains an Accepted
alternative without an optimized label against the new teaching base.
Java's old and new event versions both qualify against the direct base;
the new version's 29.93% memory reduction against the old Java alone is
not rounded up to 30%.

- `1179_strings.cpp`: 0.031 s / 116 KB; base `1179_bruteforce_strings.cpp`: 0.171 s / 2836 KB; relative change: time -81.9%, memory -95.9%.
- `1179_strings.go`: 0.015 s / 3160 KB; base `1179_bruteforce_strings.go`: 0.203 s / 3136 KB; relative change: time -92.6%, memory +0.8%.
- `1179_strings.java`: 0.125 s / 588 KB; base `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; relative change: time -69.2%, memory -83.0%.
- `1179_strings_optimized.py`: 0.203 s / 396 KB; base `1179_bruteforce_strings.py`: 0.218 s / 3128 KB; relative change: time -6.9%, memory -87.3%.
- `1179_strings_optimized.java`: 0.109 s / 412 KB; base `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; relative change: time -73.2%, memory -88.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1179_bruteforce_strings.cpp`; covering source `1179_strings.cpp`; time/memory places 4/2, other-author entries 44/44.

- Go: preferred teaching base `1179_bruteforce_strings.go`; covering source `1179_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1179_bruteforce_strings.java`; covering source `1179_strings.java`; time/memory places 2/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1179_bruteforce_strings.py`; covering source `1179_strings_optimized.py`; time/memory places 1/1, other-author entries 5/5.

- Rust: preferred teaching base `1179_bruteforce_strings.rs`; covering source `1179_bruteforce_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1179_bruteforce_strings.cpp](1179_bruteforce_strings.cpp) | G++ 13.2 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.171 s | 2836 KB | 11309345 |
| [1179_bruteforce_strings.go](1179_bruteforce_strings.go) | Go 1.14 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.203 s | 3136 KB | 11309346 |
| [1179_bruteforce_strings.java](1179_bruteforce_strings.java) | Java 1.8 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.406 s | 3464 KB | 11309350 |
| [1179_bruteforce_strings.py](1179_bruteforce_strings.py) | Python 3.12 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.218 s | 3128 KB | 11309344 |
| [1179_bruteforce_strings.rs](1179_bruteforce_strings.rs) | Rust 1.75 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.031 s | 2128 KB | 11309349 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1179_strings.py](1179_strings.py) | Python 3.12 x64 | strings | O(37^2 L) time; O(L) space | AC | 0.640 s | 3100 KB | 11283287 |
| [1179_strings.rs](1179_strings.rs) | Rust 1.75 x64 | strings | O(L+37^2) time | AC | 0.015 s | 2124 KB | 11283294 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1179_strings.cpp](1179_strings.cpp) | G++ 13.2 x64 | strings | O(L+37^2) time | AC | 0.031 s | 116 KB | 11283281 |
| [1179_strings.go](1179_strings.go) | Go 1.14 x64 | strings | O(L+37^2) time | AC | 0.015 s | 3160 KB | 11283283 |
| [1179_strings.java](1179_strings.java) \* | Java 1.8 | strings | O(L+37^2) time | AC | 0.125 s | 588 KB | 11283292 |
| [1179_strings_optimized.py](1179_strings_optimized.py) | Python 3.12 x64 | strings | O(L+36) time; bounded block/table space | AC | 0.203 s | 396 KB | 11309351 |
| [1179_strings_optimized.java](1179_strings_optimized.java) \* | Java 1.8 | strings | O(L+36) time; bounded block/table space | AC | 0.109 s | 412 KB | 11309353 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
