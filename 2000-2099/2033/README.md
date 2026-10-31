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

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2033_bruteforce.cpp`: time reduction +0.00%; memory reduction
  +67.71%; base: `2033_hashing.cpp`.

- `2033_bruteforce.rs`: time reduction +0.00%; memory reduction +47.71%;
  base: `2033_hashing.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2033_hashing.java](2033_hashing.java).

C++ uses `unordered_map`, Go `map`, Rust and Java `HashMap`, Python
`dict`. Go map values are copied out, updated and stored back. Rust
initializes an entry with the first price; the other ports also
explicitly handle first occurrence. Counts are at most six and prices
fit ordinary signed integers. Java reads the specified three lines per
record; other ports use whitespace tokens.

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
