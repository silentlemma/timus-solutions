# 1348. Goat in the Garden 2

[Timus 1348](https://acm.timus.ru/problem.aspx?space=1&num=1348) · difficulty 177 · geometry

Original problem by Pavel Egorov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goat is tied to the point C with a rope of length L, so it can reach
everything within L of C. A bed of pineapples is the segment AB. Find
how much longer the rope must be for the goat to reach at least one
pineapple, and how much longer to reach all of them, with two digits
after the point. All numbers are integers, L ≥ 0, and the coordinates
are at most 10 000 in absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The coordinates of A, B and C and the length L.

## Output

The two extra lengths, one per line.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 0.01·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
8 -6 8 6
0 0 7
```

Output:

```
1.00
3.00
```

## Solution

The nearest point of the bed is the projection of C onto the line AB,
moved to A or B if it falls outside the segment. The farthest point of a
segment from any point is one of its ends. So the answers are
max(0, d_near − L) and max(0, max(|CA|, |CB|) − L). The projection uses
t = (C − A) · (B − A) / |B − A|², kept between 0 and 1, and a bed of a
single point, A = B, takes t = 0.

There is no upper bound on L, so it is read as a floating-point number,
not as an integer, which would overflow. A huge L becomes a huge number
or infinity, and both answers are then 0, which is right: every distance
is at most 20000√2 < 30000. Geometry takes `O(1)` time; including input,
time and space are `O(k)`, where k is the number of input characters.

Pitfalls:

- the bed can be a single point (tests 02 and 08);
- with C on the line of the bed beyond an end, the nearest point is that
  end, not the projection (test 04);
- a rope that is already long enough needs 0, not a negative number
  (test 05);
- L may exceed both integer and floating-point ranges (tests 09–11): as
  a floating-point number it becomes infinity, and both answers are 0,
  while an integer type would overflow.

## Optimized solutions

`1348_geometry_optimized.rs`. Keep the clamped projection onto the segment, the farther endpoint and max(distance-rope,0). Replace parsed input text and Rust formatting with scanf of seven f64 values and printf of two two-decimal answers. A zero-length segment still uses its endpoint, and an infinite parsed rope still gives zero extensions. Geometry uses O(1) operations and explicit state; reading a k-character rope token takes O(k) time. The own Accepted measurement establishes the memory gain.

Compared with `1348_geometry.rs`: time 0.031 s → 0.031 s; memory 244 KB → 116 KB.

`1348_geometry_optimized.cpp`. Keep the projection onto the segment, clamp its parameter to [0,1], and take the farther endpoint for the maximum distance. C scanf/printf replace C++ stream setup and the explicit rope-token string. Geometry remains f64; a rope parsed as positive infinity needs zero extension in both cases. Reading a k-character rope spelling costs O(k), while the explicit geometry state is constant-sized.

Compared with `1348_geometry.cpp`: time 0.015 s → 0.015 s; memory 396 KB → 144 KB.

`1348_geometry_optimized.java`. Keep the same clamped-projection and endpoint geometry. A bounded byte reader replaces Scanner; the unbounded rope token is still decoded and passed to Double.parseDouble. Infinity then correctly gives two zero extensions. This removes general Scanner overhead without claiming constant storage for an arbitrarily long rope spelling: time and token storage are O(k).

Compared with `1348_geometry.java`: time 0.140 s → 0.109 s; memory 1856 KB → 1 072 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1348_geometry_optimized.cpp`: time place 1/276, memory place 8/276 in this comparable sample.

`1348_geometry_optimized.java`: time place 10/47, memory place 9/47 in this comparable sample.

`1348_geometry_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry.cpp](1348_geometry.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 396 KB | 11307276 |
| [1348_geometry.go](1348_geometry.go) | Go 1.14 x64 | geometry | O(k) | AC | 0.031 s | 1080 KB | 11307278 |
| [1348_geometry.java](1348_geometry.java) | Java 1.8 | geometry | O(k) | AC | 0.140 s | 1856 KB | 11307281 |
| [1348_geometry.py](1348_geometry.py) | Python 3.12 x64 | geometry | O(k) | AC | 0.078 s | 496 KB | 11307292 |
| [1348_geometry.rs](1348_geometry.rs) | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 244 KB | 11307285 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1348_geometry_optimized.cpp](1348_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 144 KB | 11325059 |
| [1348_geometry_optimized.java](1348_geometry_optimized.java) \* | Java 1.8 | geometry | O(k) | AC | 0.109 s | 1072 KB | 11324783 |
| [1348_geometry_optimized.rs](1348_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 116 KB | 11325502 |


\* Accepted; the rating target is not yet met. This version may be optimized further.
