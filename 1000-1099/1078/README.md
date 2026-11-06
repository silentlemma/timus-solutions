# 1078. The longest chain of segments nested one inside the next

[Timus 1078](https://acm.timus.ru/problem.aspx?space=1&num=1078) · difficulty 356 · dp

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` segments on a line (`0 < N < 500`) have integer ends in
`[−10000, 10000]`. A segment is inside another if it lies within it and
neither of its ends coincides with an end of the other. Find the longest
sequence of segments in which each one is inside the next, and print its
length and the numbers of its segments from the shortest to the longest.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the left and right ends of a segment.

## Output

The length of the sequence, then the numbers of its segments.

## Checking

Any longest sequence is accepted. The checker verifies that it has the
greatest possible length and that each listed segment is strictly inside
the next one.

## Examples

### Example 1

Input:

```
4
-2 2
-1 1
-3 3
4 5
```

Output:

```
3
2 1 3
```

## Solution

"Inside" means `L₂ < L₁` and `R₁ < R₂`, so a segment inside another is
strictly shorter. Sorted by length, the segments form a topological order
of the nesting relation, and a longest path in this order is a simple
dynamic programming: `best[i] = 1 + max best[j]` over the shorter segments
`j` that lie inside `i`, with `prev[i]` remembering the choice. The
answer ends at the segment with the largest `best`, and following `prev`
lists the chain from the outside in, so it is printed reversed.
`O(N^2)`.

Pitfalls:

- common ends do not count: `[0, 1]` is not inside `[0, 3]`, and equal
  segments are not inside each other;
- a segment of zero length can be inside another, and nothing can be
  inside it;
- the order must go from the shortest segment to the longest;
- if a segment is given with its ends in the other order, the solutions
  swap them, which describes the same segment.

The checker finds the longest length by a memoised search over all
segments and checks the listed chain.

## Optimized solutions

Go sorts by decreasing left endpoint and finds a strictly increasing subsequence of right endpoints. Equal left endpoints are ordered by decreasing right endpoint, so they cannot both be selected. Rust reverses both comparisons and finds a strictly decreasing subsequence instead. Each version binary-searches its array of best endpoints and records a predecessor to reconstruct the chain. Rust uses fixed arrays with 16-bit endpoints and indices, which fit the input bounds, plus byte buffers for input and output.

The accepted base implementations [1078_dp.cpp](1078_dp.cpp), [1078_dp.java](1078_dp.java), [1078_dp.py](1078_dp.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Python reads the ends with stepped slices and builds `left` and
  `right` with `min` and `max`.
- Rust picks the last segment with `max_by_key`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1078_dp.cpp](1078_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 204 KB | 11278988 |
| [1078_dp.go](1078_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 3448 KB | 11278990 |
| [1078_dp.java](1078_dp.java) \* | Java 1.8 | dp | O(N^2) | AC | 0.140 s | 4608 KB | 11278994 |
| [1078_dp.py](1078_dp.py) \* | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 888 KB | 11278993 |
| [1078_dp.rs](1078_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 292 KB | 11278995 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1078_binary_search_sorting.go](1078_binary_search_sorting.go) \* | Go 1.14 x64 | binary_search, sorting | O(N log N) | AC | 0.015 s | 964 KB | 11310522 |
| [1078_dp_binary_search.rs](1078_dp_binary_search.rs) \* | Rust 1.75 x64 | dp, binary_search | O(N log N) | AC | 0.015 s | 196 KB | 11311144 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
