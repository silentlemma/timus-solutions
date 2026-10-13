# 1369. Cockroach Race

[Timus 1369](https://acm.timus.ru/problem.aspx?space=1&num=1369) · difficulty 10221 · geometry

Original problem by Den Raskovalov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

M cockroaches (1 ≤ M ≤ 100 000) and N sweets (0 ≤ N ≤ 10 000) stand on the
plane, with real coordinates between −10 000 and 10 000; any two
cockroaches, and any two sweets, are at least 0.001 apart. For every
sweet print the numbers of the cockroaches nearest to it, in increasing
order.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

M and the cockroaches, then N and the sweets, one point per line.

## Output

N lines, the nearest cockroaches of each sweet.

## Examples

### Example 1

Input:

```
4
0 0
1 0
0 1
1 2
2
0 0
0 2
```

Output:

```
1
3 4
```

## Solution

The implementations use a tolerance that the statement does not mention:
a cockroach counts when its squared distance is below the smallest one
plus 2⁻²⁴. Coordinates can have more than 20 digits after the point, so
doubles can lose distinctions near this cutoff. Exact comparisons use
integers scaled by 10³⁰, truncating after 30 decimal places.

C++, Go, Java and Rust join the cockroaches into a graph: the Delaunay
triangulation, built by divide and conquer on quad-edges, plus each cockroach's
neighbours in the order by x and in the order by y. The orientation and
in-circle tests are computed in doubles with a bound on their rounding
error, and recomputed exactly when the result falls inside that bound.
If all cockroaches lie on one line, the graph is the path along it.

For a sweet, a walk starts at the closest among the previous answer and
up to 1 024 cockroaches spread over the order by x, and moves to a closer
neighbour while there is one: first with doubles, then exactly. On a
Delaunay triangulation such a walk ends at the nearest cockroach. A
search through the graph from there collects every cockroach within the
tolerance, expanding only such vertices. W counts examined vertices and
adjacency entries, and K reported cockroaches per query (maxima over queries).

Pitfalls:

- the tolerance 2⁻²⁴ on squared distances: test 06 has squared-distance
  differences below it and above it;
- twelve cockroaches can be equally near (test 04);
- cockroaches on one line make the triangulation degenerate (test 05);
- N can be 0 (test 03).

The answers match an exact brute force on all the small tests and on
samples of the large ones. An independent accepted implementation
agrees everywhere except five lines of the generated ring and circle
tests, where the brute force sides with the solutions here.

## Language notes

- C++ and Rust keep the coordinates in 128-bit integers and the
  products in a 512-bit integer of sixteen 32-bit limbs. Go keeps the
  coordinates in 128 bits too and widens them only for exact steps, with
  32-bit edge arrays: a first version holding 512-bit coordinates used
  88 MB on the judge's test 9.
- Java compares distances in doubles first and exactly only when they
  are within the rounding error, and multiplies only the used limbs:
  without that it took over 2 s on the judge's test 9.
- Python runs under PyPy and does not build the triangulation: it finds
  the nearest cockroaches in a k-d tree of bounding boxes kept in flat
  arrays, turned along the main axis of an elongated cloud. When the
  cockroaches lie near one circle, they are ordered by angle instead,
  and a node is bounded by its angular interval and its least distance
  from the centre; narrow angular windows or the whole circle can also
  be scanned directly. Doubles decide everything except possible ties,
  which are compared exactly. Earlier versions with a triangulation
  took just over 2 s on the judge's test 15 or used 70 MB on test 9.
  V counts examined tree nodes and points per query (maximum over queries).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1369_geometry.cpp](1369_geometry.cpp) | G++ 13.2 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 0.812 s | 33540 KB |
| [1369_geometry.go](1369_geometry.go) | Go 1.14 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 1.328 s | 40448 KB |
| [1369_geometry.java](1369_geometry.java) | Java 1.8 | geometry | O(M log M + N · (W + K log K)) | AC | 1.781 s | 53152 KB |
| [1369_geometry.py](1369_geometry.py) | PyPy 3.10 x64 | geometry | O(M log² M + N · (log M + V + K log K)) | AC | 1.687 s | 46264 KB |
| [1369_geometry.rs](1369_geometry.rs) | Rust 1.75 x64 | geometry | O(M log M + N · (W + K log K)) | AC | 0.656 s | 39668 KB |
