# 1162. Can a chain of currency exchanges with commissions increase the money

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · difficulty 185 · shortest_paths

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 100` currencies and `M ≤ 100` exchange points, each
working between two currencies in both directions with its own rate and
commission per direction: exchanging `x` gives `(x − commission)·rate`,
and the amount may never become negative. Starting with `V` units of
currency `S`, decide whether some sequence of exchanges ends in currency
`S` with more than `V`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M`, `S` and `V`, then `M` lines with two currencies and the rate
and commission each way.

`1 ≤ S ≤ N ≤ 100`, `1 ≤ M ≤ 100`, and `0 ≤ V ≤ 1000`.
Rates are in `[0.01, 100]` and commissions in `[0, 100]`, each with at most
two fractional digits. The number of fractional digits in `V` is not
restricted. For any exchange sequence using each exchange point at most
once, the ratio of the final amount to the initial amount is less than
`10000`.

## Output

`YES` or `NO`.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
3 2 1 10.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Output:

```
NO
```

### Example 2

Input:

```
3 2 1 20.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Output:

```
YES
```

## Solution

Represent each currency as a vertex and each exchange direction as
an edge. A feasible exchange sends `x` to `(x−fee)·rate` with `x≥fee`.
The five readable bases use synchronous Bellman–Ford: `best[c]` is the
largest reachable amount after at most `j` exchanges, and pass `j+1`
reads only that array while updating a separate next array. Positive
rates make every suffix monotone, so keeping only the largest amount
per currency loses no feasible or better continuation. Keep unreachable
states distinct from a reachable zero.

Arithmetic is exact. Put `P=max(2, fractional digits in V)` and start
with denominator `D=10^P`. Store rates and fees as integer hundredths
`R,C`. For numerator `x`, skip if `x<C·D/100`; otherwise the next
numerator is `(x−C·D/100)·R` with denominator `100D`. Scale retained
amounts and the initial capital by 100 on every pass as well. No initial
precision is discarded and no epsilon or floating comparison is used.

Return YES as soon as the source amount exceeds its initial value. A
pass without improvements is a fixed point and proves NO. A strict
improvement on pass `N` exposes a gaining repeated-vertex cycle: if
every cycle in an improving walk failed to increase its entry amount,
deleting those cycles would preserve feasibility and could only help
the monotone suffix, yielding a simple walk of at most `N−1` edges.
A gaining cycle is an affine map `A·x−B`, `B≥0`; a strict gain at `x≥0`
implies `A>1`, so repetition grows capital without bound. Every exchange
point has a positive-rate reverse direction: eventually the return path
to `S` is affordable and profitable. Zero initial capital never grows.

With `P` fractional digits, states have `O(P+N)` digits after at most `N`
passes. Relaxation and state copying cost `O(N(N+M)(P+N))` digit-time;
a conservative bound including decimal parsing is
`O(P²+N(N+M)(P+N))`. Live state storage is `O(N(P+N))` digits plus
`O(M)` fixed-size edge records. C++/Rust bases use base-100 digit arrays;
Go uses `big.Int`, Java `BigInteger`, and Python arbitrary integers.
Only names for existing literal-100 roles and repository formatting
change in these bases. Each has its own new exact-SHA Accepted, and all
five original byte sequences are backed up. The algorithms stay intact.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1162_shortest_paths.cpp`; covering source `1162_shortest_paths_optimized.cpp`; time/memory places 380/107, other-author entries 426/426.

- Go: preferred teaching base `1162_shortest_paths.go`; covering source `1162_shortest_paths_optimized.go`; time/memory places 3/5, other-author entries 5/5.

- Java: preferred teaching base `1162_shortest_paths.java`; covering source `1162_shortest_paths_optimized.java`; time/memory places 43/46, other-author entries 117/117.

- Python/PyPy: preferred teaching base `1162_shortest_paths.py`; covering source `1162_shortest_paths_optimized.py`; time/memory places 75/1, other-author entries 77/77.

