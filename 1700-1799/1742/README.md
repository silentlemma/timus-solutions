# 1742. Team building

[Timus 1742](https://acm.timus.ru/problem.aspx?space=1&num=1742) · difficulty 312 · graphs

Original problem by Artyom Ripatti, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n programmers names the colleague they consider the strongest,
possibly themselves. Groups are formed one at a time: pick any
programmer not yet in a group, then keep adding the named colleague of
the last one added while that colleague is still free. Find the fewest
and the most groups this can give.

## Input

n (1 ≤ n ≤ 10⁵), then the number named by each programmer.

## Output

The fewest and the most groups.

## Examples

### Example 1

Input:

```
4
2
3
4
2
```

Output:

```
1 2
```

## Solution

The names form a graph where every programmer has one arrow out: trees
that lead into cycles. A group is a walk along the arrows.

- Fewest: a programmer that nobody names can only be in a group that
  starts with them, and so can a cycle that nobody outside points into;
  starting from those, every walk runs on until it meets a group, so
  each of them gives exactly one group and nothing else is needed.
- Most: once a walk enters a cycle, it goes all the way round, so each
  cycle is one group at best. Taking the cycles first and then everyone
  else from the cycles outwards, each other programmer can form a group
  alone.

So the answers are (programmers nobody names) + (cycles nobody points
into) and (programmers off the cycles) + (cycles). Following the arrows
from each new programmer while marking the walk finds every cycle once.
`O(n)`.

In the example, 2 → 3 → 4 → 2 is a cycle and 1 points into it: starting
from 1 takes everyone, while starting on the cycle leaves 1 alone.

Pitfalls:

- a programmer who names themselves is a cycle of one;
- a cycle with a tree hanging on it needs no group of its own for the
  minimum;
- the walks must be followed with a loop, not recursion, since a chain
  can be 10⁵ long.

The answers match a search over every order of choosing on 300 random
graphs of up to 8 programmers, and an independent accepted
implementation on the large tests.

## Optimized solutions

Formatting-only accepted revisions: `1742_graphs.cpp` #11327489, `1742_graphs.py` #11327491, `1742_graphs.rs` #11327493. Each table row uses that exact file revision and its own paired time/memory; no performance improvement is attributed to formatting.

`1742_graphs_optimized.cpp`. Keep the linear functional-graph traversal and saturated indegree counts 0/1/2. A byte state marks fresh, walking and finished vertices; follow a completed walk again to clear it without a path array. The C++ revision reads integers from a fixed 4096-byte fread buffer instead of formatted per-number input. O(n) time and O(n) graph storage; no new graph algorithm or duplicate source is introduced.

Exact-source G++ 13.2 x64 Accepted #11326976: 0.015 s / 532 KB. Saved 2026-11-20 compiler comparison: time 1/53, memory 1/53; top-ten targets pass in both metrics, so no asterisk. Below 1024 KB, strict admission uses time only. Previous optimized run #11310429: 0.062 s / 576 KB. These are independent paired runs; the new recorded memory is lower. The retained teaching C++ source's own current Accepted #11327489 is 0.093 s / 2324 KB; its algorithm is unchanged.

The compact versions store incoming counts only up to two. Zero identifies a start, and a cycle is isolated exactly when every member has count one. A byte per vertex records whether it is unseen, on the current walk, or finished. After counting any cycle found, follow the same arrows again to mark the walk as finished. Each vertex is visited only a constant number of times, and no separate array of vertices on the walk is needed.

Rust optimized / retained teaching base: Accepted #11310368 0.031 s / 2088 KB; Accepted #11327493 0.031 s / 5168 KB.

Retained accepted teaching sources [1742_graphs.java](1742_graphs.java), [1742_graphs.py](1742_graphs.py) also meet the strict top-ten or top-15% criterion on the required metrics in the saved comparison. The current exact paired measurements are in the table, including the formatting-only revisions. Their algorithms are unchanged and no identical optimized copies are added. The asterisk denotes the separate language rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1742_graphs.cpp](1742_graphs.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.093 s | 2324 KB | 11327489 |
| [1742_graphs.go](1742_graphs.go) | Go 1.14 x64 | graphs | O(n) | AC | 0.078 s | 8728 KB | 11289503 |
| [1742_graphs.java](1742_graphs.java) \* | Java 1.8 | graphs | O(n) | AC | 0.140 s | 2020 KB | 11289505 |
| [1742_graphs.py](1742_graphs.py) \* | Python 3.12 x64 | graphs | O(n) | AC | 0.156 s | 13532 KB | 11327491 |
| [1742_graphs.rs](1742_graphs.rs) | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 5168 KB | 11327493 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1742_graphs_optimized.cpp](1742_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.015 s | 532 KB | 11326976 |
| [1742_graphs_optimized.go](1742_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(n) | AC | 0.046 s | 2084 KB | 11310371 |
| [1742_graphs_optimized.rs](1742_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 2088 KB | 11310368 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
