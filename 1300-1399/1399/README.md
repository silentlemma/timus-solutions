# 1399. Economical Director

[Timus 1399](https://acm.timus.ru/problem.aspx?space=1&num=1399) · difficulty 8299 · dp, local_search

Original problem by Alexander Ipatov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One truck of capacity Lmax ≤ 3000 delivers N ≤ 50 items from a depot to
M ≤ 20 clients. Every item has a weight and a client, the distances
between the depot and the clients are given and satisfy the triangle
inequality, and every trip starts and ends at the depot. Plan the trips
so that the total distance is small: a plan is accepted if it is no
longer than the one the jury's own program finds.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

M, N and Lmax, the (M+1)×(M+1) distance matrix with the depot as 0,
then the weight and the client of every item.

## Output

The number of trips; then for every trip its items, its load, its route
from 0 back to 0 and its length; then the total length, with blank
lines between the blocks as in the example.

## Examples

### Example 1

Input:

```
7 10 5
0 2 3 4 5 6 5 4
2 0 4 5 6 7 6 5
3 4 0 3 4 5 4 1
4 5 3 0 3 4 1 2
5 6 4 3 0 1 2 3
6 7 5 4 1 0 3 4
5 6 4 1 2 3 0 3
4 5 1 2 3 4 3 0
3 1
5 2
1 3
1 4
2 5
1 6
2 7
1 5
2 2
1 1
```

Output:

```
4

1 10
4
0 1 0
4

4 5 6 8
5
0 4 5 6 0
14

2
5
0 2 0
6

3 7 9
5
0 3 7 2 0
10

34
```

## Solution

A trip's minimum cost depends only on its set of clients. C++, Go and
Rust compute it for all 2ᴹ sets with Held-Karp: 16-bit entries in up to
2²⁰·20 cells store shortest depot paths through each set, ending at
each client; paths extend only outside the set. Java stores feasible
sets and their internal endpoints;
Python estimates tours on demand.

Then the plan is a choice of a trip for every item. Start from cheapest
insertion: each item goes to the trip whose round grows the least, or a
new trip, with the capacity respected. Then up to 300 000 rounds of large
neighbourhood search: take out some items (a few random ones, a whole
trip, or all items of one client), put them back one by one in a random
order by cheapest insertion, and undo the round if the total grew by
more than a threshold that falls linearly from 2% of the first plan to
zero. The best plan seen is printed, with each route read back from the
table in the DP versions.
Here R counts rounds, T trip slots, S cached client sets and B
branch-and-bound calls.

Pitfalls:

- items of one client may need several trips (test 03 and generated
  test 6), so the plan is per item, not per client;
- an emptied trip is reused before a new one is opened, or empty trip
  slots can accumulate with the number of search rounds;
- the random numbers come from the same xorshift generator and the
  acceptance uses integers only, so C++, Go, Java and Rust print the
  same plan; Python searches on a time budget, so its plans can differ
  in length depending on the runtime and machine.

The plans were compared with the exact optimum, found by a search over
all splits of the items, on 300 random small instances, and all were
optimal; on the example the total is the jury's 34. The checker validates
plans and allows totals up to 10 % above the test's value. Python's
acceptance gives no general approximation guarantee.

## Language notes

- Java keeps the subset table only for walks that end inside their set,
  the walks of one set side by side, and fills it by pulling from the
  set without the last client, so it is read and written in order; with
  one slot for every client and set it exceeded the 64 MB limit. It also
  skips clients without items and sets that no trip can carry, draws the
  random numbers without BigInteger, and stops early when the first plan
  is provably optimal: 1.48 s on the judge, where an earlier version
  exceeded the time limit on test 25.

- Python runs under PyPy, avoiding the dense subset table that led to
  2.03 s on judge test 24. It removes unused clients and caches tours
  built from neighbouring sets or cheapest insertion, improved by
  2-opt, moves of up to three clients and restarts that swap adjacent
  segments at three cut points. If all goods fit in one trip, or every
  proper subset of active clients fits with all its goods, it attempts
  exact one- or two-trip solving with one-tree bounds and branch and
  bound, falling back after 10 000 nodes. The main search targets 1.4 s
  of total processor time, checked every 256 rounds, with early stopping
  at a lower bound; its threshold falls by rounds or time, whichever
  runs out first. Exact solving and final tour polishing lie outside
  the clock check: 1.39 s on the judge.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1399_dp.cpp](1399_dp.cpp) | G++ 13.2 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.531 s | 44860 KB |
| [1399_dp.go](1399_dp.go) | Go 1.14 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.906 s | 52476 KB |
| [1399_dp.java](1399_dp.java) | Java 1.8 | dp | O(2^M·M^2 + R·N·T) | AC | 1.484 s | 32160 KB |
| [1399_local_search.py](1399_local_search.py) | PyPy 3.10 x64 | local_search | O(R·N·T + (S+1)·M^3 + B·M^2) | AC | 1.390 s | 11836 KB |
| [1399_dp.rs](1399_dp.rs) | Rust 1.75 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.750 s | 49288 KB |
