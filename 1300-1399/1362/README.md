# 1362. Classmates 2

[Timus 1362](https://acm.timus.ru/problem.aspx?space=1&num=1362) · difficulty 442 · dp

Original problem by Evgeny Krokhalev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An agency of N ≤ 100 000 employees is a tree: everyone but the director
has exactly one boss. Tanya has news, and anyone who knows it can call
their boss or one of their direct subordinates; a call takes one minute,
and one person makes one call at a time. Print the least number of
minutes until the whole agency knows. This is the tree version of
[1323](../1323/README.md).

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then N lines: line K lists the subordinates of employee K and ends
with 0. The last line holds Tanya's number.

## Output

The least number of minutes.

## Examples

### Example 1

Input:

```
10
2 3 0
4 5 7 0
6 9 0
0
0
8 10 0
0
0
0
0
2
```

Output:

```
5
```

## Solution

Calls go both up and down, so the boss is just one more neighbour. Root
the tree at Tanya; then the news enters every subtree once, through its
root.

Let time(v) be the minutes v needs to tell its whole subtree after
learning the news. If v calls its children in some order, the i-th
child hears at minute i and finishes at i + time(child). The best
order calls the slowest subtree first: sort the children's times in
decreasing order t₁ ≥ t₂ ≥ …, and time(v) = max(tᵢ + i). Swapping two
neighbours that are out of this order never hurts, which proves it.

The tree is walked in breadth-first order and the times are computed
from the leaves up, so even a chain of 100 000 needs no recursion.
`O(N log N)`.

Pitfalls:

- the director need not be the root: when Tanya is a subordinate, the news
  goes up and then down other branches (tests 03 and 04);
- a chain of 100 000 is too deep for recursion in most languages
  (generated test 2);
- a star of 100 000 needs 99 999 minutes, one call at a time (generated
  test 3).

The answers were compared with a search over all ways to make calls,
minute by minute, on 400 random trees of up to 8 employees.

## Optimized solutions

The new C++, Go and Rust sources retain decreasing-child-time scheduling. Store the input tree with one original-boss index, first-child index and next-sibling index per employee. Together they enumerate every undirected neighbour without per-vertex containers or duplicate edge objects. Root at the informer using a flat breadth-first order and parent array; the original boss is an ordinary neighbour and the original director may differ. Process that order backwards, collecting child finish times into one reused scratch prefix, sorting descending and taking max(time[i]+i+1). Leaves take zero. All identifiers and times fit 32 bits: a sequential schedule always finishes within N−1 minutes. Time remains O(N log N), packed tree storage O(N), with no recursive traversal. C++ and Go stream input; Rust retains its input string, so its complete storage is O(N+input bytes). All simple files remain; Java and Python reuse admitted bases.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.031 s for the base and uses 3 948 KB versus 15320 KB.

The accepted base implementations [1362_dp.java](1362_dp.java), [1362_dp.py](1362_dp.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1362_dp_optimized.py`. Allocate child-time lists only for non-leaves, sort them in place and compute each parent delay with a direct maximum loop. Leaves share no unnecessary empty lists. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328667 (Python 3.12 x64): **0.312 s / 29520 KB**. Archived comparison: `1362_dp.py` (Python 3.12 x64) — 0.468 s / 33988 KB (#11285503).

## Language notes

These notes describe the simple implementations.

- Java keeps the tree in flat arrays and reads the input byte by byte;
  Go reads it byte by byte too.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1362_dp.cpp](1362_dp.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.171 s | 8896 KB | 11285481 |
| [1362_dp.go](1362_dp.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.093 s | 17784 KB | 11285489 |
| [1362_dp.java](1362_dp.java) | Java 1.8 | dp | O(N log N) | AC | 0.093 s | 6848 KB | 11285508 |
| [1362_dp.py](1362_dp.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.468 s | 33988 KB | 11285503 |
| [1362_dp.rs](1362_dp.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.031 s | 15320 KB | 11285514 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1362_dp_optimized.cpp](1362_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.015 s | 2824 KB | 11315122 |
| [1362_dp_optimized.go](1362_dp_optimized.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.015 s | 4256 KB | 11315125 |
| [1362_dp_optimized.rs](1362_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.046 s | 3948 KB | 11315130 |
| [1362_dp_optimized.py](1362_dp_optimized.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.312 s | 29520 KB | 11328667 |
