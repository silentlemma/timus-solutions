# 1437. Gasoline Station

[Timus 1437](https://acm.timus.ru/problem.aspx?space=1&num=1437) · difficulty 493 · bfs

Original problem by Alexey Lakhtin, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three cans hold from 0 to 255 litres each. The pump can only fill a can
to the brim, petrol may be poured from one can into another until the
first is empty or the second is full, and nothing may be spilled. Only
after all pouring, some of the cans are emptied into the tank. How many
different positive volumes can the tank receive?

Time limit: 1 second. Memory limit: 64 MB.

## Input

The three capacities, one per line.

## Output

The number of volumes.

## Examples

### Example 1

Input:

```
0
3
4
```

Output:

```
6
```

## Solution

Search all states (x, y, z) of the cans from all empty, with three
moves to fill a can and six moves to pour one can into another. After
any move some can is empty or full, so at most about 3·2·256² of
the 256³ states can be reached. Every reached state gives the sums of
its non-empty subsets of cans as volumes for the tank; count the
distinct positive ones. For capacities a, b, c, let P=(a+1)(b+1)(c+1),
V=a+b+c+1 and S be the number of reached states. Including flag
initialization, time is `O(P)` on average, or `O(P + S log V)` in C++
with its ordered set.

Pitfalls:

- zero litres does not count (tests 01, 03);
- a can that is already full cannot take more, so in the example 5
  litres cannot be made (test 01);
- three equal cans are always empty or full (test 05).

## Optimized solutions

C++ and Go keep every original fill/pour transition but store visited states only on the boundary of the capacity box. Each move fills a can, empties its donor, or fills its receiver. Choose the first empty/full can as a canonical face and encode the two other amounts; edges and corners therefore get only one visited bit. With U=256, six U² faces need 49152 bytes of bitmap. A 24-bit amount triple fits uint32; the fixed queue has at most six U² entries (1572864 bytes). A 766-byte flag array replaces the volume set. All seven subset sums are checked, zero excluded; no petrol is discarded during search. For S reached states, time O(U²+S), space O(U²), including fixed-array initialization. All simple implementations remain; Java, Python and Rust reuse admitted bases.

The accepted base implementations [1437_bfs.java](1437_bfs.java), [1437_bfs.py](1437_bfs.py), [1437_bfs.rs](1437_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1437_bfs.cpp](1437_bfs.cpp) | G++ 13.2 x64 | bfs | O(P + S log V) | AC | 0.031 s | 16164 KB | 11286236 |
| [1437_bfs.go](1437_bfs.go) | Go 1.14 x64 | bfs | O(P) | AC | 0.046 s | 10572 KB | 11286237 |
| [1437_bfs.java](1437_bfs.java) \* | Java 1.8 | bfs | O(P) | AC | 0.156 s | 20420 KB | 11286239 |
| [1437_bfs.py](1437_bfs.py) \* | Python 3.12 x64 | bfs | O(P) | AC | 0.406 s | 17212 KB | 11286238 |
| [1437_bfs.rs](1437_bfs.rs) \* | Rust 1.75 x64 | bfs | O(P) | AC | 0.062 s | 3104 KB | 11286240 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1437_bfs_optimized.cpp](1437_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(U² + S) | AC | 0.015 s | 332 KB | 11315367 |
| [1437_bfs_optimized.go](1437_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(U² + S) | AC | 0.015 s | 1140 KB | 11315371 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
