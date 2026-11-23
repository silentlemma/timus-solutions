# 1182. Two teams of mutual acquaintances, as equal as possible

[Timus 1182](https://acm.timus.ru/problem.aspx?space=1&num=1182) · difficulty 507 · graphs

Original problem by Vladimir Kotov and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`2 ≤ N ≤ 100` persons each list whom they know; knowing need not be
mutual. Split everyone into two non-empty teams so that in each team
every member knows every other member, with team sizes as close as
possible, or say that no split exists.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then for each person the list of persons they know, ending with 0.

## Output

`No solution`, or two lines, each with a team size and its members.

## Checking

Any split is accepted if both teams are non-empty, cover everyone, are
groups of mutual acquaintances and differ in size as little as possible;
the checker takes the best difference from the stored answer.

## Examples

### Example 1

Input:

```
5
3 4 5 0
1 3 5 0
2 1 4 5 0
2 3 5 0
1 2 3 4 0
```

Output:

```
No solution
```

### Example 2

Input:

```
5
2 3 5 0
1 4 5 3 0
1 2 5 0
1 2 3 0
4 3 2 1 0
```

Output:

```
3 1 3 5
2 2 4
```

## Solution

Call two persons strangers unless each knows the other. Strangers must
be in different teams, so the strangers graph must be bipartite, which a
breadth-first colouring checks; an odd cycle means `No solution`. Each
connected component of that graph has two sides, and its sides must go to
different teams, either way round. Persons in different components know
each other both ways, so any combination of choices is valid.

What remains is a knapsack: `reach[k][s]` says whether the first `k`
components can give the first team exactly `s` persons, and remembers the
side used. Take the reachable `s` closest to `N/2` and walk back to
collect the teams. `O(N²)`.

Pitfalls:

- knowing is one-way in the input, so a pair counts as acquainted only if
  both list each other;
- a component of one person can join either team, which is what lets the
  sizes even out;
- both teams are automatically non-empty: a component with strangers has
  both sides non-empty, and single persons are spread by the knapsack.

The answers were compared with a separately written solution on 300
random groups of up to 41 persons, twelve of them without a solution, and
every printed split passed the checker.

## Optimized solutions

Go and Rust keep the same complement-graph bipartition and component-orientation knapsack. A pair is incompatible unless both directed acquaintance entries exist. Store each row in two 64-bit words in Go or one u128 in Rust. During BFS, intersect a row with its own colour mask to detect a conflict; enumerate only unseen neighbours with trailing-zero scans. Each component stores its two member masks and sizes a,b. Update reachable sizes as (old<<a)|(old<<b), retaining one small history mask per component. Swapping the team names lets us take the first team size s≤floor(N/2). Its size difference is N−2s, so choose the largest reachable s≥1. If none exists there is no split into two nonempty teams. Recover each orientation by checking the preceding history. N≤100 fits all size masks in 128 bits. Time O(N²), dominated by input/pair checks; packed rows and history replace bool and integer matrices. All simple sources remain; the other three families reuse admitted bases.

The accepted base implementations [1182_graphs.cpp](1182_graphs.cpp), [1182_graphs.java](1182_graphs.java), [1182_graphs.py](1182_graphs.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1182_graphs_optimized.java`. Retain the archived algorithm, replacing Scanner with buffered byte input. Output avoids Formatter where ordinary numeric conversion suffices. EOF is stable even without a final newline; the simple source remains unchanged.

Accepted #11328638 (Java 1.8): **0.109 s / 652 KB**. Archived comparison: `1182_graphs.java` (Java 1.8) — 0.171 s / 5732 KB (#11283340).

## Language notes

Original ports keep the acquaintance matrix and scalar knapsack. New Go/Rust use packed rows and reachability histories; Go explicitly handles shifts across64 bits, Rust uses u128. Reconstruction retains component membership, tests mutual acquaintance, and excludes empty teams.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1182_graphs.cpp](1182_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 280 KB | 11283330 |
| [1182_graphs.go](1182_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1400 KB | 11283331 |
| [1182_graphs.java](1182_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.171 s | 5732 KB | 11283340 |
| [1182_graphs.py](1182_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.078 s | 1332 KB | 11283339 |
| [1182_graphs.rs](1182_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 384 KB | 11283341 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1182_graphs_bitmask.go](1182_graphs_bitmask.go) \* | Go 1.14 x64 | graphs, bitmask | O(N²) | AC | 0.031 s | 816 KB | 11315485 |
| [1182_graphs_bitmask.rs](1182_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(N²) | AC | 0.015 s | 204 KB | 11315493 |
| [1182_graphs_optimized.java](1182_graphs_optimized.java) | Java 1.8 | graphs | O(N²) | AC | 0.109 s | 652 KB | 11328638 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
