# 1096. The fewest exchanges of two-sided route plates

[Timus 1096](https://acm.timus.ru/problem.aspx?space=1&num=1096) · difficulty 709 · bfs, graphs

Original problem by Stanislav Vasiliev, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `K` buses (`1 ≤ K ≤ 1000`) runs on route `rᵢ` and carries a plate
with `rᵢ` on the front and another number `bᵢ` on the back (numbers 1 to
2000). A new bus must run on route `T` but got a plate showing `S1` and
`S2`. A driver agrees to swap plates with the new driver when the new
driver's plate shows the route of his bus on either side. Find the
fewest swaps after which the new driver holds a plate showing `T`, and
the buses to swap with, or print `IMPOSSIBLE`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then `K` lines with `rᵢ` and `bᵢ`, then `T`, `S1` and `S2`.

## Output

The number of swaps `M` and `M` bus numbers in order, or `IMPOSSIBLE`.

## Checking

Any shortest sequence is accepted. The checker replays the swaps and
compares their number with the fewest possible.

## Examples

### Example 1

Input:

```
4
8 5
5 4
7 4
1 5
4 1 8
```

Output:

```
2
1
2
```

## Solution

What matters is which plate the new driver holds: the first one or the
plate of some bus `j`. From a plate showing `x` and `y`, a swap with any
bus on route `x` or route `y` is possible and gives that bus's plate. A
breadth-first search over these states finds the fewest swaps; each bus
is reached once, so the buses are grouped by route and every group is
used up the first time one of its routes is shown. The search stops at
the first plate showing `T`, and the remembered predecessors give the
buses in order. `O(K)`.

Why the swapped plates do not spoil this: after a swap, bus `j` holds the
plate the new driver had before. Swapping with `j` again would only bring
that old plate back, so a shortest sequence never does it, and the other
buses are untouched.

Pitfalls:

- the bus numbers, not the route numbers, are printed;
- the answer has at least one swap, since `T` is on neither side of the
  first plate;
- `S1` may equal `S2`, and many buses may share a route.

The checker computes the fewest swaps layer by layer and replays the
listed swaps with the plates changing hands.

## Language notes

- Every language removes a route's group from its map once it is used
  (`pop`, `erase`, `delete`, `remove`), so no bus enters the queue twice.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1096_bfs.cpp](1096_bfs.cpp) | G++ 13.2 x64 | bfs | O(K) | AC | 0.015 s | 368 KB |
| [1096_bfs.go](1096_bfs.go) | Go 1.14 x64 | bfs | O(K) | AC | 0.015 s | 1388 KB |
| [1096_bfs.java](1096_bfs.java) | Java 1.8 | bfs | O(K) | AC | 0.187 s | 5636 KB |
| [1096_bfs.py](1096_bfs.py) | Python 3.12 x64 | bfs | O(K) | AC | 0.078 s | 796 KB |
| [1096_bfs.rs](1096_bfs.rs) | Rust 1.75 x64 | bfs | O(K) | AC | 0.031 s | 504 KB |
