# 1181. Cutting a three-colored polygon into rainbow triangles

[Timus 1181](https://acm.timus.ru/problem.aspx?space=1&num=1181) · difficulty 456 · constructive

Original problem by Dmitry Filimonenkov, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The vertices of a convex polygon with `4 ≤ N ≤ 1000` vertices are colored
R, G and B; all three colors occur and no two neighbours share a color.
Cut the polygon by non-crossing diagonals into triangles that each have
one vertex of every color, or print 0 if that is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the colors in order around the polygon.

## Output

The number of diagonals, then the diagonals as pairs of vertex numbers.

## Checking

Any cut is accepted if its `N − 3` distinct diagonals do not cross and
every triangle they make has all three colors. Such a cut always exists,
so `0` is never right.

## Examples

### Example 1

Input:

```
7
RBGBRGB
```

Output:

```
4
1 3
3 7
5 7
5 3
```

## Solution

If some color occurs only once, draw every diagonal from that vertex.
Each triangle of the fan has this vertex and two neighbouring vertices of
the rest, which differ from each other and from it.

Otherwise every color occurs at least twice. There is a vertex whose two
neighbours have different colors: if every vertex had equal neighbours,
the colors would repeat with period two around the polygon, and only two
colors would occur. Cut off that vertex with the diagonal between its
neighbours; the triangle has three colors, the rest still has all three
colors (the removed one occurs elsewhere) and no equal neighbours. Repeat
until a color is alone or a triangle remains. So the answer always
exists, with `N − 3` diagonals. `O(N²)` with plain list removal.

Pitfalls:

- the answer is never 0, which is easy to miss in a problem that asks
  for it;
- after a cut, the color counts change, so a color can become single
  later, which is when the fan finishes the job;
- an odd polygon cannot alternate two colors, which is another way to see
  that the search for a vertex with different neighbours never fails.

Every printed cut passed the checker on 200 random polygons of up to 33
vertices and on all tests, including thousand-vertex polygons.

## Optimized solutions

The linear version keeps the same rainbow-ear proof and the final fan from a uniquely coloured vertex. Arrays left and right form a cyclic doubly linked list, so removing an ear takes O(1). Colour counts are updated after each cut. Initially enqueue every vertex whose neighbours have different colours; after a removal, only its two surviving neighbours can change eligibility. Ignore stale or removed queue entries. While each colour occurs at least twice, a suitable ear exists, since otherwise the remaining polygon would alternate only two colours. When one colour becomes unique, finish with a fan from its vertex. There are at most N initial entries and two additions per cut, so the total time and space are O(N). Original vertex numbers are preserved.

The accepted Python 3.12 x64 run takes 0.093 s versus 0.203 s for the base and uses 900 KB versus 760 KB.

## Language notes

The original list-based implementations remain the simple O(N²) versions. All new implementations use the linear queue and linked neighbours. C++, Go and Rust bound their arrays using N ≤ 1000; the queue needs at most 3N entries. Go and Rust buffer output in 12000 bytes, enough for N−3 pairs of four-digit indices. Go uses standard handles and Rust bounded C-runtime I/O with a C entry point. Python uses deque; Java uses a primitive array queue. Any valid rainbow triangulation is accepted.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1181_constructive.cpp](1181_constructive.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 408 KB | 11283313 |
| [1181_constructive.go](1181_constructive.go) | Go 1.14 x64 | constructive | O(N²) | AC | 0.031 s | 1188 KB | 11283315 |
| [1181_constructive.java](1181_constructive.java) | Java 1.8 | constructive | O(N²) | AC | 0.218 s | 6632 KB | 11283326 |
| [1181_constructive.py](1181_constructive.py) | Python 3.12 x64 | constructive | O(N²) | AC | 0.203 s | 760 KB | 11283321 |
| [1181_constructive.rs](1181_constructive.rs) | Rust 1.75 x64 | constructive | O(N²) | AC | 0.031 s | 476 KB | 11283329 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1181_constructive_optimized.cpp](1181_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 132 KB | 11314704 |
| [1181_constructive_optimized.go](1181_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 388 KB | 11314727 |
| [1181_constructive_optimized.java](1181_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.109 s | 552 KB | 11314749 |
| [1181_constructive_optimized.py](1181_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.093 s | 900 KB | 11314762 |
| [1181_constructive_optimized.rs](1181_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 92 KB | 11314780 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
