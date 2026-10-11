# 1279. Warehouse

[Timus 1279](https://acm.timus.ru/problem.aspx?space=1&num=1279) · difficulty 424 · binary_search

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A warehouse of N × M sections (N, M ≤ 100) holds stacks of containers
with heights from 1 to 1000. K ≤ 10⁷ new containers arrive and are put
one by one onto a lowest section. Find the lowest height after all of
them are placed.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, M and K, then N rows of M heights.

## Output

The least height after placing the containers.

## Examples

### Example 1

Input:

```
2 2 3
1 3
2 4
```

Output:

```
3
```

### Example 2

Input:

```
3 3 10
1 2 3
4 5 6
7 8 9
```

Output:

```
5
```

## Solution

Always adding to a lowest section works like pouring water: at the end
all sections below some level h have been raised to h, and the
containers left over lifted some of those to h + 1 but not all of them.
Raising everything to level h takes need(h) = Σ max(0, h − height)
containers, which grows with h. So the answer is the largest h with
need(h) ≤ K, found by binary search between the lowest height and that
height plus K. `O(N · M · log K)`.

Pitfalls:

- the answer can exceed 10⁷, and need(h) up to 10⁴ · 10⁷ needs 64 bits
  (tests 03, 12);
- leftover containers do not raise the minimum unless they reach every
  section at that level (test 05);
- simulating the containers one at a time is far too slow for K = 10⁷.

The answers were compared with placing the containers one at a time on
a heap on 199 small warehouses.

## Language notes

- Same binary search in all languages: arbitrary-precision sums in Python,
  64-bit sums elsewhere.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N · M · log K) | AC | 0.015 s | 280 KB |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 1208 KB |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(N · M · log K) | AC | 0.109 s | 600 KB |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB |
