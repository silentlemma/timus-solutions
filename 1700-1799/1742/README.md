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

The compact versions store incoming counts only up to two. Zero identifies a start, and a cycle is isolated exactly when every member has count one. A byte per vertex records whether it is unseen, on the current walk, or finished. After counting any cycle found, follow the same arrows again to mark the walk as finished. Each vertex is visited only a constant number of times, and no separate array of vertices on the walk is needed.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 2 088 KB versus 5148 KB.

The accepted base implementations [1742_graphs.java](1742_graphs.java), [1742_graphs.py](1742_graphs.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1742_graphs.cpp](1742_graphs.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.078 s | 2344 KB | 11289502 |
| [1742_graphs.go](1742_graphs.go) | Go 1.14 x64 | graphs | O(n) | AC | 0.078 s | 8728 KB | 11289503 |
| [1742_graphs.java](1742_graphs.java) \* | Java 1.8 | graphs | O(n) | AC | 0.140 s | 2020 KB | 11289505 |
| [1742_graphs.py](1742_graphs.py) \* | Python 3.12 x64 | graphs | O(n) | AC | 0.187 s | 13504 KB | 11289504 |
| [1742_graphs.rs](1742_graphs.rs) | Rust 1.75 x64 | graphs | O(n) | AC | 0.015 s | 5148 KB | 11289506 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1742_graphs_optimized.cpp](1742_graphs_optimized.cpp) \* | G++ 13.2 x64 | graphs | O(n) | AC | 0.062 s | 576 KB | 11310429 |
| [1742_graphs_optimized.go](1742_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(n) | AC | 0.046 s | 2084 KB | 11310371 |
| [1742_graphs_optimized.rs](1742_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 2088 KB | 11310368 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
