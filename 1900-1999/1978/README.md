# 1978. Best vector sum for every cardinality

[Timus 1978](https://acm.timus.ru/problem.aspx?space=1&num=1978) · difficulty 3234 · geometry, sorting

Original problem by Alexander Ipatov, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `n` planar vectors, choose exactly `k` distinct input entries and
maximize the Euclidean length of their sum. Compute the answer for every
`k=1,…,n`. Equal vectors are separate entries; zero and negative
coordinates are allowed.

The limits are `1≤n≤1000` and integer coordinates `−10⁶≤x,y≤10⁶`. Time
limit: 2 seconds; memory limit: 64 MB.

## Input

The first line contains `n`. Each of the next `n` lines contains one pair `x y`.

## Output

Print `n` lines: line `k` gives the maximum length using exactly `k` entries.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
3
3 -2
-3 -2
0 4
```

Output:

```
4.000000
4.000000
0.000000
```

## Solution

For a direction `u`, take the `k` largest scalar projections onto `u`.
Such sets contain an optimum for every cardinality as the direction
rotates. Indeed, if an optimal sum is `s≠0`, any set with a larger
projection onto `s/|s|` would have length greater than `|s|`, a
contradiction. At a tie, a sufficiently small perturbation gives a
projection-maximal set with the same optimal limiting projection. Zero
optima cause no difficulty.

Maintain the vectors in ascending projection order for directions
`(1,t)` as `t` increases from negative to positive infinity. Initially
sort by decreasing `y`, breaking ties by increasing `x`. A prefix gives
a smallest-projection set; its complement gives a largest-projection
set. Recording both covers the opposite half-circle too.

Two vectors with different `y` exchange order at
`t=(x_low−x_high)/(y_high−y_low)`, where `high` has the larger `y`. Sort
these pair events by exact cross multiplication. Equal-`y` pairs do not
cross in the open half-circle, and identical vectors never need an
event.

At an isolated event the pair is adjacent. Swap it and update only the
prefix ending between the two positions. Store each prefix's coordinate
sums and maximize their squared length; also update the complementary
size using the total sum minus the prefix.

Simultaneous events need a batch. Every equal-projection group occupies
a contiguous block and reverses as the direction crosses its event. For
every pair in the batch, form the interval between its current
positions. Merge overlapping intervals, but keep merely adjacent
intervals separate. Reverse each resulting block, rebuild its internal
prefix sums, and record the changed candidates. Prefixes outside a block
keep their sums. Duplicate vectors are handled by these blocks without
special assumptions about distinct points.

Between event directions the projection order is fixed. The initial
state and all batch reversals therefore visit the required
projection-maximal candidates. Every recorded prefix or complement is an
actual subset, so none can exceed the true optimum. Together with the
projection argument, this proves every reported maximum.

There are `O(n²)` pair events. Sorting takes `O(n² log n)` time. The
total size of all reversed blocks is `O(n²)`: a nontrivial block is
connected by its pair events, so its length is at most twice their
count. Sorting starts inside batches fits the same bound. Memory is
`O(n²)`.

In the example, `(0,4)` gives length 4 for one vector. The first two sum
to `(0,−4)`, also length 4. All three sum to zero.

Pitfalls:

- Exactly `k` entries are required, even when adding one decreases the optimum.
- Equal directions can contain several distinct projection groups; do
  not reverse adjacent groups together.
- A tied pair need not be adjacent before the whole batch is processed.
- Compare event slopes exactly; nearly parallel integer directions can
  differ by determinant one.
- Squared sums can reach `2·10¹⁸`; coordinate products and norms require
  64-bit integers.

## Language notes

C++, Go, Java and Rust sort packed pair indices with exact 64-bit cross
products. Java uses primitive arrays and merge sort for the events.

Python does not store the O(n²) events. An optimal set is cut off from
every other distinct vector by a line, and that line can be turned until
it passes through one of the vectors. So for each distinct vector as a
pivot it sorts the other vectors by the slope of their line through the
pivot, turns the line around the pivot and records the set on one side
and its complement at every step, adding the pivot's own copies one at a
time. The coordinate bounds keep distinct slopes far apart compared with
the rounding of doubles, and vectors with equal slopes may be passed in
any order, since every intermediate set is a real subset. Squared
lengths stay exact integers; only the final square roots use floating
point. `O(n² log n)` time and `O(n)` memory. It runs under PyPy, 0.80 s
of the 2 s on the judge; the earlier version with all pair events
exceeded the time limit on the judge's test 7 under CPython and on test
33 under PyPy.

The answers agree with trying all subsets on 14 139 small cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1978_geometry.cpp](1978_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^2 log n) | AC | 0.078 s | 2048 KB |
| [1978_geometry.go](1978_geometry.go) | Go 1.14 x64 | geometry | O(n^2 log n) | AC | 0.218 s | 6416 KB |
| [1978_geometry.java](1978_geometry.java) | Java 1.8 | geometry | O(n^2 log n) | AC | 0.453 s | 7792 KB |
| [1978_geometry.py](1978_geometry.py) | PyPy 3.10 x64 | geometry | O(n^2 log n) | AC | 0.796 s | 9808 KB |
| [1978_geometry.rs](1978_geometry.rs) | Rust 1.75 x64 | geometry | O(n^2 log n) | AC | 0.093 s | 4092 KB |
