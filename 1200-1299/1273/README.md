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

## Language notes

- All languages sort the pairs and run the same DP.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1273_dp.cpp](1273_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.015 s | 192 KB |
| [1273_dp.go](1273_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.015 s | 1140 KB |
| [1273_dp.java](1273_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.140 s | 2780 KB |
| [1273_dp.py](1273_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.093 s | 392 KB |
| [1273_dp.rs](1273_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.015 s | 232 KB |
