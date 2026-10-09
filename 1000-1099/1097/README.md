# 1097. Placing a square park so that it disturbs the least important owners

[Timus 1097](https://acm.timus.ru/problem.aspx?space=1&num=1097) · difficulty 1363 · bruteforce

Original problem by Stanislav Vasiliev, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A square country of side `L` has its lower left corner at `(1, 1)`
(`1 ≤ A ≤ L ≤ 10000`). `M ≤ 100` square plots with integer corners and
sides parallel to the axes are taken; they touch at most along their
borders, and each has an influence from 2 to 100, or 255 for plots of the
jury, which cannot be taken. Place a square park of side `A` with integer
corners inside the country so that the largest influence among the plots
it overlaps (with positive area) is as small as possible. Print 1 if the
park fits on free land, the smallest possible influence otherwise, or
`IMPOSSIBLE` if every place overlaps a jury plot.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`L` and `A`, then `M`, then `M` lines with the influence, the side and
the lower left corner of a plot.

## Output

1, the smallest influence, or `IMPOSSIBLE`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5 3
6
94 2 4 1
3 1 1 1
2 1 1 2
2 2 2 1
100 1 2 4
255 1 5 5
```

Output:

```
3
```

### Example 2

Input:

```
5 3
1
255 1 3 3
```

Output:

```
IMPOSSIBLE
```

## Solution

The park with lower left corner `(px, py)` covers `[px, px + A] × [py, py + A]`
and overlaps a plot `[x, x + s] × [y, y + s]` exactly when
`px < x + s`, `x < px + A`, and the same holds for `y`.

Fix `py` and slide the park from left to right. The set of plots it
overlaps changes only when its left side passes a plot's right side (that
plot is left behind, at `px = x + s`) or its right side passes a plot's
left side (that plot is entered). Entering only adds plots, so the best
positions are at `px = 1` or at some `x + s`. The same holds for `py`
with `x` fixed, so `(px, py)` can be taken from at most 101 values on each
axis, and every pair is checked against all plots. `O(M³)`, about a
million checks.

Pitfalls:

- plots that only touch the park along a side do not count, so all
  comparisons are strict;
- the park must stay inside the country: `px + A − 1 ≤ L`, that is
  `px ≤ L − A + 1`;
- 255 is not a large influence but a forbidden plot: a place that
  overlaps one is not allowed at all.

The answers were checked against trying every position of the park in
countries with `L ≤ 40`.

## Language notes

- Python first keeps, for each `px`, the plots in that vertical strip,
  which makes the inner loop much shorter.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1097_bruteforce.cpp](1097_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M^3) | AC | 0.015 s | 388 KB |
| [1097_bruteforce.go](1097_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M^3) | AC | 0.031 s | 1348 KB |
| [1097_bruteforce.java](1097_bruteforce.java) | Java 1.8 | bruteforce | O(M^3) | AC | 0.125 s | 2152 KB |
| [1097_bruteforce.py](1097_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M^3) | AC | 0.078 s | 572 KB |
| [1097_bruteforce.rs](1097_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M^3) | AC | 0.031 s | 232 KB |
