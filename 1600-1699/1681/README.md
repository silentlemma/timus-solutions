# 1681. Brother Bear's Garden

[Timus 1681](https://acm.timus.ru/problem.aspx?space=1&num=1681) · difficulty 3537 · geometry

Original problem by Pavel Egorov, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A garden is a strictly convex polygon with n posts, given
counterclockwise. From every post a rope goes to the post k steps
further counterclockwise. A rabbit comes in over the fence and never
crosses a rope. Find the share of the garden's area it cannot reach.

## Input

n and k (3 ≤ n ≤ 300; 1 ≤ k < n), then the n posts, integer
coordinates up to 10000 in absolute value.

## Output

The ratio of the saved area to the whole area, with an error of at
most 10⁻⁴.

## Examples

### Example 1

Input:

```
5 3
0 0
20 0
20 20
10 30
0 20
```

Output:

```
0.466666667
```

### Example 2

Input:

```
6 2
0 2
-2 1
-2 -1
0 -2
2 -1
2 1
```

Output:

```
0.666666667
```

## Solution

The ropes for k and for n − k are the same chords, so let
k = min(k, n − k). With k = 1 every rope lies along the fence and the
rabbit cannot get in at all: the answer is 1.

Otherwise every rope is a chord that cuts the garden in two, so two
points are in the same piece exactly when no rope separates them, and
each piece is the garden intersected with one half-plane per rope. The
rabbit reaches precisely the pieces that contain a stretch of the
fence. The piece next to side i (from post i to post i + 1) is the
garden clipped, for every rope, to the half-plane holding the side's
midpoint. Two sides never share a piece: the ropes from posts i + 1 − k
and i both border side i, and between them they separate it from every
other side. So the answer is 1 − Σ area(piece of side i) / area.

Only the k ropes that pass over side i, from posts i + 1 − k, …, i,
need to be applied. The part of the garden on side i's side of any
other rope is the hull of a run of n − k + 1 consecutive posts around
side i, and since 2k ≤ n that run contains the k + 1 posts of some
rope over side i. So that rope already cuts at least as deep.

Clipping a convex polygon by a half-plane is linear in its size. Start
with the two ropes from the ends of the side, which leave a small
triangle, then apply the rest. `O(n² + n · k · s)`, where s is the
maximum piece size after the first two clips.

Pitfalls:

- k = 1 and k = n − 1 give 1, not 0: the ropes are the fence itself;
- a piece that touches the fence only at a post, like a star tip of a
  pentagram (test 05), is saved;
- when 2k = n every rope appears twice, which is harmless.

The answers match the clipping by all n ropes on 500 random polygons,
and an independent accepted implementation on random polygons, both
near-circular and irregular.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1681_geometry.cpp](1681_geometry.cpp) | G++ 13.2 x64 | geometry | O(n² + n · k · s) | AC | 0.015 s | 252 KB |
| [1681_geometry.go](1681_geometry.go) | Go 1.14 x64 | geometry | O(n² + n · k · s) | AC | 0.031 s | 5624 KB |
| [1681_geometry.java](1681_geometry.java) | Java 1.8 | geometry | O(n² + n · k · s) | AC | 0.125 s | 4932 KB |
| [1681_geometry.py](1681_geometry.py) | Python 3.12 x64 | geometry | O(n² + n · k · s) | AC | 0.265 s | 756 KB |
| [1681_geometry.rs](1681_geometry.rs) | Rust 1.75 x64 | geometry | O(n² + n · k · s) | AC | 0.031 s | 312 KB |
