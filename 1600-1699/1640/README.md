# 1640. Circle of Winter

[Timus 1640](https://acm.timus.ru/problem.aspx?space=1&num=1640) · difficulty 178 · geometry

Original problem by Dmitry Ivankov (prepared by Alexander Ipatov), from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Demons stand at n lattice points. Sandro may teleport to any point that
holds no demon and cast a ring of ice of radius at most 10000 centred
there. The ring must kill at least one demon (one lying on the circle),
and every demon left alive must be inside it. Output a centre and a
radius.

## Input

n (1 ≤ n ≤ 100), then the coordinates of the demons, integers up to
1000 in absolute value, measured from Sandro's current position. All
demons are at distinct points, none at Sandro's.

## Output

The centre and the radius, accurate to 10⁻⁹. Any valid answer is
accepted.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The repository checker requires exactly three finite numbers x,y,r, with 0<=r<=10000+1e-6. The centre must be at least 1e-6 from every demon, every demon must be within r+1e-6, and at least one distance must differ from r by at most 1e-6. This is the repository tolerance; the statement separately requests 1e-9 accuracy.

## Examples

### Example 1

Input:

```
7
1 1
1 5
3 6
5 3
8 0
9 5
5 9
```

Output:

```
5 4 5
```

### Example 2

Input:

```
2
0 2
2 0
```

Output:

```
1 1 1.41421356237309
```

## Solution

No teleport is needed. Sandro's own position holds no demon, and the
circle around it through the farthest demon kills that demon and
encloses all the others. Its radius is at most 1000 · √2, well within
10000. `O(n)`.

Pitfalls:

- the centre must not be a demon's point, so the centre of the smallest
  enclosing circle is not always allowed; the start point always is;
- several valid answers exist, so a checker accepts any circle that
  meets the rules.

## Optimized solutions

The optimized Java solution prints the same circle, but reads the
numbers by hand from 4 KB blocks of bytes instead of with `Scanner`,
whose regular expressions take time and memory to set up:
{1640_geometry_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1640_geometry_optimized.java`: time reduction +33.57%; memory
  reduction +54.92%; base: `1640_geometry.java`.

`1640_geometry_optimized.rs`. Keep the circle centred at the origin, which is guaranteed demon-free. Read integer coordinates one pair at a time, track max(x*x+y*y) exactly in i64, and take one square root at the end instead of one hypot per point. Coordinates of absolute value at most 1000 keep these squares safely bounded. Emit the radius with ten fractional digits. Time O(n), auxiliary state O(1), without the vector of all floating-point input values. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1640_geometry.rs`: time 0.062 s → 0.031 s; memory 268 KB → 96 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1640_geometry_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry.cpp](1640_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 148 KB | 11288466 |
| [1640_geometry.go](1640_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.015 s | 1112 KB | 11288467 |
| [1640_geometry.java](1640_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 2032 KB | 11288469 |
| [1640_geometry.py](1640_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB | 11288468 |
| [1640_geometry.rs](1640_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 268 KB | 11304017 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry_optimized.java](1640_geometry_optimized.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 916 KB | 11307283 |
| [1640_geometry_optimized.rs](1640_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 96 KB | 11325103 |
