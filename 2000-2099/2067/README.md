# 2067. Pairs that no third point can join

[Timus 2067](https://acm.timus.ru/problem.aspx?space=1&num=2067) · difficulty 326 · geometry

Original problem by Alexey Danilyuk, prepared by Alexey Danilyuk and Alexander Borzunov, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n distinct points (sᵢ, rᵢ) are given. For two points v, u let p(v, u)
be the distance between them, and for three points let p(v, u, w) be
half the sum of the three pairwise distances. Two different points v, u
form a best pair when p(v, u) ≥ p(v, u, w) for every point w. Find all
best pairs. The limits are 2 seconds and 64 MB.

## Input

The number of points n, 2 ≤ n ≤ 2·10⁵, then n lines with the integers
sᵢ and rᵢ, −10⁸ ≤ sᵢ, rᵢ ≤ 10⁸. No two points coincide.

## Output

The number of best pairs, then the pairs, one per line, as the numbers
of their points in the input order. The pairs and the two numbers of a
pair may come in any order.

## Checking

A checker compares the number of pairs and the set of pairs, with the
two numbers of each pair in any order.

## Examples

### Example 1

Input:

```
2
2 3
7 6
```

Output:

```
1
1 2
```

### Example 2

Input:

```
3
5 5
2 -4
-4 2
```

Output:

```
0
```

## Solution

Multiply the condition by 2: p(v, u) ≥ p(v, u, w) means
p(v, u) ≥ p(v, w) + p(w, u). The triangle inequality says the opposite,
so equality must hold, and that happens exactly when w lies on the
segment vu (for w = v or w = u it holds trivially). So v and u are a
best pair exactly when every point lies on the segment between them.

If the points are not all on one line, there is no best pair. If they
are, the only candidates are the two extreme points of the line, and
they do work: every other point lies between them. Two points are always
collinear, so n = 2 gives the single pair 1 2.

Collinearity is checked exactly with the cross product
(p₂ − p₁) × (pᵢ − p₁) = 0, whose terms reach 4·10¹⁶ and fit 64-bit
integers. The extremes are the smallest and the largest point in the
order by s and then by r. Everything takes O(n), except Python's sort: O(n log n).

In the second example the three points form a triangle, so the answer
is 0.

## Optimized solutions

`2067_geometry_optimized.py`. Keep the geometric condition that a best pair exists only when all distinct points are collinear. Use the first two promised distinct points as anchors, stream the rest and test exact integer cross-products. Track lexicographic minimum/maximum point IDs during that scan instead of storing coordinate arrays and sorting all points. In a collinear set those extremes are the unique best pair. Stop on the first noncollinear witness. Time O(n), auxiliary space O(B) for 4096-byte chunks and bounded coordinate tokens; point and pair order flexibility is preserved.

Compared with `2067_geometry.py`: time 0.421 s → 0.203 s; memory 62 116 KB → 6 124 KB.

C++ and Go use the first two points to fix the line and process the remaining points as they are read. A nonzero cross product immediately rules out a best pair. Otherwise keep the indices with minimum and maximum x, or minimum and maximum y for a vertical line. This keeps O(n) time and uses O(1) extra space.

The accepted base implementations [2067_geometry.java](2067_geometry.java), [2067_geometry.py](2067_geometry.py), [2067_geometry.rs](2067_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2067_geometry_optimized.py`: time place 1/13, memory place 3/13 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2067_geometry.cpp](2067_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.296 s | 2864 KB | 11325661 |
| [2067_geometry.go](2067_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.281 s | 8768 KB | 11294402 |
| [2067_geometry.java](2067_geometry.java) \* | Java 1.8 | geometry | O(n) | AC | 0.125 s | 3720 KB | 11325646 |
| [2067_geometry.py](2067_geometry.py) \* | Python 3.12 x64 | geometry | O(n log n) | AC | 0.421 s | 62116 KB | 11325664 |
| [2067_geometry.rs](2067_geometry.rs) \* | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 10484 KB | 11325667 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2067_geometry_optimized.cpp](2067_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 96 KB | 11310454 |
| [2067_geometry_optimized.go](2067_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 900 KB | 11310455 |
| [2067_geometry_optimized.py](2067_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(n) time; O(B) space | AC | 0.203 s | 6124 KB | 11325495 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
