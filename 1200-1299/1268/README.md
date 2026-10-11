# 1268. Little Chu

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · difficulty 728 · number_theory

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 708 KB |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 2440 KB |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.093 s | 2884 KB |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 4508 KB |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 1420 KB |
