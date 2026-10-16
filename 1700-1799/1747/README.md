# 1747. Kingdom Inspection

[Timus 1747](https://acm.timus.ru/problem.aspx?space=1&num=1747) · difficulty 1366 · combinatorics

Original problem by Artyom Ripatti, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every two of n cities are joined by a road. The king starts in the
capital, must visit every city exactly twice and return to the capital.
Count the possible routes modulo p.

## Input

n and p (3 ≤ n ≤ 10⁵, 1 ≤ p ≤ 10⁹ + 7).

## Output

The number of routes modulo p.

## Examples

### Example 1

Input:

```
3 123
```

Output:

```
2
```

### Example 2

Input:

```
4 123
```

Output:

```
30
```

## Solution

The capital is visited at the start and at the end, so in between the
route is a word in which each of the other m = n − 1 cities appears
twice and no city follows itself, since a road joins two different
cities. Inclusion and exclusion over the pairs written side by side
count such words as

a(m) = Σ (−1)^k C(m, k) (2m − k)! / 2^(m − k),

but p need not be prime, and dividing modulo p is not always possible.
The same numbers satisfy

a(m) = m(2m − 1)·a(m − 1) + m(m − 1)·a(m − 2), a(0) = 1, a(1) = 0,

which needs only multiplications, so the answer comes out in `O(n)`
steps modulo any p.

For n = 4 there are three other cities and the words are 30, such as
`ABCABC` and `ABACBC`.

Pitfalls:

- p can be 1, or even, or any composite, which rules out modular
  inverses;
- m(2m − 1) reaches 2·10¹⁰, so it is reduced modulo p before the next
  multiplication to stay within 64 bits.

The recurrence gives the same numbers as the inclusion-exclusion sum,
both with exact integers, for every m up to 59 and for m = 100, 250,
500, 1000 and 1500. The answers also match an independent accepted
implementation, which splits p into prime powers, on 68 tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1747_combinatorics.cpp](1747_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 384 KB |
| [1747_combinatorics.go](1747_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.031 s | 1080 KB |
| [1747_combinatorics.java](1747_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 1592 KB |
| [1747_combinatorics.py](1747_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.140 s | 376 KB |
| [1747_combinatorics.rs](1747_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 244 KB |
