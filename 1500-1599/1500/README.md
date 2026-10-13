# 1500. Pass Licenses

[Timus 1500](https://acm.timus.ru/problem.aspx?space=1&num=1500) · difficulty 641 · bitmask

Original problem by Magaz Asanov, Alexander Mironenko, Anton Botov and Evgeny Krokhalev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has N crossings (2 ≤ N ≤ 30) joined by M road segments, each of
one of K categories (1 ≤ K ≤ 20); two crossings may be joined by roads
of several categories. A permit for a category allows driving on all
its roads. Find the fewest permits that allow a way from crossing 0 to
crossing 1, and list their categories.

Time limit: 2.5 seconds. Memory limit: 64 MB.

## Input

K, N and M, then M lines with two crossings and a category.

## Output

The number of permits, then the categories. Any smallest set is
accepted.

## Examples

### Example 1

Input:

```
3 3 3
0 2 0
0 2 1
1 2 2
```

Output:

```
2
0 2
```

## Solution

Choosing the fewest categories is a covering problem with no shortcut,
but there are at most 2²⁰ sets of categories, so try them by size and
stop at the first set that connects 0 with 1.

The test for one set must be fast. For every crossing u and category c
keep the bit mask of crossings joined to u by a road of category c. The
neighbours of u under a whole set are the union of these masks; it is
precomputed for every subset of the low ten categories and of the high
ten, so two lookups give it. A search from crossing 0 then grows the
mask of reached crossings and stops as soon as crossing 1 is in it.
`O(2^K · N)`.

Pitfalls:

- the shortest route is not always the cheapest: a long route on one
  category beats a short one on two (test 04);
- a pair of crossings can have roads of several categories, and any of
  them is enough (tests 01, 03);
- when the answer needs all 20 categories almost every set is tried, so
  the test per set must be a few table lookups (gen2).

## Language notes

- Python runs under PyPy: the chain that needs all 20 categories takes
  about 1.25 s with CPython and about 0.14 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1500_bitmask.cpp](1500_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K N) | AC | 0.093 s | 576 KB |
| [1500_bitmask.go](1500_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K N) | AC | 0.171 s | 1596 KB |
| [1500_bitmask.java](1500_bitmask.java) | Java 1.8 | bitmask | O(2^K N) | AC | 0.343 s | 6136 KB |
| [1500_bitmask.py](1500_bitmask.py) | PyPy 3.10 x64 | bitmask | O(2^K N) | AC | 0.718 s | 4484 KB |
| [1500_bitmask.rs](1500_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K N) | AC | 0.140 s | 680 KB |
