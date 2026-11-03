# 1052. The most points on one line

[Timus 1052](https://acm.timus.ru/problem.aspx?space=1&num=1052) · difficulty 239 · geometry, sorting

Original problem by Stanislav Vasiliev, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` distinct points (`3 ≤ N ≤ 200`) with integer coordinates from
−2000 to 2000, find the largest number of them that lie on one straight
line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with `x` and `y`.

## Output

The largest number of points on one line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
7 122
8 139
9 156
10 173
11 190
-100 1
```

Output:

```
5
```

### Example 2

Input:

```
3
0 0
1 0
0 1
```

Output:

```
2
```

## Solution

Try every pair of distinct input points `i,j`. They define one line.
Count all points `k` on it using the exact equality
`(x[k]−x[i])·(y[j]−y[i]) = (y[k]−y[i])·(x[j]−x[i])`.
Take the largest count. A largest line contains at least two input points,
so one of the tried pairs defines it; conversely, every counted point is
on the selected line. This proves that the maximum is exactly the answer.

This direct `geometry_bruteforce` implementation is the preferred simple
version in all five languages. Time is `O(N³)`, at most 3,980,000 point
checks for `N=200`; storing the input needs `O(N)` space. If a pair already
contains all points on its line, the answer `N` is optimal and we stop.
Coordinate differences have magnitude at most 4000, so each product is
at most 16,000,000 in magnitude and fits signed 32 bits. No floating-point
slopes, division or gcd normalization is needed.

Vertical and horizontal lines, points on opposite sides of the chosen
anchor, and nearly equal slopes all use the same equality. Distinct input
points guarantee that the chosen pair is not a zero vector; the answer
is always at least two. The direct programs passed all judge tests; local
tests also compare them with an independent canonical-line oracle.

## Optimized solutions

The retained direction-counting algorithm fixes an anchor and reduces
each direction `(dx,dy)` by `gcd(|dx|,|dy|)`. Flip its sign to make
`dx>0`, or `dx=0,dy>0`; opposite vectors then represent the same line.
Equal reduced directions share a line through the anchor. Count only later
points: the earliest point on any largest line still sees all the others.

With hash maps, expected time is `O(N² log C)` and working storage `O(N)`,
where `C=4000` bounds coordinate differences. C++ uses an ordered map,
so its bound is `O(N²(log N+log C))`, including map operations. Hash-table
worst-case lookup costs are not claimed constant.

The unchanged Python direction-counting source is classified as
optimized relative to the new simple base: its CPython Accepted is
0.078 s and 508 KB, against the simple PyPy Accepted's 0.250 s and 2840 KB.
That is 68.8% less time and 82.1% less memory. This comparison includes
both algorithm and interpreter; the table names the accepted runtime.
The old native direction maps are preserved as additional accepted
algorithms, but have no measured 30% advantage over the new simple source
in the same language. A one-tick timer difference is not an admission.

The new Rust `geometry_sorting` source reduces directions in the same exact way,
then sorts a fixed array and counts equal runs. This replaces the former
hash table with deterministic `O(N²(log N+log C))` time and `O(N)` space.
The earliest point of an optimal line sees every other point on it; once
at most `best` later points including the anchor remain, no improvement is possible.
Two arrays of 200 coordinate/direction pairs and bounded raw I/O use no heap.
The C entry avoids unused Rust startup and formatting facilities.
Its own Accepted is 0.015 s / 52 KB, versus the preferred cubic Rust's
0.031 s / 212 KB: memory is reduced by 75.5%. The time difference is one
judge tick and is not used to justify admission. All 466 distinct subsets
of at least two points from a signed 3×3 grid matched an independent
pair-cross-product oracle, in addition to the repository tests.

## Language notes

The cubic Python source is accepted under PyPy 3.10; the direction-map
source is accepted under CPython 3.12. Other simple versions use the normal
judge compilers and standard input facilities. Direction counting uses
`std::map` in C++, hash maps in Go/Rust, `Counter` in Python, and a Java
`HashMap` with the collision-free key `dx·8192+dy` (`|dy|≤4000`).

## Solutions

### Simple

The first five rows are the preferred simple versions. The final four retain the earlier native direction-map alternatives for comparison.

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1052_geometry_bruteforce.cpp](1052_geometry_bruteforce.cpp) | G++ 13.2 x64 | geometry, bruteforce | O(N³) | AC | 0.015 s | 108 KB | 11308047 |
| [1052_geometry_bruteforce.go](1052_geometry_bruteforce.go) | Go 1.14 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 1076 KB | 11308048 |
| [1052_geometry_bruteforce.java](1052_geometry_bruteforce.java) | Java 1.8 | geometry, bruteforce | O(N³) | AC | 0.125 s | 452 KB | 11308050 |
| [1052_geometry_bruteforce.py](1052_geometry_bruteforce.py) | PyPy 3.10 x64 | geometry, bruteforce | O(N³) | AC | 0.250 s | 2840 KB | 11308046 |
| [1052_geometry_bruteforce.rs](1052_geometry_bruteforce.rs) | Rust 1.75 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 212 KB | 11308054 |
| [1052_geometry.cpp](1052_geometry.cpp) | G++ 13.2 x64 | geometry | O(N²(log N+log C)) | AC | 0.001 s | 208 KB | 11278696 |
| [1052_geometry.go](1052_geometry.go) | Go 1.14 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 3264 KB | 11278697 |
| [1052_geometry.java](1052_geometry.java) | Java 1.8 | geometry | O(N² log C) expected | AC | 0.156 s | 4180 KB | 11278700 |
| [1052_geometry.rs](1052_geometry.rs) | Rust 1.75 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 412 KB | 11278703 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1052_geometry.py](1052_geometry.py) | Python 3.12 x64 | geometry | O(N² log C) expected | AC | 0.078 s | 508 KB | 11278698 |
| [1052_geometry_sorting.rs](1052_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N²(log N+log C)) | AC | 0.015 s | 52 KB | 11309709 |
