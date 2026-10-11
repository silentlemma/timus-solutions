# 1229. A second layer of bricks that never repeats the first

[Timus 1229](https://acm.timus.ru/problem.aspx?space=1&num=1229) · difficulty 384 · constructive

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An `N × M` field, both sides even and at most 100, is covered by a layer
of 1 × 2 bricks, each marked by its number in its two cells. Lay a second
layer of such bricks over the whole field so that no brick of the second
layer lies exactly on a brick of the first, or print `-1` if that is
impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`, then `N` rows of `M` numbers: the first layer.

## Output

`N` rows of `M` numbers describing the second layer, or `-1`.

## Checking

Many second layers work, so any is accepted if every number marks
exactly two neighbouring cells and no brick covers the same two cells as
a brick of the first layer.

## Examples

### Example 1

Input:

```
2 4
1 1 2 2
3 3 4 4
```

Output:

```
2 1 1 4
2 3 3 4
```

## Solution

Cut the field into 2 × 2 blocks and cover each with two bricks, either
both lying (one on the top row, one on the bottom row) or both standing
(one in each column). A lying brick can only repeat the first layer if a
first-layer brick fills that row of the block exactly. But then that
brick holds one cell of each column of the block, so no first-layer
brick can fill a column of the block, and standing bricks are safe. So:
lay the bricks flat unless the first layer has a brick on the block's top
or bottom row, and stand them up otherwise. A second layer therefore
always exists, and `-1` is never needed. `O(NM)`.

Pitfalls:

- the first-layer bricks may cross the borders of the 2 × 2 blocks; only
  bricks lying wholly inside a block can be repeated, which is what the
  test looks at;
- the numbering of the second layer is free; numbering block by block is
  enough.

Every output was checked by the checker, and the outputs of a separately
written solution pass it too, on 100 random first layers made by flipping
pairs of bricks.

## Language notes

- All languages scan the 2 × 2 blocks in the same order and number the
  bricks the same way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1229_constructive.cpp](1229_constructive.cpp) | G++ 13.2 x64 | constructive | O(NM) | AC | 0.015 s | 296 KB |
| [1229_constructive.go](1229_constructive.go) | Go 1.14 x64 | constructive | O(NM) | AC | 0.031 s | 1304 KB |
| [1229_constructive.java](1229_constructive.java) | Java 1.8 | constructive | O(NM) | AC | 0.093 s | 960 KB |
| [1229_constructive.py](1229_constructive.py) | Python 3.12 x64 | constructive | O(NM) | AC | 0.062 s | 1384 KB |
| [1229_constructive.rs](1229_constructive.rs) | Rust 1.75 x64 | constructive | O(NM) | AC | 0.015 s | 432 KB |
