# 2183. Flipping the signs of one segment to raise the minimum

[Timus 2183](https://acm.timus.ru/problem.aspx?space=1&num=2183) · difficulty 687 · binary_search, dp

Original problem by Artyom Abaturov, from the Ural Team Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Change the signs of all numbers in exactly one non-empty segment of an
array so that its minimum becomes as large as possible, and print that
minimum. The array has a negative number. The limits are 1 second and
256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then a₁ … aₙ, −10⁹ ≤ aᵢ ≤ 10⁹.

## Output

The largest possible minimum.

## Examples

### Example 1

Input:

```
5
-1 3 -2 -4 5
```

Output:

```
-1
```

### Example 2

Input:

```
4
2 -4 -3 -10
```

Output:

```
2
```

## Solution

Ask whether a minimum of at least x is possible. Every number below x
must be flipped, so the segment has to cover all of them, and every
number inside the segment must become at least x, that is, be at most
−x. A longer segment only adds conditions, so it is enough to test the
shortest one, from the first to the last number below x. If no number
is below x, a single number at most −x still has to be flipped, which
holds whenever the smallest number is at most −x.

Larger x only makes the test harder, so a binary search over x from
−10⁹ to 10⁹ finds the largest value that passes, with an O(n) test,
O(n log C) in total.

In the second example flipping −4 −3 −10 gives 2 4 3 10, whose minimum
is 2.

## Language notes

- The Python solution skips the binary search: one left-to-right pass
  keeps the best prefix minimum with the flip not started, running, or
  finished, which is O(n).

## Optimized solutions

The streaming DP keeps three prefix minima. The first has no flip; the second ends a flipped segment at the latest value; the third allows that segment to end anywhere in the prefix. This needs one pass and constant auxiliary space.

`2183_dp_optimized.cpp` retains this three-state DP and parses signed input through a fixed 16 KB buffer instead of calling scanf for every value. The short unbuffered `2183_dp.cpp` is retained to teach the same algorithm, and all binary-search versions remain. Both DP implementations take O(n) time and O(1) auxiliary space. The new exact-source Accepted is 0.015 s / 96 KB, versus 0.093 s / 116 KB for the unbuffered DP.

**Timus submissions for the optimized versions**

G++ 13.2 x64 №11317399 (`2183_dp.cpp`) · G++ 13.2 x64 №11326641 (`2183_dp_optimized.cpp`) · Go 1.14 x64 №11317402 · Java 1.8 №11317412 · Rust 1.75 x64 №11317407.

**Timus submissions for the simple versions**

Python 3.12 x64 №11321738 · G++ 13.2 x64 №11321929 · Java 1.8 №11321932 · Rust 1.75 x64 №11321934.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2183_binary_search_optimized.java`. Retain the archived algorithm, replacing Scanner with buffered byte input. Output avoids Formatter where ordinary numeric conversion suffices. EOF is stable even without a final newline; the simple source remains unchanged.

Accepted #11328647 (Java 1.8): **0.109 s / 1208 KB**. Archived comparison: `2183_binary_search.java` (Java 1.8) — 0.14 s / 1296 KB (#11321932).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2183_binary_search.cpp](2183_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log C) | AC | 0.093 s | 964 KB | 11321929 |
| [2183_binary_search.go](2183_binary_search.go) | Go 1.14 x64 | binary_search | O(n log C) | AC | 0.031 s | 3500 KB | 11322055 |
| [2183_binary_search.java](2183_binary_search.java) | Java 1.8 | binary_search | O(n log C) | AC | 0.14 s | 1296 KB | 11321932 |
| [2183_binary_search.rs](2183_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log C) | AC | 0.046 s | 3660 KB | 11321934 |
| [2183_dp.py](2183_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.109 s | 8144 KB | 11321738 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2183_dp.cpp](2183_dp.cpp) \* | G++ 13.2 x64 | dp | O(n) | AC | 0.093 s | 116 KB | 11317399 |
| [2183_dp_optimized.cpp](2183_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 96 KB | 11326641 |
| [2183_dp.go](2183_dp.go) \* | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 1008 KB | 11317402 |
| [2183_dp.rs](2183_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.046 s | 208 KB | 11317407 |
| [2183_dp.java](2183_dp.java) \* | Java 1.8 | dp | O(n) | AC | 0.14 s | 416 KB | 11317412 |
| [2183_binary_search_optimized.java](2183_binary_search_optimized.java) | Java 1.8 | binary_search | O(n log C) | AC | 0.109 s | 1208 KB | 11328647 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
