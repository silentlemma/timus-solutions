# 1645. Ski Race

[Timus 1645](https://acm.timus.ru/problem.aspx?space=1&num=1645) · difficulty 200 · fenwick

Original problem by Eugene Kurpilyansky and Alexey Samsonov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Skiers 1 to n start one after another, 30 seconds apart, and the final
table ranks them by their own time. Only the order of finishing is
known. For each skier find the best and the worst place they could
take.

## Input

n (1 ≤ n ≤ 2000), then the skiers in the order they finished.

## Output

For each skier i, the best and the worst possible place.

## Examples

### Example 1

Input:

```
6
3 5 1 4 2 6
```

Output:

```
3 6
4 6
1 4
2 5
1 3
1 6
```

## Solution

Skier numbers give start order, with a 30-second gap. Relative to
skier `i`, a later starter finishing earlier is necessarily faster; an
earlier starter finishing later is necessarily slower. The other two
orders allow either comparison. Thus the best possible rank is
`1 + forced_faster`, and the worst is `n − forced_slower`.

These bounds are attainable simultaneously for all undecided opponents
relative to the chosen skier. For the best rank, cluster all earlier
finishes just before its finish, within less than 30 seconds total;
place all later finishes more than `30n` seconds after it. Every earlier
starter who finished earlier then took longer; every later starter who
finished later also took longer. For the worst rank, put all earlier
finishes more than `30n` seconds before it and cluster later finishes
just after it within less than 30 seconds. Every undecided opponent is
then faster. Preserve each group's given strict finish order, and add a
common large offset so all race durations are positive. Durations may
be chosen distinct. The construction is separate for each requested
skier/bound, as required; all skiers need not achieve their extrema in
one race.

Let `p=place[i]` and let `e` count skiers who both started and finished
before `i`. There are `p−1−e` forced faster skiers and `i−1−e` forced
slower ones. The answers are `p−e` and `n−i+e+1`.

Process skiers in start order. A Fenwick tree contains the finish
positions of precisely the earlier starters. Query the prefix through
`p−1` to obtain `e`, print the two ranks, then insert `p`. Querying
before insertion preserves this invariant. Induction proves all counts
and ranks. Time `O(n log n)`, storage `O(n)`. With `n≤2000`, counts and
indices fit ordinary machine integers. Finish order equal to start order
permits every rank; reverse order fixes each rank.

## Checking

Compare the two integer tokens for each skier in start order.
The rank formulas were checked using 10078 exact physical race-time
constructions: best and worst for every target in all permutations
through six skiers, with positive distinct durations and the required
finish order. This validates attainability as well as necessary pairwise
comparisons. Separately, both actual newly formatted C++/Rust programs
passed 996 extra inputs against direct pair counts: all 873 permutations
through six skiers, 120 random races and three maximum-size races. Each
also passed 13 repository inputs in Docker and has its own exact-source
Accepted. The physical witnesses are mathematical checks, not 10078
executions of each native program.

## Language notes

The same Fenwick algorithm remains in all five languages. C++ and
Rust received only exact formatter output, each independently rejudged;
the table uses those new Accepted measurements. Original bytes are kept
in the local revision backup. Go, Java and Python remain byte-identical
to their Accepted archive versions. Formatting is not called an
optimization and no duplicate optimized file is created.

The saved 2 November 2026 snapshot meets the agreed rating goal for every
current language base. C++ uses top 15% or the first ten places in both
metrics; other families require first in both. An empty filtered sample
offers formal coverage, not a proof of superiority. Separate simpler
pair-scan teaching candidates are still awaiting judge confirmation and
are not included as Accepted here.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1645_fenwick.cpp](1645_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.015 s | 184 KB | 11308415 |
| [1645_fenwick.go](1645_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.031 s | 1176 KB | 11288492 |
| [1645_fenwick.java](1645_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.093 s | 652 KB | 11288494 |
| [1645_fenwick.py](1645_fenwick.py) | Python 3.12 x64 | fenwick | O(n log n) | AC | 0.093 s | 852 KB | 11288493 |
| [1645_fenwick.rs](1645_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.046 s | 268 KB | 11308416 |
