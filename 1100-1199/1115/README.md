# 1115. Splitting lengths into rows of given total lengths

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · difficulty 409 · backtracking

Original problem from the first selection contest for the Bulgarian IOI team.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N < 100` items with integer lengths from 1 to 100 and
`M` rows (`1 < M < 10`) with given lengths. Split all items into the rows
so that the lengths in every row add up exactly to the row length; every
row gets at least one item. A split is known to exist. Print one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N M`, then `N` lines with the item lengths, then `M` lines with the row
lengths.

## Output

For every row, in input order, two lines: the number of items in it and
their lengths.

## Checking

Any valid split is accepted. The checker verifies that every row adds up
to its length and that the items used are exactly the given ones.

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

This is exact multi-way partitioning, a hard problem in general, so the
solutions search with pruning. Initially, rows are filled shortest first
and items are tried in decreasing length. This is only a heuristic:
shorter rows need not have fewer fillings. The last row takes every item
that remains. Equal lengths are tried only once at each place, since
equal items are interchangeable.

Before filling a row, the bitset `reach[k]` records the sums that the
still-free items from position `k` on can make, built from the end with
`reach[k] = reach[k+1] | reach[k+1] << len`. If any unfinished row's target
is unreachable, the branch fails immediately. An item is taken only if
the rest of the current row is reachable from the items after it.

A fixed search order can still spend too long on incompatible row
fillings. Each of the first 128 attempts allows 256 calls to the subset
search, then unwinds all assignments and permutes the rows and the order
of distinct item lengths. Equal lengths remain together. The permutations
use the same fixed integer generator in every language, so outputs stay
identical. If these attempts fail, a final unrestricted search examines
all remaining possibilities; reaching a budget never means that no split
exists. Output rows retain their original input indices.

With total item length `S` and bitset word width `W`, a conservative
worst-case time bound is `O(M^N * N^2 * ceil(S/W))`, and auxiliary memory
is `O(M * N * ceil(S/W))` words. Restarts do not remove the exponential
worst case; measured speed is not a guarantee for every valid input.

Pitfalls:

- trying equal items in every order makes the search explode on fleets
  with many equal lengths;
- without the subset-sum checks, unreachable current or future rows
  remain in the search;
- test **07** exposes millions of calls with a fixed shortest-first
  order; short rows do not necessarily have the fewest fillings (items
  `[1,1,2,5]`, targets `[2,2,5]` give two fillings for 2 but only one for 5);
- interrupted attempts must undo every assignment, and the final search
  must have no call budget;
- the rows must be printed in input order, though they are filled in a
  different one.

The Python solution was checked on all 7 stored tests, all 5 declared
generator cases, 1,500 small random cases against an independent exact
oracle, and 406 large or boundary cases.

## Optimized solutions

`1115_backtracking_optimized.java`. Keep complete subset backtracking, equal-length symmetry pruning and 128 bounded deterministic restarts followed by an unrestricted complete search; the worst case is still exponential. At each depth reuse a flat long suffix-bitset workspace and free-index array. A later row of target t can test min(t,total-t), since every subset has a complementary subset; the current row still retains its full target for reconstruction. Cap positive subset sums at the largest actual query, clear reused cells and keep workspaces separate by recursion depth. Primitive stable insertion sorting replaces boxed ordering, and 1024-byte raw input/output replaces Scanner/StringBuilder. A conservative bound is O(M^N*N^2*ceil(S/64)) time and O(M*N*ceil(S/64)) words plus search state for largest row target S. Exact current solver checks covered 30935 small instances and 10000 stable sorts; the final unrestricted search preserves completeness.

Exact-source Java 1.8 Accepted #11327476: 0.093 s / 420 KB. Saved 2026-11-20 compiler-cohort comparison: time 2/25, memory 1/25. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325125 was 0.14 s / 2928 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1115_backtracking_optimized.java`: 0.093 s / 420 KB; retained teaching base `1115_backtracking.java`: 0.125 s / 4464 KB.

The C++ version allocates only the 64-bit words needed by the current suffix-sum table. For a future row of target T, the unused ships of total length U have a subset of length T exactly when they have one of length U − T. The feasibility test uses the smaller value. The current row still keeps its full target for reconstructing the chosen ships. The unbounded final search preserves completeness.

The accepted base implementations [1115_backtracking.go](1115_backtracking.go), [1115_backtracking.java](1115_backtracking.java), [1115_backtracking.py](1115_backtracking.py), [1115_backtracking.rs](1115_backtracking.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1115_implementation_parsing_optimized.go`. Use specialized insertion ordering for the bounded ship/row arrays instead of reflective sorting. Preserve all search heuristics, bounded suffix bitsets, reproducible restarts and the final unlimited complete search. Write assignments without temporary string lists. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11329250 (Go 1.14 x64): **0.015 s / 916 KB**. Archived comparison: `1115_backtracking.go` (Go 1.14 x64) — 0.015 s / 1864 KB (#11325575).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 424 KB | 11325586 |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 1864 KB | 11325575 |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.125 s | 4464 KB | 11325558 |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.078 s | 844 KB | 11325596 |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 756 KB | 11325611 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1115_backtracking_optimized.cpp](1115_backtracking_optimized.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 232 KB | 11310422 |
| [1115_backtracking_optimized.java](1115_backtracking_optimized.java) | Java 1.8 | backtracking | O(M^N*N^2*ceil(S/64)) worst case; exponential | AC | 0.093 s | 420 KB | 11327476 |
| [1115_implementation_parsing_optimized.go](1115_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 916 KB | 11329250 |
