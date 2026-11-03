# 2072. Water by moisture, ending each group at one of its ends

[Timus 2072](https://acm.timus.ru/problem.aspx?space=1&num=2072) · difficulty 206 · sorting, dp

Original problem by Ilya Kuchumov, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n flowers stand in a row, one step apart, each with its own moisture level. A
gardener starts at the leftmost flower and must water all of them in
order of non-decreasing moisture; flowers of equal moisture may go in any
order. Watering a flower and a step to a neighbour take one minute each.
Find the shortest total time. The limits are 2 seconds and 64 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then the n moisture values from left to right, each from
1 to 10⁹.

## Output

The smallest total time in minutes.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
6
3 2 5 6 2 5
```

Output:

```
21
```

## Solution

Watering always takes n minutes, so only the walking matters. Sort the
flowers by moisture and split them into groups of equal moisture; the
groups must be done one after another. Inside a group the gardener must
visit every flower between its leftmost position l and its rightmost
position r, so the walk covers the whole segment [l; r], and the best
way is to go to one end and sweep to the other. It finishes at l or at
r, and nothing else about the past matters for the next group.

So two values are kept per group: the shortest time to finish it at l
and at r. Coming from position p, finishing at l costs |p − r| + (r − l)
(go to r first), and finishing at r costs |p − l| + (r − l). Each is
minimised over the two possible ends of the previous group, with the
start at position 1 before the first group. The answer is the smaller
final value plus n. Sorting dominates: O(n log n).

In the example the groups are {2, 5}, {1}, {3, 6} and {4} (moisture 2, 3,
5 and 6), and the best walk takes 15 steps, plus 6 waterings: 21.

## Optimized solutions

Keep the same two-endpoint DP after ordering by moisture and position. Pack both sort fields into one integer key using their stated bounds; numeric order is therefore exactly lexicographic order. Unpacking recovers the original position without collisions. Primitive keys replace tuples and object comparators, while the DP state transitions and the treatment of equal-moisture groups remain unchanged.

- `2072_sorting_dp_optimized.cpp`: 0.031 s / 924 KB; base `2072_sorting_dp.cpp`: 0.093 s / 956 KB; relative change: time -66.7%, memory -3.3%.
- `2072_sorting_dp_optimized.py`: 0.328 s / 12940 KB; base `2072_sorting_dp.py`: 0.343 s / 21636 KB; relative change: time -4.4%, memory -40.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2072_sorting_dp.cpp`; covering source `2072_sorting_dp_optimized.cpp`; time/memory places 4/2, other-author entries 114/114.

- Go: preferred teaching base `2072_sorting_dp.go`; covering source `2072_sorting_dp.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2072_sorting_dp.java`; covering source `2072_sorting_dp.java`; time/memory places 1/1, other-author entries 6/6.

- Python/PyPy: preferred teaching base `2072_sorting_dp.py`; covering source `2072_sorting_dp_optimized.py`; time/memory places 3/1, other-author entries 11/11.

- Rust: preferred teaching base `2072_sorting_dp.rs`; covering source `2072_sorting_dp.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2072_sorting_dp.cpp](2072_sorting_dp.cpp) | G++ 13.2 x64 | sorting, dp | O(n log n) | AC | 0.093 s | 956 KB | 11309226 |
| [2072_sorting_dp.go](2072_sorting_dp.go) | Go 1.14 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 4292 KB | 11294463 |
| [2072_sorting_dp.java](2072_sorting_dp.java) | Java 1.8 | sorting, dp | O(n log n) | AC | 0.140 s | 2072 KB | 11309227 |
| [2072_sorting_dp.py](2072_sorting_dp.py) | Python 3.12 x64 | sorting, dp | O(n log n) | AC | 0.343 s | 21636 KB | 11309228 |
| [2072_sorting_dp.rs](2072_sorting_dp.rs) | Rust 1.75 x64 | sorting, dp | O(n log n) | AC | 0.015 s | 3420 KB | 11309229 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2072_sorting_dp_optimized.cpp](2072_sorting_dp_optimized.cpp) | G++ 13.2 x64 | sorting, dp | O(N log N) | AC | 0.031 s | 924 KB | 11308423 |
| [2072_sorting_dp_optimized.py](2072_sorting_dp_optimized.py) \* | Python 3.12 x64 | sorting, dp | O(N log N) | AC | 0.328 s | 12940 KB | 11308422 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
