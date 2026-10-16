# 1771. A Deputy's Morning

[Timus 1771](https://acm.timus.ru/problem.aspx?space=1&num=1771) · difficulty 5549 · implementation

Original problem by Alex Samsonov, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has n stops and m bus routes; each route is a list of distinct
stops, a bus takes one minute between neighbouring stops and does not
turn back, buses leave the first stop of a route at whole minutes from
07:00, never two on one route at once, and there is no other schedule.
Every passenger is at a stop by 06:59 and takes the first bus that goes
to their stop; among buses arriving together, the one that gets there
sooner, then the one with the smaller route number.

From 07:00 a man at stop 1 wrote down every bus stopping there, with
its minute and route, including all buses at the minute of the last
one, which he boarded. It already held 42 people and 13 more got on
with him. How few and how many of these 55 can still be on board when
the bus reaches stop 2?

## Input

n and m (3 ≤ n, m ≤ 100), then the m routes, each a list of stops ended
by −1, then k (1 ≤ k ≤ 100) and the k records `hh:mm route` in time
order, the last being his bus. That bus goes on to stop 2, and stop 1
is not the first stop of its route.

## Output

The smallest and the largest number of the 55 riding with him from
stop 1 to stop 2.

## Examples

### Example 1

Input:

```
4 3
1 4 -1
4 1 -1
3 1 4 2 -1
2
07:00 1
07:10 3
```

Output:

```
13 55
```

## Solution

A recorded bus has a known start: its minute at stop 1 minus the
position of stop 1 in its route, so its minute at every stop of its
route is known. A passenger waiting at a stop `src` for a stop `dst`
took this bus exactly when no recorded bus serving `src` to `dst` came
to `src` sooner, or at the same minute reaching `dst` sooner, or as
soon with a smaller route number. Buses not in the notebook do not
restrict the possible trips: both buses that would reach stop 1 after
the man leaves and buses whose routes avoid stop 1 may simply not
run.

The 13 boarded at stop 1, the 42 at the stops before it, and since all
of them are still aboard at stop 1, they ride to stops after it. For
each group it is enough to know whether some trip with a destination
before stop 2 can pick this bus, and whether some trip to stop 2 or
beyond can: all members of a group can then share that destination. So
the smallest count adds a group only when no early destination is
possible, and the largest only when a late one is. `O(mn + L² · k)`
for the chosen route of length L.

In the example the earlier bus of route 1 also goes from stop 1 to 4,
so the 13 cannot be riding to 4 and must stay to stop 2, while the 42
from stop 3 may ride to 4 or to 2: between 13 and 55.

Pitfalls:

- the man himself does not count, and he did not necessarily follow
  the rule;
- among buses at the same minute, the one reaching the destination
  sooner wins, and only then the smaller route;
- a bus seen at stop 1 may reach the earlier stops of this route before
  this bus does, so it can take those passengers away.

The answers agree with an independent accepted implementation on 450
random notebooks, all of them possible under the rules.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1771_implementation.cpp](1771_implementation.cpp) | G++ 13.2 x64 | implementation | O(mn + L^2 k) | AC | 0.015 s | 284 KB |
| [1771_implementation.go](1771_implementation.go) | Go 1.14 x64 | implementation | O(mn + L^2 k) | AC | 0.031 s | 1604 KB |
| [1771_implementation.java](1771_implementation.java) | Java 1.8 | implementation | O(mn + L^2 k) | AC | 0.125 s | 3292 KB |
| [1771_implementation.py](1771_implementation.py) | Python 3.12 x64 | implementation | O(mn + L^2 k) | AC | 0.078 s | 1748 KB |
| [1771_implementation.rs](1771_implementation.rs) | Rust 1.75 x64 | implementation | O(mn + L^2 k) | AC | 0.031 s | 384 KB |
