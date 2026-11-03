# 1656. Far Away Kingdom's Army

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · difficulty 206 · constructive

Original problem by Vladimir Yakovlev (idea by Magaz Asanov), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Arrange n² soldiers of given heights in an n × n square so that in every
row and every column the tallest stands in the middle and heights never
grow from the middle towards either end.

## Input

An odd n from 3 to 9, then n² heights from 170 to 200.

## Output

The square, n rows of n heights. Any valid arrangement is accepted.

## Checking

Check the output dimensions, the original multiset of heights and every required outward monotonicity inequality; any valid grid is accepted.

## Examples

### Example 1

Input:

```
3
170
170
180
175
170
175
175
170
175
```

Output:

```
170 175 170
175 180 175
170 175 170
```

## Solution

Rank the cells by the pair (nearer, farther) of their distances from the
centre row and the centre column, and give the tallest soldiers to the
lowest ranks. Along a row at distance a from the centre, a cell at
distance b has rank (b, a) while b < a and (a, b) from then on: either
way the rank grows as b grows, so on each side of the middle the heights
never increase outwards. Columns are the same by symmetry. Cells with
equal rank are mirror images, never on the same side of one line.
`O(n² log n)`; Go’s stable sort: `O(n² log² n)`.

Pitfalls:

- "never grow towards the ends" allows equal heights (test 02);
- many arrangements are valid, so a checker verifies the rules and the
  set of heights.

The program's squares pass the checker on 90 random armies.

## Optimized solutions

Count bounded height values instead of sorting every coordinate tuple. Cells of a smaller Manhattan distance from the center receive no smaller heights: every outward row or column step increases the distance, proving the constraints. Each cell is assigned once and equal heights are allowed. Python expands the height counts into a byte array and uses prefix offsets of distance levels to emit rows without a full grid. The simple coordinate-order construction is retained.

- `1656_constructive_optimized.cpp`: 0.001 s / 108 KB; base `1656_constructive.cpp`: 0.001 s / 180 KB; relative change: time -0.0%, memory -40.0%.
- `1656_constructive_optimized.java`: 0.078 s / 472 KB; base `1656_constructive.java`: 0.156 s / 4188 KB; relative change: time -50.0%, memory -88.7%.
- `1656_constructive_optimized.py`: 0.109 s / 268 KB; base `1656_constructive.py`: 0.046 s / 436 KB; relative change: time +137.0%, memory -38.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1656_constructive.cpp`; covering source `1656_constructive.cpp`; time/memory places 1/1, other-author entries 48/48.

- Go: preferred teaching base `1656_constructive.go`; covering source `1656_constructive.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1656_constructive.java`; covering source `1656_constructive_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1656_constructive.py`; covering source `1656_constructive_optimized.py`; time/memory places 9/2, other-author entries 13/13.

- Rust: preferred teaching base `1656_constructive.rs`; covering source `1656_constructive.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.001 s | 180 KB | 11308831 |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log² n) | AC | 0.031 s | 1152 KB | 11288581 |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB | 11288583 |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.046 s | 436 KB | 11308832 |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.031 s | 220 KB | 11308833 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1656_constructive_optimized.cpp](1656_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2+H) | AC | 0.001 s | 108 KB | 11308068 |
| [1656_constructive_optimized.java](1656_constructive_optimized.java) | Java 1.8 | constructive | O(N^2+H) | AC | 0.078 s | 472 KB | 11308073 |
| [1656_constructive_optimized.py](1656_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(N^2+H) time, O(N^2+H+N) compact bytes/counts; H31 | AC | 0.109 s | 268 KB | 11309461 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
