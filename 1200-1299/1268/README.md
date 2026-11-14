# 1268. Little Chu

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · difficulty 722 · number_theory

Original problem by Pavel Atnashev, from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Little Chu wakes up K, K², K³, … days after birth and must never see
the same day of the week twice; a week has N days, N prime
(2 < N < 65 536), and K is at most a week. For each of T ≤ 6553 values
of N, print the K that gives the most wake-ups; the sample shows that
the largest such K is expected.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

T, then T primes N.

## Output

K for each N, one per line.

## Examples

### Example 1

Input:

```
4
3
5
7
11
```

Output:

```
2
3
5
8
```

## Solution

The day of the week of the i-th wake-up is K^i mod N. These values
repeat with the multiplicative order of K modulo N, so the most
wake-ups, N − 1 of them, come from a primitive root. The answer is the
largest primitive root modulo N.

A number g is a primitive root exactly when g^((N−1)/q) ≠ 1 mod N for
every prime q dividing N − 1. Factor N − 1 with a sieve of smallest
prime factors up to 65 536, then try g = N − 1, N − 2, … until one
passes. Primitive roots make up a fair share of all residues, so only a
few candidates are tried, each with a handful of fast powerings.
Repeated values of N are answered from a table. Roughly
`O(L log log L + T · k log N)` for the sieve limit L and k candidates.

Pitfalls:

- any primitive root keeps the days distinct, but the expected one is
  the largest (in the example, 8 for N = 11 rather than 2);
- the time limit is a quarter of a second for up to 6553 queries, so
  N − 1 should be factored with the sieve rather than tried from scratch
  each time (tests 04, 05);
- when N − 1 is a power of two, only one test power is needed
  (test 06).

The answers were compared with listing the powers of every candidate
for each prime below 3000.

## Language notes

- All languages build the same sieve and keep a table of answers by N.

## Optimized solutions

The optimized versions sieve only odd numbers and test the factor 2 separately. Cached answers avoid repeating the search for the same modulus.

Python 3.12 x64, submission 11322010. Time 0.156 → 0.125 s, memory 4400 → 2368 KB.

Rust 1.75 x64, submission 11322011. Time 0.031 → 0.031 s, memory 1420 → 312 KB.

Go 1.14 x64, submission 11322012. Time 0.015 → 0.031 s, memory 2420 → 1004 KB.

G++ 13.2 x64, submission 11322013. Time 0.031 → 0.031 s, memory 692 → 212 KB.

Java 1.8, submission 11322014. Time 0.109 → 0.078 s, memory 2928 → 920 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322241 · Go 1.14 x64 №11322242 · Java 1.8 №11322243 · Python 3.12 x64 №11322244 · Rust 1.75 x64 №11322245.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 692 KB | 11322241 |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 2420 KB | 11322242 |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 2928 KB | 11322243 |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.156 s | 4400 KB | 11322244 |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1420 KB | 11322245 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1268_number_theory_optimized.py](1268_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.125 s | 2368 KB | 11322010 |
| [1268_number_theory_optimized.rs](1268_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 312 KB | 11322011 |
| [1268_number_theory_optimized.go](1268_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 1004 KB | 11322012 |
| [1268_number_theory_optimized.cpp](1268_number_theory_optimized.cpp) \* | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 212 KB | 11322013 |
| [1268_number_theory_optimized.java](1268_number_theory_optimized.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.078 s | 920 KB | 11322014 |

\* The marked versions have room to improve in the ratings.
