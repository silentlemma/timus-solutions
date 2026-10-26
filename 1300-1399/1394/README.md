# 1394. Ships. Version 2

[Timus 1394](https://acm.timus.ru/problem.aspx?space=1&num=1394) · difficulty 14802 · backtracking

Original problem prepared by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The same task as [problem 1115](../../1100-1199/1115/README.md) with a
much harder set of tests: N < 100 ships with integer lengths from 1 to
100 fill 1 < M < 10 rows of given lengths exactly, every row with at
least one ship. A placement exists; print one. The judge keeps at most
20 tests, each chosen to beat some kind of heuristic, and no test is
meant to beat all of them.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then N lines with the ship lengths, then M lines with the row
lengths.

## Output

For every row, in input order, two lines: the number of ships in it and
their lengths.

## Examples

### Example 1

Input:

```
5 2
4
10
2
5
3
11
13
```

Output:

```
3
5 4 2
2
10 3
```

## Solution

Exact multi-way partitioning is hard in general, and the judge's tests
are chosen to beat single heuristics.

Backtracking cycles three exact searches through five slots: B, B with
the rows in increasing length, C, D and B again. Time slices grow
1.6-fold up to a cap and later rounds perturb the orders, until one
search places all ships or the internal cutoff comes.

- B, rows one at a time. Ships go longest first; inside a row each ship
  is taken or skipped, and the copies of a skipped length are skipped
  together. Every open row must stay a subset sum of the unused ships
  (bitsets of suffix sums, rebuilt when a row opens). A failed state,
  the unused ships plus the open rows, goes into a hash table that
  survives restarts, since it does not depend on the order. Every other
  B slot also checks residues for D's moduli and small moduli.
- C, B over the rare lengths only (at most one to three copies): a row
  then needs a remainder that the common ships can make, and a nested B
  places the common ships at the end. This avoids the many
  interchangeable ways to fill rows with common ships.
- D, C where "rare" means not divisible by a modulus K that divides many
  ships, plus an exact residue check: the remaining non-multiples of
  each residue must split among the remaining rows so that every row
  gets its length modulo K. A DP over rows and count vectors (in mixed
  radix) answers it, with a budget per query and a cache that survives
  restarts.

All three are needed: without C the judge's test 8 runs out of time,
without D its test 10, and with B in two slots of four instead of three
of five its test 7. A fourth search, ships one at a time into rows, was
not needed.

S is the total ship length.

Pitfalls:

- on the fleet from the forum's test 70, with a row of 820, plain
  restarts find nothing in 20 seconds (test 03); the forum's test 80 is
  hard for other orders (test 04);
- residue puzzles: almost all ships multiples of some k and one special
  ship per row whose residue constrains the row assignments (generated
  tests 7 and 8);
- fleets that only the row-by-row search B solves, and only in a lucky
  order, while C and D fail (tests 14 and 15);
- the rows must be printed in input order.

The placements pass the checker on all the tests here, on 130 hard
fleets and on 11 000 generated fleets (6 000 of them with equal rows):
backtracking within 0.55 s and 0.08 s, on the hard and the generated
fleets.

## Language notes

- Backtracking in Python exceeded the limit on the judge's test 7 in
  four versions, each built around a different main search, so Python
  has no solution here.
- The backtracking Java needed a closer port to pass the judge's test 8
  within 1 s: the skip branch of a row is a loop, not a tail call, and
  indexes use shifts and masks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1394_backtracking.cpp](1394_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.406 s | 26108 KB |
| [1394_backtracking.go](1394_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.468 s | 28492 KB |
| [1394_backtracking.java](1394_backtracking.java) | Java 1.8 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.546 s | 26652 KB |
| [1394_backtracking.rs](1394_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.453 s | 27520 KB |
