# 1273. Sleepers

[Timus 1273](https://acm.timus.ru/problem.aspx?space=1&num=1273) · difficulty 464 · dp

Original problem by Magaz Asanov (prepared by Leonid Volkov), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two rails are the lines x = 0 and x = 1. Each of K ≤ 100 sleepers joins
(0, Y1) to (1, Y2) at integer points, |Y1|, |Y2| ≤ 1000; no two
sleepers share a left end or a right end. Remove as few sleepers as
possible so that no two of the rest cross.

Time limit: 1 second. Memory limit: 64 MB.

## Input

K, then K pairs Y1 Y2.

## Output

The least number of sleepers to remove.

## Examples

### Example 1

Input:

```
3
0 1
3 0
1 2
```

Output:

```
1
```

## Solution

Since ends never coincide, two sleepers cross exactly when their left
ends and right ends come in opposite orders. Sort the sleepers by the
left end; then a set without crossings is a set whose right ends
increase, and the most sleepers to keep is the longest increasing
subsequence of the right ends. The answer is K minus its length, found
by the quadratic DP over the last kept sleeper. `O(K²)`.

Pitfalls:

- the input is not sorted by either end (test 06);
- K may be 0 (test 02);
- coordinates may be negative.

The answers were compared with trying every subset of sleepers on 119
random cases of up to 12 sleepers.

## Optimized solutions

The sorting and binary-search version keeps the same reduction to a longest strictly increasing subsequence of right endpoints after sorting by left endpoints. Instead of quadratic DP, tails[i] stores the smallest possible ending coordinate of an increasing subsequence of length i+1. Replace the first tail not smaller than the next coordinate, or extend the array if none exists. Smaller tails preserve every possible continuation, so the occupied length is the optimum. The answer is K minus that length. Both sorting and the searches take O(K log K) time; storage is O(K). The empty input set returns 0.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 56 KB versus 232 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1273_dp_binary_search_optimized.py`. Find the insertion point of each LIS tail with bisect_left; the strict increasing-subsequence invariant and O(n log n) time are unchanged. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328532 (Python 3.12 x64): **0.078 s / 712 KB**. Archived comparison: `1273_dp.py` (Python 3.12 x64) — 0.093 s / 392 KB (#11284283).

## Language notes

The simple files retain quadratic DP in every language. The new Go and Java versions pack two shifted coordinates into one integer: each is in 0..2000 and fits 11 bits. Sorting packed values orders the left endpoints; the right endpoint is recovered with a mask. C++ and Rust use fixed arrays bounded by K ≤ 100; Python uses bisect_left. Go uses standard handles and Rust uses bounded C-runtime I/O with a C entry point.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1273_dp.cpp](1273_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.015 s | 192 KB | 11284277 |
| [1273_dp.go](1273_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.015 s | 1140 KB | 11284281 |
| [1273_dp.java](1273_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.140 s | 2780 KB | 11284285 |
| [1273_dp.py](1273_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.093 s | 392 KB | 11284283 |
| [1273_dp.rs](1273_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.015 s | 232 KB | 11284290 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1273_binary_search_sorting.cpp](1273_binary_search_sorting.cpp) | G++ 13.2 x64 | binary_search, sorting | O(K log K) | AC | 0.001 s | 116 KB | 11314674 |
| [1273_binary_search_sorting.go](1273_binary_search_sorting.go) \* | Go 1.14 x64 | binary_search, sorting | O(K log K) | AC | 0.015 s | 260 KB | 11314678 |
| [1273_binary_search_sorting.java](1273_binary_search_sorting.java) | Java 1.8 | binary_search, sorting | O(K log K) | AC | 0.109 s | 392 KB | 11314681 |
| [1273_binary_search_sorting.py](1273_binary_search_sorting.py) | Python 3.12 x64 | binary_search, sorting | O(K log K) | AC | 0.093 s | 384 KB | 11314686 |
| [1273_binary_search_sorting.rs](1273_binary_search_sorting.rs) | Rust 1.75 x64 | binary_search, sorting | O(K log K) | AC | 0.031 s | 56 KB | 11314875 |
| [1273_dp_binary_search_optimized.py](1273_dp_binary_search_optimized.py) | Python 3.12 x64 | dp, binary_search | O(K log K) time; O(K) space | AC | 0.078 s | 712 KB | 11328532 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
