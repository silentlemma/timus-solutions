# 1857. Alice and Bandersnatch

[Timus 1857](https://acm.timus.ru/problem.aspx?space=1&num=1857) · difficulty 1351 · combinatorics

Original problem by Pavel Klimov, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Alice's cipher key is a sequence x₁, …, xₙ of numbers from 0 to a − 1,
where a is the size of the alphabet; the key is applied over and over to
the letters of a message. Keys that differ only by a cyclic shift count
as one, and keys that repeat a shorter block (period below n) are not
used. Count the different keys.

## Input

a and n (1 ≤ a ≤ 26, 1 ≤ n ≤ 10 000).

## Output

The number of keys, exactly.

## Examples

### Example 1

Input:

```
3 4
```

Output:

```
18
```

### Example 2

Input:

```
10 2
```

Output:

```
45
```

## Solution

The keys are the necklaces of length n over a letters whose period is
exactly n, that is, the Lyndon words. Every word of length n repeats a
primitive block whose length d divides n, so aⁿ = Σ over d | n of d·L(d),
where L(d) counts the Lyndon words of length d (each gives d different
rotations). Möbius inversion turns this into
n·L(n) = Σ over d | n of μ(d)·a^(n/d), where only square-free d count,
with the sign (−1) to the number of their prime factors.

A number up to 10 000 has at most five different prime factors, so
there are at most 32 terms, but a^(n/d) has up to 14 150 digits. Python,
Go and Java use their big integers; the C++ and Rust solutions keep
numbers in base 10⁹ and need only multiplication by a, addition,
subtraction and division by n: the positive and the negative terms are
summed apart and subtracted once. In C++ and Rust each term is built by
multiplying by a step by step: fewer than 3n multiplications of numbers
of up to 1600 limbs in all, taking O(n^2) time.

In the first example the 81 keys of length 4 include 9 with a period of
2 or 1, and the remaining 72 fall into rotation classes of 4: 18.

Pitfalls:

- with one letter every key longer than 1 repeats itself: the answer
  is 0, and 1 for n = 1;
- the answer is exact and long; Python 3.12 needs the default limit on
  printing long integers lifted.

The answers agree with a count over all keys for small a and n and with
an independent accepted implementation on lengths up to 10 000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1857_combinatorics.cpp](1857_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n^2) | AC | 0.031 s | 228 KB |
| [1857_combinatorics.go](1857_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n^2) | AC | 0.031 s | 1464 KB |
| [1857_combinatorics.java](1857_combinatorics.java) | Java 1.8 | combinatorics | O(n^2) | AC | 0.140 s | 3932 KB |
| [1857_combinatorics.py](1857_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n^2) | AC | 0.093 s | 840 KB |
| [1857_combinatorics.rs](1857_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n^2) | AC | 0.062 s | 260 KB |
