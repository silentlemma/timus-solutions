# 2166. Farthest crossing of lines from the origin in the L1 distance

[Timus 2166](https://acm.timus.ru/problem.aspx?space=1&num=2166) · difficulty 1868 · geometry, sorting

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
The best fraction is kept exactly with integer cross multiplication. For
output, split off the integer quotient and round only the remainder to
twelve decimal places, carrying into the integer part if necessary. This
avoids overflow from scaling the whole numerator. The denominator is at
most 8 · 10⁶, so any positive answer is at least 1/(8 · 10⁶); rounding
introduces relative error at most 4 · 10⁻⁶. Zero is printed exactly.
The work is O(N log N), with O(N) memory.

Pitfall (test [22](tests/22.in)): six decimal places can exceed the relative
error limit near zero: 18/3617 rounds to 0.004976, with relative error
greater than 10⁻⁴. The checker uses the exact fraction computed from the
input, since stored outputs may themselves be rounded.

In the example the lines y = x and x = 1 meet at (1, 1), the line
through (1, 3) and (2, 1) meets y = x at (5/3, 5/3) and x = 1 at (1, 3),
the farthest with cost 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2166_geometry_sorting.cpp](2166_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(N log N) | AC | 0.078 s | 2304 KB |
| [2166_geometry_sorting.go](2166_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(N log N) | AC | 0.062 s | 8264 KB |
| [2166_geometry_sorting.java](2166_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(N log N) | AC | 0.203 s | 9096 KB |
| [2166_geometry_sorting.py](2166_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(N log N) | AC | 1.078 s | 44556 KB |
| [2166_geometry_sorting.rs](2166_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N log N) | AC | 0.062 s | 5520 KB |
