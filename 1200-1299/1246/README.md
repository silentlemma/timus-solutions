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

## Language notes

These notes describe the simple implementations.

- Python multiplies the coordinate lists with a rotated copy using `map`;
  the other languages run one loop.

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

\* Accepted; the rating target is not yet met. This version may be optimized further.
