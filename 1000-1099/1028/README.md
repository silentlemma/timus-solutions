# 1028. Counting points below and to the left of each point

[Timus 1028](https://acm.timus.ru/problem.aspx?space=1&num=1028) · difficulty 265 · fenwick, segment_tree

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` distinct points, `1 ≤ N ≤ 15000`, have integer coordinates `0 ≤ x, y ≤ 32000`. They arrive in increasing `y`, then increasing `x` for equal `y`. A point's level is the number of other points with `x' ≤ x` and `y' ≤ y`. Count the points at every level from 0 to `N − 1`. Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N`, followed by `N` lines `x y` in the stated order; no two points coincide.

## Output

`N` lines, giving the counts of levels 0, 1, …, `N − 1`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
2 0
6 0
0 2
4 2
4 4
1 6
```

Output:

```
2
2
1
1
0
0
```

### Example 2

Input:

```
1
32000 32000
```

Output:

```
1
```

## Solution

At the current point, every earlier point already has `y′ ≤ y`.
A later point either has larger `y`, or equal `y` and larger `x`, so it
cannot contribute. The level is therefore the number of previous points
with `x′ ≤ x`.

Use a Fenwick tree of frequencies over `x = 0..32000`. Shift `x` by one:
query the prefix ending at `x + 1`, increment that level's histogram cell,
then insert this point. A Fenwick cell stores a suffix of its index
prefix; repeatedly clearing the lowest set bit partitions the queried
prefix into disjoint intervals. An insertion visits precisely the cells
whose intervals contain its index. Thus each query counts exactly the
required previous points. Querying before inserting excludes the point
itself. Equal-`y` points are processed immediately, not as a batch, since
the earlier points on the same row must count.

Time is `O(N log C)`, `C = 32001`, and the tree plus histogram use
`O(C + N)` cells. The original C++ segment tree is also retained: it
queries `[0, x + 1)` and inserts `x` with the same ordering argument.
Its asymptotic bound is the same, with a larger tree. All six original
Accepted sources are preserved without byte changes.

## Optimized solutions

Every tree or histogram counter is at most `N ≤ 15000`, so an unsigned
16-bit cell is sufficient; query totals use wider arithmetic. The compact
Fenwick versions use 16-bit counters instead of full native integers or
Python object lists. At maximum size their two counter arrays occupy
`2 × (32002 + 15000) = 94004` bytes, excluding input, output and runtime.

C++ uses a small buffered reader and standard buffered output. Python
streams input tokens and discards that generator after processing, but
still builds its final output string. Rust retains the input text but
parses lazily without a vector of all numeric tokens, and writes through
a buffered writer. Time remains `O(N log C)` and counter storage remains
`O(C + N)`; this is an implementation and memory optimization.

Measured memory changes relative to the original Fenwick on the same
language: C++ 348 → 224 KB (35.6%), Python 3644 → 1576 KB (56.8%), Rust
1076 → 580 KB (46.1%). All three have their own Accepted and qualify by
memory. Python is slower, 0.156 s versus 0.109 s; Rust stays at 0.031 s.
C++ records 0.015 s versus 0.031 s, but that single timer tick is not used
to establish a speedup. C++ is compared with the original Fenwick,
not the more memory-hungry segment tree.

## Language notes

Python was checked on 811 small point sets against direct two-dimensional
dominance counts, including every nonempty subset of a 3 × 3 coordinate
grid and random boundary coordinates. Two further 15000-point extremes
use closed-form expected histograms, covering a count of 15000 and maximal Fenwick counts. Each of the
three actual candidates also passed 14 repository inputs in Docker.

The rating snapshot is from 2 November 2026. C++ is at time place 1 and
memory place 2 among 235 filtered other-author entries and meets the
target. Rust is first in both against two entries. Python is at places
5 and 3 against 19 entries, so its optimized row keeps a star. Existing
Java is first in both against five entries. Go's filtered comparison
sample is empty; its formal coverage does not prove competitive superiority.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1028_fenwick.cpp](1028_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 348 KB | 11278320 |
| [1028_fenwick.go](1028_fenwick.go) | Go 1.14 x64 | fenwick | O(N log C), C = 32001 | AC | 0.046 s | 1512 KB | 11278322 |
| [1028_fenwick.java](1028_fenwick.java) | Java 1.8 | fenwick | O(N log C), C = 32001 | AC | 0.093 s | 888 KB | 11278326 |
| [1028_fenwick.py](1028_fenwick.py) | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.109 s | 3644 KB | 11278325 |
| [1028_fenwick.rs](1028_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 1076 KB | 11278327 |
| [1028_segment_tree.cpp](1028_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(N log C), C = 32001 | AC | 0.031 s | 472 KB | 11278321 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1028_fenwick_optimized.cpp](1028_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.015 s | 224 KB | 11308209 |
| [1028_fenwick_optimized.py](1028_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.156 s | 1576 KB | 11308208 |
| [1028_fenwick_optimized.rs](1028_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 580 KB | 11308211 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
