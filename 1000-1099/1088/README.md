# 1088. The distance between two forks in a binary tree of roads

[Timus 1088](https://acm.timus.ru/problem.aspx?space=1&num=1088) · difficulty 751 · trees

Original problem by Oleg Kats, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

From the first stone the road forks left and right every hour, and after
`F` hours every branch reaches a pier on the sea. The piers are numbered
so that always turning right leads to pier 1, turning left only at the
last fork leads to pier 2, turning left only at the fork before last
leads to pier 3, and so on. Ilya stands at the fork `E` hours from the
sea on the way to pier `Ep`; the magic stone is the fork `D` hours from
the sea on the way to pier `Dp`. His horse can ride at most `H` hours,
one hour per road. Can Ilya reach the magic stone? (`0 ≤ D, E, F, H ≤ 30`,
`1 ≤ Dp, Ep ≤ 2^30`.)

Time limit: 1 second. Memory limit: 64 MB.

## Input

`D`, `E`, `F`, `Dp`, `Ep` and `H`.

## Output

`YES` or `NO`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1 2 3 2 6 4
```

Output:

```
YES
```

## Solution

The roads form a complete binary tree of depth `F`. The numbering says
that `p − 1`, written in `F` binary digits, is the path to pier `p`: the
highest digit is the first fork, and 1 means a left turn. A fork `k`
hours from the sea on the way to pier `p` is the same path without its
last `k` turns: the number `(p − 1) >> k` at depth `F − k`.

So Ilya is the node `a = (Ep − 1) >> E` at depth `F − E`, and the stone is
`b = (Dp − 1) >> D` at depth `F − D`. Lift the deeper one to the depth of
the other with right shifts, one hour each, then lift both together, two
hours per step, until the numbers are equal: that is their lowest common
fork. Compare the hours with `H`. `O(F)`.

Pitfalls:

- the piers count from 1, so the path is `p − 1`, not `p`;
- the two forks may be at different depths, and one of them may be the
  ancestor of the other;
- the numbers go up to `2^30`, which fits 32-bit signed integers, but the
  solutions use 64 bits to keep `p − 1` and the shifts simple.

The answers were checked by writing both paths as strings of turns and
counting the roads through their longest common prefix.

## Language notes

- Rust destructures the six numbers with a slice pattern and `let else`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1088_trees.cpp](1088_trees.cpp) | G++ 13.2 x64 | trees | O(F) | AC | 0.015 s | 376 KB |
| [1088_trees.go](1088_trees.go) | Go 1.14 x64 | trees | O(F) | AC | 0.031 s | 1076 KB |
| [1088_trees.java](1088_trees.java) | Java 1.8 | trees | O(F) | AC | 0.109 s | 1604 KB |
| [1088_trees.py](1088_trees.py) | Python 3.12 x64 | trees | O(F) | AC | 0.093 s | 388 KB |
| [1088_trees.rs](1088_trees.rs) | Rust 1.75 x64 | trees | O(F) | AC | 0.031 s | 220 KB |
