# 1930. A Route with Fewest Gear Changes

[Timus 1930](https://acm.timus.ru/problem.aspx?space=1&num=1930) · difficulty 162 · shortest_paths

Original problem from Ural Regional School Programming Contest 2012 | by Grigoriy Nazarov (prepared by Bulat Zaynullin).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A road can be traversed in either direction. Each road record lists its
uphill direction first-to-second; the reverse direction requires downhill
gear. Find a route from a given start city to a different target city that
minimizes changes between these two gears. The first gear may be selected
freely and costs nothing. A route exists. Limits: 1.5 seconds, 64 MB.

## Input

First n,m, with 2≤n≤10000 and 1≤m≤100000. The next m lines contain
distinct endpoint identifiers a,b in 1..n, representing uphill a→b.
There are no loops and at most one road per unordered city pair.
The final line contains start and target, which differ and are connected.
Other cities may be disconnected. Numeric identifiers do not encode direction.

## Output

One integer: the least possible number of gear changes.

## Checking

Compare the single integer token exactly.

## Examples

```
3 2
1 2
3 2
1 3
```

```
1
```

```
3 3
1 2
2 3
3 1
1 3
```

```
0
```

## Solution

Use two states per city: the city and the currently selected gear.
For a road traversal requiring gear d, move from (city,g) to (neighbor,d),
with cost 0 if g=d and cost 1 otherwise. Both states of the start have
distance 0, expressing the free initial choice. Either target state is valid.

Run 0–1 BFS. An improved state reached by a zero-cost edge goes to the
front of a deque; a unit-cost edge goes to the back. Mark a state settled
when first popped, and skip later copies. Return when a target state
is settled. The deque processes unsettled distances as Dijkstra would:
zero-cost improvements stay at the current distance, unit ones follow.
Thus each state's first settled distance is optimal.

Every actual route induces an expanded-state path with exactly its switch
count. Conversely, each expanded transition is a valid road traversal,
optionally preceded by one gear change. The two start states include
both possible free first gears. Therefore the minimum expanded distance
is exactly the required answer; the first settled target attains it.

O(n+m) time and space. There are 2n states and 4m possible expanded arcs;
each state scans its city's adjacency once when settled. Duplicate queue
entries are skipped, and every successful relaxation is charged to an arc.

Counting roads instead of changes can select a worse route. A city must
have two states: equally cheap arrivals in different gears are not
interchangeable. Do not charge the initial gear or require an uphill start.
Treat each road's direction independently; the second sample contains a
directed cycle. Do not infer an altitude order from city numbers.
Only start and target need be connected, not the whole graph.

## Optimized solutions

The optimized C++ solution parses the up to 200 004 numbers by hand from
a 4 KB buffer refilled with `fread` and prints with `printf` instead of
using `iostream`; the graph and the 0–1 BFS are the same:
{1930_shortest_paths_optimized.cpp}.

The optimized Go solution parses the numbers by hand from a 4 KB buffer
read from the standard input instead of calling `fmt.Fscan` for each of
up to 200 004 numbers; the graph and the 0–1 BFS are the same:
{1930_shortest_paths_optimized.go}.

The optimized Java solution parses the numbers by hand from a
`BufferedInputStream` instead of `StreamTokenizer` and keeps the deque
as a ring buffer in an `int` array instead of an `ArrayDeque` of boxed
`Integer`s. With `A = 2m` adjacency entries at most `2 + 2A` states are
ever inserted, so a capacity of `2A + 3` never fills up and leaves one
cell spare: {1930_shortest_paths_optimized.java}.

The optimized Python solution reads the input in 4 KB chunks instead of
splitting all of it at once and keeps each adjacency list in an
`array("H")` of unsigned 16-bit numbers instead of a list of integer
objects: a destination 2·city+gear is at most 19 999, since n ≤ 10000:
{1930_shortest_paths_optimized.py}.

The optimized Rust solution keeps the adjacency lists as `Vec<u16>`
instead of `Vec<usize>`, 2 bytes instead of 8 per entry: a destination
2·city+gear is at most 19 999, since n ≤ 10000. The numbers are parsed
by hand from a 4 KB buffer instead of reading the whole input into a
`String`: {1930_shortest_paths_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1930_shortest_paths_optimized.cpp`: time reduction +67.39%; memory
  reduction +12.81%; base: `1930_shortest_paths.cpp`.

- `1930_shortest_paths_optimized.go`: time reduction +66.67%; memory
  reduction +20.11%; base: `1930_shortest_paths.go`.

- `1930_shortest_paths_optimized.java`: time reduction +37.60%; memory
  reduction -36.59%; base: `1930_shortest_paths.java`.

- `1930_shortest_paths_optimized.py`: time reduction +0.00%; memory
  reduction +87.93%; base: `1930_shortest_paths.py`.

- `1930_shortest_paths_optimized.rs`: time reduction +0.00%; memory
  reduction +69.02%; base: `1930_shortest_paths.rs`.

## Language notes

Adjacency stores packed destinations 2·neighbor+requiredGear, two
entries per road. Distances fit signed 32-bit integers; 2n is a safe
infinity since a simple path in the expanded graph has fewer than 2n
arcs, each costing ≤1. Java reads with `StreamTokenizer`, keeps an `int`
array of destinations per city and uses `ArrayDeque`. Go uses two stacks
as a deque: reverse the deferred back stack only when the front is
empty. Each deferred entry transfers once, so the total transfer time is
linear. C++ and Rust use standard deques; Python uses deque and a
bytearray for settled flags. All input buffers and adjacency remain
O(n+m).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths.cpp](1930_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 1936 KB | 11291679 |
| [1930_shortest_paths.go](1930_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 6744 KB | 11291681 |
| [1930_shortest_paths.java](1930_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 2536 KB | 11307200 |
| [1930_shortest_paths.py](1930_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 19520 KB | 11291686 |
| [1930_shortest_paths.rs](1930_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 4468 KB | 11291694 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1930_shortest_paths_optimized.cpp](1930_shortest_paths_optimized.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1688 KB | 11307202 |
| [1930_shortest_paths_optimized.go](1930_shortest_paths_optimized.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.031 s | 5388 KB | 11307203 |
| [1930_shortest_paths_optimized.java](1930_shortest_paths_optimized.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.078 s | 3464 KB | 11307206 |
| [1930_shortest_paths_optimized.py](1930_shortest_paths_optimized.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 2356 KB | 11307205 |
| [1930_shortest_paths_optimized.rs](1930_shortest_paths_optimized.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.015 s | 1384 KB | 11307204 |
