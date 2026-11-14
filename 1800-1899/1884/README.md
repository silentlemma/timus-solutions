# 1884. Way to the University

[Timus 1884](https://acm.timus.ru/problem.aspx?space=1&num=1884) · difficulty 675 · sorting

Original problem by Egor Shchelkonogov, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Egor wants to cross a road of two 2-metre lanes, walking straight
across at 5 km/h without stopping. Traffic keeps to the right, so the
n cars coming from the left use the near lane and the m cars from the
right the far lane. Every car is 2 m wide and 5 m long and drives at
20 km/h; the distances to them are given. What is the least time Egor
must wait before starting?

## Input

n (1 ≤ n ≤ 300) and the distances to the cars on the left, then m
(1 ≤ m ≤ 300) and the distances to the cars on the right. Distances are
from 1 to 10 000 metres and grow by at least 5 along each row.

## Output

The least waiting time in seconds, with at least six digits after the
decimal point.

## Examples

### Example 1

Input:

```
1
1
1
100
```

Output:

```
1.080000
```

## Solution

Measure time in units of 1/50 s, so that everything is an integer: a
car at 20 km/h covers a metre in 9 units, and Egor crosses a lane in 72
units. A car at distance d is on Egor's path from 9d to 9(d + 5). Starting
at s, Egor is in the near lane from s to s + 72 and in the far lane
from s + 72 to s + 144. A car makes s bad when these times overlap
with more than a point. That is an open interval of bad starts:
(9d − 72, 9(d + 5)) for a car on the left and (9d − 144, 9(d + 5) − 72)
for a car on the right. Sort the intervals by their left end and sweep
from s = 0: while the next interval starts before s, move s to its
right end if that is later. The first interval starting at or after s
ends the sweep. Print s/50. `O((n + m) log(n + m))`.

In the example the car on the left blocks the starts below 54 units,
and the car on the right blocks only (756, 873), so Egor waits
54/50 = 1.08 s.

Pitfalls:

- touching a car only at a moment is allowed, so the intervals are
  open: a car 8 m away on the left lets Egor go at once;
- the cars on the right matter only while Egor is in the far lane,
  72 units later;
- integer units avoid any rounding when gaps between cars are exactly
  wide enough.

The waits match a search over every start time in 1/50 s steps on 26
random roads, and an independent accepted implementation on 100.

## Optimized solutions

The C++ variant merges the already sorted lists of interval starts from both lanes. It keeps the earliest possible start time. If the next open interval starts at or after that time, the time is feasible. Otherwise the interval can move the time forward to its right endpoint. The merge takes O(n + m) time and uses O(n + m) space to store the lane data. The metrics come from submission 11317001.

Java 1.8 also merges the two ordered lists of open intervals and advances the earliest starting time only when an interval covers it. Submission 11317148 took 0.234 s and 392 KB; the base took 0.171 s and 3200 KB.

Rust stores the intervals of the near lane and merges them with the far lane as its intervals are read. Rust 1.75 x64, submission 11323323. Time 0.015 → 0.046 s, memory 268 → 56 KB.

Python 3.12 x64 also merges the two ordered lists of open intervals and advances the earliest starting time only when an interval covers it. Submission 11317139 took 0.062 s and 552 KB; the base took 0.078 s and 472 KB.

Go 1.14 x64 also merges the two ordered lists of open intervals and advances the earliest starting time only when an interval covers it. Submission 11317133 took 0.015 s and 1136 KB; the base took 0.046 s and 1192 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321924 · Java 1.8 №11321925 · Go 1.14 x64 №11322075 · Python 3.12 x64 №11322076 · Rust 1.75 x64 №11321926.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1884_sorting.cpp](1884_sorting.cpp) | G++ 13.2 x64 | sorting | O((n + m) log(n + m)) | AC | 0.015 s | 196 KB | 11321924 |
| [1884_sorting.go](1884_sorting.go) | Go 1.14 x64 | sorting | O((n + m) log(n + m)) | AC | 0.046 s | 1192 KB | 11322075 |
| [1884_sorting.java](1884_sorting.java) | Java 1.8 | sorting | O((n + m) log(n + m)) | AC | 0.14 s | 3228 KB | 11321925 |
| [1884_sorting.py](1884_sorting.py) | Python 3.12 x64 | sorting | O((n + m) log(n + m)) | AC | 0.078 s | 472 KB | 11322076 |
| [1884_sorting.rs](1884_sorting.rs) | Rust 1.75 x64 | sorting | O((n + m) log(n + m)) | AC | 0.015 s | 268 KB | 11321926 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1884_two_pointers.cpp](1884_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n + m) | AC | 0.001 s | 124 KB | 11317001 |
| [1884_two_pointers.go](1884_two_pointers.go) \* | Go 1.14 x64 | two_pointers | O(n + m) | AC | 0.015 s | 1136 KB | 11317133 |
| [1884_two_pointers.py](1884_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n + m) | AC | 0.062 s | 552 KB | 11317139 |
| [1884_two_pointers.rs](1884_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(n + m) | AC | 0.046 s | 56 KB | 11323323 |
| [1884_two_pointers.java](1884_two_pointers.java) \* | Java 1.8 | two_pointers | O(n + m) | AC | 0.234 s | 392 KB | 11317148 |

\* The Go version is accepted and remains outside the rating target. The Python version is accepted and remains outside the rating target. The Rust version is accepted and remains outside the rating target. The Java version is accepted and remains outside the rating target.
