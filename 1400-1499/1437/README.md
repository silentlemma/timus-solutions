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

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

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

`1437_bfs_optimized.java`. Keep the same fill/pour BFS but encode each triple as one integer, mark visited states in long-bitsets, and store queue entries in a primitive int array. Let S=(a+1)(b+1)(c+1) and B=S-product(max(0,capacity-1)). Every move leaves a can empty or full, so at most B boundary states can ever be queued; the zero state is included even for zero capacities. Use a boolean array for achievable subset volumes up to C=a+b+c rather than a HashSet. This avoids cloned triples, boxed volumes and object queues. Time including initialization is O(S), auxiliary storage O(S/64+B+C) cells, with the word packing explicit; at capacities<=255 all state indices fit int. Zero volume is omitted from the answer. The compact buffered input is 256 bytes.

Compared with `1437_bfs.java`: time 0.156 s → 0.109 s; memory 20420 KB → 4 004 KB.

C++ and Go keep every original fill/pour transition but store visited states only on the boundary of the capacity box. Each move fills a can, empties its donor, or fills its receiver. Choose the first empty/full can as a canonical face and encode the two other amounts; edges and corners therefore get only one visited bit. With U=256, six U² faces need 49152 bytes of bitmap. A 24-bit amount triple fits uint32; the fixed queue has at most six U² entries (1572864 bytes). A 766-byte flag array replaces the volume set. All seven subset sums are checked, zero excluded; no petrol is discarded during search. For S reached states, time O(U²+S), space O(U²), including fixed-array initialization. All simple implementations remain; Java, Python and Rust reuse admitted bases.

The accepted base implementations [1437_bfs.java](1437_bfs.java), [1437_bfs.py](1437_bfs.py), [1437_bfs.rs](1437_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1437_bfs_optimized.py`. Every noninitial state after filling or pouring has an empty or full vessel. Encode only the six boundary planes in a byte visited array, rather than the entire volume cube; keep the same BFS moves. The state bound becomes O(ab + ac + bc). The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328684 (Python 3.12 x64): **0.281 s / 2860 KB**. Archived comparison: `1437_bfs.py` (Python 3.12 x64) — 0.406 s / 17212 KB (#11286238).

`1437_bfs_optimized.rs`. Retain the archived algorithm and its integer types. Convert decimal integer tokens directly instead of calling the general string parser; negative values are accumulated with their sign so the minimum signed value remains representable. Existing input storage and algorithmic bounds are unchanged.

Accepted #11328552 (Rust 1.75 x64): **0.015 s / 3092 KB**. Archived comparison: `1437_bfs.rs` (Rust 1.75 x64) — 0.062 s / 3104 KB (#11286240).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1437_bfs_optimized.java`: time place 2/17, memory place 2/17 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1437_bfs.cpp](1437_bfs.cpp) | G++ 13.2 x64 | bfs | O(P + S log V) | AC | 0.031 s | 16164 KB | 11286236 |
| [1437_bfs.go](1437_bfs.go) | Go 1.14 x64 | bfs | O(P) | AC | 0.046 s | 10572 KB | 11286237 |
| [1437_bfs.java](1437_bfs.java) | Java 1.8 | bfs | O(P) | AC | 0.156 s | 20420 KB | 11286239 |
| [1437_bfs.py](1437_bfs.py) | Python 3.12 x64 | bfs | O(P) | AC | 0.406 s | 17212 KB | 11286238 |
| [1437_bfs.rs](1437_bfs.rs) | Rust 1.75 x64 | bfs | O(P) | AC | 0.062 s | 3104 KB | 11286240 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1437_bfs_optimized.cpp](1437_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(U² + S) | AC | 0.015 s | 332 KB | 11315367 |
| [1437_bfs_optimized.go](1437_bfs_optimized.go) | Go 1.14 x64 | bfs | O(U² + S) | AC | 0.015 s | 1140 KB | 11315371 |
| [1437_bfs_optimized.java](1437_bfs_optimized.java) | Java 1.8 | bfs | O(S) time; O(S/64+B+C) space | AC | 0.109 s | 4004 KB | 11325435 |
| [1437_bfs_optimized.py](1437_bfs_optimized.py) | Python 3.12 x64 | bfs | O(ab + ac + bc) boundary states | AC | 0.281 s | 2860 KB | 11328684 |
| [1437_bfs_optimized.rs](1437_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(P) | AC | 0.015 s | 3092 KB | 11328552 |
