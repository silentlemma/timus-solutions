# 1208. The most legendary teams without a shared member

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · difficulty 210 · bitmask, dp

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose the largest subset of `1 ≤ K ≤ 18` teams such that no person
belongs to two chosen teams. Each team contains three different names,
each at most 20 lowercase Latin letters; the same name can occur in
several teams. Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`K`, then the three names of each team, up to 20 lowercase letters each.

## Output

The largest number of teams that can take part.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

Output:

```
4
```

## Solution

Two teams conflict if their member sets intersect. Store for each
team `i` a bit mask `clash[i]` of conflicting teams, including itself.
For a remaining set `S`, choose its lowest team `i`. Every feasible
selection either omits `i`, or includes it and omits all its conflicts:

`best(S) = max(best(S without i), 1 + best(S without clash[i]))`.

The two alternatives cover all possibilities, and the empty set has
answer zero. Both smaller masks are numerically smaller because they
clear `i`, so the native bases fill a table in increasing mask order.
Python evaluates the same recurrence lazily with `lru_cache`; it need
not visit every mask. Time is `O(2^K + K²)` with bounded name lengths,
and the table or memo uses up to `O(2^K)` space. Keep all five original
Accepted bases unchanged. Shared names in different columns still
conflict; an identical team listed twice cannot be selected twice.

## Optimized solutions

**C++, Go, Java, Rust.** The new algorithm searches an include/exclude tree without storing
answers for all masks. Its state is the remaining mask and the number
already selected; the mask contains only teams compatible with that
selection. An incumbent stores the best feasible count found so far.
`selected + popcount(mask)` is an upper bound even if remaining teams
conflict, so a node no better than the incumbent can be pruned safely.

Otherwise select a remaining team with the most conflicts within the
mask, counting itself. If this maximum is at most one, no two remaining
teams conflict: taking them all attains the upper bound immediately.
In other cases, first include the chosen team and remove its conflict
mask, then exclude just that team. These branches partition all feasible
extensions. Inclusion first may improve the incumbent before exclusion;
the choice of highest degree is a heuristic, not a correctness assumption.
Each branch removes a team, so depth is at most `K ≤ 18`.

Worst-case time is `O(K 2^K + K²)`, because choosing the next team scans
up to `K` bits per search node. Working search space is `O(K)` for
conflict masks and recursion, besides input names; there is no exponential
DP table. The masks fit 32 bits. This changes the search algorithm,
so the filenames use `backtracking_bitmask`, not duplicate `_optimized`
copies. All four published versions qualify by memory. Java records
a higher time, 0.125 s versus 0.109 s, while using 83.3% less memory.
The raw times are measurements; a single tick is not reliable CPU evidence.

**Python/PyPy.** Preserve the readable whole-mask memoized independent-set algorithm. The new meet-in-the-middle variant splits at most 18 teams into halves of at most 9. Build the optimum for every left-half subset: omit its lowest team, or take it and remove its conflicts. Recursively omit/take each right-half team, removing both its right conflicts and its conflicting left teams. At a right leaf, the left-table lookup completes the optimum. Every compatible selection has exactly one right branch and an optimal compatible left subset, proving correctness. Conflicts are computed by exact name equality, never a probabilistic name hash. O(K²+2^ceil(K/2)) time and O(2^floor(K/2)+K) storage.

- `1208_backtracking_bitmask.cpp`: 0.015 s / 176 KB; base `1208_bitmask.cpp`: 0.015 s / 976 KB; relative change: time -0.0%, memory -82.0%.
- `1208_backtracking_bitmask.go`: 0.031 s / 1104 KB; base `1208_bitmask.go`: 0.062 s / 3204 KB; relative change: time -50.0%, memory -65.5%.
- `1208_backtracking_bitmask.java`: 0.125 s / 448 KB; base `1208_bitmask.java`: 0.109 s / 2688 KB; relative change: time +14.7%, memory -83.3%.
- `1208_backtracking_bitmask.rs`: 0.015 s / 224 KB; base `1208_bitmask.rs`: 0.046 s / 684 KB; relative change: time -67.4%, memory -67.3%.
- `1208_bitmask_dp.py`: 0.125 s / 296 KB; base `1208_bitmask.py`: 0.078 s / 456 KB; relative change: time +60.3%, memory -35.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1208_bitmask.cpp`; covering source `1208_backtracking_bitmask.cpp`; time/memory places 1/27, other-author entries 109/109.

- Go: preferred teaching base `1208_bitmask.go`; covering source `1208_backtracking_bitmask.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1208_bitmask.java`; covering source `1208_backtracking_bitmask.java`; time/memory places 2/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1208_bitmask.py`; covering source `1208_bitmask_dp.py`; time/memory places 4/2, other-author entries 21/21.

- Rust: preferred teaching base `1208_bitmask.rs`; covering source `1208_backtracking_bitmask.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K^2) | AC | 0.015 s | 976 KB | 11283611 |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K^2) | AC | 0.062 s | 3204 KB | 11283615 |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K^2) | AC | 0.109 s | 2688 KB | 11283617 |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K^2) | AC | 0.078 s | 456 KB | 11283616 |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K^2) | AC | 0.046 s | 684 KB | 11283620 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1208_backtracking_bitmask.cpp](1208_backtracking_bitmask.cpp) \* | G++ 13.2 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 176 KB | 11308198 |
| [1208_backtracking_bitmask.go](1208_backtracking_bitmask.go) | Go 1.14 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.031 s | 1104 KB | 11308199 |
| [1208_backtracking_bitmask.java](1208_backtracking_bitmask.java) \* | Java 1.8 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.125 s | 448 KB | 11308200 |
| [1208_backtracking_bitmask.rs](1208_backtracking_bitmask.rs) | Rust 1.75 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 224 KB | 11308202 |
| [1208_bitmask_dp.py](1208_bitmask_dp.py) \* | PyPy 3.10 x64 | bitmask, dp | O(K^2 + 2^(K/2)) time, O(2^(K/2)+K) memory | AC | 0.125 s | 296 KB | 11309782 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
