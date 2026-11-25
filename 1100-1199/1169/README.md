# 1169. A connected network with exactly K critical pairs of computers

[Timus 1169](https://acm.timus.ru/problem.aspx?space=1&num=1169) · difficulty 725 · constructive

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

## Acceptance update

Refreshed files: [1169_constructive.py](1169_constructive.py), [1169_constructive.rs](1169_constructive.rs), [1169_dp.java](1169_dp.java). Their new exact-source Accepted results are listed in the solution tables. Earlier comparison measurements and rankings for these files refer to preceding source snapshots and are retained as historical evidence. The cached audit confirms qualifying coverage in every available language. Teaching versions are retained for clarity; a source that also serves as the fast version must meet the performance criterion.

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
about 20 million, or far fewer with bitsets.

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

## Optimized solutions

Go uses a one-dimensional unbounded knapsack. For each number of non-critical pairs it minimizes the number of vertices in cycles. Remaining vertices become singletons, and stored cycle sizes reconstruct a solution. Submission 11317280 took 0.031 s and used 1104 KB, versus 0.062 s and 1680 KB for the base.

Rust uses a one-dimensional unbounded knapsack. For each number of non-critical pairs it minimizes the number of vertices in cycles. Remaining vertices become singletons, and stored cycle sizes reconstruct a solution. Submission 11317285 took 0.015 s and used 200 KB, versus 0.031 s and 616 KB for the base.

Java uses a one-dimensional unbounded knapsack. For each number of non-critical pairs it minimizes the number of vertices in cycles. Remaining vertices become singletons, and stored cycle sizes reconstruct a solution. Submission 11317286 took 0.109 s and used 492 KB, versus 0.343 s and 2136 KB for the base.

Python searches cycle sizes in descending order and memoizes failed states by remaining vertices, remaining pairs and largest cycle size. Submission 11317371 took 0.093 s and used 692 KB, compared with 0.109 s and 592 KB for the simple version. In the saved ranking, this submission placed second for time and first for memory.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321735 · Go 1.14 x64 №11322174 · Java 1.8 №11322176 · Python 3.12 x64 №11328267 · Rust 1.75 x64 №11322180.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1169_backtracking_parsing_optimized.py`. Compute only the triangular weights actually visited by exact isqrt-bounded search, avoiding the length-n setup list. Keep safe component-capacity pruning, failed-state memoization and graph reconstruction. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11329235 (Python 3.12 x64): **0.078 s / 988 KB**. Archived comparison: `1169_backtracking.py` (Python 3.12 x64) — 0.093 s / 692 KB (#11317371).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1169_constructive.cpp](1169_constructive.cpp) | G++ 13.2 x64 | constructive | O(N⁴) bit steps | AC | 0.015 s | 236 KB | 11321735 |
| [1169_constructive.go](1169_constructive.go) | Go 1.14 x64 | constructive | O(N⁴) bit steps | AC | 0.062 s | 1680 KB | 11322174 |
| [1169_constructive.java](1169_constructive.java) | Java 1.8 | constructive | O(N⁴) bit steps | AC | 0.343 s | 2136 KB | 11322176 |
| [1169_constructive.py](1169_constructive.py) | Python 3.12 x64 | constructive | O(N⁴) bit steps | AC | 0.078 s | 608 KB | 11330222 |
| [1169_constructive.rs](1169_constructive.rs) | Rust 1.75 x64 | constructive | O(N⁴) bit steps | AC | 0.046 s | 632 KB | 11330223 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1169_dp.go](1169_dp.go) | Go 1.14 x64 | dp | O(N³) | AC | 0.031 s | 1104 KB | 11317280 |
| [1169_dp.rs](1169_dp.rs) | Rust 1.75 x64 | dp | O(N³) | AC | 0.015 s | 200 KB | 11317285 |
| [1169_dp.java](1169_dp.java) | Java 1.8 | dp | O(N³) | AC | 0.109 s | 512 KB | 11330224 |
| [1169_backtracking.py](1169_backtracking.py) | Python 3.12 x64 | backtracking | O(N^5) | AC | 0.093 s | 692 KB | 11317371 |
| [1169_backtracking_parsing_optimized.py](1169_backtracking_parsing_optimized.py) | Python 3.12 x64 | backtracking, parsing | O(N^5) | AC | 0.078 s | 988 KB | 11329235 |
