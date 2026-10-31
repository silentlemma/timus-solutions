# 1806. Mobile Telegraphs

[Timus 1806](https://acm.timus.ru/problem.aspx?space=1&num=1806) · difficulty 178 · graphs

Original problem by Pavel Atnashev, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n telegraphs has a distinct ten-digit number. A message can go
from a to b if b differs from a in exactly one digit or by swapping two
digits; it takes cost[l] time, where l is the length of their common
prefix. Find the fastest route from the first telegraph to the last
one, or report that there is none.

## Input

n (2 ≤ n ≤ 50000), then the ten costs from 1 to 10000 in non-increasing
order, then the n numbers; the first is Anka's, the last Chapaev's.

## Output

"-1", or the least time, the number of telegraphs on the route and
their indices from the first to the last.

## Examples

### Example 1

Input:

```
5
100 10 10 10 1 1 1 1 1 1
9123493342
3123493942
9223433942
3223493942
9223433945
```

Output:

```
211
5
1 2 4 3 5
```

### Example 2

Input:

```
2
1 1 1 1 1 1 1 1 1 1
0123493342
0223433945
```

Output:

```
-1
```

## Solution

Run Dijkstra's algorithm from the first telegraph, building the edges
on the fly. A telegraph has at most 90 numbers one changed digit away
and 45 numbers one swap away, and a hash map from numbers to
telegraphs tells which of them exist. For a change at digit p, or a
swap of digits p < q, the common prefix is exactly p, so its cost is
cost[p]. With the numbers stored as integers, a neighbour is the
number plus a multiple of a power of ten. The search stops when the
last telegraph leaves the queue, and the route is read back along the
predecessors. `O(135·n log n)`.

In the first example the route swaps the first and eighth digits
(100), changes the second digit (10), swaps the first and sixth digits
(100) and changes the last one (1): 211.

Pitfalls:

- ten-digit numbers do not fit in 32 bits, and leading zeros only
  matter for the digit positions;
- a swap of two equal digits changes nothing and is not an edge;
- any fastest route is accepted.

The checker sums the costs along the printed route, requires every
step to be one changed digit or one swap, and compares the total with
the least time. All solutions pass it on small random cases and on
up to 50000 telegraphs in dense, sparse, chain-like and unreachable layouts,
against an independent accepted implementation.

## Optimized solutions

The optimized C++ solution replaces `std::unordered_map` with a flat
open-addressing table whose size is a power of two, at least `2n`, and
whose slots hold the telegraph index plus one, zero meaning empty; a
slot is chosen by multiplicative hashing of the number, a collision
moves on to the next slot, and since the table is at most half full, a
search usually ends after a few probes. Distances are `int`: a fastest
route has at most `n − 1 ≤ 49 999` steps of at most 10000 each, below
`5 · 10^8 < 2^31`. The queue is an indexed binary heap with
decrease-key, so every telegraph holds at most one heap slot instead of
duplicate entries, and the heap array is reused to print the route. The
numbers are parsed by hand from 4 KB blocks instead of being read as
strings with `scanf` and converted: {1806_graphs_optimized.cpp}.

The optimized Go solution replaces the map with a flat open-addressing
table of `int32` indices whose size is a power of two, at least `2n`,
with zero meaning empty; a slot is chosen by multiplicative hashing of
the number, a collision moves on to the next slot, and the half-empty
table usually keeps the probes short. Distances are `int32`: a fastest
route has at most `n − 1 ≤ 49 999` steps of at most 10000 each, below
`5 · 10^8 < 2^31`. The queue is an indexed binary heap of `int32` with
decrease-key instead of `container/heap` with its interface calls and
duplicate entries. The numbers are parsed by hand from the buffered
reader instead of with `fmt.Fscan`, and the route is written straight to
the output: {1806_graphs_optimized.go}.

The optimized Java solution replaces the `HashMap` of boxed `Long` keys
with a flat open-addressing table of `int` indices whose size is a power
of two, at least `2n`, with zero meaning empty; a slot is chosen by
multiplicative hashing of the number, a collision moves on to the next
slot, and the half-empty table usually keeps the probes short. Distances
are `int`: a fastest route has at most `n − 1 ≤ 49 999` steps of at most
10000 each, below `5 · 10^8 < 2^31`. The queue is an indexed binary heap
with decrease-key instead of a `PriorityQueue` of `long[]` pairs with a
lambda comparator, so no object is allocated for a queue entry. The
numbers are parsed by hand from 4 KB blocks of bytes:
{1806_graphs_optimized.java}.

The optimized Python solution notes, for every digit position, which
digits occur there in some telegraph number, and skips the changes and
swaps that would put any other digit there, since no telegraph can have
such a neighbour number. A telegraph leaves the dictionary of numbers
once it is taken from the queue, since with positive costs it can never
improve again, so later lookups find fewer numbers, and the list of
input tokens is freed before the search. It runs under PyPy, whose
compiled integer loops are faster here: {1806_graphs_optimized.py}.

The optimized Rust solution replaces the `HashMap` with a flat
open-addressing table of `u32` indices whose size is a power of two, at
least `2n`, with zero meaning empty; a slot is chosen by multiplicative
hashing of the number, a collision moves on to the next slot, and the
half-empty table usually keeps the probes short. Distances are `i32` and
heap vertices `u32`, half the size of `i64` and `usize`: a fastest route
has at most `n − 1 ≤ 49 999` steps of at most 10000 each, below
`5 · 10^8 < 2^31`. The digits of a number go into a fixed array instead
of a new vector for every telegraph, and the route is written straight
to the output instead of being collected into strings:
{1806_graphs_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1806_graphs_optimized.cpp`: time reduction +65.06%; memory reduction
  +70.82%; base: `1806_graphs.cpp`.

- `1806_graphs_optimized.go`: time reduction +38.11%; memory reduction
  +65.91%; base: `1806_graphs.go`.

- `1806_graphs_optimized.java`: time reduction +46.02%; memory reduction
  +69.51%; base: `1806_graphs.java`.

- `1806_graphs_optimized.py`: time reduction +58.00%; memory reduction
  +16.30%; base: `1806_graphs.py`.

- `1806_graphs_optimized.rs`: time reduction +35.78%; memory reduction
  +50.36%; base: `1806_graphs.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1806_graphs.cpp](1806_graphs.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.312 s | 4756 KB | 11304248 |
| [1806_graphs.go](1806_graphs.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.328 s | 8788 KB | 11290019 |
| [1806_graphs.java](1806_graphs.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.578 s | 12740 KB | 11304250 |
| [1806_graphs.py](1806_graphs.py) | Python 3.12 x64 | graphs | O(135 n log n) | AC | 2.343 s | 16464 KB | 11304252 |
| [1806_graphs.rs](1806_graphs.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.218 s | 6680 KB | 11304254 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1806_graphs_optimized.cpp](1806_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.109 s | 1388 KB | 11307284 |
| [1806_graphs_optimized.go](1806_graphs_optimized.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.203 s | 2996 KB | 11307288 |
| [1806_graphs_optimized.java](1806_graphs_optimized.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.312 s | 3884 KB | 11307286 |
| [1806_graphs_optimized.py](1806_graphs_optimized.py) | PyPy 3.10 x64 | graphs | O(135 n log n) | AC | 0.984 s | 13780 KB | 11307367 |
| [1806_graphs_optimized.rs](1806_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.140 s | 3316 KB | 11307327 |
