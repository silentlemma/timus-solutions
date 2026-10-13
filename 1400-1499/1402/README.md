# 1402. Cocktails

[Timus 1402](https://acm.timus.ru/problem.aspx?space=1&num=1402) · difficulty 130 · combinatorics

Original problem by Sergey Pupyrev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cocktail mixes two or more of N ≤ 21 drinks, each at most once, and
the order of the drinks matters. Count the different cocktails.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

The number of cocktails.

## Examples

### Example 1

Input:

```
3
```

Output:

```
12
```

## Solution

A cocktail of k drinks is an ordered choice of k different drinks, and
there are N·(N − 1)·…·(N − k + 1) of them. Add these for k from 2 to N,
building each product from the previous one. `O(N)`.

Pitfalls:

- with one drink there is no cocktail at all (test 02);
- for N = 21 the answer is about 1.4·10²⁰, past 64 bits, so the
  solutions use 128-bit or big integers (test 07).

The tests are judged by exact comparison.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1402_combinatorics.cpp](1402_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N) | AC | 0.015 s | 188 KB |
| [1402_combinatorics.go](1402_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N) | AC | 0.031 s | 1176 KB |
| [1402_combinatorics.java](1402_combinatorics.java) | Java 1.8 | combinatorics | O(N) | AC | 0.109 s | 1688 KB |
| [1402_combinatorics.py](1402_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N) | AC | 0.078 s | 388 KB |
| [1402_combinatorics.rs](1402_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N) | AC | 0.031 s | 232 KB |
