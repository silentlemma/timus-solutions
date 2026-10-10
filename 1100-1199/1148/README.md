# 1148. The K-th tower in lexicographic order with levels differing by one brick

[Timus 1148](https://acm.timus.ru/problem.aspx?space=1&num=1148) · difficulty 1730 · dp

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tower has `H ≤ 60` levels; the lowest has `M ≤ 10` bricks and every
next level has exactly one brick more or one less than the level below,
never zero. Consider all such towers that use at most `N ≤ 32767` bricks,
written as the list of level widths from the bottom up and ordered
lexicographically. Print how many there are, then the tower with each
given number `K`, counting from 1.

Time limit: 1 second. Memory limit: 4 MB.

## Input

`N`, `H` and `M`, then numbers `K`, one per line, ending with `-1`.

## Output

The number of towers, then the widths of each asked tower.

## Examples

### Example 1

Input:

```
22 5 4
1
10
-1
```

Output:

```
10
4 3 2 1 2
4 5 4 5 4
```

## Solution

Let `count(n, h, m)` be the number of towers of `h` levels whose lowest
level has `m` bricks and that use at most `n` bricks. It is `0` when
`m = 0` or `m > n`, `1` when `h = 1`, and otherwise

`count(n, h, m) = count(n − m, h − 1, m − 1) + count(n − m, h − 1, m + 1)`.

The answer to the first question is `count(N, H, M)`, at most
`2^59`, which fits in 64 bits. The `K`-th tower is read off level by
level: the narrower continuation comes first in lexicographic order, so
if `K` is at most the number of towers that continue with `m − 1`, take
it; otherwise subtract that number and continue with `m + 1`.

The difficulty is memory. A tower of `h` levels starting at `m` never
needs more than `m·h + h(h − 1)/2` bricks, so `n` can be capped there, and
at a given height only widths of one parity, within `M ± (H − h)`, can
occur. Even so, a full table over `(n, h, m)` would take tens of
megabytes. So counts are stored only for every fourth height, about
245 thousand 64-bit values or 2 MB, and the three heights in between are
recomputed by plain recursion, which reaches at most `2⁴ = 16` values of
the next stored height for each stored value. A stored value is computed
once, the first time it is needed.

Pitfalls:

- the count reaches about `4.7·10¹⁷`, so 64-bit integers are needed;
- a level of one brick cannot shrink to zero;
- `n` larger than any tower could use is capped, which keeps the table
  small and the stored values shared;
- `M > N` leaves no towers at all.

The answers were compared with a listing of all towers in order on 200
random inputs with up to 14 levels, and the large tests with an
unranking that memoizes every state.

## Language notes

- All languages store the same sparse table and recurse between its
  layers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1148_dp.cpp](1148_dp.cpp) | G++ 13.2 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 1664 KB |
| [1148_dp.go](1148_dp.go) | Go 1.14 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 3020 KB |
| [1148_dp.java](1148_dp.java) | Java 1.8 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.093 s | 2432 KB |
| [1148_dp.py](1148_dp.py) | Python 3.12 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.625 s | 2480 KB |
| [1148_dp.rs](1148_dp.rs) | Rust 1.75 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 2028 KB |
