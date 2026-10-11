# 1251. A cemetery that frees forgotten graves

[Timus 1251](https://acm.timus.ru/problem.aspx?space=1&num=1251) · difficulty 1486 · simulation

Original problem by Stanislav Vasilyev, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cemetery is an N × M grid of graves (1 ≤ N, M ≤ 100), empty at first. Each
newcomer takes the free grave with the smallest row, then the smallest
column; with no free grave, the newcomer goes to the crematorium.
Relatives visit clients now and then. A grave becomes free on the first
day when its client has not been buried or visited for more than 1000
days and none of its up to 8 neighbours (including diagonals) has been
visited in the last 100 days. Given up to 15 000 events in time order
(days 0 to 7600, at most 10 000 arrivals), count the clients sent to the crematorium.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then one event per line: `day d` for an arrival, or `day v k`
for a visit to client k (clients are numbered in order of arrival).

## Output

The number of cremated clients.

## Examples

### Example 1

Input:

```
2 2
1 d
1 d
1 d
1 d
300 d
500 v 2
1001 d
1002 d
1002 d
1003 v 3
1003 d
1003 d
1236 v 2
2032 v 2
2033 d
```

Output:

```
3
```

## Solution

For an occupied grave the day it becomes free is fixed by two numbers:
`max(touched + 1001, nearVisit + 101)`, where `touched` is the last burial
or visit of its client and `nearVisit` the last visit to a neighbour. A
visit raises `touched` of its grave and `nearVisit` of the neighbours, so
the release day only ever moves later.

The program keeps each occupied grave's release day in a min-heap, with
new entries after burials and visits, and stale entries skipped when popped.
Before the events of a day it frees every grave whose release day has
come; then it handles the day's events in order. Free graves sit in a
second min-heap keyed by `row · M + column`, so an arrival takes the
smallest. `O(NM + E log(NM + E))` with E ≤ 15 000.

Pitfalls:

- graves free at the start of a day, before that day's arrivals; the
  example needs this on day 1002;
- a grave is still held on day `touched + 1000` and frees on the next
  day (test 02);
- a visit to a client whose grave was already freed, or who was
  cremated, changes nothing (test 04), and clients keep their numbers
  even when cremated;
- a burial does not delay the neighbours.

The answers were compared with a day-by-day simulation on 200 random
small cemeteries.

## Language notes

- Go, C++ and Java pack a pending release into one integer,
  `day · cells + grave`; Python and Rust push a pair.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1251_simulation.cpp](1251_simulation.cpp) | G++ 13.2 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.031 s | 396 KB |
| [1251_simulation.go](1251_simulation.go) | Go 1.14 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.062 s | 4676 KB |
| [1251_simulation.java](1251_simulation.java) | Java 1.8 | simulation | O(NM + E log(NM + E)) | AC | 0.125 s | 5108 KB |
| [1251_simulation.py](1251_simulation.py) | Python 3.12 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.265 s | 8396 KB |
| [1251_simulation.rs](1251_simulation.rs) | Rust 1.75 x64 | simulation | O(NM + E log(NM + E)) | AC | 0.015 s | 1604 KB |
