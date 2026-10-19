# 1892. Morning in Koltsovo

[Timus 1892](https://acm.timus.ru/problem.aspx?space=1&num=1892) · difficulty 886 · simulation

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Schedule two FIFO queues of operations on one runway: departures and
landings. Each flight joins its queue at a known time and starts as
soon as permitted. Required gaps are measured between operation starts:

| Earlier start | Later start | Minimum gap |
| --- | --- | --- |
| departure | departure | t₁ |
| departure | landing | t₂ |
| landing | departure | t₃ |
| landing | landing | t₄ |

A departure cannot start while any flight is waiting to land, even
when that landing must still wait for a safety gap. A flight joining
the landing queue exactly when a departure could start also takes
priority. Find the start time of every operation.

The limits are 1 second and 64 MB.

## Input

The first line contains t₁, t₂, t₃ and t₄ in seconds, with
30 ≤ tᵢ ≤ 500 and max(t₁, t₄) ≤ min(t₂, t₃).

Then comes n, the number of departures, with 1 ≤ n ≤ 50, followed by
their n queue-arrival times. Next comes m, the number of landings,
with 1 ≤ m ≤ 50, followed by their m queue-arrival times.

Each time has the format `hh:mm:ss` and lies between `06:00:00` and
`10:00:00`, inclusive. Each list is strictly increasing; times in the
two different lists may coincide.

## Output

Print the n departure start times, then the m landing start times,
preserving the input order within each group. Use `hh:mm:ss`, with
two digits per field. Starts may be later than `10:00:00`.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
60 60 60 60
2
07:01:00
07:01:30
2
07:00:00
07:02:10
```

Output:

```
07:01:00
07:02:00
07:00:00
07:03:00
```

## Solution

Convert times to seconds. Keep a pointer to the first unprocessed
flight in each queue, plus the most recent departure start D and
landing start A. A missing previous operation imposes no restriction.

For the next departure, compute its earliest safety-compatible start
d = max(its arrival time, D + t₁, A + t₃). Compare d with the next
landing's queue-arrival time a, rather than its feasible start time.
If a ≤ d, process that landing first at
max(a, D + t₂, A + t₄), then update A. Otherwise process the departure
at d and update D. If one queue is exhausted, keep processing the other
with the same safety constraints.

This choice is forced. No departure can start before d. If a ≤ d,
the first landing is already queued when the departure becomes
possible, and it blocks departures even if its own safety delay ends
later. If a > d, no landing is queued at d, so the departure starts
then. After choosing a queue, its first flight starts at the maximum
of its arrival time and the required gaps. Only the latest start of
each kind matters, because every earlier start of that kind gives a
weaker lower bound. Repeating the step produces the required schedule.

Each step processes one flight, so the time is `O(n + m)`. Storing the
input lists and their grouped answers takes `O(n + m)` memory.

In the example, the first landing starts at `07:00:00`. Departures
start at `07:01:00` and `07:02:00`: the second landing has not arrived
yet. It joins its queue at `07:02:10`, but the last departure forces
its start to `07:03:00`. The output groups departures before landings,
rather than listing all four starts chronologically.

Pitfalls:

- compare the next landing's arrival with d, including equality;
- a queued landing blocks departures before its own feasible start;
- keep separate latest starts for departures and landings;
- measure gaps from starts, not operation completion;
- preserve FIFO order and print the two groups in input order.

The answers agree with a second-by-second simulation on 179 cases, with
exhaustive search on 700 small ones and with an independent accepted
implementation on 56 generated ones.

## Language notes

All five versions use the same simulation with integer seconds. C++, Java
and Rust store times in signed 32-bit integers; Go uses `int` and Python
uses its integer type. These ranges are sufficient for at most 100
operations with gaps no larger than 500 seconds. The initial negative
sentinel must remain signed.

Python reads byte tokens, while Java uses buffered line input. Every
version pads each clock field with leading zeroes and retains times past
the last possible input arrival; it does not wrap the answer at `10:00:00`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1892_simulation.cpp](1892_simulation.cpp) | G++ 13.2 x64 | simulation | O(n + m) | AC | 0.015 s | 444 KB |
| [1892_simulation.go](1892_simulation.go) | Go 1.14 x64 | simulation | O(n + m) | AC | 0.031 s | 1148 KB |
| [1892_simulation.java](1892_simulation.java) | Java 1.8 | simulation | O(n + m) | AC | 0.140 s | 540 KB |
| [1892_simulation.py](1892_simulation.py) | Python 3.12 x64 | simulation | O(n + m) | AC | 0.078 s | 612 KB |
| [1892_simulation.rs](1892_simulation.rs) | Rust 1.75 x64 | simulation | O(n + m) | AC | 0.015 s | 248 KB |
