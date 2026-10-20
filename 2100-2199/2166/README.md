# 2166. Farthest crossing of lines from the origin in the L1 distance

[Timus 2166](https://acm.timus.ru/problem.aspx?space=1&num=2166) · difficulty 2116 · geometry, sorting

Original problem by Vadim Barinov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N pairwise non-parallel lines are given by two integer points each, and
every crossing of two lines is a station. Reaching a station (x, y) from
the origin along the axes costs |x| + |y|. Print the largest such cost
over all stations within 10⁻⁴ relative error. The limits are 3 seconds
and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then the lines as x₁ y₁ x₂ y₂ with coordinates up to
1000 in absolute value.

## Output

The largest |x| + |y| over all crossings.

## Examples

### Example 1

Input:

```
3
0 0 1 1
1 0 1 1
1 3 2 1
```

Output:

```
4
```

## Solution

The cost |x| + |y| is the largest of the four linear functions ±x ± y,
so the answer is the largest value of a linear function over all
crossings of the arrangement, taken over four directions. A classical
fact about line arrangements says that the crossing extreme in any
direction is formed by two lines that are neighbours in the cyclic order
of slopes. So sort the lines by direction with an exact cross-product
comparison and check the N crossings of cyclic neighbours.

With a line written as dy · x − dx · y = c, the crossing of two lines is
a fraction with denominator |dx₁ dy₂ − dy₁ dx₂|, and its L1 norm is
(|dx₁ c₂ − c₁ dx₂| + |dy₁ c₂ − c₁ dy₂|) divided by that denominator.
The best fraction is kept exactly with integer cross multiplication and
printed by exact rounding. The work is O(N log N).

In the example the lines y = x and x = 1 meet at (1, 1), the line
through (1, 3) and (2, 1) meets y = x at (5/3, 5/3) and x = 1 at (1, 3),
the farthest with cost 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2166_geometry_sorting.cpp](2166_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 2312 KB |
| [2166_geometry_sorting.go](2166_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 8296 KB |
| [2166_geometry_sorting.java](2166_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(N log N) | AC | 0.218 s | 9168 KB |
| [2166_geometry_sorting.py](2166_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(N log N) | AC | 0.953 s | 44364 KB |
| [2166_geometry_sorting.rs](2166_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N log N) | AC | 0.046 s | 5304 KB |
