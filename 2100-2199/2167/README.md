# 2167. Smallest XOR key that turns a number into a prime

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · difficulty 493 · bitmask, number_theory

Original problem by Vadim Barinov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of T numbers a below 2²⁰ find the smallest non-negative key k
such that a XOR k is a prime. The limits are 2 seconds and 256 MB.

## Input

T, 1 ≤ T ≤ 10⁵, then the numbers, 0 ≤ a ≤ 1 048 575.

## Output

The smallest key for every number.

## Examples

### Example 1

Input:

```
3
5
6
1
```

Output:

```
0
1
2
```

## Solution

For a fixed a the key k = a XOR p is in one-to-one correspondence with
the prime p, so the task is to find the prime p that minimizes a XOR p.
Keys below 2²⁰ already reach every prime below 2²⁰, the prime 2 among
them, and a larger prime would need a key of at least 2²⁰, so only the
primes below 2²⁰ matter.

The XOR is smallest when p agrees with a on the highest possible bits.
Sieve the primes below 2²⁰ and build, for every j, a table telling
whether some prime starts with a given j-bit prefix; each table is the
OR of pairs of entries of the next one. A query then picks the bits of p
from the top: it keeps the bit of a when some prime has that longer
prefix, and takes the other bit otherwise. That is 20 steps per number
after O(2²⁰) preparation.

In the example 5 is prime, 6 XOR 1 = 7 and 1 XOR 2 = 3.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.109 s | 2300 KB |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 3080 KB |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.140 s | 4904 KB |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.671 s | 16692 KB |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) | Rust 1.75 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 4172 KB |