- Rust: preferred teaching base `1162_shortest_paths.rs`; covering source `1162_shortest_paths.rs`; time/memory places 1/1, other-author entries 0/0.

## Optimized solutions

**C++, Go, Java.** The three optimized versions keep the same exact Jacobi algorithm
and use `_optimized` filenames. First restrict the graph to the undirected
component of `S`: exchange points work both ways, so other components
can never help. With `C` retained vertices, `C` passes suffice. This is
only structural pruning, not a claim that every commission is affordable.

Go reuses independently owned `big.Int` buffers and scratch values;
copy amounts with `Set`, not a shallow struct assignment. C++ and Java
store nonnegative amounts in base `10^9`, use nine-digit parsing chunks,
and reuse scratch/capacity instead of short decimal limbs or immutable
intermediate objects. Zero fees skip a cost subtraction. All edge reads
still use the previous-pass states; buffer reuse does not turn the
algorithm into an in-place relaxation.

For radix `B=10^9`, a limb is below `B` and a rate/fee factor is at most
10000. Limb multiplication plus carry is below `B·10000=10^13`, fitting
C++ `uint64_t` and Java `long`. Subtraction is used only when affordable;
borrow is 0 or 1 and a limb plus its borrow fits the chosen types.
An aliased multiplication reads each old limb before writing it, so
`value.multiply(value,factor)` is valid. Separate buffers own their
storage. Bounds include zero, powers of the radix and long borrow chains.
The asymptotic bound is unchanged; fewer limbs, allocations and vertices
reduce constants.

**Python/PyPy.** Python keeps exact synchronous Bellman–Ford and the reserve 100^N: each of at most N exchanges can divide by 100 without losing a digit. Initial decimals are converted in blocks of at most 1000 digits, so arbitrarily long inputs do not hit a single-conversion limit. The edge tuples keep their precomputed exact fees. Every eight exchange-input lines, collect dead parsing objects before they accumulate; this changes memory lifetime only, never an amount or reachability. It trades collection time for peak memory. All five readable exact-decimal versions remain. Complexity is O(NM) exact relaxations and O(N+M) numeric records, plus the explicitly measured collection overhead.

- `1162_shortest_paths_optimized.cpp`: 0.031 s / 244 KB; base `1162_shortest_paths.cpp`: 0.046 s / 676 KB; relative change: time -32.6%, memory -63.9%.
- `1162_shortest_paths_optimized.go`: 0.031 s / 1304 KB; base `1162_shortest_paths.go`: 0.031 s / 5436 KB; relative change: time -0.0%, memory -76.0%.
- `1162_shortest_paths_optimized.java`: 0.125 s / 1224 KB; base `1162_shortest_paths.java`: 0.125 s / 4932 KB; relative change: time -0.0%, memory -75.2%.
- `1162_shortest_paths_optimized.py`: 0.156 s / 416 KB; base `1162_shortest_paths.py`: 0.078 s / 708 KB; relative change: time +100.0%, memory -41.2%.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 676 KB | 11308458 |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.031 s | 5436 KB | 11308459 |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.125 s | 4932 KB | 11308466 |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.078 s | 708 KB | 11308471 |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 300 KB | 11308481 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths_optimized.cpp](1162_shortest_paths_optimized.cpp) \* | G++ 13.2 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.031 s | 244 KB | 11308451 |
| [1162_shortest_paths_optimized.go](1162_shortest_paths_optimized.go) \* | Go 1.14 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.031 s | 1304 KB | 11308453 |
| [1162_shortest_paths_optimized.java](1162_shortest_paths_optimized.java) \* | Java 1.8 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.125 s | 1224 KB | 11308454 |
| [1162_shortest_paths_optimized.py](1162_shortest_paths_optimized.py) \* | PyPy 3.10 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.156 s | 416 KB | 11309920 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
