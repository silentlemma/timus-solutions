# 1470. UFOs

[Timus 1470](https://acm.timus.ru/problem.aspx?space=1&num=1470) · difficulty 253 · fenwick

Original problem by Dmitry Zhukov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cube of N × N × N unit sectors (1 ≤ N ≤ 128, coordinates from 0 to
N − 1) starts empty. Records arrive one per line. "1 x y z K" changes
the number of objects in sector (x, y, z) by K (−20000 ≤ K ≤ 20000);
no sector ever goes below zero. "2 x1 y1 z1 x2 y2 z2" asks how many
objects lie in the box x1 ≤ x ≤ x2, y1 ≤ y ≤ y2, z1 ≤ z ≤ z2. "3"
ends the input. There are at most 100002 records.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then the records, the last of them "3".

## Output

The answer to each question on its own line.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
2
2 1 1 1 1 1 1
1 0 0 0 1
1 0 1 0 3
2 0 0 0 0 0 0
2 0 0 0 0 1 0
1 0 1 0 -2
2 0 0 0 1 1 1
3
```

Output:

```
0
1
4
2
```

## Solution

A Fenwick tree works in any number of dimensions: cell (i, j, w) holds
the sum over the block of sectors whose indices end at i, j and w and
are as long as their lowest set bits. A change walks i upwards and,
inside it, j and w upwards; a prefix sum over [1, x] × [1, y] × [1, z]
walks all three downwards. Each walk has at most 8 steps per axis, so an
update or prefix sum costs at most 8³ cell visits. The sum over a box comes from
inclusion and exclusion over its eight corners, the corners on the
lower side shifted by one. The tree takes (N + 1)³ 64-bit cells, about
17 MB. `O(log³ N)` per record.

Pitfalls:

- the coordinates start at 0, while a Fenwick tree starts at 1, so
  every index moves up by one (tests 03, 04);
- the counts in all sectors together reach 2·10⁹, and the partial sums
  of the eight-corner formula go past the 32-bit range, so sums are
  64-bit (gen4);
- questions may come before any change and a change may be 0 (tests
  01, 02).

## Optimized solutions

Keep the three-dimensional Fenwick tree but store node sums in 32-bit cells. Nonnegative sector values imply each node is at most the total legal mass, which is below the signed 32-bit maximum. Prefix totals and intermediate inclusion–exclusion expressions still use sufficiently wide arithmetic. This reduces tree storage without changing update ranges or query signs. Python additionally reads one operation at a time instead of retaining all input tokens and answers.

- `1470_fenwick_optimized.cpp`: 0.359 s / 8144 KB; base `1470_fenwick.cpp`: 0.375 s / 16552 KB; relative change: time -4.3%, memory -50.8%.
- `1470_fenwick_optimized.go`: 0.140 s / 10320 KB; base `1470_fenwick.go`: 0.156 s / 20044 KB; relative change: time -10.3%, memory -48.5%.
- `1470_fenwick_optimized.java`: 0.187 s / 12064 KB; base `1470_fenwick.java`: 0.281 s / 20908 KB; relative change: time -33.5%, memory -42.3%.
- `1470_fenwick_optimized.py`: 0.734 s / 16836 KB; base `1470_fenwick.py`: 0.890 s / 61120 KB; relative change: time -17.5%, memory -72.5%.
- `1470_fenwick_optimized.rs`: 0.046 s / 11476 KB; base `1470_fenwick.rs`: 0.125 s / 19804 KB; relative change: time -63.2%, memory -42.1%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1470_fenwick.cpp`; covering source `1470_fenwick_optimized.cpp`; time/memory places 60/1, other-author entries 89/89.

- Go: preferred teaching base `1470_fenwick.go`; covering source `1470_fenwick.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1470_fenwick.java`; covering source `1470_fenwick_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1470_fenwick.py`; covering source `1470_fenwick_optimized.py`; time/memory places 1/1, other-author entries 2/2.

- Rust: preferred teaching base `1470_fenwick.rs`; covering source `1470_fenwick_optimized.rs`; time/memory places 1/1, other-author entries 2/2.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1470_fenwick.cpp](1470_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(log^3 N) per record | AC | 0.375 s | 16552 KB | 11286549 |
| [1470_fenwick.go](1470_fenwick.go) | Go 1.14 x64 | fenwick | O(log^3 N) per record | AC | 0.156 s | 20044 KB | 11286550 |
| [1470_fenwick.java](1470_fenwick.java) | Java 1.8 | fenwick | O(log^3 N) per record | AC | 0.281 s | 20908 KB | 11286552 |
| [1470_fenwick.py](1470_fenwick.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per record | AC | 0.890 s | 61120 KB | 11286551 |
| [1470_fenwick.rs](1470_fenwick.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per record | AC | 0.125 s | 19804 KB | 11286553 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1470_fenwick_optimized.cpp](1470_fenwick_optimized.cpp) \* | G++ 13.2 x64 | fenwick | O(log^3 N) per operation | AC | 0.359 s | 8144 KB | 11308809 |
| [1470_fenwick_optimized.go](1470_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(log^3 N) per operation | AC | 0.140 s | 10320 KB | 11308810 |
| [1470_fenwick_optimized.java](1470_fenwick_optimized.java) | Java 1.8 | fenwick | O(log^3 N) per operation | AC | 0.187 s | 12064 KB | 11308811 |
| [1470_fenwick_optimized.py](1470_fenwick_optimized.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per operation | AC | 0.734 s | 16836 KB | 11308813 |
| [1470_fenwick_optimized.rs](1470_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per operation | AC | 0.046 s | 11476 KB | 11308812 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
