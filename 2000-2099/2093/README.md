# 2093. Fastest route over roads that snow slows down

[Timus 2093](https://acm.timus.ru/problem.aspx?space=1&num=2093) · difficulty 1369 · dijkstra

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n crossroads are joined by m roads with normal travel times tᵢ. Snow
falls from moment 0; a road entered T minutes after its last cleaning
(or after the start) takes min(⌈(1 + T/100) tᵢ⌉, 100500 tᵢ). Each road
has a timetable of cleanings, during which it is closed, and a drive
must also end before the road's next cleaning starts. Waiting at a
crossroads is allowed. Find the earliest arrival at crossroads n when
leaving crossroads 1 at moment 0. The limits are 2 seconds and 64 MB.

## Input

n and m (up to 10⁵), the m roads aᵢ bᵢ tᵢ (tᵢ ≤ 10⁶), then k ≤ 10⁵
cleanings pᵢ sᵢ fᵢ (road and closing interval, times up to 10⁹; the
cleanings of one road do not overlap).

## Output

The earliest arrival time.

## Examples

### Example 1

Input:

```
4 3
1 2 10
2 3 10
3 4 10
1
2 10 15
```

Output:

```
38
```

## Solution

Fix a road and the moment we reach its end. Between two cleanings, a
later departure only means more snow, so inside each open gap the best
departure is the earliest one. A later gap starts after a cleaning that
began after the earlier departure could have finished, so the first gap
whose earliest departure still finishes before the next cleaning gives
the earliest arrival; after the last cleaning the road is always usable.
This arrival function never decreases when we come later, so Dijkstra's
algorithm on arrival times works: popping a crossroads, each road is
relaxed by scanning its sorted cleanings. Every road is relaxed at most
twice, so scanning takes O(m + k) and the heap work takes O((n + m) log n).
Sorting the cleaning schedules takes O(k log k), giving a total of
O((n + m) log n + k log k). Travel times are computed in integers with
the cap of 100500 tᵢ.

A pitfall is omitting sorting from the bound: test gen7 (generator
`5 7`) has only two crossroads and one road, but 100000 unsorted cleanings,
so their sorting cost cannot be absorbed into O(k log n).

In the example the first road takes 10 minutes; the second is cleaned
from 10 to 15, so it is entered at 15 and done at 25; the third has had
25 minutes of snow and takes ⌈1.25 · 10⌉ = 13 minutes, arriving at 38.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2093_dijkstra.cpp](2093_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.156 s | 7948 KB |
| [2093_dijkstra.go](2093_dijkstra.go) | Go 1.14 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.062 s | 13480 KB |
| [2093_dijkstra.java](2093_dijkstra.java) | Java 1.8 | dijkstra | O((n + m) log n + k log k) | AC | 0.187 s | 10832 KB |
| [2093_dijkstra.py](2093_dijkstra.py) | Python 3.12 x64 | dijkstra | O((n + m) log n + k log k) | AC | 1.015 s | 21440 KB |
| [2093_dijkstra.rs](2093_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O((n + m) log n + k log k) | AC | 0.031 s | 15516 KB |
