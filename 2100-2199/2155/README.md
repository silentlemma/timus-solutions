# 2155. Catching a drone carried by the wind on a weighted grid

[Timus 2155](https://acm.timus.ru/problem.aspx?space=1&num=2155) · difficulty 990 · dijkstra

Original problem by Valentin Zuev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On an h × w grid every cell has a cost from 1 to 999 999 and a wind
direction. A walker moves to a side neighbour in as many seconds as the
cost of that neighbour, or waits anywhere. A drone moves one cell per
second in the wind direction of its cell and is lost when the wind
points off the grid. The walker catches it on being in the drone's cell
while the drone is there; arriving at the moment it leaves is too late.
Find the earliest catch, or −1. The limits are 2 seconds and 256 MB.

## Input

h and w, 1 ≤ h, w ≤ 250, the two starting cells, the costs, then the
wind letters U, D, L, R.

## Output

The earliest time, or −1.

## Examples

### Example 1

Input:

```
2 7
1 1
1 4
1 1 1 1 1 1 1
1 1 1 1 1 1 1
RDRDRDR
URURURU
```

Output:

```
7
```

### Example 2

Input:

```
2 6
1 1
1 4
1 1 1 1 1 1
1 1 1 1 1 1
RDRDRD
URURUR
```

Output:

```
-1
```

### Example 3

Input:

```
3 3
2 2
1 1
8 9 8
8 8 8
8 8 8
RRD
URD
ULL
```

Output:

```
9
```

## Solution

Waiting is free, so the walker can be in a cell at any time from the
shortest arrival time on, and Dijkstra's algorithm from the start gives
those times for all cells.

The drone's route is fixed: it is a walk along the wind arrows, and
since it has one successor per cell it either leaves the grid or enters
a cycle. Follow it until a cell repeats or it is lost, recording the
time t of every visit. The drone is in its cell at time t, so a catch
there at time t is possible exactly when the shortest arrival is at
most t. Cells on the cycle are visited again every period p, so for
them the first visit at or after the arrival time,
t + ⌈(arrival − t) / p⌉ · p, also counts. The answer is the smallest of
these times. The work is O(hw log(hw)).

In the second example the drone keeps moving away along a path that
leaves the grid before the walker can get ahead of it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2155_dijkstra.cpp](2155_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 1972 KB |
| [2155_dijkstra.go](2155_dijkstra.go) | Go 1.14 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 4784 KB |
| [2155_dijkstra.java](2155_dijkstra.java) | Java 1.8 | dijkstra | O(hw log(hw)) | AC | 0.125 s | 2720 KB |
| [2155_dijkstra.py](2155_dijkstra.py) | Python 3.12 x64 | dijkstra | O(hw log(hw)) | AC | 0.234 s | 16068 KB |
| [2155_dijkstra.rs](2155_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 4140 KB |
