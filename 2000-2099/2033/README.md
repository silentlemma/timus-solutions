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

## Language notes

C++ uses `unordered_map`, Go `map`, Rust and Java `HashMap`, Python
`dict`. Go map values are copied out, updated and stored back. Rust
initializes an entry with the first price; the other ports also
explicitly handle first occurrence. Counts are at most six and prices
fit ordinary signed integers. Java reads the specified three lines per
record; other ports use whitespace tokens.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2033_hashing.cpp](2033_hashing.cpp) | G++ 13.2 x64 | hashing | O(1) | AC | 0.015 s | 384 KB |
| [2033_hashing.go](2033_hashing.go) | Go 1.14 x64 | hashing | O(1) | AC | 0.031 s | 1116 KB |
| [2033_hashing.java](2033_hashing.java) | Java 1.8 | hashing | O(1) | AC | 0.109 s | 612 KB |
| [2033_hashing.py](2033_hashing.py) | Python 3.12 x64 | hashing | O(1) | AC | 0.109 s | 452 KB |
| [2033_hashing.rs](2033_hashing.rs) | Rust 1.75 x64 | hashing | O(1) | AC | 0.046 s | 436 KB |
