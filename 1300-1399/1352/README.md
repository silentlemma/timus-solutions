# 1352. Mersenne Primes

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · difficulty 132 · number_theory

Original problem by Vladimir Yakovlev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Mersenne prime is a prime of the form 2^p − 1. Given T queries, each
a number N ≤ 38, print the exponent p of the N-th Mersenne prime in
increasing order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N.

## Output

T lines with the exponents.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

Output:

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## Solution

No program can find these primes in a second: the 38th exponent is
6 972 593, and checking even one number of that size takes a lot of
computation. The order of the first 38 Mersenne primes was settled long
ago, so the solutions keep the list of their exponents as a constant
table and answer each query by indexing it. `O(T)`.

Pitfalls:

- N counts from 1: the first Mersenne prime is 2² − 1 = 3, exponent 2
  (test 03);
- all exponents fit in 32-bit integers.

The first 22 entries were checked by running the Lucas–Lehmer test on
every prime exponent up to 10 000; the rest come from the published list
and agree with the example and the entries named in the statement.

## Optimized solutions

`1352_number_theory_optimized.rs`. Keep the exact table of the first 38 Mersenne-prime exponents specified by the problem. Stream Q indices directly into that table and write each integer immediately through the C runtime, avoiding retained input/output Strings and per-answer to_string allocations. O(Q) time and O(1) auxiliary space under the fixed table; no new primality algorithm or additional answer table is introduced.

Compared with `1352_number_theory.rs`: time 0.001 s → 0.001 s; memory 216 KB → 56 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1352_parsing_optimized.go`. Use direct typed conversion over a 256-byte refill buffer and compact output with complete writes. Signed integer conversion accumulates negative values directly, including the signed minimum; no reflection-based input or generic output dispatch is needed. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Convert complete digit runs within the current input block, keeping the cursor local until a token or block boundary. Negative accumulation handles the full signed minimum and removes a sign branch or byte-reader call per digit; EOF and optional signs are preserved.

Accepted #11329135 (Go 1.14 x64): **0.015 s / 796 KB**. Archived comparison: `1352_number_theory.go` (Go 1.14 x64) — 0.031 s / 1084 KB (#11285182).

## Language notes

The unchanged CPython source was measured three more times: (0.078 s, 468 KB), (0.093 s, 400 KB), and (0.046 s, 312 KB). The table records the last actual Accepted pair; these repeated measurements do not constitute an algorithmic speedup. In the saved comparable current-interpreter sample, that run shares time place 1/30 and has memory place 11/30. With memory below 1 MiB, admission uses the time ranking. The readable baseline already meets it, so no duplicate optimized Python source is added.

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1352_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB | 11285181 |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB | 11285182 |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB | 11285186 |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.046 s | 312 KB | 11326033 |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB | 11285188 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory_optimized.rs](1352_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(Q) time; O(1) auxiliary space | AC | 0.001 s | 56 KB | 11325503 |
| [1352_parsing_optimized.go](1352_parsing_optimized.go) | Go 1.14 x64 | parsing | O(T) | AC | 0.015 s | 796 KB | 11329135 |
