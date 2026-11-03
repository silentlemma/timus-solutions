# 2144. Ordering sealed boxes into one sorted row

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · difficulty 221 · sorting

Original problem by Ivan Smirnov, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n boxes, each holding a fixed row of figure sizes that cannot
be rearranged or reversed. Decide whether the boxes can be put in some
order so that all sizes together form a non-decreasing row. The limits
are 0.5 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 100, then for every box kᵢ, 1 ≤ kᵢ ≤ 100, and its sizes,
1 ≤ aᵢⱼ ≤ 10⁴.

## Output

YES or NO.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
3
2 1 2
3 7 7 7
1 5
```

Output:

```
YES
```

### Example 2

Input:

```
2
2 1 3
1 2
```

Output:

```
NO
```

## Solution

Every box must be non-decreasing inside. After that only its first size
f and last size l matter, and a valid order needs l of each box to be at
most f of the next one.

In any valid order the first sizes do not decrease, since f ≤ l ≤ f of
the next box. Among boxes with the same first size f, all but the last
one have l ≤ f, so l = f. Therefore sorting the boxes by (f, l) gives a
valid order whenever one exists, and it is enough to check the
neighbours in that order. The work is O(Σ kᵢ + n log n).

In the first example the boxes (1, 2), (5, 5) and (7, 7) fit in this
order; in the second (1, 3) and (2, 2) overlap.

## Optimized solutions

Stream each box's contents, rejecting an internal inversion as soon as it is found. A valid box then needs only its two endpoint values. Pack the bounded endpoints into one integer so ordinary numeric sorting gives the required lexicographic interval order; recover the endpoints for the same neighboring-interval check as in the simple proof. Java uses primitive keys rather than boxed arrays and a comparator; Python avoids the full input list and temporary endpoint tuples.

- `2144_sorting_optimized.java`: 0.109 s / 2064 KB; base `2144_sorting.java`: 0.187 s / 6916 KB; relative change: time -41.7%, memory -70.2%.
- `2144_sorting_optimized.py`: 0.078 s / 420 KB; base `2144_sorting.py`: 0.093 s / 1040 KB; relative change: time -16.1%, memory -59.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2144_sorting.cpp`; covering source `2144_sorting.cpp`; time/memory places 1/6, other-author entries 100/100.

- Go: preferred teaching base `2144_sorting.go`; covering source `2144_sorting.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2144_sorting.java`; covering source `2144_sorting_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `2144_sorting.py`; covering source `2144_sorting_optimized.py`; time/memory places 7/2, other-author entries 66/66.

- Rust: preferred teaching base `2144_sorting.rs`; covering source `2144_sorting.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 168 KB | 11309245 |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB | 11294957 |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6916 KB | 11309246 |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.093 s | 1040 KB | 11309247 |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 320 KB | 11309248 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2144_sorting_optimized.java](2144_sorting_optimized.java) | Java 1.8 | sorting | O(total sizes+N log N) | AC | 0.109 s | 2064 KB | 11308445 |
| [2144_sorting_optimized.py](2144_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(total sizes+N log N) | AC | 0.078 s | 420 KB | 11308442 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
