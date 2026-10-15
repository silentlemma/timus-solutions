# 1693. Loyd's Problem

[Timus 1693](https://acm.timus.ru/problem.aspx?space=1&num=1693) · difficulty 9125 · constructive

Original problem by Sam Loyd and Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Cut an n × n chessboard along the grid into as many connected parts as
possible so that no two parts are the same. Parts that differ only by a
rotation are the same, but the colours of the cells count: a black cell
and a white cell are two different parts.

## Input

n (1 ≤ n ≤ 30).

## Output

The number of parts, then n rows of n lowercase letters. Each part is
written with one letter, and parts that share an edge use different letters.
Any optimal cutting is accepted.

## Examples

### Example 1

Input:

```
8
```

Output:

```
18
aaaacaaa
bbbcccba
baddabbb
aacdacba
accdacaa
babdccbb
baaadbba
babbaaaa
```

## Solution

**The bound.** Count the coloured pieces of each area up to rotation:
2 of area 1, 1 of area 2, 4 of area 3, 10 of area 4, 36 of area 5,
110 of area 6, and 392 of area 7. Distinct parts have total area at
least the sum of the k smallest of these areas, so k is at most the
largest number whose smallest-areas sum fits into n². For n = 8 that
is 2 + 1 + 4 + 10 = 17 pieces of area up to 4, total area 56, and one
more part made of the 8 remaining cells, which gives 18.

**The construction.** The bound is reached for every allowed n by a
suitable packing of distinct coloured pieces. Packing up to 163 pieces
exactly into the square is a hard search, though. So the cuttings for
all 30 sizes were found once, offline, by a
randomized depth-first search with restarts, and the program prints
the stored board for the given n.
`O(n²)`.

Every stored board was checked independently. Its one-letter regions
are connected parts, all different up to rotation with the colours
kept, and their number equals the bound above. The piece counts per
area were recomputed by enumerating polyominoes.

Pitfalls:

- the colours matter, so there are two single cells, not one;
- reflections are not allowed as equivalences, only rotations;
- a letter may be reused by parts that do not share an edge.

The checker rebuilds the parts from the letters and verifies the count
and the pairwise differences.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1693_constructive.cpp](1693_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 140 KB |
| [1693_constructive.go](1693_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1084 KB |
| [1693_constructive.java](1693_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 1784 KB |
| [1693_constructive.py](1693_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1100 KB |
| [1693_constructive.rs](1693_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 220 KB |
