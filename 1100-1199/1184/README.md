# 1184. The longest equal pieces that K cables can be cut into

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · difficulty 244 · binary_search

Original problem by Vladimir Pinaev and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 10000` cables from 1 m to 100 km long, given to the
centimetre. Find the largest length, in whole centimetres, such that the
cables can be cut into at least `K ≤ 10000` pieces of that length.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`, then the lengths in metres with exactly two decimals.

## Output

The length in metres with two decimals, `0.00` if not even 1 cm works.

## Examples

### Example 1

Input:

```
4 11
8.02
7.43
4.57
5.39
```

Output:

```
2.00
```

## Solution

Work in centimetres: the lengths have exactly two decimals, so removing
the point gives exact integers. A cable of length `c` gives `⌊c/L⌋` pieces
of length `L`, and this count only falls as `L` grows. So binary search
for the largest `L` with `Σ ⌊c/L⌋ ≥ K`, between 0 and the longest cable;
if even `L = 1` is not enough, the answer stays 0. `O(N log C)`.

Pitfalls:

- reading the lengths as floating-point numbers can turn `8.02` into
  `801.99…` centimetres; parsing them as text avoids that;
- `K` may exceed the total length in centimetres, which must print
  `0.00`, not fail;
- the output needs two decimals, so `2` is printed as `2.00`.

The answers were compared with a separately written solution on 300
random stocks and on every test.

## Language notes

- Python, Go, Java and Rust drop the decimal point from each length;
  C++ reads the whole and fractional parts as two integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB |
