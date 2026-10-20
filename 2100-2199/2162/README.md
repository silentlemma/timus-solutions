# 2162. Counting segments of an array that encode a simple graph

[Timus 2162](https://acm.timus.ru/problem.aspx?space=1&num=2162) · difficulty 1088 · hashing, segment_tree

Original problem by Valentin Zuev, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph is written as N, M and then M pairs of vertices from 1 to
N, with N ≥ 1, no loops and no repeated edges. Count the contiguous
segments of an array of K numbers that are such a record. The limits are
2 seconds and 256 MB.

## Input

K, 1 ≤ K ≤ 10⁵, then the numbers, each from 0 to 10⁹.

## Output

The number of segments.

## Examples

### Example 1

Input:

```
12
2 2 2 2 1 1 2 1 2 1 0 0
```

Output:

```
3
```

## Solution

A start s fixes the whole segment: N = a[s], M = a[s + 1], and the edges
are the M pairs after them, so there are at most K candidates. A
candidate is valid when N ≥ 1, the segment fits, and its pairs

- contain no 0 and no pair of equal numbers,
- repeat no unordered pair,
- use only numbers up to N.

The pairs of a candidate start at positions of one parity, so the first
two conditions are prepared for both parities from right to left: for
each pair position p, good(p) is where the run of acceptable pairs from
p must stop, the earliest bad pair or the next occurrence of a pair
already seen, found with a hash map from each unordered pair to its
nearest later position. A candidate passes them when its end is not
beyond good(s + 2). The third condition is a range maximum, taken from
a segment tree. With M = 0 the record is just "N 0". The work is
O(K log K).

In the example "2 1 1 2", "2 1 2 1" and "1 0" are the three valid
records.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2162_hashing_segment_tree.cpp](2162_hashing_segment_tree.cpp) | G++ 13.2 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 3988 KB |
| [2162_hashing_segment_tree.go](2162_hashing_segment_tree.go) | Go 1.14 x64 | hashing, segment_tree | O(K log K) | AC | 0.046 s | 8964 KB |
| [2162_hashing_segment_tree.java](2162_hashing_segment_tree.java) | Java 1.8 | hashing, segment_tree | O(K log K) | AC | 0.125 s | 13232 KB |
| [2162_hashing_segment_tree.py](2162_hashing_segment_tree.py) | Python 3.12 x64 | hashing, segment_tree | O(K log K) | AC | 0.687 s | 15264 KB |
| [2162_hashing_segment_tree.rs](2162_hashing_segment_tree.rs) | Rust 1.75 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 5560 KB |
