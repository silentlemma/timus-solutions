# 1865. The Island of Märket

[Timus 1865](https://acm.timus.ru/problem.aspx?space=1&num=1865) · difficulty 3334 · constructive

Original problem by Eugene Kurpilyanskiy (idea by Leonid Volkov), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The island is the rectangle from (0, 0) to (w, h), and the lighthouse is
a d × d square with its south-west corner at (x, y), strictly inside.
Draw a border from the north coast to the south coast: a polyline with
integer vertices whose segments are alternately vertical and horizontal,
the first and the last vertical, all of nonzero length. It must not
touch itself or the west and east coasts, must touch the north and the
south coast once each, and must split the island into two equal halves
with the whole lighthouse in the eastern (Finnish) one. The border may
touch the lighthouse but not cross it. At most 1000 vertices are
allowed.

## Input

w and h (3 ≤ w, h ≤ 10⁶, w·h even), then x, y and d (d > 0, 0 < x < w − d,
0 < y < h − d).

## Output

The number of vertices and the vertices from north to south, or
"Impossible". Any valid border is accepted.

## Examples

### Example 1

Input:

```
6 3
1 1 1
```

Output:

```
6
4 3
4 2
1 2
1 1
4 1
4 0
```

### Example 2

Input:

```
10 10
1 1 8
```

Output:

```
Impossible
```

## Solution

With integer vertices both parts are made of unit cells, and half is
w·h/2 cells. Some cells are Finnish whatever the border. The border
cannot reach the east coast, so the column of h cells along it belongs
to Finland. The lighthouse adds d² cells. Finland is connected, so some
row also holds the w − 1 − x − d cells between the lighthouse and that
column. If h + d² + (w − 1 − x − d) exceeds half, the answer is
"Impossible". Otherwise one of two shapes works.

If h + d(w − 1 − x) ≤ half, let every row of Finland run from some
column to the coast: the rows of the lighthouse from column x, the
other rows from column w − 1. The cells still missing are taken from
the top down, moving rows west but never past column 1. Within each of
the three bands of rows (above, beside and below the lighthouse) a few
rows reach column 1, one row stops part of the way, and the rest keep
their column. The border goes down through these columns, so it never
touches itself, and it has fewer than 20 vertices.

Otherwise whole lighthouse rows give Finland too much, and the border
goes round the lighthouse instead. It goes down column w − 1 to the
top of the lighthouse, along its top, west and south sides, and up its
east side. Finland then takes whole rows of the corridor east of the
lighthouse from the top down, and part of one more row. The amount
left to take is less than (d − 1) times the corridor width, so all
this stays beside the lighthouse. The border returns to column w − 1
and goes straight down to the south coast. Both shapes take `O(1)`
time.

The answer to the first example is different but just as valid: rows
of 3, 5 and 1 cells from the top give Finland 9 cells, half of 18.

Pitfalls:

- w·h reaches 10¹², so 64-bit integers are needed;
- touching the lighthouse is allowed, so the border may run along its
  sides;
- rows moved west stop at column 1, or the border would touch the west
  coast;
- pieces of the border in the same column must be merged, or a segment
  would have zero length;
- when the lighthouse is next to the coast column the corridor is
  empty, and the first shape always fits.

The borders pass a checker on all 2354 islands with sides up to 10 and
on large random ones, and the "Impossible" answers agree with an
independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1865_constructive.cpp](1865_constructive.cpp) | G++ 13.2 x64 | constructive | O(1) | AC | 0.015 s | 196 KB |
| [1865_constructive.go](1865_constructive.go) | Go 1.14 x64 | constructive | O(1) | AC | 0.046 s | 1156 KB |
| [1865_constructive.java](1865_constructive.java) | Java 1.8 | constructive | O(1) | AC | 0.125 s | 552 KB |
| [1865_constructive.py](1865_constructive.py) | Python 3.12 x64 | constructive | O(1) | AC | 0.109 s | 820 KB |
| [1865_constructive.rs](1865_constructive.rs) | Rust 1.75 x64 | constructive | O(1) | AC | 0.031 s | 252 KB |
