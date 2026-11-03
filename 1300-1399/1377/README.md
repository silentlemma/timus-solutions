# 1377. Distance between two cells along a rectangular spiral

[Timus 1377](https://acm.timus.ru/problem.aspx?space=1&num=1377) · difficulty 295 · simulation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Visit an `N × M` grid, `2 ≤ N,M ≤ 100`, starting at `(1,1)` and moving
right. Continue straight while the next cell is unvisited and in bounds;
otherwise turn clockwise. Two distinct cells are given by their row and
column, each within the grid. Find the absolute difference of their visit
indices. Time limit: 1 second. Memory limit: 64 MB.

## Input

`N M`, followed by `r₁ c₁` and `r₂ c₂`, all one-based.

## Output

The absolute difference of the visit indices.

## Checking

Integer answers are compared as whitespace-separated tokens.

## Examples

### Example 1

Input:

```
5 4
2 2
5 3
```

Output:

```
6
```

## Solution

Simulate the clockwise spiral. Mark an outer frame as visited, number
each grid cell when reached, and turn right when the next cell is already
visited. Each step visits one new cell; the frame prevents leaving the
grid. The answer is the absolute difference of the two numbers. Time and
space are `O(N·M)`. Either input cell may come first; thin rectangles and
the final single row or column need no separate simulation rule.

## Optimized solutions

For a zero-based cell `(r,c)`, its layer is
`d = min(r,c,N−1−r,M−1−c)`. Remove the outer `d` layers: the remaining
rectangle has height `h=N−2d` and width `w=M−2d`, and exactly `N·M−h·w`
cells precede it. Translate the cell by subtracting `d`. Its offset on the
perimeter is `c` on the top edge, `w−1+r` on the right edge,
`w−1+h−1+w−1−c` on the bottom edge, and `2(h+w−2)−r` on the left edge,
testing the edges in that order. For a final single row or column use `c`
or `r` instead. This counts every cell once in spiral order; subtract the
two indices and take the absolute value. Time and extra space are `O(1)`.

The unchanged simulation programs remain the simple versions. The new
formula reduces memory by 57.8% in C++, 73.4% in Java and 50.2% in Python;
Go time falls from 0.046 s to 0.015 s (67.4%). C++ and Java meet the ranking
goal in the snapshot of 1 November 2026. Python is third by time and first
by memory, missing the stricter first-place target for this language, so
its row is starred. Go has no competitors in the filtered sample. Rust's
formula saves only 25% memory and one timer tick: it is not added as an
optimized source. All layer formulas were checked against a separately
generated spiral, including final strips and every cell of small grids.

## Language notes

All five base sources simulate the same spiral. Four distinct formula sources are listed below.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1377_simulation.cpp](1377_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.001 s | 256 KB | 11285700 |
| [1377_simulation.go](1377_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.046 s | 1172 KB | 11285703 |
| [1377_simulation.java](1377_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.109 s | 1640 KB | 11285709 |
| [1377_simulation.py](1377_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 924 KB | 11285705 |
| [1377_simulation.rs](1377_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.031 s | 272 KB | 11285712 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1377_math.cpp](1377_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 108 KB | 11308023 |
| [1377_math.go](1377_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1052 KB | 11308026 |
| [1377_math.java](1377_math.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 436 KB | 11308028 |
| [1377_math.py](1377_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 460 KB | 11308022 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
