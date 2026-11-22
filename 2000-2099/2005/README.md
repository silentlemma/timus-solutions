# 2005. The Shortest Allowed Five-Stop Route

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · difficulty 94 · bruteforce

Original problem by Mikhail Rubinchik. (Prepared by Oleg Merkurev), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Visit five locations exactly once, starting at 1 and finishing at 5.
Location 3 must not be the penultimate stop. Given distances between
every pair, find a route of minimum total distance and its length. Any
optimal allowed route is acceptable.

## Input

A 5 by 5 integer distance matrix. Every entry is between 0 and 10000,
diagonal entries are zero, distances are symmetric and satisfy the
triangle inequality: `d[i][j]≤d[i][k]+d[k][j]`. Time limit 0.5 seconds,
memory 64 MB.

## Output

On the first line print the minimum total distance. On the second print
the five location numbers in visiting order, separated by spaces. Ties
may be resolved arbitrarily.

## Checking

A checker verifies that the route is allowed, that the printed length is
its length and that it is optimal; any optimal route is accepted.

## Examples

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

The displayed route costs `2600+5300+1900+3700=13500`; its penultimate
stop is 4, so it obeys the restriction.

## Solution

Point 1 is first and point 5 is last, so only the order of points 2, 3
and 4 varies: six orders, of which the two with 3 just before 5 are
forbidden. Try the four others, add up the four distances of each route,
and keep the shortest. `O(1)`.

Pitfalls:

- the rule concerns the stop just before the last one;
- a route costs from 0 to 40 000, so the minimum starts from "none yet",
  not from 0 or 10 000.

## Optimized solutions

`2005_bruteforce_optimized.py`. Python keeps exhaustive search over the same four legal routes. itertools.permutations generates the six orders of the three middle points in C, then rejects the two with forbidden penultimate point; the cost matrix stays flat with 25 integers. This version intentionally uses permutation tuples again instead of the earlier Python nested loops, while avoiding the teaching matrix row copies and module-level state. Print any optimal tied route through one binary output block and exit inside main. The fixed five-point problem has O(1) time and storage; no route-answer lookup is used and teaching sources remain.

Exact-source Python 3.12 x64 Accepted #11327537: 0.078 s / 732 KB. Saved 2026-11-20 compiler-cohort comparison: time 7/50, memory 43/50. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325492 (PyPy 3.10 x64) was 0.109 s / 212 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2005_bruteforce_optimized.py`: 0.078 s / 732 KB; retained teaching base `2005_bruteforce.py`: 0.093 s / 432 KB.

`2005_bruteforce_optimized.java`. Java still exhaustively checks every allowed five-point route. Choose the penultimate zero-based vertex c from {1,3}, then either remaining a; the last middle vertex is b=6-a-c. These are exactly the four legal routes, without 27 triples and filtering. A flat 25-int matrix replaces nested arrays, and only the winning cost and three middle indices are retained during the search; one result array is made afterwards. Primitive byte input/output replaces generic parsing and formatting. Any tied optimal witness is valid. This fixed five-point problem uses O(1) time and space.

Exact-source Java 1.8 Accepted #11327443: 0.078 s / 360 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/170, memory 3/170. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324781 was 0.125 s / 496 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2005_bruteforce_optimized.java`: 0.078 s / 360 KB; retained teaching base `2005_bruteforce.java`: 0.125 s / 1616 KB.

`2005_bruteforce_optimized.rs`. Keep exhaustive routes on five points, but read directly into a fixed 25-cell i64 cost array and derive the third middle vertex as 6-a-b. This replaces the redundant third loop and retained parsed-input vector. Emit the five route vertices directly instead of allocating formatted strings. The same four admissible routes and tie order remain, with wider exact cost arithmetic. Work and storage are bounded constants.

Compared with `2005_bruteforce.rs`: time 0.031 s → 0.015 s; memory 236 KB → 48 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2005_bruteforce_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11303437 |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1104 KB | 11303440 |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1616 KB | 11303442 |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 432 KB | 11303445 |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 236 KB | 11303446 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2005_bruteforce_optimized.java](2005_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(1) | AC | 0.078 s | 360 KB | 11327443 |
| [2005_bruteforce_optimized.py](2005_bruteforce_optimized.py) \* | Python 3.12 x64 | bruteforce | O(1), fixed five points | AC | 0.078 s | 732 KB | 11327537 |
| [2005_bruteforce_optimized.rs](2005_bruteforce_optimized.rs) \* | Rust 1.75 x64 | bruteforce | O(1), fixed five points | AC | 0.015 s | 48 KB | 11325508 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
