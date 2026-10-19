# 1872. Spacious Office

[Timus 1872](https://acm.timus.ru/problem.aspx?space=1&num=1872) · difficulty 799 · matching

Original problem by Alexander Klepinin, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n project teams and n rooms with given areas. Team i agrees
to a room with an area from lᵢ to rᵢ. Give every team its own room. If
there is exactly one way, print it; if there are several, or none, say
so.

## Input

n (2 ≤ n ≤ 1000), then the n room areas, then n lines lᵢ rᵢ
(lᵢ ≤ rᵢ). All areas are from 1 to 10 000.

## Output

"Perfect!" and the room of every team when the seating is unique,
"Ask Shiftman for help." when there are several seatings, and
"Let's search for another office." when there is none.

## Examples

### Example 1

Input:

```
3
40 50 60
30 70
20 40
60 60
```

Output:

```
Perfect!
2 1 3
```

### Example 2

Input:

```
3
40 50 70
30 70
20 50
60 60
```

Output:

```
Let's search for another office.
```

## Solution

Sort the rooms by area. To find a seating, give the rooms out from the
smallest up: each room goes to the waiting team (one with lᵢ at most
its area) whose rᵢ is the smallest. If no team is waiting, or that team's
rᵢ is already below the room, there is no seating. Any seating can be
turned into this one by swaps that keep it valid, so the greedy never
fails when a seating exists.

In sorted order the team in room q accepts a contiguous block of rooms
first(q) … last(q) that contains q. Another seating exists exactly
when some teams can pass rooms round in a cycle, each moving into the
room of the next. The shortest such cycle always has length 2. Take its
largest room M, the room P of the team that moves into M, and the room
S that the team of M moves into; both P and S are smaller than M. If
P ≥ S, the block of M covers P, so the teams of P and M can swap. If
P < S, the block of P covers S, so the team of P could move straight
into S, which gives a shorter cycle. So the seating is unique exactly
when no p < q have last(p) ≥ q and first(q) ≤ p. Rooms of equal area
always give such a pair. The greedy takes `O(n log n)` and the check
`O(n²)`.

In the first example the rooms 40, 50 and 60 go to teams 2, 1 and 3.
Team 1 accepts all three rooms, but teams 2 and 3 accept only their own,
so nobody can swap.

Pitfalls:

- two rooms of the same area can always be swapped, so a seating that
  uses both is never unique;
- a swap need not involve neighbouring rooms: the teams of the smallest
  and the largest room may swap over a middle room taken by a team that
  wants only it;
- checking feasibility with the greedy alone is not enough; the
  uniqueness test is a separate step.

The verdicts match a search over all seatings on 30 000 random offices
of up to 6 rooms, and an independent accepted implementation on 180
random offices of up to 1000 rooms.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1872_matching.cpp](1872_matching.cpp) | G++ 13.2 x64 | matching | O(n^2) | AC | 0.015 s | 244 KB |
| [1872_matching.go](1872_matching.go) | Go 1.14 x64 | matching | O(n^2) | AC | 0.031 s | 1260 KB |
| [1872_matching.java](1872_matching.java) | Java 1.8 | matching | O(n^2) | AC | 0.156 s | 2884 KB |
| [1872_matching.py](1872_matching.py) | Python 3.12 x64 | matching | O(n^2) | AC | 0.125 s | 2932 KB |
| [1872_matching.rs](1872_matching.rs) | Rust 1.75 x64 | matching | O(n^2) | AC | 0.046 s | 292 KB |
