# 1371. Cargo Agency

[Timus 1371](https://acm.timus.ru/problem.aspx?space=1&num=1371) · difficulty 516 · dp

Original problem: idea by Den Raskovalov, prepared by Alexander Klepinin, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 50 000 branches are joined by N − 1 roads into a tree, and every
road has a delivery time from 0 to 1000. Print the average delivery
time over all ordered pairs of different branches, the sum of all
distances divided by N(N − 1), to 4 decimal places.

Time limit: 1 second. Memory limit: 64 MB.

## Input

2 ≤ N ≤ 50000, followed by N−1 triples a,b,c. Endpoints are numbered 1 through N and road times c are integers from 0 through 1000. The roads form a connected tree.

## Output

The average time.

## Checking

Numeric-token comparison (`judging: float:0.0001`): the single output must be finite and satisfy abs(actual−expected) ≤ 0.0001·max(1,abs(expected)). The statement asks for four digits after the decimal point; the repository comparison accepts other numeric spellings within that tolerance.

## Examples

### Example 1

Input:

```
4
1 2 2
2 3 0
3 4 4
```

Output:

```
3.0000
```

## Solution

Count each road once per pair that uses it. Removing a road splits the
tree into parts of s and N − s branches, and exactly the s · (N − s)
pairs with one end in each part go along it. So the sum over ordered
pairs is 2 · Σ c · s · (N − s).

Root the tree at branch 1 and list the branches parents first, by a
breadth-first walk. Read backwards, that list gives the subtree sizes:
each branch adds its size to its parent. `O(N)`.

Pitfalls:

- the sum reaches 4·10¹⁶ on a path of the dearest roads, so it needs
  64-bit integers (generated test 2);
- a path of 50 000 branches is too deep for recursion, hence the
  breadth-first order;
- free roads, with time 0, are allowed (test 03).

The answers were compared with summing all distances by a search from
every branch, on 300 random trees of up to 30 branches.

## Optimized solutions

C++ keeps the same edge-cut sum, storing a flat forward-star tree. Each directed edge has a 32-bit next index, 16-bit target and weight. Parents, parent-edge costs, traversal order and subtree sizes also fit 16 bits because N≤50000 and weights≤1000. An iterative parent-first order is processed backwards; each edge adds weight·s·(N−s), promoted to 64 bits before multiplication. Twice the sum and N(N−1) fit signed 64 bits. Divide into integer part and remainder first. With denominator d and remainder r, the rounded fractional digits are floor((10000r+floor(d/2))/d). A result of 10000 carries into the integer part. This keeps the scaled remainder below 2.5·10¹³ and the rounding error at most 0.00005. Time and space O(N), no recursive traversal or per-vertex edge containers. All simple sources remain; Java/Rust reuse qualifying bases; Go/Python use their distinct optimized sources.

In the earlier comparison snapshot, the base implementations [1371_dp.go](1371_dp.go), [1371_dp.java](1371_dp.java), [1371_dp.py](1371_dp.py), [1371_dp.rs](1371_dp.rs) met the top-15% or top-ten admission rule on both metrics. Their measured results are kept in the Simple table.

Current saved-audit coverage uses Go [1371_dp_optimized.go](1371_dp_optimized.go), #11328658, 0.046 s / 10744 KB: one exact-compiler rival gives limits 0.078 s / 15686.00 KB, both required and passed. The 0.109 s Go base fails time. Python uses PyPy [1371_graphs.py](1371_graphs.py), #11324213, 0.156 s / 5856 KB, both ranks 1/13 in the available current-interpreter cohort; this cohort contains CPython rivals, not an exact-PyPy small sample. The Python base fails memory at rank 11/13. Java base passes both ranks 1/17; Rust base passes both one-rival limits 0.062 s / 13740.20 KB. C++ fast passes both ranks 1/61. Selected versions use at least 1024 KB, so both metrics count. Shared [criteria](../../RATING_CRITERIA.md) exclude memory only strictly below 1024 KB; exactly 1024 KB still requires both. Exclude rivals below 0.015 s and floor only our own time. Meaningful simple files and historical paired measurements remain.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1371_dp_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328658 (Go 1.14 x64): **0.046 s / 10744 KB**. Archived comparison: `1371_dp.go` (Go 1.14 x64) — 0.109 s / 10604 KB (#11285602).

## Language notes

These notes describe the simple implementations.

- Java keeps the tree in flat arrays; all languages print with a dot as
  the decimal point.

Peel leaves from the tree. At a leaf, the XOR accumulators recover its last neighbour and edge weight, so there are no adjacency lists to store. Accepted submission 11324213 took 0.156 s and used 5 856 KB. The simple version took 0.218 s and used 29648 KB.

Only lint-required constants in `1371_dp_optimized.go` were given names; their values, algorithm and comments are unchanged. Accepted #11328658 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1371_dp.cpp](1371_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.078 s | 3976 KB | 11285601 |
| [1371_dp.go](1371_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.109 s | 10604 KB | 11285602 |
| [1371_dp.java](1371_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 3308 KB | 11285604 |
| [1371_dp.py](1371_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.218 s | 29648 KB | 11285603 |
| [1371_dp.rs](1371_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 9444 KB | 11285607 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1371_dp_optimized.cpp](1371_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 1120 KB | 11315476 |
| [1371_graphs.py](1371_graphs.py) | PyPy 3.10 x64 | graphs | O(N) | AC | 0.156 s | 5856 KB | 11324213 |
| [1371_dp_optimized.go](1371_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.062 s | 11812 KB | 11331032 |
