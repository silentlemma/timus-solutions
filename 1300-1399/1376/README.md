# 1376. Dean's Pyramid 2

[Timus 1376](https://acm.timus.ru/problem.aspx?space=1&num=1376) · difficulty 12875 · backtracking

Original problem by Alexander Mironenko, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pyramid with a square base of edge A1 and four equal isosceles sides
with lateral edges A2 (both from 0.1 to 10, A2/A1 from 0.9 to 1.9)
stands on its base, centred at the origin with the base edges along the
axes. It rolls over an edge from one face onto a neighbouring face, the
edge staying in place. In at most N rolls (2 ≤ N ≤ 32) bring it back
onto its base with the base centre as close as possible to (X, Y), which
is at least 20.05·A1 away; among equally close endings use the fewest
rolls. Print the distance to 3 decimals, the number of rolls M and the
M + 1 faces it stands on: 0 is the base, 1 to 4 the sides clockwise
from the one facing +y.

Time limit: 2.5 seconds. Memory limit: 64 MB.

## Input

A1, A2, X, Y and N.

## Output

The distance, M, and the faces from the starting 0.

## Examples

### Example 1

Input:

```
10.0 10.0 1000.0 0.0 5
```

Output:

```
972.679
5
0 2 3 4 1 0
```

## Solution

The state is the face on the table and the corners of that face; a roll
reflects or unfolds them over the shared edge. Four rules cover all
rolls: from the base onto side k over the edge of corners k and k + 1;
from a side onto the base, which unfolds a square; and from a side to
the next side clockwise or counterclockwise over a lateral edge, which
reflects the third corner.

The search is exact. One roll moves the centre of the face on the table
by a fixed amount, A1/2 + h/3 between the base and a side (h the height
of a side) and 2·A1·h/(3·A2) between two sides, so a table gives for
every state and number of rolls left how far the centre can still go
and end on the base. A depth-first search over the rolls (never rolling
straight back) cuts every branch that cannot beat the best distance by
the triangle inequality and tries the nearest positions first. A beam
search keeping 4 000 states per depth gives a good first answer, so the
cuts bite at once. `O(3^N)` in the worst case, far less in practice.

Pitfalls:

- the answer is not unique: the example's rolls can be taken in another
  order (test 01), so a checker replays the rolls;
- with N = 2 nothing gets closer and the answer is 0 rolls (test 02);
- on equal distances the number of rolls decides.

The answers match an independent accepted implementation on all the
tests here and on 150 generated ones, and an exhaustive search over all
roll sequences on 240 cases with N up to 8.

## Language notes

- Python bounds the first 8 rolls exactly: from one state of each of the
  17 kinds it plays every sequence of up to 8 rolls and keeps the
  farthest end on the base; beyond, the fixed steps are added as in the
  other languages. A base-side-base roll always comes back, so the old
  bound was far too loose: the search visits 11 to 25 times fewer nodes,
  and a beam of 200 states is enough. The largest tests take 0.25 s with
  CPython; a first version without the exact bounds exceeded 2.5 s on the
  judge's test 5 even under PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1376_backtracking.cpp](1376_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(3^N) worst case | AC | 0.218 s | 7376 KB |
| [1376_backtracking.go](1376_backtracking.go) | Go 1.14 x64 | backtracking | O(3^N) worst case | AC | 0.375 s | 25964 KB |
| [1376_backtracking.java](1376_backtracking.java) | Java 1.8 | backtracking | O(3^N) worst case | AC | 1.203 s | 18948 KB |
| [1376_backtracking.py](1376_backtracking.py) | Python 3.12 x64 | backtracking | O(3^N) worst case | AC | 0.750 s | 2988 KB |
| [1376_backtracking.rs](1376_backtracking.rs) | Rust 1.75 x64 | backtracking | O(3^N) worst case | AC | 0.390 s | 11432 KB |
