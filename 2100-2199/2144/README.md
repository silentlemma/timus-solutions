# 2144. Ordering sealed boxes into one sorted row

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · difficulty 221 · sorting

Original problem by Ivan Smirnov, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n boxes, each holding a fixed row of figure sizes that cannot
be rearranged or reversed. Decide whether the boxes can be put in some
order so that all sizes together form a non-decreasing row. The limits
are 0.5 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 100, then for every box kᵢ, 1 ≤ kᵢ ≤ 100, and its sizes,
1 ≤ aᵢⱼ ≤ 10⁴.

## Output

YES or NO.

## Examples

### Example 1

Input:

```
3
2 1 2
3 7 7 7
1 5
```

Output:

```
YES
```

### Example 2

Input:

```
2
2 1 3
1 2
```

Output:

```
NO
```

## Solution

Every box must be non-decreasing inside. After that only its first size
f and last size l matter, and a valid order needs l of each box to be at
most f of the next one.

In any valid order the first sizes do not decrease, since f ≤ l ≤ f of
the next box. Among boxes with the same first size f, all but the last
one have l ≤ f, so l = f. Therefore sorting the boxes by (f, l) gives a
valid order whenever one exists, and it is enough to check the
neighbours in that order. The work is O(Σ kᵢ + n log n).

In the first example the boxes (1, 2), (5, 5) and (7, 7) fit in this
order; in the second (1, 3) and (2, 2) overlap.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 192 KB |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6900 KB |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.062 s | 1140 KB |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 336 KB |
