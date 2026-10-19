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

## Language notes

The total can exceed 2³¹ (up to about 10¹⁰), so C++, Go, Java and Rust use
64-bit integers. Java sorts the moisture and the position packed into one long.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2072_sorting_dp.cpp](2072_sorting_dp.cpp) | G++ 13.2 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 980 KB |
| [2072_sorting_dp.go](2072_sorting_dp.go) | Go 1.14 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 4292 KB |
| [2072_sorting_dp.java](2072_sorting_dp.java) | Java 1.8 | sorting, dp | O(n log n) | AC | 0.125 s | 2132 KB |
| [2072_sorting_dp.py](2072_sorting_dp.py) | Python 3.12 x64 | sorting, dp | O(n log n) | AC | 0.312 s | 22588 KB |
| [2072_sorting_dp.rs](2072_sorting_dp.rs) | Rust 1.75 x64 | sorting, dp | O(n log n) | AC | 0.031 s | 3424 KB |
