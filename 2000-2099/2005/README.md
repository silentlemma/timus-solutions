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

`2005_bruteforce_optimized.py`. Keep exhaustive route enumeration, but store the 5×5 cost matrix flat and derive the third middle vertex as 6-a-b after choosing distinct a,b from 1,2,3. Reject middle vertex 2 immediately before the finish. The same four legal routes are considered in the same order, so tied choices remain valid. Avoid permutation tuples and matrix row copies; the fixed five-point problem has constant time and storage. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `2005_bruteforce.py`: time 0.093 s → 0.109 s; memory 432 KB → 212 KB.

`2005_bruteforce_optimized.rs`. Keep exhaustive routes on five points, but read directly into a fixed 25-cell i64 cost array and derive the third middle vertex as 6-a-b. This replaces the redundant third loop and retained parsed-input vector. Emit the five route vertices directly instead of allocating formatted strings. The same four admissible routes and tie order remain, with wider exact cost arithmetic. Work and storage are bounded constants.

Compared with `2005_bruteforce.rs`: time 0.031 s → 0.015 s; memory 236 KB → 48 KB.

`2005_bruteforce_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `2005_bruteforce.java`: time 0.125 s → 0.125 s; memory 1616 KB → 496 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2005_bruteforce_optimized.java`: time place 106/170, memory place 13/170 in this comparable sample.

`2005_bruteforce_optimized.py`: time place 33/50, memory place 1/50 in this comparable sample.

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
| [2005_bruteforce_optimized.java](2005_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 496 KB | 11324781 |
| [2005_bruteforce_optimized.py](2005_bruteforce_optimized.py) \* | PyPy 3.10 x64 | bruteforce | O(1), fixed five points | AC | 0.109 s | 212 KB | 11325492 |
| [2005_bruteforce_optimized.rs](2005_bruteforce_optimized.rs) \* | Rust 1.75 x64 | bruteforce | O(1), fixed five points | AC | 0.015 s | 48 KB | 11325508 |


\* Accepted; the rating target is not yet met. This version may be optimized further.
