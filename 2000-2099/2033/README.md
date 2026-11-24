# 2033. Selecting a model by frequency and cheapest offer

[Timus 2033](https://acm.timus.ru/problem.aspx?space=1&num=2033) · difficulty 104 · hashing

Original problem by Ilya Kuchumov, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are exactly six purchase records. Each gives a person's name, a
device model and a price. Choose a model occurring in the greatest
number of records. Among models tied in that count, choose one with the
smallest observed price for that model. If both criteria tie, any tied
model is acceptable. Repeated person names still represent separate
records and must all be counted.

Person names contain 1–20 lowercase English letters. Model names contain
1–20 lowercase English letters or digits. Prices are integers from 1 to
`1000000`. Limits: 1 second, 64 MB.

## Input

Exactly six descriptions, each on three lines: person name, model name, price.
There is no leading record count.

## Output

One optimal model name. Preserve the model string, including any leading zeros.

## Checking

A checker accepts any model with the largest count and, among those, the
smallest price.

## Examples

```
oleg
nexus4
13000
kirill
kurtka
20000
den
nexus4
12000
nikita
htc
10000
mikhail
nexus4
14000
alexey
htc
9500
```

```
nexus4
```

## Solution

Use a hash map from the model string to two values: occurrence count and
minimum observed price. For each record, consume the person's name but use
only its model and price. Create a new entry with count zero and the current
price, then increase the count and take the minimum price.

Scan the entries, preferring larger count and, for equal count, smaller price.
The programs choose the lexicographically smaller model if both scores tie,
solely to make their answer deterministic; the task permits all such models.

After any prefix of the input, each map entry equals the number of records
of that model in the prefix and the minimum of their prices. Initialization
and the increment/minimum update preserve this invariant. After six records
the map therefore contains the exact scores. During the final scan, the
current answer is best among visited entries; comparing the two criteria
preserves this property, so the final model is globally optimal.

In the sample, `nexus4` occurs three times with minimum price 12000,
`htc` twice with minimum 9500, and `kurtka` once at 20000. Frequency is
the first criterion, so `nexus4` wins despite a cheaper minority model.

For `k` records, hash-map time is expected `O(k)` and space `O(k)`,
with word length bounded by 20. Here `k=6` is fixed, so actual time and space
are bounded constants. No input larger than six records is assumed.

Pitfalls:

- Count records, not distinct person names.
- Use the minimum price of a model, not its sum, average, last or maximum price.
- Popularity takes priority over price.
- Initialize the first price from its record; a default zero is invalid.
- Treat digit-only model names as strings, preserving leading zeros.

## Optimized solutions

`2033_hashing_optimized.py`. Read byte tokens one line at a time, retaining mutable [count, minimum_price] entries per model rather than record tuples and a full-input token list. Count all six records, including repeated person names, and preserve leading zeros in model names. Select maximum frequency, then minimum price; lexicographic order only resolves an allowed final tie. For I input bytes, M distinct models and maximum input line length Lmax: expected O(I) time and O(M+Lmax) auxiliary storage under the 20-character name limit. The readable record-based hash map remains.

Reused exact historical CPython 3.12 Accepted #11307496: 0.078 s / 500 KB. In the saved 2026-11-20 comparable compiler cohort: time rank 4/61, memory rank 32/61. Below 1024 KB, strict admission uses time only and passes. The asterisk follows the separate language rating target. These are paired measurements of this source, not a new submission or a guaranteed portable speedup. This version uses normal interpreter exit.

- `2033_hashing_optimized.py`: 0.078 s / 500 KB; retained teaching base `2033_hashing.py` (Python 3.12 x64): 0.109 s / 452 KB. Both base time and memory remain documented even where one metric increases.

`2033_implementation.java`. Replace hash-based grouping by a direct scan of at most six model strings in fixed arrays. Count every purchase record, even when person names repeat; retain each model minimum price. Preserve model strings verbatim, including leading zeros, and use lexicographic order only as an allowed tie-break after count and price. The six-record limit makes the total character work O(L) and storage bounded by six model names, without Record objects or HashMap entries. The public filename is implementation, because this source no longer hashes models; the accepted source bytes and original hashing teaching version remain unchanged.

Compared with `2033_hashing.java`: time 0.125 s → 0.109 s; memory 628 KB → 572 KB.

The optimized C++ solution drops the hash map: with only six records it
compares every record with all six, counting the records of the same
model and taking their smallest price, 36 comparisons in all, and keeps
the best record with the same tie-break. The names are read with `scanf`
into fixed arrays of 21 bytes, enough for 20 characters and the
terminating zero, instead of `std::string` and `iostream`:
{2033_bruteforce.cpp}.

The optimized Rust solution drops the hash map: with only six records it
compares every record with all six, counting the records of the same
model and taking their smallest price, 36 comparisons in all, and keeps
the best record with the same tie-break. The six models stay slices of
the input text in a fixed array instead of copies in a `HashMap`:
{2033_bruteforce.rs}.

### Measured gains

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2033_bruteforce.cpp`: time reduction +0.00%; memory reduction
  +67.71%; base: `2033_hashing.cpp`.

- `2033_bruteforce.rs`: time reduction +0.00%; memory reduction +47.71%;
  base: `2033_hashing.rs`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2033_implementation.java`: time place 24/207, memory place 32/207 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2033_hashing.cpp](2033_hashing.cpp) | G++ 13.2 x64 | hashing | O(1) | AC | 0.015 s | 384 KB | 11293121 |
| [2033_hashing.go](2033_hashing.go) | Go 1.14 x64 | hashing | O(1) | AC | 0.031 s | 1116 KB | 11293123 |
| [2033_hashing.java](2033_hashing.java) | Java 1.8 | hashing | O(1) | AC | 0.125 s | 628 KB | 11304031 |
| [2033_hashing.py](2033_hashing.py) | Python 3.12 x64 | hashing | O(1) | AC | 0.109 s | 452 KB | 11293124 |
| [2033_hashing.rs](2033_hashing.rs) | Rust 1.75 x64 | hashing | O(1) | AC | 0.046 s | 436 KB | 11293128 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2033_bruteforce.cpp](2033_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11304029 |
| [2033_bruteforce.rs](2033_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 228 KB | 11304030 |
| [2033_implementation.java](2033_implementation.java) | Java 1.8 | implementation | O(L), six records | AC | 0.109 s | 572 KB | 11325123 |
| [2033_hashing_optimized.py](2033_hashing_optimized.py) | Python 3.12 x64 | hashing | O(I) expected time; O(M+Lmax) space | AC | 0.078 s | 500 KB | 11307496 |
