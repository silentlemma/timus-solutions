# 1748. The Most Complex Number

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · difficulty 268 · number_theory

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The complexity of a number is the number of its divisors. For each
given n, find the most complex number from 1 to n, the smallest one if
several tie, and its complexity.

## Input

t (1 ≤ t ≤ 100), then t numbers n (1 ≤ n ≤ 10¹⁸).

## Output

For each n, the number and its number of divisors.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
1
10
100
1000
10000
```

Output:

```
1 1
6 4
60 12
840 32
7560 64
```

## Solution

The number of divisors of p₁^a₁ · p₂^a₂ · … is (a₁ + 1)(a₂ + 1)…, which
depends only on the exponents. Putting the largest exponents on the
smallest primes gives the smallest number with those exponents, so the
answer is always of the form 2^a · 3^b · 5^c · … with
a ≥ b ≥ c ≥ … on consecutive primes. There are only a few tens of
thousands of such numbers up to 10¹⁸, and the primes needed stop
before 53, since 2 · 3 · … · 53 is already above 10¹⁸.

List them all by a search over the exponents, sort them, and walk up
keeping the best so far: a number replaces the best only with strictly
more divisors, which keeps the smallest on ties. Each query is then a
binary search for the last listed number not above n.
`O(K log K + t log K)` for the K = 32 749 listed numbers.

For n = 100 the answer is 60 = 2² · 3 · 5 with 3 · 2 · 2 = 12 divisors.

Pitfalls:

- multiplying near 10¹⁸ can overflow 64 bits; check the bound by
  division before multiplying;
- on ties the smaller number wins: 2 and 3 both have two divisors.

The answers match a sieve of divisor counts for every query of 100
random numbers up to 20 000, and an independent accepted implementation
on 30 random tests up to 10¹⁸ and around record holders.

## Optimized solutions

Enumerate nonincreasing prime exponents only up to the largest requested bound. Maintain the nondominated frontier ordered by value, with strictly increasing divisor counts. A predecessor with at least as many divisors makes a new candidate useless; otherwise remove following records with no greater count. This preserves every possible best answer and keeps the smallest value on ties. Queries binary-search the compact frontier instead of storing and sorting all generated candidates and separate prefix-best arrays.

Here C counts generated exponent candidates, R is the largest frontier size and T the number of queries; frontier insertion may shift R entries.

- `1748_number_theory_optimized.cpp`: 0.015 s / 168 KB; base `1748_number_theory.cpp`: 0.015 s / 1904 KB; relative change: time -0.0%, memory -91.2%.
- `1748_number_theory_optimized.go`: 0.031 s / 1136 KB; base `1748_number_theory.go`: 0.031 s / 5404 KB; relative change: time -0.0%, memory -79.0%.
- `1748_number_theory_optimized.java`: 0.109 s / 488 KB; base `1748_number_theory.java`: 0.187 s / 8084 KB; relative change: time -41.7%, memory -94.0%.
- `1748_number_theory_optimized.py`: 0.093 s / 536 KB; base `1748_number_theory.py`: 0.187 s / 6476 KB; relative change: time -50.3%, memory -91.7%.
- `1748_number_theory_optimized.rs`: 0.031 s / 224 KB; base `1748_number_theory.rs`: 0.031 s / 1368 KB; relative change: time -0.0%, memory -83.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1748_number_theory.cpp`; covering source `1748_number_theory_optimized.cpp`; time/memory places 1/2, other-author entries 71/71.

- Go: preferred teaching base `1748_number_theory.go`; covering source `1748_number_theory.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1748_number_theory.java`; covering source `1748_number_theory_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1748_number_theory.py`; covering source `1748_number_theory_optimized.py`; time/memory places 1/1, other-author entries 8/8.

- Rust: preferred teaching base `1748_number_theory.rs`; covering source `1748_number_theory.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1904 KB | 11308921 |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB | 11289533 |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB | 11289536 |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.187 s | 6476 KB | 11308922 |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB | 11289537 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1748_number_theory_optimized.cpp](1748_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(CR+T log R) | AC | 0.015 s | 168 KB | 11309275 |
| [1748_number_theory_optimized.go](1748_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 1136 KB | 11309278 |
| [1748_number_theory_optimized.java](1748_number_theory_optimized.java) | Java 1.8 | number_theory | O(CR+T log R) | AC | 0.109 s | 488 KB | 11309276 |
| [1748_number_theory_optimized.py](1748_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(CR+T log R) | AC | 0.093 s | 536 KB | 11309274 |
| [1748_number_theory_optimized.rs](1748_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 224 KB | 11309279 |
