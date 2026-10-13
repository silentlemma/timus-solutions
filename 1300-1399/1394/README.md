# 1394. Ships. Version 2

[Timus 1394](https://acm.timus.ru/problem.aspx?space=1&num=1394) · difficulty 27928 · backtracking

Original problem prepared by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The same task as [problem 1115](../../1100-1199/1115/README.md) with a
much harder set of tests: N < 100 ships with lengths from 1 to 100 fill
1 < M < 10 rows of given lengths exactly, every row with at least one
ship. A placement exists; print one. The judge keeps at most 20 tests,
each chosen to beat some kind of heuristic, and no test is meant to beat
all of them.

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
are chosen to beat single heuristics. The solutions run four exact
searches in turns, each in a time slice that grows 1.6 times every
round, with the orders shuffled a little in later rounds, and stop as
soon as one of them places all ships.

- B, rows one at a time. Ships go longest first; inside a row each ship
  is taken or skipped, and the copies of a skipped length are skipped
  together. Every open row must stay a subset sum of the unused ships
  (bitsets of suffix sums, rebuilt when a row opens). A failed state,
  the unused ships plus the open rows, goes into a hash table that
  survives restarts, since it does not depend on the order. Every other
  round B also runs the residue check below for small moduli.
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
- A, ships one at a time into rows, the rarest lengths first. Every
  row's remaining length must be a sum of unplaced ships; a row that
  cannot be completed without the current ship gets it; rows with equal
  remaining lengths are tried once; equal ships go to rows in order; and
  the rows' ship counts must be able to add up (bitsets of the sums of
  exactly c ships).

`O(M^N)` in the worst case, as any exact search.

Pitfalls:

- on the fleet from the forum's test 70, with a row of 820, plain
  restarts find nothing in 20 seconds (test 03); the forum's test 80 is
  hard for other orders (test 04);
- residue puzzles: almost all ships multiples of some k and one special
  ship per row whose residue fixes its row (generated tests 7 and 8);
- the rows must be printed in input order.

The placements pass the checker on all the tests here, on 200 generated
fleets of eight kinds and on a few known hard fleets, each in well under
the limit; an independent accepted implementation solves the same set.

## Language notes

- There is no Python solution: on test 03 PyPy needs about 5 s and
  CPython more than 10 s, against a limit of 1 s.
- Java needed a closer port to pass the judge's test 8 within 1 s: the
  skip branch of a row is a loop, not a tail call; the bitsets of A stop
  at the longest row; indexes use shifts and masks. A first version without
  these exceeded 1 s on that test.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1394_backtracking.cpp](1394_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N) worst case | AC | 0.406 s | 26956 KB |
| [1394_backtracking.go](1394_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N) worst case | AC | 0.515 s | 35124 KB |
| [1394_backtracking.java](1394_backtracking.java) | Java 1.8 | backtracking | O(M^N) worst case | AC | 0.859 s | 49668 KB |
| [1394_backtracking.rs](1394_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N) worst case | AC | 0.406 s | 32072 KB |
