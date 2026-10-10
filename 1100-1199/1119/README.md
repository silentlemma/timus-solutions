# 1119. The shortest walk across a grid with some diagonal shortcuts

[Timus 1119](https://acm.timus.ru/problem.aspx?space=1&num=1119) · difficulty 70 · dp

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid has `N × M` square blocks (`0 < N, M ≤ 1000`) with sides of 100
metres. A walk goes from the south-west corner of block `(1, 1)` to the
north-east corner of block `(N, M)` along the streets, only north or east;
`K ≤ 100` given blocks may also be crossed along their south-west to
north-east diagonal. Find the length of the shortest walk, rounded to the
nearest metre.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N M`, then `K`, then `K` lines `x y` with the blocks that can be crossed.

## Output

The shortest length in metres, rounded.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 2
3
1 1
3 2
1 2
```

Output:

```
383
```

## Solution

A walk only moves north and east, so the diagonals it uses form a chain
of blocks strictly increasing in both coordinates, and any such chain can
be walked. Each diagonal replaces two sides (200 m) by `100√2` m, so the
best walk uses the longest chain. Sort the blocks and find the longest
chain with the quadratic DP of the longest increasing subsequence; with
`L` diagonals the length is `100·(N + M − 2L) + 100√2·L`. `O(K²)`.

Pitfalls:

- two blocks in the same row or column cannot both be used: the chain
  must increase strictly in both coordinates;
- blocks may repeat in the input;
- the length is never exactly halfway between integers, since
  `100√2·L` is irrational for `L > 0`, so ordinary rounding is safe.

The answers were checked against a DP over all `(N + 1)(M + 1)` crossings
of the grid, each reached from the west, from the south or along a
diagonal, on every test and 60 random grids.

## Language notes

- All languages run the same quadratic DP.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1119_dp.cpp](1119_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.031 s | 212 KB |
| [1119_dp.go](1119_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.031 s | 1136 KB |
| [1119_dp.java](1119_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.187 s | 3928 KB |
| [1119_dp.py](1119_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.078 s | 504 KB |
| [1119_dp.rs](1119_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.031 s | 232 KB |
