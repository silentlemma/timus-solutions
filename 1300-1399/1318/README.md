# 1318. Logarithm

[Timus 1318](https://acm.timus.ru/problem.aspx?space=1&num=1318) · difficulty 1393 · bitmask

Original problem: idea by Nikita Shamgunov, prepared by Nikita Shamgunov and Anton Botov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N ≤ 5000 numbers A₀, …, A_{N−1} of 128 bits, compute the sum of
⌊log₁₀(A_k xor A_j)⌋ over all ordered pairs k, j from 0 to N − 1,
counting the logarithm of 0 as 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line has N. Each of the next N lines has four numbers from 0
to 2³² − 1, the 32-bit words of A_k from the highest to the lowest:
A_k = 2⁹⁶ · a₁ + 2⁶⁴ · a₂ + 2³² · a₃ + a₄.

## Output

The sum.

## Examples

### Example 1

Input:

```
2
0 0 0 2324
0 2332 0 0
```

Output:

```
44
```

## Solution

⌊log₁₀ x⌋ is the number of powers 10¹, 10², … that are at most x. A
power of ten shorter in bits than x is always below x, and since 10 > 2
at most one power has exactly as many bits as x. So a table indexed by
the bit length L gives the count of shorter powers, and the one power of
length L, if any, needs a single comparison. Each pair k < j costs a
xor, a bit length and at most one comparison, and the sum over ordered
pairs is twice the sum over k < j, since the diagonal gives 0.
`O(N²)`, about 12.5 million pairs.

Pitfalls:

- the pairs are ordered, so the example gives 22 twice (test 01);
- a xor of exactly 10³⁸ has 38 as its logarithm and 10³⁸ − 1 has 37
  (test 06), and the largest xor 2¹²⁸ − 1 is still 38 (test 05);
- the words must be read as unsigned: 4 294 967 295 does not fit a
  signed 32-bit integer;
- the sum is at most 5000 · 4999 · 38 ≈ 9.5 · 10⁸, which still fits 32
  bits, but a 64-bit counter costs nothing.

## Language notes

- C++ and Rust use a native 128-bit integer; Go and Java keep each
  number as two 64-bit halves and compare them as unsigned.
- In Python the 12.5 million pairs would take several seconds, so it
  works on the sorted numbers instead. In a range that shares the bits
  above some bit t, every pair across the split at t has a xor with t
  as its highest bit, so all those pairs share the shorter powers. When
  a power of ten has t as its highest bit, the pairs that reach it are
  counted by going down both halves bit by bit, the way a binary trie
  would, with tiny groups checked pair by pair. This takes about
  0.2 seconds, and the results were compared with a direct sum over all
  pairs on 800 small random sets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1318_bitmask.cpp](1318_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(N^2) | AC | 0.062 s | 280 KB |
| [1318_bitmask.go](1318_bitmask.go) | Go 1.14 x64 | bitmask | O(N^2) | AC | 0.093 s | 1420 KB |
| [1318_bitmask.java](1318_bitmask.java) | Java 1.8 | bitmask | O(N^2) | AC | 0.328 s | 2368 KB |
| [1318_bitmask.py](1318_bitmask.py) | Python 3.12 x64 | bitmask | O(N log N) | AC | 0.093 s | 2268 KB |
| [1318_bitmask.rs](1318_bitmask.rs) | Rust 1.75 x64 | bitmask | O(N^2) | AC | 0.093 s | 588 KB |
