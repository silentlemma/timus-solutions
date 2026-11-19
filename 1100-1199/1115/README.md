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

`1115_backtracking_optimized.java`. Keep the complete subset-search strategy, equal-length symmetry pruning and 128 bounded deterministic restarts followed by an unbounded complete search. Replace the nested suffix bitsets and cloned fixed 10000-bit rows by one flat long array. At a fill call, allocate only ceil((T+1)/64) words per suffix, where T is the largest remaining row target; positive ship lengths make larger sums irrelevant. Copy and shift from the following suffix in the flat array, preserving the same feasibility tests. The search is still exponential, not polynomial: O(M^N*N²*ceil(S/64)) is a conservative worst-case bound for largest target S. Simultaneously retained recursion levels can require O(M*N*ceil(S/64)) words, plus search state. Boxed ship/row ordering and final StringBuilder output are still present; only the suffix representation, capacity and byte input are reduced.

Compared with `1115_backtracking.java`: time 0.125 s → 0.14 s; memory 4 464 KB → 2 928 KB.

The C++ version allocates only the 64-bit words needed by the current suffix-sum table. For a future row of target T, the unused ships of total length U have a subset of length T exactly when they have one of length U − T. The feasibility test uses the smaller value. The current row still keeps its full target for reconstructing the chosen ships. The unbounded final search preserves completeness.

The accepted base implementations [1115_backtracking.go](1115_backtracking.go), [1115_backtracking.java](1115_backtracking.java), [1115_backtracking.py](1115_backtracking.py), [1115_backtracking.rs](1115_backtracking.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1115_backtracking_optimized.java`: time place 16/25, memory place 19/25 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 424 KB | 11325586 |
| [1115_backtracking.go](1115_backtracking.go) \* | Go 1.14 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 1864 KB | 11325575 |
| [1115_backtracking.java](1115_backtracking.java) \* | Java 1.8 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.125 s | 4464 KB | 11325558 |
| [1115_backtracking.py](1115_backtracking.py) \* | Python 3.12 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.078 s | 844 KB | 11325596 |
| [1115_backtracking.rs](1115_backtracking.rs) \* | Rust 1.75 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 756 KB | 11325611 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1115_backtracking_optimized.cpp](1115_backtracking_optimized.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 232 KB | 11310422 |
| [1115_backtracking_optimized.java](1115_backtracking_optimized.java) \* | Java 1.8 | backtracking | O(M^N·N²·ceil(S/64)) worst case | AC | 0.14 s | 2928 KB | 11325125 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
