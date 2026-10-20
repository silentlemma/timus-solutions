# 2225. Fewest strikes of a two-nail hammer to drive a row of nails

[Timus 2225](https://acm.timus.ru/problem.aspx?space=1&num=2225) · difficulty 1110 · dsu, sorting

Original problem by Vadim Barinov, from the Ural Championship 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N nails stick out by lᵢ centimeters. A strike covers two neighboring
nails: the higher one goes down by 1, or both if they are equally high.
Find the fewest strikes that drive all nails in. The limits are 1 second
and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then l₁ … l_N with 1 ≤ lᵢ ≤ 10⁹.

## Output

The fewest strikes.

## Examples

### Example 1

Input:

```
3
4 1 3
```

Output:

```
7
```

### Example 2

Input:

```
4
2 2 6 6
```

Output:

```
8
```

## Solution

Think of the nails level by level, from the top. At level h the nails
with height at least h form maximal runs of neighbors. A strike lowers
at most two nails, and only two nails of the same height that stand
side by side, so a run of k nails at that level needs ⌈k / 2⌉ strikes,
and driving the runs level by level from the top reaches exactly this
count. The answer is the sum of ⌈k / 2⌉ over all runs of all levels,
which a brute force over small cases also confirms.

There are up to 10⁹ levels, but the runs only change at the heights of
the nails. Process the nails from the highest down and join each one
with already processed neighbors in a disjoint set union. A new nail is
a run of length 1, adding 1 at every level up to its height, so it adds
its height. Joining two runs changes ⌈a / 2⌉ + ⌈b / 2⌉ into
⌈(a + b) / 2⌉, one less exactly when both lengths are odd, and the
joined run lasts for all levels up to the current height, so that join
subtracts the current height.

In the first example the levels hold the runs {1} at height 4, {1} and
{3} at heights 3 and 2, and {1, 2, 3} at height 1, so the answer is
1 + 2 + 2 + 2 = 7.

Sorting makes it O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 1788 KB |
| [2225_dsu_sorting.go](2225_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.125 s | 5764 KB |
| [2225_dsu_sorting.java](2225_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.187 s | 2624 KB |
| [2225_dsu_sorting.py](2225_dsu_sorting.py) | PyPy 3.10 x64 | dsu, sorting | O(N log N) | AC | 0.359 s | 19808 KB |
| [2225_dsu_sorting.rs](2225_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 4660 KB |
