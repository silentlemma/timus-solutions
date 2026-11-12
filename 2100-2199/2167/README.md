# 2167. Smallest XOR key that turns a number into a prime

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · difficulty 503 · bitmask, number_theory

Original problem by Vadim Barinov, from the Ural Team Programming Contest 2022.

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
after O(2²⁰ log log 2²⁰) preparation.

In the example 5 is prime, 6 XOR 1 = 7 and 1 XOR 2 = 3.

The teaching C++ version first sieves primes below U = 2²⁰. For each input a, try keys in increasing order and stop at the first prime a XOR k. This gives the smallest key directly. A key below U always exists because a XOR 2 reaches the prime 2. Exhaustive comparison for all U input values found a maximum answer of 95. The sieve uses O(U) space and O(U log log U) time. Each query uses at most 96 lookups for this input range.

## Optimized solutions

The C++ alternative packs the same prime-prefix tree into one bit per heap node. With U=2²⁰, the 2U-bit array occupies 262144 bytes. Leaf bits are the sieve itself: start with odd candidates and prime two, clear one and odd composites. This odd/even initialization mask is not a stored prime or answer table. Internal bits are ORs of their children. A query starts at root one and prefers the input bit when that child contains a prime. This sets the highest undecided XOR bit to zero whenever possible. If that child is empty, the sibling is forced. The chosen leaf index minus U gives the prime p, and the answer is the query value XOR p. Fixed input/output blocks replace the growing answer string. Time O(U log log U+T log U), storage O(U) bits. All simple files remain; the other four families reuse admitted bases.

The accepted base implementations [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go), [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java), [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py), [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.109 s | 2300 KB | 11295058 |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.031 s | 3080 KB | 11295059 |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.140 s | 4904 KB | 11295061 |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) \* | Python 3.12 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.671 s | 16692 KB | 11295060 |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) \* | Rust 1.75 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.031 s | 4172 KB | 11295062 |
| [2167_number_theory.cpp](2167_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(U log log U + 96 T) | AC | 0.109 s | 1136 KB | 11315938 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory_optimized.cpp](2167_bitmask_number_theory_optimized.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(U log log U + T log U) | AC | 0.031 s | 336 KB | 11315846 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
