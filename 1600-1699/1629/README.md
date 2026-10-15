# 1629. Trip

[Timus 1629](https://acm.timus.ru/problem.aspx?space=1&num=1629) · difficulty 792 · simulation

Original problem by Alex Samsonov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A traveller has to fly through airports 1, 2, …, N, always from airport i
to airport i + 1, and is at airport 1 exactly at midnight. Every day
Q_i flights leave airport i at the times of a fixed schedule, but from
now on each of them leaves D_i minutes late; the flight to airport i + 1
takes T_i minutes, and changing planes is instant. In how many minutes
does the traveller reach airport N?

## Input

The first line holds N (2 ≤ N ≤ 100). Then airports 1 to N − 1 are
described by two lines each: Q_i, D_i and T_i (1 ≤ Q_i ≤ 10;
0 ≤ D_i, T_i < 1440), then the Q_i scheduled departure times as HH:MM.

## Output

The number of minutes after midnight when the traveller lands at
airport N.

## Examples

### Example 1

Input:

```
3
2 60 1200
00:00 01:00
2 0 300
20:30 21:30
```

Output:

```
1590
```

### Example 2

Input:

```
3
1 0 600
10:00
1 60 60
19:00
```

Output:

```
1260
```

## Solution

Waiting longer never helps, so at every airport the traveller takes the
first flight that leaves no earlier than the arrival. A flight scheduled
at HH:MM leaves today at 60 · HH + MM + D_i minutes, and on later days
whole multiples of 1440 after that; when it has already left, rounding
the difference up to whole days gives its next departure. The earliest
of the Q_i candidates plus T_i is the arrival at the next airport.
`O(ΣQ_i)`.

Pitfalls:

- a flight leaving exactly at the arrival minute can still be taken
  (the second example);
- the delays apply from midnight on, so a flight scheduled yesterday
  evening does not move into today: with a delay of 120 minutes the
  23:00 flight leaves at 25:00, not at 01:00 (test 06);
- with the delay, today's flight may leave after midnight of the next
  day; that is still the earliest copy of it (test 04).

The answers match an independent accepted implementation on 150 random
routes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1629_simulation.cpp](1629_simulation.cpp) | G++ 13.2 x64 | simulation | O(ΣQ_i) | AC | 0.015 s | 132 KB |
| [1629_simulation.go](1629_simulation.go) | Go 1.14 x64 | simulation | O(ΣQ_i) | AC | 0.031 s | 1160 KB |
| [1629_simulation.java](1629_simulation.java) | Java 1.8 | simulation | O(ΣQ_i) | AC | 0.109 s | 876 KB |
| [1629_simulation.py](1629_simulation.py) | Python 3.12 x64 | simulation | O(ΣQ_i) | AC | 0.093 s | 500 KB |
| [1629_simulation.rs](1629_simulation.rs) | Rust 1.75 x64 | simulation | O(ΣQ_i) | AC | 0.046 s | 220 KB |
