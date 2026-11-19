# 1246. Which way a polygon is run around

[Timus 1246](https://acm.timus.ru/problem.aspx?space=1&num=1246) · difficulty 333 · geometry

Original problem by Evgeny Kobzev, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dog is tied to a post inside a fenced plot, a simple polygon of N
vertices (3 ≤ N ≤ 200 000, integer coordinates up to 50 000 in absolute
value). A runner goes round and round along the fence, visiting the
vertices in the given order, and the dog chases the runner inside. Which
way does the rope wind around the post: clockwise (`cw`) or
counterclockwise (`ccw`)?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N vertices in the runner's order.

## Output

`cw` or `ccw`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
0 0
0 1
1 1
1 0
```

Output:

```
cw
```

## Solution

The dog follows the runner around the inside of the plot, so the rope
winds the way the runner goes around the polygon. That is the sign of
twice the polygon's signed area by the shoelace formula,
`Σ (x_i·y_{i+1} − x_{i+1}·y_i)`: positive for counterclockwise, negative
for clockwise. The polygon is simple and not flat, so the sum is never
zero. `O(N)`.

Pitfalls:

- the polygon need not be convex, so the turn at one vertex says nothing;
  only the total area decides (tests 04 and 05);
- each term reaches 5·10⁹, beyond 32 bits, so use 64-bit or
  arbitrary-precision integers.

## Optimized solutions

C++ and Rust accumulate the signed doubled area while reading the vertices. They keep the first and previous points, add each edge's cross product once, and then close the polygon. Products and the sum use signed 64-bit integers. The input buffer and geometric state take constant space.

The accepted base implementations [1246_geometry.go](1246_geometry.go), [1246_geometry.java](1246_geometry.java), [1246_geometry.py](1246_geometry.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1246_geometry_optimized.py`. Keep the shoelace orientation test, but accumulate each edge as the next vertex arrives and finally close the last-to-first edge. Retain only the first and previous vertex and the exact signed double area; positive means ccw, otherwise cw as in the base. The 65536-byte tokenizer carries a split numeric token between blocks, replacing the complete input integer list, coordinate slices and rotated copies. With B input bytes and N vertices, time O(B+N); storage is bounded parser blocks plus constant arithmetic state under the coordinate and vertex limits. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1246_geometry.py`: time 0.218 s → 0.187 s; memory 41236 KB → 10 140 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1246_geometry_optimized.py`: time place 2/22, memory place 7/22 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1246_geometry.cpp](1246_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.265 s | 128 KB | 11283934 |
| [1246_geometry.go](1246_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.062 s | 4120 KB | 11283936 |
| [1246_geometry.java](1246_geometry.java) \* | Java 1.8 | geometry | O(N) | AC | 0.156 s | 3584 KB | 11283939 |
| [1246_geometry.py](1246_geometry.py) \* | Python 3.12 x64 | geometry | O(N) | AC | 0.218 s | 41236 KB | 11283937 |
| [1246_geometry.rs](1246_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.062 s | 10468 KB | 11283943 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1246_geometry_optimized.cpp](1246_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 76 KB | 11310921 |
| [1246_geometry_optimized.rs](1246_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 196 KB | 11310553 |
| [1246_geometry_optimized.py](1246_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(B+N) | AC | 0.187 s | 10140 KB | 11325066 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
