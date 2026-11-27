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

Compared with `1352_number_theory.rs`: time 0.031 s → 0.001 s; memory 216 KB → 56 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1352_parsing_optimized.go`. Use direct typed conversion over a 256-byte refill buffer and compact output with complete writes. Signed integer conversion accumulates negative values directly, including the signed minimum; no reflection-based input or generic output dispatch is needed. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Convert complete digit runs within the current input block, keeping the cursor local until a token or block boundary. Negative accumulation handles the full signed minimum and removes a sign branch or byte-reader call per digit; EOF and optional signs are preserved.

Accepted #11329135 (Go 1.14 x64): **0.015 s / 796 KB**. Archived comparison: `1352_number_theory.go` (Go 1.14 x64) — 0.031 s / 1084 KB (#11285182).


`1352_number_theory_parsing_optimized.java`. Keep the same 38 Mersenne-prime exponents, with their OEIS citation. Parse queries and format answers through reusable 1 KiB byte buffers, avoiding StreamTokenizer, character decoding and temporary decimal strings. Write the final buffered bytes before Runtime.halt(0). The query count need not fit in either buffer: processing is streamed. The simple implementation remains unchanged.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329348 (Java 1.8): **0.046 s / 480 KB**.

## Language notes

The unchanged CPython source was measured three more times: (0.078 s, 468 KB), (0.093 s, 400 KB), and (0.046 s, 312 KB). The table records the last actual Accepted pair; these repeated measurements do not constitute an algorithmic speedup. In the saved comparable current-interpreter sample, that run shares time place 1/30 and has memory place 11/30. With memory below 1 MiB, admission uses the time ranking. The readable baseline already meets it, so no duplicate optimized Python source is added.

Use the shared [criteria](../../RATING_CRITERIA.md): no separate
first-place target or 30% improvement admission. Only memory strictly
below 1024 KB excludes memory comparison; at 1024 KB both metrics count.
Rivals below 0.015 s are excluded; our own time is floored. Rust has
three eligible older-compiler rivals in its same-language fallback;
base/optimized time ranks 4/4 and 1/4 pass, not an empty-sample rule.

The 38-entry table is fixed O(1) space. Simple C++/Go stream queries
and answers with O(1) bounded storage. Simple Java accumulates O(T)
output; Python retains split input and joined output, and Rust keeps
input/output Strings, using O(I+T) space for I input bytes. The lookup
kernel is O(T), full byte-input work O(I+T). Optimized Rust/Go/Java
stream through fixed buffers, O(1) auxiliary storage.

Only lint-required constants in `1352_parsing_optimized.go` were given names; their values, algorithm and comments are unchanged. Accepted #11329135 describes the preceding exact bytes and paired metrics.

Only lint-required constants in `1352_number_theory_parsing_optimized.java` were given names; their values, algorithm and comments are unchanged. Accepted #11329348 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 116 KB | 11329301 |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1080 KB | 11329303 |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.125 s | 428 KB | 11329302 |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.046 s | 312 KB | 11326033 |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.031 s | 216 KB | 11329304 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1352_number_theory_optimized.rs](1352_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(Q) time; O(1) auxiliary space | AC | 0.001 s | 56 KB | 11325503 |
| [1352_parsing_optimized.go](1352_parsing_optimized.go) | Go 1.14 x64 | parsing | O(T) | AC | 0.015 s | 792 KB | 11331002 |
| [1352_number_theory_parsing_optimized.java](1352_number_theory_parsing_optimized.java) | Java 1.8 | number_theory, parsing | O(T) time; O(1) auxiliary space | AC | 0.062 s | 496 KB | 11331042 |

**Current measurements.** The solution tables record the exact preserved sources and their latest Accepted runs. Earlier performance comparisons describe historical runs; current admission follows the shared [rating criteria](../../RATING_CRITERIA.md).
