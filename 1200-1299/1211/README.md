# 1211. Accusations without a ring and with one confession

[Timus 1211](https://acm.timus.ru/problem.aspx?space=1&num=1211) · difficulty 311 · graphs

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N ≤ 25000` children either confesses to breaking the cup (written
as 0) or names a child as the culprit. The statements look
consistent if exactly one child confessed and no group of children accuse
each other around a ring. Answer `YES` or `NO` for each of up to 16
tests.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The first line contains integer `1 ≤ T ≤ 16`. Each test has two lines: integer `1 ≤ N ≤ 25000`, then N integers `0 ≤ a_i ≤ N`. Position i is child i: 0 means a confession; a positive value names that 1-based child, including possibly i itself.

## Output

`YES` or `NO` for each test, one per line.

## Examples

### Example 1

Input:

```
5
1
0
1
1
5
3 3 0 2 4
6
2 3 2 0 4 5
4
0 0 2 3
```

Output:

```
YES
NO
YES
NO
NO
```

## Solution

Every child except a confessor points at exactly one child, so the
statements form a graph where each vertex has at most one outgoing edge.
With exactly one confession, there is no ring exactly when following the
accusations from any child always ends at the confessor.

Walk from every child in turn, marking the children on the current walk.
The walk stops at the confessor or at a child already known to lead
there; then every child on the walk leads there too. If it instead runs
into a child marked on the current walk, the accusations go round in a
ring. Each child is walked over once. `O(N)` per test.

Pitfalls:

- a child naming themselves is a ring of one;
- no confession, or two, already means `NO`;
- chains can be 25000 long, so the walk is a loop rather than a recursion.

The answers were compared with a separately written solution on 200
files of 16 random tests of every kind.

The chain algorithm uses `O(N)` working space per test for accusations, states and a current path. Across T tests its time is `O(Σ N_i)`. Let I be the total input bytes and H the longest input line. Simple Python retains all split input tokens and Rust retains its whole String, so their storage is `O(I + max N_i + T)`. C++ and Go stream with bounded buffers, using `O(max N_i)` graph space. Java also retains its current line and all T output words: `O(max N_i + H + T)` plus library buffers. Optimized Rust retains only a bounded input buffer/token, accusations, states, path and T output words: `O(max N_i + T + B)`, with B the fixed buffer size. The DSU implementations process accusations as they arrive, taking `O(N α(N))` amortized time per test; their actual statically sized 25001-entry signed 16-bit arrays and input buffers use `O(M + B)` storage with M=25000, even for a small test. Indices up to 25000 and negative component sizes down to −25000 fit signed 16-bit entries.

## Optimized solutions

C++ and Go process accusations as they arrive using union–find. When an accusation joins vertices already connected, it closes an undirected cycle. Every vertex in such a cycle has at most one outgoing accusation, so each must supply exactly one cycle edge and the cycle is directed. This also covers a self-accusation or two mutual accusations. Require exactly one confession and no cycle. The component array stores either a parent index or a negative size in each signed 16-bit entry.

The cached exact-source audit applies the shared [rating criteria](../../RATING_CRITERIA.md). Java and Python simple sources already qualify and are reused without duplicate files. Both Go versions qualify through the same-language fallback because there are no exact-compiler rivals. C++ fast coverage is `1211_dsu.cpp`; Rust fast coverage is `1211_graphs_implementation_optimized.rs` (#11328956, 0.031 s / 580 KB). Simple Rust #11283644 at 0.031 s / 5212 KB fails its required memory comparison, and simple C++ misses time; both remain meaningful unstarred teaching sources. Below 1024 KB compare only time; qualifying Go/Java/Python above it require both metrics. There is no separate first-place target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1211_graphs_implementation_optimized.rs`. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328956 (Rust 1.75 x64): **0.031 s / 580 KB**. Archived comparison: `1211_graphs.rs` (Rust 1.75 x64) — 0.031 s / 5212 KB (#11283644).

The Accepted #11328956 row and qualification above refer to the historical exact source. This review only names its existing 32-byte inline-token capacity as `INLINE_TOKEN_BYTES`; substituting 32 back reproduces the previous bytes exactly. All comments and the simple Rust version are preserved.

## Language notes

These notes describe the simple implementations.

- All languages walk the chains iteratively with the same three states.

## Checking

`tests/tests.json` uses `tokens`: compare exactly T YES/NO tokens in test order, ignoring whitespace and line breaks. Output is conventionally one result per line. The own example includes a single confessor, a self-cycle, merged paths to a confessor, a separate cycle and two confessors. Other fixtures exercise long chains, late cycles, maximum sizes and state reset between tests.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1211_graphs.cpp](1211_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) per test | AC | 0.265 s | 592 KB | 11283637 |
| [1211_graphs.go](1211_graphs.go) | Go 1.14 x64 | graphs | O(N) per test | AC | 0.218 s | 6820 KB | 11283638 |
| [1211_graphs.java](1211_graphs.java) | Java 1.8 | graphs | O(N) per test | AC | 0.156 s | 5760 KB | 11283643 |
| [1211_graphs.py](1211_graphs.py) | Python 3.12 x64 | graphs | O(N) per test | AC | 0.343 s | 26364 KB | 11283642 |
| [1211_graphs.rs](1211_graphs.rs) | Rust 1.75 x64 | graphs | O(N) per test | AC | 0.031 s | 5212 KB | 11283644 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1211_dsu.cpp](1211_dsu.cpp) | G++ 13.2 x64 | dsu | O(N α(N)) per test | AC | 0.015 s | 136 KB | 11310412 |
| [1211_dsu.go](1211_dsu.go) | Go 1.14 x64 | dsu | O(N α(N)) per test | AC | 0.046 s | 3228 KB | 11310413 |
| [1211_graphs_implementation_optimized.rs](1211_graphs_implementation_optimized.rs) | Rust 1.75 x64 | graphs, implementation | O(N) per test | AC | 0.031 s | 592 KB | 11331113 |
