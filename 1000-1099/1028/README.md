# 1028. Counting points below and to the left of each point

[Timus 1028](https://acm.timus.ru/problem.aspx?space=1&num=1028) · difficulty 264 · fenwick, segment_tree

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` distinct points (`1 ≤ N ≤ 15 000`) with integer coordinates
`0 ≤ x, y ≤ 32 000` are given in increasing order of `y`, and of `x` for
equal `y`. The **level** of a point is the number of other points with
`x' ≤ x` and `y' ≤ y`. For every `k` from 0 to `N - 1` print how many points
have level `k`.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines `x y` in the order described above.

## Output

`N` lines: the number of points of level 0, 1, ..., `N - 1`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
2 0
6 0
0 2
4 2
4 4
1 6
```

Output:

```
2
2
1
1
0
0
```

### Example 2

Input:

```
1
32000 32000
```

Output:

```
1
```

## Solution

The order of the input does half of the work. When a point arrives, every
point with a smaller `y`, and every point with the same `y` and a smaller
`x`, has already arrived — and no later point has `y' ≤ y` and `x' ≤ x`
unless it is the same point. So the level of a point is the number of
points **seen so far** with `x' ≤ x`.

That is a prefix count over `x` with insertions: a **Fenwick tree**
(binary indexed tree) over the coordinates `0..32 000` answers "how many
inserted values are `≤ x`" and inserts a value in `O(log C)` each, `C` being
the coordinate range. Process the points in order: query, count the level,
insert. `O(N log C)` in total.

A segment tree over the coordinates works the same way, a little slower.

Pitfalls:

- `x` can be 0, and Fenwick trees are 1-based: shift by one;
- a quadratic count of earlier points is `10^8` comparisons — too slow for
  the 0.25-second limit;
- `N` numbers in the output: build it in a buffer.

## Language notes

- **C++**: a Fenwick tree and a bottom-up segment tree.
- **Go**, **Python**, **Java**, **Rust**: a Fenwick tree; Python keeps the
  loops tight (only the `x` coordinates are converted, `j &= j - 1` walks
  down).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1028_fenwick.cpp](1028_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 348 KB |
| [1028_fenwick.go](1028_fenwick.go) | Go 1.14 x64 | fenwick | O(N log C), C = 32001 | AC | 0.046 s | 1512 KB |
| [1028_fenwick.java](1028_fenwick.java) | Java 1.8 | fenwick | O(N log C), C = 32001 | AC | 0.093 s | 888 KB |
| [1028_fenwick.py](1028_fenwick.py) | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.109 s | 3644 KB |
| [1028_fenwick.rs](1028_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 1076 KB |
| [1028_segment_tree.cpp](1028_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(N log C), C = 32001 | AC | 0.031 s | 472 KB |
