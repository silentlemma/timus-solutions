# 1003. First contradictory parity answer

[Timus 1003](https://acm.timus.ru/problem.aspx?space=1&num=1003) · difficulty 385 · dsu, hashing

Original problem from the Central European Olympiad in Informatics 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is an unknown sequence of `L` bits (`L ≤ 10^9`). You get `q ≤ 5000`
statements in order; statement `i` says that the number of ones among the bits
`l..r` (1-based, `l ≤ r`) is even or odd.

Find the largest `X` such that some bit sequence satisfies the first `X`
statements. If all statements can hold at once, `X = q`.

The input holds several such tests.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Tests one after another. A test is a line with `L`, a line with `q`, and `q`
lines `l r even` or `l r odd`. A line `-1` ends the input.

## Output

For every test, one line with `X`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
3
1 2 odd
3 4 even
1 4 even
-1
```

Output:

```
2
```

### Example 2

Input:

```
8
4
1 8 even
1 4 odd
5 8 odd
2 3 even
3
2
1 3 odd
1 3 even
-1
```

Output:

```
4
1
```

## Solution

Let `P(k)` be the parity of the number of ones among the first `k` bits, with
`P(0) = 0`. A statement about `l..r` says `P(l-1) xor P(r) = 0` (even) or `1`
(odd). Conversely, any values of `P` with `P(0) = 0` come from exactly one
bit sequence. So the statements are consistent exactly when the equations
`P(a) xor P(b) = w` have a solution.

Process the statements in order with a disjoint set union over prefix
positions that also stores, for every node, the parity relative to its parent.
`find` returns the root and the parity of the node relative to it. For a new
equation, if both ends are in the same set the equation must agree with the
parities already known; otherwise the two sets are merged with the right
parity on the new edge. The first equation that disagrees gives `X`.

Positions go up to `10^9`, but at most `2q` occur. Hash maps assign them
consecutive IDs. With path compression and union by rank, the hash-based
versions take expected `O(q · α(q))` time per test; the teaching Python
version omits rank and takes expected `O(q log q)`. Hash-table bounds assume
expected constant-time operations, rather than a worst-case collision bound.
The tables include this qualification. DSU, coordinate maps and stored
statements use `O(q)` auxiliary space per test. Python and Rust versions
retaining the complete input and accumulated output additionally use
`O(I + O)` space for those buffers; Java's line reader may retain a whole
input line. Here `I` and `O` denote total input and output lengths.

Pitfalls:

- the equations are about prefixes `l-1` and `r`, not about `l` and `r`;
- after the first contradiction the rest of the test still has to be read;
- a test may have no statements at all.

## Optimized solutions

`1003_dsu_hashing_optimized.py`. Compared with the teaching Python source,
this version combines the separate parent/parity lists into a list of
`2 * parent + parity` values, adds a rank bytearray, and replaces stored
paths with iterative parity path halving. It consumes tokens lazily from
input lines instead of retaining all test cases and output lines. The
teaching base has no rank array and does not use packed short storage.
The first contradiction and consumption of all remaining statements are
preserved. Expected DSU/hash work is `O(q · α(q))` with `O(q)` state, plus
input processing and the current input line.

Exact-source CPython 3.12 Accepted #11326679: 0.062 s / 1040 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 3/35, memory rank 1/35. At least 1024 KB: both strict metrics are required and pass.

- `1003_dsu_hashing_optimized.py`: 0.062 s / 1040 KB; retained teaching base `1003_dsu_hashing.py` (Python 3.12 x64): 0.093 s / 4388 KB; time change -33.3%; memory change -76.3%.

Both variants encode parent index and edge parity together. C++ stores 16-bit entries; the current Python variant uses ordinary list-held integers, not a 16-bit storage array. The low bit is the parity. C++ sorts and deduplicates all prefix positions first, then finds their indices by binary search. Python assigns indices on demand with a hash table and compresses paths iteratively by reconnecting each visited node to its grandparent with the combined parity. The equations are checked in input order.

The cached audit verifies the retained C++ and Java bases by ranking and
the Go base by the exact-compiler small-cohort comparison. The simple Rust
base is still a valid teaching Accepted, but misses that comparison's memory
bound (1268 KB versus 1265 KB); `1003_dsu_hashing_optimized.rs` qualifies.
Python coverage comes from its optimized implementation. These are the
shared [rating criteria](../../RATING_CRITERIA.md); no duplicate files or
separate language-specific targets are needed.

The packed-link C++ and optimized Python sources now contain explanatory
comments added after Accepted #11310464 and #11326679. Their executable code
is unchanged; the table retains those historical paired measurements.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1003_dsu_hashing_optimized.rs`. Retain the archived algorithm and its integer types. Convert decimal integer tokens directly instead of calling the general string parser; negative values are accumulated with their sign so the minimum signed value remains representable. Existing input storage and algorithmic bounds are unchanged.

Accepted #11328483 (Rust 1.75 x64): **0.015 s / 1260 KB**. Archived comparison: `1003_dsu_hashing.rs` (Rust 1.75 x64) — 0.001 s / 1268 KB (#11277432).

## Language notes

These notes describe the simple implementations.

- **C++**: `std::unordered_map<int, int>` for the ids; a recursive `find` is
  fine, the trees are shallow with union by rank.
- **Go**: `map[int]int` and a recursive `find` with path compression.
- **Python**: an iterative `find` that compresses the path and recomputes the
  parities of the nodes on it.
- **Java**: arrays of size `2q` per test, `HashMap<Integer, Integer>` for the
  ids, iterative `find`.
- **Rust**: `HashMap<i64, usize>` with `entry().or_insert_with()` to create
  nodes; iterative `find`.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp) | G++ 13.2 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.015 s | 632 KB | 11277428 |
| [1003_dsu_hashing.go](1003_dsu_hashing.go) | Go 1.14 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.046 s | 3420 KB | 11277429 |
| [1003_dsu_hashing.java](1003_dsu_hashing.java) | Java 1.8 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.109 s | 4788 KB | 11277431 |
| [1003_dsu_hashing.py](1003_dsu_hashing.py) | Python 3.12 x64 | dsu, hashing | O(q log q) expected per test | AC | 0.093 s | 4388 KB | 11277430 |
| [1003_dsu_hashing.rs](1003_dsu_hashing.rs) | Rust 1.75 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.001 s | 1268 KB | 11277432 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1003_dsu_sorting.cpp](1003_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(q log q) per test | AC | 0.015 s | 184 KB | 11331144 |
| [1003_dsu_hashing_optimized.py](1003_dsu_hashing_optimized.py) | Python 3.12 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.078 s | 1292 KB | 11331212 |
| [1003_dsu_hashing_optimized.rs](1003_dsu_hashing_optimized.rs) | Rust 1.75 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.015 s | 1260 KB | 11328483 |
