# 1803. The Czechs' Rifles

[Timus 1803](https://acm.timus.ru/problem.aspx?space=1&num=1803) · difficulty 716 · math

Original problem by Viktor Kamashev, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Rifle i costs the i-th Fibonacci number of roubles (1, 1, 2, 3, …).
Notes are worth the powers of k, and every rifle is paid with the
fewest notes. Order the rifles by the number of notes paid, breaking
ties by the rifle number.

## Input

k and n (2 ≤ k ≤ 10, 3 ≤ n ≤ 50000).

## Output

The rifle numbers in the required order.

## Examples

### Example 1

Input:

```
10 8
```

Output:

```
1 2 3 4 8 7 5 6
```

## Solution

The fewest notes for an amount is the sum of its digits in base k, so
each rifle's note count is the digit sum of a Fibonacci number. F(50000) has
about 10⁴ decimal digits, so the numbers are added one from the other,
kept in base k. The compiled solutions store limbs in base k^m, the
largest power of k up to a million. A table gives the digit sum of
every limb, so one addition yields the next number and its digit sum
at once. A stable sort by the digit sum then gives the order.
`O(n² / log B)` for limbs of base B.

The Python solution keeps every base-k digit in a 4-bit field of one
big integer. Each field of one operand stores digit + 16 − k, so it overflows exactly
when the base-k digit carries, and an ordinary integer addition passes
the carries along. The fields that did carry are found from the
exclusive or of the operands and the sum, and get the offset back. Bit
counts of the fields' four bit planes then give the digit sum. For
k = 2 the digit sum is simply the number of ones.

In the example the prices are 1, 1, 2, 3, 5, 8, 13, 21 with digit sums
1, 1, 2, 3, 5, 8, 4, 3, which gives 1 2 3 4 8 7 5 6.

Pitfalls:

- the numbers have thousands of digits, far beyond 64 bits;
- equal note counts keep the rifles in increasing order;
- converting big numbers to text in Python is too slow for 50000 of
  them.

The answers agree with an independent accepted implementation for
every base on the largest count and on many smaller ones.

## Optimized solutions

For bases 2, 4 and 8, bit counts give digit sums. Other bases use byte lookup tables to compute limb digit sums.

`1803_math_optimized.cpp`. Keep the Fibonacci limb recurrence and index tie-break. Specialize each radix at compile time. For ordinary bases, split each limb into two blocks and use a runtime-generated digit-sum table of at most 4096 bytes, instead of a table for every limb value. For bases 2/4/8, use 60-bit limbs and bit-plane population counts; hardware POPCNT is selected only after a CPU capability check, with a software path otherwise. Unsigned borrow normalization is exact because the limb base is below half the unsigned range and the intermediate sum is below twice that base. The runtime-generated table holds digit sums, not precomputed answers. With table size T and limb base B, time is O(T+n²/log B+n log n), storage O(T+n); all teaching sources remain.

Exact-source G++ 13.2 x64 Accepted #11326993: 0.171 s / 620 KB. Saved 2026-11-20 current-compiler comparison: time rank 10/45, memory rank 2/45, so both top-ten targets pass and no asterisk is needed. Below 1024 KB, strict admission also permits time only. Previously documented C++ run #11320151 used 1380 KB at 0.14 s: the new run uses less memory but has higher recorded time. These are two distinct accepted runs; the table uses only the paired measurements of #11326993.

- `1803_math_optimized.cpp`: 0.171 s / 620 KB; retained teaching base `1803_math.cpp`: 0.375 s / 4728 KB.

Rust 1.75 x64, submission 11320179. Time 0.359 → 0.187 s, memory 6884 → 1420 KB.

In other bases, each carry reduces the digit sum by k − 1, so the program updates the sum from the number of carries. Python 3.12 x64, submission 11320239. Time 1.687 → 1.062 s, memory 26824 → 29780 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321959 · Java 1.8 №11321967 · Rust 1.75 x64 №11321960 · Go 1.14 x64 №11322289 · Python 3.12 x64 №11322290.

Go 1.14 x64, submission 11322008. Time 0.609 → 0.312 s, memory 12108 → 2564 KB.

Java 1.8, submission 11322348. Time 0.562 → 0.89 s, memory 9876 → 3796 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1803_math_implementation_optimized.rs`. For nonbinary radices, reduce the limb-base cap from one million to 200000 and select the largest radix power within it. This shrinks the digit-sum cache at the cost of processing more limbs; exact digit sums, the recurrence and the power-of-two path remain unchanged. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input.

Accepted #11328979 (Rust 1.75 x64): **0.125 s / 732 KB**. Archived comparison: `1803_math_optimized.rs` (Rust 1.75 x64) — 0.187 s / 1420 KB (#11320179).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1803_math.cpp](1803_math.cpp) | G++ 13.2 x64 | math | O(n^2 / log B) | AC | 0.375 s | 4728 KB | 11321959 |
| [1803_math.go](1803_math.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.609 s | 12108 KB | 11322289 |
| [1803_math.java](1803_math.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.562 s | 9876 KB | 11321967 |
| [1803_math.py](1803_math.py) | Python 3.12 x64 | math | O(n^2) | AC | 1.687 s | 26824 KB | 11322290 |
| [1803_math.rs](1803_math.rs) | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.359 s | 6884 KB | 11321960 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1803_math_optimized.cpp](1803_math_optimized.cpp) | G++ 13.2 x64 | math | O(T+n²/log B+n log n) time; O(T+n) space | AC | 0.171 s | 620 KB | 11326993 |
| [1803_math_optimized.rs](1803_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n^2 / log B) | AC | 0.187 s | 1420 KB | 11320179 |
| [1803_math_optimized.py](1803_math_optimized.py) | Python 3.12 x64 | math | O(n^2) | AC | 1.062 s | 29780 KB | 11320239 |
| [1803_math_optimized.go](1803_math_optimized.go) | Go 1.14 x64 | math | O(n^2 / log B) | AC | 0.312 s | 2564 KB | 11322008 |
| [1803_math_optimized.java](1803_math_optimized.java) | Java 1.8 | math | O(n^2 / log B) | AC | 0.89 s | 3796 KB | 11322348 |
| [1803_math_implementation_optimized.rs](1803_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(n^2 / log B) | AC | 0.125 s | 732 KB | 11328979 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
