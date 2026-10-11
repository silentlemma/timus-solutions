# 1311. Stable Construction

[Timus 1311](https://acm.timus.ru/problem.aspx?space=1&num=1311) · difficulty 1432 · implementation

Original problem by Alexey Lakhtin, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A wall is built from bricks of equal height, thickness and density
but different lengths, in H ≤ 10 000 layers of up to 1000 bricks
each, at most 100 000 in all. A brick spans [L, R] with integer ends
from 0 to 10 000, and no brick rests on two or more bricks of the
layer below. Without mortar, does the wall stand? Something falls if a
brick, together with everything resting on it, has its centre of mass
on the edge of its support or outside it.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

H; then for every layer from the top: the number of bricks K, then K
lines `L R` in increasing order.

## Output

`Yes` if the wall stands, otherwise `No`.

## Examples

### Example 1

Input:

```
3
1
10 20
3
1 7
13 17
100 200
2
0 20
60 160
```

Output:

```
Yes
```

## Solution

Every brick above the bottom layer rests on exactly one brick below it,
the one it overlaps (with positive length), so the bricks form trees
standing on the bottom layer. The support of a brick is its overlap
with that brick, and the load is the brick plus everything that rests
on it, directly or not.

A brick's mass is proportional to its length, and its moment about 0 is
(R² − L²) / 2. So the load of a brick is W = Σ (R − L) and
M = Σ (R² − L²) / 2 over its subtree, and its centre is M / W. Keeping
2M instead of M, the condition lo < M / W < hi becomes

2 · lo · W < 2M < 2 · hi · W,

all in exact integers (2M stays below 2 · 10¹³).

The layers come from the top, which is the order in which the loads are
complete. For each new layer, walk the layer above and the new one
together with two pointers: each brick above finds the brick below that
it overlaps, is checked against that overlap, and adds its W and 2M to
it. A brick with nothing under it, or one that only touches a brick at
a corner, falls. The bottom layer stands on the floor. `O(total bricks)`.

Pitfalls:

- a centre exactly on the edge counts as falling (test 03 against
  test 04);
- bricks that only touch at an end hold nothing (test 05), and an empty
  layer leaves the bricks above it hanging (test 06);
- weight added on top can save an overhanging brick: here nine small
  bricks are enough and eight are not (tests 09 and 10).

The answers were compared with an independent check in exact fractions,
building the tree of supports explicitly, on 600 random walls.

## Language notes

- Python slices the input into whole layers and works on plain lists,
  about 0.1 s for 100 000 bricks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1311_implementation.cpp](1311_implementation.cpp) | G++ 13.2 x64 | implementation | O(total bricks) | AC | 0.109 s | 204 KB |
| [1311_implementation.go](1311_implementation.go) | Go 1.14 x64 | implementation | O(total bricks) | AC | 0.031 s | 5572 KB |
| [1311_implementation.java](1311_implementation.java) | Java 1.8 | implementation | O(total bricks) | AC | 0.109 s | 4440 KB |
| [1311_implementation.py](1311_implementation.py) | Python 3.12 x64 | implementation | O(total bricks) | AC | 0.281 s | 21796 KB |
| [1311_implementation.rs](1311_implementation.rs) | Rust 1.75 x64 | implementation | O(total bricks) | AC | 0.015 s | 3152 KB |
