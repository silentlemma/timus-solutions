# 1643. Attack of the Dark Fortress

[Timus 1643](https://acm.timus.ru/problem.aspx?space=1&num=1643) · difficulty 425 · bfs

Original problem by Denis Dublennykh, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two armies stand on an n × m map of passable and impassable districts.
In a day an army moves to any of the 8 neighbouring passable districts;
a district with a teleport letter can send it instantly to any district
with the same letter. Once both armies are in one district they join
and move together. Before that, neither may enter the fortress. Find the
fewest days until the joined army reaches the fortress.

## Input

n and m (1 ≤ n, m ≤ 100), then the map: `#` impassable, `.` passable,
`A`–`Z` teleports, `$` and `!` the armies, `*` the fortress, each of the
last three exactly once.

## Output

The fewest days, or `Impossible`.

## Examples

### Example 1

Input:

```
5 8
....AA.#
.######!
.....*##
.#######
..B$...B
```

Output:

```
11
```

### Example 2

Input:

```
3 5
##*..
!#...
##..$
```

Output:

```
Impossible
```

## Solution

An army that arrives early can wait, so meeting in district c takes
max(d₁(c), d₂(c)) days, where d₁ and d₂ are the distances of the two
armies with the fortress closed. The joined army then needs d(c) more
days to reach the fortress, and since every move can be reversed (a
step goes both ways, a teleport links its letter in both directions),
d is the distance from the fortress itself. The answer is the minimum of
max(d₁, d₂) + d over all districts except the fortress.

Each distance is one breadth-first search in which teleports cost 0:
a 0-1 BFS, where free moves go first via a stack in Go or the deque's
front elsewhere. When the first district of a letter is processed, it
already has the least distance among that letter's districts, so every letter is spread once.
`O(n · m)` per search, three searches in all.

Pitfalls:

- an army may not pass through the fortress before the meeting (test 06),
  but the joined army may start right next to it;
- a letter's group should be spread only once, or a map full of the same
  letter costs quadratic time;
- the joined army may use teleports too (test 07).

The answers match an independent accepted implementation on 180 random
maps.

## Optimized solutions

The new C++ and Go versions store the grid and three distance arrays flat, with 16-bit cell identifiers and distances. At most 10000 cells give shortest distances below 10000; 65535 is the unreachable sentinel. On first discovering a teleport letter at day d, assign d and enqueue every cell of that letter immediately. This implicitly contracts its zero-cost component before ordinary BFS proceeds, so all remaining edges cost one day. Each cell is discovered once, bounding the queue by n·m entries. A linked array stores each letter’s membership without per-cell heap objects. Two searches forbid the fortress; the third starts there with it open. Minimise max(d₁,d₂)+d₃ over reachable non-fortress meeting cells: the earlier army waits, and reversibility makes the third distance the onward route. Time and storage are O(n·m). All ordinary sources remain; Java, Python and Rust reuse their admitted bases in the fast set.

The accepted base implementations [1643_bfs.java](1643_bfs.java), [1643_bfs.py](1643_bfs.py), [1643_bfs.rs](1643_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1643_bfs.cpp](1643_bfs.cpp) | G++ 13.2 x64 | bfs | O(n · m) | AC | 0.031 s | 1064 KB | 11328281 |
| [1643_bfs.go](1643_bfs.go) | Go 1.14 x64 | bfs | O(n · m) | AC | 0.031 s | 4792 KB | 11288482 |
| [1643_bfs.java](1643_bfs.java) | Java 1.8 | bfs | O(n · m) | AC | 0.14 s | 2216 KB | 11328282 |
| [1643_bfs.py](1643_bfs.py) | Python 3.12 x64 | bfs | O(n · m) | AC | 0.125 s | 2176 KB | 11288483 |
| [1643_bfs.rs](1643_bfs.rs) | Rust 1.75 x64 | bfs | O(n · m) | AC | 0.031 s | 1092 KB | 11328285 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1643_bfs_optimized.cpp](1643_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(n·m) | AC | 0.015 s | 220 KB | 11314974 |
| [1643_bfs_optimized.go](1643_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(n·m) | AC | 0.015 s | 388 KB | 11314986 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
