# 1169. A connected network with exactly K critical pairs of computers

[Timus 1169](https://acm.timus.ru/problem.aspx?space=1&num=1169) · difficulty 728 · constructive

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Connect `N ≤ 100` computers by two-way connections into one network.
A pair of computers is critical if removing some single connection cuts
them apart. Build a network with exactly `K` critical pairs, or report
that none exists.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`.

## Output

The connections, one pair of computers per line, or `-1`.

## Checking

Any network is accepted if its connections are distinct, join distinct
computers, connect all of them and give exactly `K` critical pairs; the
checker finds the bridges and counts the pairs itself. `-1` must match
the stored answer.

## Examples

### Example 1

Input:

```
7 12
```

Output:

```
1 2
1 3
2 3
3 4
4 5
4 6
4 7
5 6
5 7
6 7
```

## Solution

Removing the bridges of a connected network splits it into
2-edge-connected parts, and two computers form a non-critical pair
exactly when they are in the same part. A part has either one computer or
at least three (two computers need two connections between them), and any
such sizes can be realised: make each part of size `s ≥ 3` a cycle and
join the parts in a chain by single connections, which are the bridges.
So the question is whether `N` splits into sizes from `{1, 3, 4, …}` with
`Σ s·(s − 1)/2 = N·(N − 1)/2 − K`.

That is a small knapsack: `reach[m][t]` says whether `m` computers can be
split with `t` non-critical pairs. Adding a part of size `s` moves
`reach[m − s][t]` to `reach[m][t + s(s − 1)/2]`. Walking back from
`reach[N][target]` recovers the sizes. `O(N²·N²)` bit steps at worst,
about 50 million, or far fewer with bitsets.

Pitfalls:

- a part of two computers does not exist, so for example one triangle
  plus a tree is possible but one non-critical pair is not;
- `N = 1` needs no connections, and the only possible `K` is 0;
- a tree makes every pair critical, a single cycle makes none.

All verdicts were compared with a separately written solution for every
`K` with `N ≤ 12` and for 300 random pairs up to `N = 100`, and every
printed network passed the checker.

## Language notes

- C++ keeps each `reach[m]` as a bitset and Python as a big integer, so a
  part is added with one shift; Go, Java and Rust use plain boolean
  tables.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1169_constructive.cpp](1169_constructive.cpp) | G++ 13.2 x64 | constructive | O(N⁴) bit steps | AC | 0.015 s | 252 KB |
| [1169_constructive.go](1169_constructive.go) | Go 1.14 x64 | constructive | O(N⁴) bit steps | AC | 0.062 s | 1676 KB |
| [1169_constructive.java](1169_constructive.java) | Java 1.8 | constructive | O(N⁴) bit steps | AC | 0.250 s | 2152 KB |
| [1169_constructive.py](1169_constructive.py) | Python 3.12 x64 | constructive | O(N⁴) bit steps | AC | 0.093 s | 572 KB |
| [1169_constructive.rs](1169_constructive.rs) | Rust 1.75 x64 | constructive | O(N⁴) bit steps | AC | 0.046 s | 620 KB |
