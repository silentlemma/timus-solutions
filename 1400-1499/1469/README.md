# 1469. No Smoking!

[Timus 1469](https://acm.timus.ru/problem.aspx?space=1&num=1469) · difficulty 899 · geometry

Original problem by Ilya Shishkov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N cigarettes (1 ≤ N ≤ 50000) lie on a table as segments of non-zero
length with integer ends from −10000 to 10000. A cigarette may be taken
only if it touches or crosses another one. Print "YES" and the numbers of
two cigarettes that share a point, or "NO" if no two do.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

N, then N lines x1 y1 x2 y2.

## Output

"YES" and two numbers, or "NO". Any meeting pair is accepted.

## Examples

### Example 1

Input:

```
2
0 0 2 2
0 2 2 0
```

Output:

```
YES
1 2
```

### Example 2

Input:

```
2
0 0 0 5
5 0 5 10
```

Output:

```
NO
```

## Solution

This is the Shamos–Hoey sweep. Move a vertical line from left to right
and keep the segments it crosses in a list ordered by height. As long as
no two segments meet, that order never changes, and the first meeting
point to the left is always between two neighbours in the list. So it
is enough to test a new segment against its neighbours when it is
inserted, and the two segments that become neighbours when one leaves.

Degenerate cases need care. First the plane is sheared by
x' = 20001 x + y: distinct integer endpoints get distinct x', so no segment is vertical,
and touching or crossing stays the same. At one x', segments starting
there are inserted before those ending there are removed, and segments
through the same point are ordered by slope. All comparisons use exact
integer cross products, and the meeting test counts touching ends and
overlaps on one line. The list is a sorted array: insertion and removal
can shift N items. `O(N log N)` comparisons, `O(N^2)` total time.

Pitfalls:

- touching counts: an end on another cigarette, two ends at one point,
  overlaps on one line (tests 04, 05, 07, 12);
- upright cigarettes, which the shear handles (tests 07, 11);
- testing every pair is far too slow for 50000 cigarettes.

## Language notes

- Python runs under PyPy: CPython exceeds the 1.5 s limit on the judge's
  test 3, and PyPy takes 0.88 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1469_geometry.cpp](1469_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.250 s | 4952 KB |
| [1469_geometry.go](1469_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.625 s | 10184 KB |
| [1469_geometry.java](1469_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.375 s | 7668 KB |
| [1469_geometry.py](1469_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.875 s | 36680 KB |
| [1469_geometry.rs](1469_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.625 s | 9372 KB |
