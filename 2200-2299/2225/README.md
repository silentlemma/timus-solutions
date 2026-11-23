# 2225. Fewest strikes of a two-nail hammer to drive a row of nails

[Timus 2225](https://acm.timus.ru/problem.aspx?space=1&num=2225) · difficulty 422 · dsu, sorting

Original problem by Vadim Barinov, from the Ural Championship 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N nails stick out by lᵢ centimeters. A strike covers two neighboring
nails: the higher one goes down by 1, or both if they are equally high.
Find the fewest strikes that drive all nails in. The limits are 1 second
and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then l₁ … l_N with 1 ≤ lᵢ ≤ 10⁹.

## Output

The fewest strikes.

## Examples

### Example 1

Input:

```
3
4 1 3
```

Output:

```
7
```

### Example 2

Input:

```
4
2 2 6 6
```

Output:

```
8
```

## Solution

Think of the nails level by level, from the top. At level h the nails
with height at least h form maximal runs of neighbors. A strike lowers
at most two nails, and only two nails of the same height that stand
side by side, so a run of k nails at that level needs ⌈k / 2⌉ strikes,
and driving the runs level by level from the top reaches exactly this
count. The answer is the sum of ⌈k / 2⌉ over all runs of all levels,
which a brute force over small cases also confirms.

There are up to 10⁹ levels, but the runs only change at the heights of
the nails. Process the nails from the highest down and join each one
with already processed neighbors in a disjoint set union. A new nail is
a run of length 1, adding 1 at every level up to its height, so it adds
its height. Joining two runs changes ⌈a / 2⌉ + ⌈b / 2⌉ into
⌈(a + b) / 2⌉, one less exactly when both lengths are odd, and the
joined run lasts for all levels up to the current height, so that join
subtracts the current height.

In the first example the levels hold the runs {1} at height 4, {1} and
{3} at heights 3 and 2, and {1, 2, 3} at height 1, so the answer is
1 + 2 + 2 + 2 = 7.

Sorting makes it O(N log N).

## Optimized solutions

The Go version sums the same level-by-level run cost using a monotone stack, implicitly building a minimum Cartesian tree. Each entry stores a height and the number of positions already merged into its left part. When the next height h is no greater, pop entries and accumulate their widths into span. A popped height t contributes (t−max(h,remaining-top-height))·ceil(span/2): across precisely those levels, its completed contiguous component has span nails. Equal heights merge with zero additional height cost. A zero sentinel finishes all remaining components. Every entry is pushed and popped once, giving O(N) time and O(N) storage without sorting or DSU. Heights and widths fit uint32; the answer needs int64. All original DSU versions remain, with the other four also covering the fast set.

The accepted base implementations [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp), [2225_dsu_sorting.java](2225_dsu_sorting.java), [2225_dsu_sorting.py](2225_dsu_sorting.py), [2225_dsu_sorting.rs](2225_dsu_sorting.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2225_greedy_trees_optimized.py`. Use a monotone stack representing the minimum Cartesian tree. A horizontal layer of a positive run of length L costs ceil(L/2); popping a subtree adds its height difference times that layer cost. Each value is pushed and popped once, replacing sorting/DSU with O(n) time and O(n) storage. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328777 (Python 3.12 x64): **0.187 s / 3924 KB**. Archived comparison: `2225_dsu_sorting.py` (PyPy 3.10 x64) — 0.359 s / 19808 KB (#11295847).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 1788 KB | 11295843 |
| [2225_dsu_sorting.go](2225_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.125 s | 5764 KB | 11295845 |
| [2225_dsu_sorting.java](2225_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.14 s | 2776 KB | 11328353 |
| [2225_dsu_sorting.py](2225_dsu_sorting.py) | PyPy 3.10 x64 | dsu, sorting | O(N log N) | AC | 0.359 s | 19808 KB | 11295847 |
| [2225_dsu_sorting.rs](2225_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 4660 KB | 11295852 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2225_trees.go](2225_trees.go) \* | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1136 KB | 11314953 |
| [2225_greedy_trees_optimized.py](2225_greedy_trees_optimized.py) | Python 3.12 x64 | greedy, trees | O(n) time and space | AC | 0.187 s | 3924 KB | 11328777 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
