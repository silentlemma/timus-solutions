# 1250. Islands inside the sacred sea

[Timus 1250](https://acm.timus.ru/problem.aspx?space=1&num=1250) · difficulty 724 · graphs

Original problem by Stanislav Skorb (prepared by Ivan Dashkevich), from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A W × H map (W, H ≤ 500) shows sea `.` and land `#`. Sea cells form one
sea when they touch by a side or a corner; land cells form one island
when they touch by a side only. The sea containing the cell (X, Y),
counted from the top-left corner, is sacred, and all land inside it is
sacred too, including islands in seas inside its islands, and so on.
Count the sacred islands that do not touch the border of the map.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W, H, X and Y separated by one or more spaces, then H lines of W
characters.

## Output

The number of such islands.

## Examples

### Example 1

Input:

```
9 7 1 1
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Output:

```
3
```

### Example 2

Input:

```
9 7 3 3
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Output:

```
2
```

## Solution

Pad the map with a ring of outside cells. A sea joined through corners
cannot be crossed by a path that moves only through sides: wherever it
looks thin, two of its cells meet at a corner and close the gap. So the
land inside the sacred sea is exactly the land that a side-to-side flood
from the outside ring cannot reach while avoiding the sacred sea.

The program finds the sacred sea by a flood through all eight directions
from (X, Y), floods from the outside ring through every cell that is not
in it, and counts the islands among the cells left unreached, with one
more side-to-side flood per island. An island touching the border is
always reached from the ring, so it never counts. Every flood uses an
explicit stack to avoid deep recursion on large maps.
`O(W·H)`.

Pitfalls:

- islands nested inside lakes of sacred islands count too: in the first
  example the ring and both islands inside it (test 06 has a lake);
- land touching only at a corner forms separate islands (test 08);
- the first line may hold several spaces between numbers, so the map is
  read as the next W·H characters `.` and `#`, whatever lies between
  them.

The counts were compared with a second solution that builds the tree of
seas and islands, on 1500 random small maps.

## Language notes

- Python floods with byte arrays standing for "still free" cells, which
  the flood clears as it goes.

## Optimized solutions

The floods share one byte of state per cell. An outer guard ring blocks moves past the grid, so the floods can use fixed index offsets without checking row and column bounds at each step.

Go 1.14 x64, submission 11318425. Time 0.046 → 0.031 s, memory 6644 → 4280 KB.

Rust 1.75 x64, submission 11318428. Time 0.046 → 0.015 s, memory 4948 → 1684 KB.

Python 3.12 x64, submission 11318431. Time 0.468 → 0.328 s, memory 14592 → 6444 KB.

Java 1.8, submission 11318433. Time 0.093 → 0.125 s, memory 3184 → 1620 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321900 · Go 1.14 x64 №11322182 · Java 1.8 №11322183 · Python 3.12 x64 №11322184 · Rust 1.75 x64 №11322185.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1250_graphs.cpp](1250_graphs.cpp) | G++ 13.2 x64 | graphs | O(W·H) | AC | 0.015 s | 2408 KB | 11321900 |
| [1250_graphs.go](1250_graphs.go) | Go 1.14 x64 | graphs | O(W·H) | AC | 0.046 s | 6644 KB | 11322182 |
| [1250_graphs.java](1250_graphs.java) | Java 1.8 | graphs | O(W·H) | AC | 0.093 s | 3184 KB | 11322183 |
| [1250_graphs.py](1250_graphs.py) | Python 3.12 x64 | graphs | O(W·H) | AC | 0.468 s | 14592 KB | 11322184 |
| [1250_graphs.rs](1250_graphs.rs) | Rust 1.75 x64 | graphs | O(W·H) | AC | 0.046 s | 4948 KB | 11322185 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1250_graphs_optimized.go](1250_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(W·H) | AC | 0.031 s | 4280 KB | 11318425 |
| [1250_graphs_optimized.rs](1250_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(W·H) | AC | 0.015 s | 1684 KB | 11318428 |
| [1250_graphs_optimized.py](1250_graphs_optimized.py) | Python 3.12 x64 | graphs | O(W·H) | AC | 0.328 s | 6444 KB | 11318431 |
| [1250_graphs_optimized.java](1250_graphs_optimized.java) \* | Java 1.8 | graphs | O(W·H) | AC | 0.125 s | 1620 KB | 11318433 |

\* The marked versions have room to improve in the ratings.
