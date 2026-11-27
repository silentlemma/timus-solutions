# 1279. Warehouse

[Timus 1279](https://acm.timus.ru/problem.aspx?space=1&num=1279) · difficulty 424 · binary_search

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A warehouse of N × M sections (N, M ≤ 100) holds stacks of containers
with heights from 1 to 1000. K ≤ 10⁷ new containers arrive and are put
one by one onto a lowest section. Find the lowest height after all of
them are placed.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains integers `N`, `M`, `K`: `1 ≤ N, M ≤ 100` and
`1 ≤ K ≤ 10⁷`. The next `N` rows each contain `M` integer heights in
`1..1000`.

## Output

The least height after placing the containers.

## Checking

Token comparison, as specified by `tests.json`: output one decimal integer
equal to the final minimum height. Whitespace around the token is ignored;
extra tokens or another spelling of the number do not match.

## Examples

### Example 1

Input:

```
1 4 5
2 2 8 8
```

Output:

```
4
```

### Example 2

Input:

```
2 3 26
1 2 3
4 5 6
```

Output:

```
7
```

## Solution

Always adding to a lowest section works like pouring water: at the end
all sections below some level h have been raised to h, and the
containers left over lifted some of those to h + 1 but not all of them.
Raising everything to level h takes need(h) = Σ max(0, h − height)
containers, which grows with h. So the answer is the largest h with
need(h) ≤ K, found by binary search between the lowest height and that
height plus K. `O(N · M · log(K+1))`.

Pitfalls:

- the answer can exceed 10⁷, and need(h) up to 10⁴ · 10⁷ needs 64 bits
  (tests 03, 12);
- leftover containers do not raise the minimum unless they reach every
  section at that level (test 05);
- simulating the containers one at a time is far too slow for K = 10⁷.

All nine sources pass the 19 cases. Every result is independently
certified by the exact costs at that height and the next; small cases
are also checked by placing containers individually on a heap.

## Optimized solutions

The new Go and Rust versions use the initial-height bound H=1000. Count stacks by height, then raise the water level from 1 upwards. Before leaving level h, add its stacks to the active count; a full next layer costs exactly one container per active stack. If the remaining budget cannot cover that layer, h is the final minimum. Once all stacks are active, divide the remaining budget by N·M and jump directly, discarding the incomplete layer. This is O(N·M+H) time and O(H) storage without sorting or repeated feasibility passes. A 64-bit budget avoids arithmetic ambiguity. Original binary-search sources remain, with C++, Java and Python also covering the fast set.

The saved snapshot admits the base [1279_binary_search.cpp](1279_binary_search.cpp)
and [1279_binary_search.java](1279_binary_search.java) by the ordinary top-ten
or top-15% ranking rule on time only: their receipts use 280 and 600 KB.
The base [1279_binary_search.py](1279_binary_search.py) uses 1344 KB and
qualifies by the exact-compiler sparse-cohort reference rule on both time
and memory. These meaningful base sources also cover the fast set without
identical copies. The Go base requires both metrics by ordinary ranking;
Go greedy uses time-only ordinary ranking. All three Rust versions use
the time-only sparse-cohort rule. The sorting Python version also requires
both metrics against its sparse-cohort reference.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1279_sorting_optimized.py`. Sort all section heights and raise the lowest prefix to the next height until the remaining containers no longer suffice. Divide the remainder by that prefix size. This replaces binary search over heights by one sorted scan: O(nm log(nm+1)) time and O(nm) storage. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328665 (Python 3.12 x64): **0.062 s / 1296 KB**. Archived comparison: `1279_binary_search.py` (Python 3.12 x64) — 0.109 s / 1344 KB (#11284394).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1279_binary_search_implementation_optimized.rs`. The C entry calls the solver directly and flushes Rust output before returning. It also replaces standard integer parsing with `parse_integer`: decimal digits are accumulated by multiply-by-ten and add/subtract, including optional signs. Tokens still come from the retained whole-input string, and the binary-search algorithm is unchanged. The ordinary-entry implementation remains available.

Accepted #11328966 (Rust 1.75 x64): **0.015 s / 460 KB**. Archived comparison: `1279_binary_search.rs` (Rust 1.75 x64) — 0.031 s / 512 KB (#11284398).


For binary search, let `I` be the input bytes and `B` the fixed I/O
buffers. Time is `O(I + N·M·log(K+1))`; auxiliary space is `O(N·M+B)`
for streamed C++/Go/Java and `O(I+N·M+B)` for whole-input Python/Rust,
including the Rust entry-point variant. Sorting Python also retains
the input and a sorted-array suffix, using `O(I+N·M+B)` space and
`O(I+N·M·log(N·M+1))` time. Histogram Go/Rust use `O(I+N·M+H)` time
and `O(H+B)` space with 256-byte input and 20-byte output arrays.

Seven sources have only had their water-level comment clarified: initially
taller stacks stay unchanged. Both
histogram sources are unchanged, with their exact Accepted bindings intact.

## Language notes

These notes describe the simple implementations.

- Same binary search in all languages: arbitrary-precision sums in Python,
  64-bit sums elsewhere.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(I + N·M·log(K+1)) | AC | 0.015 s | 264 KB | 11331147 |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(I + N·M·log(K+1)) | AC | 0.031 s | 1196 KB | 11331027 |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(I + N·M·log(K+1)) | AC | 0.109 s | 576 KB | 11331219 |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(I + N·M·log(K+1)) | AC | 0.093 s | 1380 KB | 11331078 |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(I + N·M·log(K+1)) | AC | 0.031 s | 500 KB | 11331123 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1279_greedy.go](1279_greedy.go) | Go 1.14 x64 | greedy | O(N·M + H) | AC | 0.015 s | 320 KB | 11314936 |
| [1279_greedy.rs](1279_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M + H) | AC | 0.031 s | 56 KB | 11314955 |
| [1279_sorting_optimized.py](1279_sorting_optimized.py) | Python 3.12 x64 | sorting | O(nm log(nm+1)) time; O(nm) space | AC | 0.078 s | 1440 KB | 11331079 |
| [1279_binary_search_implementation_optimized.rs](1279_binary_search_implementation_optimized.rs) | Rust 1.75 x64 | binary_search, implementation | O(I + N·M·log(K+1)) | AC | 0.015 s | 460 KB | 11331213 |
