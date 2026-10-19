# 1849. Rabbit Hunt 2

[Timus 1849](https://acm.timus.ru/problem.aspx?space=1&num=1849) · difficulty 2492 · sorting

Original problem by Alexey Samsonov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n rabbits sit at distinct points of the plane. A program generates q
shots, each a hunter's position and a direction; a shot kills every
rabbit on the ray from the hunter along the direction, including a
rabbit at the hunter's own point. Shot 1 is given, and every next shot
comes from the previous one by
x′ = (aₓ·(x + 10000) + bₓ) mod 20001 − 10000, the same for y with
a_y, b_y, and v′ = (a_v·(v + 10) + b_v) mod 21 − 10 for each part of
the direction with its own pair of numbers. Find the shot that kills
the most rabbits, and how many it kills.

## Input

n (1 ≤ n ≤ 10 000) and the rabbits, integers of absolute value at most
10 000; then q (1 ≤ q ≤ 10⁶); then x₁, y₁, vx₁, vy₁ (|x₁|, |y₁| ≤
10 000, |vx₁|, |vy₁| ≤ 10); then aₓ, bₓ, a_y, b_y, a_vx, b_vx, a_vy,
b_vy, from 0 to 10⁵. No direction among the first q shots is zero.

## Output

The number of the best shot and the number of rabbits it kills. Among
equally good shots the solutions print the last one.

## Examples

### Example 1

Input:

```
4
0 0
2 0
3 0
2 2
3
-1 -1 1 0
1 0 1 1 1 0 1 0
```

Output:

```
2 3
```

## Solution

A direction (vx, vy) only matters through its primitive vector (dx, dy)
= (vx, vy) / gcd(vx, vy), and there are only a few hundred of those.
Generate all shots first and sort them by primitive vector with a
counting sort. Then take the vectors one at a time. Along (dx, dy) a
point (x, y) lies on the line x·dy − y·dx and at the place x·dx + y·dy
on that line. Sort the rabbits by line and place (Python groups by line
and sorts places); a shot hits rabbits on its line whose place is at
least its own, counted by two binary searches (one in Python).
Each vector costs `O(n log n)` once and every
shot `O(log n)`.

The direction parts follow a map v → a·v + b on 21 values, so they
soon repeat with a period of at most 42 pairs, and in practice only a
few dozen vectors are ever used.

In the example the second shot stands at (−1, 0) and looks along
(1, 0): its line holds (0, 0), (2, 0) and (3, 0), all in front, so it
kills 3. The first and third shots look along y = −1 and y = 1, where
no rabbit sits.

Pitfalls:

- (2, 0) and (1, 0) are the same direction; reduce by the gcd;
- a rabbit at the hunter's point counts, one behind does not;
- the shots are many, so they are generated once and stored compactly.

The answers agree with an independent accepted implementation on three
hundred small cases and on the large tests, ties included.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1849_sorting.cpp](1849_sorting.cpp) | G++ 13.2 x64 | sorting | O(D n log n + q log n) | AC | 0.171 s | 15560 KB |
| [1849_sorting.go](1849_sorting.go) | Go 1.14 x64 | sorting | O(D n log n + q log n) | AC | 0.296 s | 18392 KB |
| [1849_sorting.java](1849_sorting.java) | Java 1.8 | sorting | O(D n log n + q log n) | AC | 0.281 s | 17612 KB |
| [1849_sorting.py](1849_sorting.py) | Python 3.12 x64 | sorting | O(D n log n + q log n) | AC | 2.265 s | 20952 KB |
| [1849_sorting.rs](1849_sorting.rs) | Rust 1.75 x64 | sorting | O(D n log n + q log n) | AC | 0.187 s | 31916 KB |
