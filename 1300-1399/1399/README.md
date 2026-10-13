# 1399. Economical Director

[Timus 1399](https://acm.timus.ru/problem.aspx?space=1&num=1399) · difficulty 9494 · dp

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

A trip costs only the shortest round through its set of clients, so the
solutions first compute that for every one of the 2ᴹ sets. A Held-Karp
table holds the shortest walk from the depot through each set ending at
each client, 16-bit numbers in 2²⁰·20 cells; walks are extended only
from clients in the set to clients outside it.

Then the plan is a choice of a trip for every item. Start from cheapest
insertion: each item goes to the trip whose round grows the least, or a
new trip, with the capacity respected. Then 300 000 rounds of large
neighbourhood search: take out some items (a few random ones, a whole
trip, or all items of one client), put them back one by one in a random
order by cheapest insertion, and undo the round if the total grew by
more than a threshold that falls linearly from 2% of the first plan to
zero. The best plan seen is printed, with each route read back from the
table. An item insertion costs one look-up per trip, so the search is
cheap next to the table: `O(2ᴹ·M²)` plus the rounds.

Pitfalls:

- items of one client may need several trips (test 03 and generated
  test 6), so the plan is per item, not per client;
- an emptied trip is reused before a new one is opened, or the number of
  trips grows without end during the search;
- the random numbers come from the same xorshift generator and the
  acceptance uses integers only, so C++, Go, Java and Rust print the
  same plan, and the tests can ask for its length; Python, which solves
  the cases of one or two trips exactly, may print a shorter plan.

The plans were compared with the exact optimum, found by a search over
all splits of the items, on 300 random small instances, and all were
optimal; on the example the total is the jury's 34. The tests are judged
by a checker that validates the plan and asks for a total no longer than
the one given in the test.

## Language notes

- Java keeps the subset table only for walks that end inside their set,
  the walks of one set side by side, and fills it by pulling from the
  set without the last client, so it is read and written in order; with
  one slot for every client and set it exceeded the 64 MB limit. It also
  skips clients without items and sets that no trip can carry, draws the
  random numbers without BigInteger, and stops early when the first plan
  is provably optimal: 1.48 s on the judge, where an earlier version
  exceeded the time limit on test 25.

- Python runs under PyPy and computes round lengths only for the sets
  the search asks about, by a dynamic programme over the counts of
  clients that are interchangeable and by branch and bound with one-tree
  lower bounds; when one or two trips suffice it finds the optimal plan
  directly, and otherwise it runs the same search as the other
  languages. Four rounds of such changes brought it from test 17 to test
  24 of the judge, where it still exceeds the time limit (2.03 s): on
  the hardest cases here, twenty clients and loads that nearly fill the
  truck, the subset tables still take about 10⁸ steps, about 0.7 s of
  PyPy alone. It is kept marked TLE: it passes all the tests here but is
  not claimed to be fast enough for every test of the judge.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1399_dp.cpp](1399_dp.cpp) | G++ 13.2 x64 | dp | O(2^M·M^2) | AC | 0.531 s | 44860 KB |
| [1399_dp.go](1399_dp.go) | Go 1.14 x64 | dp | O(2^M·M^2) | AC | 0.906 s | 52476 KB |
| [1399_dp.java](1399_dp.java) | Java 1.8 | dp | O(2^M·M^2) | AC | 1.484 s | 32160 KB |
| [1399_dp.py](1399_dp.py) | PyPy 3.10 x64 | dp | O(2^M·M^2) | TLE (test 24) | 2.031 s | 32636 KB |
| [1399_dp.rs](1399_dp.rs) | Rust 1.75 x64 | dp | O(2^M·M^2) | AC | 0.750 s | 49288 KB |
