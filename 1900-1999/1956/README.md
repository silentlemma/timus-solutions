# 1956. A Line with Minimum Total Distance

[Timus 1956](https://acm.timus.ru/problem.aspx?space=1&num=1956) · difficulty 2319 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Pavel Klimov (prepared by Olga Soboleva).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Move n points in the plane onto a common infinite straight line. Minimize
the sum of their Euclidean travel distances; both the line and the new
positions are free choices. Points may coincide. Limits: 1 second, 64 MB.

## Input

First n, 2≤n≤1000. Then n pairs of integer coordinates x,y, each between
−10⁶ and 10⁶ inclusive.

## Output

One real number, the minimum total distance. Absolute or relative error
must not exceed 10⁻⁶. The programs print twelve fractional digits.

## Checking

The answer is compared with absolute or relative error 10⁻⁶.

## Examples

```
4
0 0
0 1
1 1
1 0
```

```
1.414214
```

## Solution

For a chosen line, orthogonal projections give the shortest individual
moves. For a fixed direction, project the original points onto a unit
normal: the offset minimizing the sum of absolute deviations is a median.
Thus an optimal line of that direction can pass through an input point P;
for even n, choose an endpoint of the median interval.

Fix such P and rotate the line. Between directions through another distinct
point, every signed cross product keeps its sign. The total cost is
A cos θ+B sin θ≥0, with second derivative equal to minus itself. If the
points are not collinear, this cost is positive and strictly concave on
each such interval, so its minimum is at an interval boundary. Therefore
some global optimum passes through two distinct input locations. If all
locations coincide, the answer is zero.

Evaluating all pairs literally costs O(n³). Instead, fix each pivot P and
form v=Q−P for every other point. Skip zero vectors and negate a vector if
its y is negative, or if y=0 and x<0. This puts unoriented directions in
the half-plane y≥0, with the positive horizontal ray included. Negation
does not change any absolute cross product.

Sort by k=−x/(|x|+y), a strictly increasing function of angle on [0,π).
Initialize R to the sum of these normalized vectors. At direction d,
vectors not yet passed have cross(d,v)≥0; passed vectors have it ≤0.
Consequently cross(d,R) is exactly the sum of absolute cross products.
The cost is cross(d,R)/sqrt(d.x²+d.y²). After processing a vector v,
subtract 2v from R. Collinear vectors contribute zero, so ties need no
special grouping. Examine a pair only at its smaller input index.

Python combines identical locations with their multiplicities. A vector
with weight w contributes wv to R and subtracts 2wv after its event. Other
languages keep repeated points explicitly. Both versions count every
original point and use O(n) working space. The total running time is
O(n² log n).

### Exact arithmetic and pitfalls

Directions are integer vectors of magnitude at most 2·10⁶ per coordinate.
Key denominators are at most 4·10⁶. Distinct rational keys differ by at
least 1/(4·10⁶)², far more than binary64 rounding on [−1,1]. Equal rational
directions round equally, so sorting needs no epsilon or atan2.

R coordinates have absolute value below 2·10⁹. Each cross product term is
below 4·10¹⁵ and its difference below 8·10¹⁵. Native versions use signed
64-bit integers. Python deliberately uses binary64 integer-valued vectors:
each multiplication and subtraction here is exact, because the products
are below 2⁵² and the integer result below 2⁵³. Squared norms are at most
8·10¹² and exact too. Only sqrt and division round, well within 10⁻⁶.
Do not replace distances by squared distances: that changes the optimum.
Do not ignore multiplicities, divide by a zero vector, or restrict the line
to horizontal/vertical directions. An all-collinear set has answer zero.

## Language notes

C++ and Rust reuse one vector, Go 1.14 uses sort.Slice, and Java 8
reuses its direction objects instead of allocating one per pair. Python
uses Counter, precomputed doubled updates and an itemgetter sort key. It
runs under PyPy: under CPython 3.12 it exceeds the time limit on the
judge's test 49, while PyPy 3.10 is accepted in 0.843 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1956_geometry.cpp](1956_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^2 log n) | AC | 0.046 s | 552 KB |
| [1956_geometry.go](1956_geometry.go) | Go 1.14 x64 | geometry | O(n^2 log n) | AC | 0.218 s | 1300 KB |
| [1956_geometry.java](1956_geometry.java) | Java 1.8 | geometry | O(n^2 log n) | AC | 0.296 s | 4040 KB |
| [1956_geometry.py](1956_geometry.py) | PyPy 3.10 x64 | geometry | O(n^2 log n) | AC | 0.843 s | 11748 KB |
| [1956_geometry.rs](1956_geometry.rs) | Rust 1.75 x64 | geometry | O(n^2 log n) | AC | 0.031 s | 280 KB |
