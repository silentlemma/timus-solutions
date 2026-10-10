# 1129. Painting doors green on one side and orange on the other so that every room is balanced

[Timus 1129](https://acm.timus.ru/problem.aspx?space=1&num=1129) · difficulty 406 · graphs

Original problem by Magaz Asanov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A building has `N ≤ 100` rooms joined by doors; two rooms may share
several doors. Every door is painted green on one side and orange on the
other. Paint the doors so that in every room the numbers of green and
orange door sides differ by at most one. Print `Impossible` if this
cannot be done.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines: the number of doors of a room, then the numbers of
the rooms they lead to, in increasing order.

## Output

`N` lines: the colours of the doors of each room in the input order, `G`
for green and `Y` for orange, or the word `Impossible`.

## Checking

Any valid colouring is accepted. The checker verifies that every room gets
one colour per listed door, that each room is balanced within one, and
that for every pair of rooms the doors between them are green on exactly
one side. The doors between the same two rooms look alike, so it counts
green marks per pair instead of matching single doors.

## Examples

### Example 1

Input:

```
5
3 2 3 4
3 1 3 5
4 1 2 4 5
3 1 3 5
3 2 3 4
```

Output:

```
G Y G
Y G Y
G Y Y G
Y G G
G Y Y
```

## Solution

Think of the rooms as vertices and the doors as edges. Painting a door
green in room `u` and orange in room `v` is the same as directing the edge
from `u` to `v`, so the task asks for an orientation where every vertex has
out-degree and in-degree differing by at most one. Such an orientation
always exists. Add a dummy vertex joined by one extra edge to each vertex
of odd degree; there is an even number of those, so now every degree is
even. Each connected part then has an Euler circuit, and walking it
leaves every vertex exactly as often as it enters. Direct each edge the
way the walk goes and drop the extra edges: a vertex loses at most one
edge, so its two counts differ by at most one. `O(N + D)` for `D` doors,
plus the cost of the map that pairs door mentions.

Pitfalls:

- `Impossible` is never the answer;
- a door appears in the rows of both its rooms, so the two mentions must
  be paired: the `k`-th mention of `v` in room `u` goes with the `k`-th
  mention of `u` in room `v`; doors between the same rooms are
  interchangeable, so any consistent pairing works;
- the circuit is walked with an explicit stack and a pointer to the next
  unused edge of each vertex, so every edge is looked at a constant number
  of times;
- rooms without doors print an empty line.

The answers were checked by the checker on every test and on random
buildings with many doors repeated between the same rooms.

## Language notes

- All languages run the same walk with an explicit stack.
- Python pairs mentions with lists keyed by the pair of rooms; with at
  most a few thousand doors the queue operations are cheap.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1129_graphs.cpp](1129_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2096 KB |
| [1129_graphs.go](1129_graphs.go) | Go 1.14 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2424 KB |
| [1129_graphs.java](1129_graphs.java) | Java 1.8 | graphs | O(N + D log D) | AC | 0.156 s | 3876 KB |
| [1129_graphs.py](1129_graphs.py) | Python 3.12 x64 | graphs | O(N + D log D) | AC | 0.093 s | 2592 KB |
| [1129_graphs.rs](1129_graphs.rs) | Rust 1.75 x64 | graphs | O(N + D log D) | AC | 0.015 s | 1172 KB |
