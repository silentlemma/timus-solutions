# 1669. Universal Word

[Timus 1669](https://acm.timus.ru/problem.aspx?space=1&num=1669) · difficulty 1396 · bitmask

Original problem by Ivan Burmistrov (prepared by Alex Samsonov), from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A word over the first N letters is universal if every arrangement of
those N letters, each used once, is a subsequence of it. Decide whether
the given word is universal.

## Input

N (1 ≤ N ≤ 26), then the word: at most 300 lowercase letters among the
first N.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
3
abacaba
```

Output:

```
YES
```

### Example 2

Input:

```
3
abcba
```

Output:

```
NO
```

## Solution

A fixed order of letters is a subsequence exactly when taking each next
letter at its first occurrence after the previous one gets through the
word. So for a set S of letters, let reach(S) be how far this greedy
embedding gets for the worst order of S. The worst order ends with some
letter c, after the worst order of the others:

reach(S) = max over c in S of after(c, reach(S \ {c})),

where after(c, p) is the place just past the first c at or after p.
The word is universal exactly when reach of all N letters stays within
the word. If any set fails, every larger set fails too, since an
adversary can start with the failing set.

- Masks in increasing order list every subset before its supersets, so
  the table is filled bottom-up and grows only as far as needed: the
  first failing mask ends the search with `NO`.
- A quick bound first: whatever has been placed, the remaining k letters
  have k different next occurrences, so the one farthest away moves at
  least k places. A universal word therefore needs N + (N − 1) + … + 1
  letters, and N ≥ 25 is always `NO`.

`O(2^N · N)` in the worst case, which only a word universal on many
letters reaches; the shortest known universal words for 18 letters
already take 292 places.

Pitfalls:

- a full table of 2²⁴ entries would not fit in memory up front, so the
  table only grows as masks are reached;
- the zigzag a…q, p…a, b…q, … over 17 letters is universal in 273
  letters and makes every one of the 2¹⁷ subsets count (test 06);
- a word universal on the first letters but not on all fails only late
  in the order (test 08).

The answers match an exhaustive check of all orders on 500 random small
inputs and an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1669_bitmask.cpp](1669_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^N N) | AC | 0.015 s | 1196 KB |
| [1669_bitmask.go](1669_bitmask.go) | Go 1.14 x64 | bitmask | O(2^N N) | AC | 0.031 s | 4180 KB |
| [1669_bitmask.java](1669_bitmask.java) | Java 1.8 | bitmask | O(2^N N) | AC | 0.109 s | 1580 KB |
| [1669_bitmask.py](1669_bitmask.py) | Python 3.12 x64 | bitmask | O(2^N N) | AC | 0.718 s | 6764 KB |
| [1669_bitmask.rs](1669_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^N N) | AC | 0.046 s | 1268 KB |
