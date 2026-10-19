# 2036. Finite closure under line intersections

[Timus 2036](https://acm.timus.ru/problem.aspx?space=1&num=2036) · difficulty 1706 · geometry

Original problem by Mikhail Rubinchik, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Start with `n` distinct points. In one iteration draw every line determined
by two different current points, intersect every pair of distinct nonparallel
lines, and add all those intersection points to the set. Repeat while it grows.
Find the final number of points, or determine that growth never stops.
Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

An integer `1 ≤ n ≤ 100000`, followed by `n` lines containing integer
coordinates `x y` with `|x|,|y| ≤ 100000000`. All input points are different.
There is one instance, without a test-count prefix. The bounds concern
the initial points: later intersections need not be integral or bounded.

## Output

The final count, or exactly `oo`, two lowercase Latin letters, for
infinite growth.

## Checking

Outputs are compared token by token.

## Examples

```
4
0 0
0 1
1 0
1 1
```

```
5
```

## Solution

Call a set closed if one iteration adds nothing. We first classify all
finite closed sets. Collinear points are closed. So is a set with all points
except one on a single line: every other determined line joins that outlier
to a base point, and every finite intersection is already present.
The other possibility is four corners of a parallelogram together with
the intersection of its diagonals.

### Why there are no other finite closed configurations

In a finite noncollinear closed set choose a triangle `ABC` of minimum
positive area. No point of the set lies in an open side segment, since it
and the opposite vertex would form a smaller positive-area triangle.
Moreover, every point lies on one of the three extended side lines.
Otherwise its three barycentric coordinates are nonzero, and two have
the same sign. Joining the point to the remaining vertex intersects the
opposite open side segment. Closure gives a forbidden point there.
The argument also applies when the two coordinates are both negative.

Use an invertible affine transformation to write
`A=(0,0), B=(1,0), C=(0,1)`. Suppose extra points occur on two sides;
rename the vertices to put them at `D=(t,0)` and `E=(0,u)`.
Both parameters lie outside `[0,1]`. If `tu≠1`, lines `DC` and `EB` meet at
`(t(u−1)/(tu−1), u(t−1)/(tu−1))`. Neither coordinate is zero, and their
sum is not one, because `(t−1)(u−1)≠0`. This point is on none of the three
side lines, a contradiction. Hence `tu=1`; the parameter restrictions
force both `t` and `u` to be negative.

If `DE` meets `BC`, the intersection is an extra point `F` on that side,
outside its open segment. Apply the same two-side argument at vertex `B`
to `D` on `BA` and `F` on `BC`. The first parameter is `1−t>1`, whereas
the argument requires both parameters to be negative. Thus `DE` must be
parallel to `BC`, giving `t=u`. Consequently `t=u=−1`.
The five points are the parallelogram corners `B,C,D,E` and their center `A`.
No further point can occur: another on `AB` or `AC` violates `tu=1`
with the existing point on the other line, and one on `BC` contradicts
the same argument at `B`. All points already lie on these three lines.

If extras occur on at most one side, all points but the opposite vertex
are collinear. This finishes the classification. Conversely, the five-point
parallelogram configuration is closed: its only determined lines are its
four sides and two diagonals; their finite intersections are corners or center.

### Applying the classification to the initial set

For `n≤3` the set is already closed. Otherwise test the three lines through
pairs of the first three points. If at most one point lies off any tested
line, output `n`. This finds every such configuration: at least two of
the first three points must lie on its base line.

After those tests fail, a finite closure must be the five-point exceptional
configuration. Thus `n>5` gives `oo`. For `n=4`, finiteness requires the four
corners of a parallelogram; adding their center gives five points.
A four-point subset containing the center and three corners has three
collinear points, which the previous test would already have handled.
For `n=5`, the input itself must be the four corners and center.

Test a four-point parallelogram by trying its three ways to partition
the points into diagonal endpoint pairs: the two coordinate sums must
match. For five points, try each as the center; the other four must pass
that test and their sum must equal four times the center, coordinatewise.
Every remaining case is infinite, since it cannot fit in any finite closed set.

In the sample, the four square corners form a parallelogram. Its
diagonals add `(1/2,1/2)`, and the resulting five-point set is closed,
so the answer is `5`. The center may be nonintegral even though every
input point is integral.

The three line scans take `O(n)` time. The four/five-point checks are constant.
Stored input uses `O(n)` space, with `O(1)` auxiliary geometric workspace.

Pitfalls:

- Arbitrary near-collinear sets may have far more than five points and
  still be closed.
- A trapezoid with only one parallel side pair is not the exceptional
  configuration.
- For five points, the extra point must be the actual diagonal center.
- Intersect complete lines, including beyond the input segments.
- Print letters `oo`, not digits `00`; never use a numeric iteration cutoff.

## Language notes

Use exact signed 64-bit coordinates before multiplication in C++, Go, Java
and Rust; Python uses exact integers. Coordinate differences are at most
`2·10^8`, so a determinant is at most `8·10^16` in absolute value.
Endpoint-sum tests avoid division and also handle half-integer centers.
Java stores primitive coordinate arrays; Python converts input directly into
point tuples and does not retain a second list of all converted integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2036_geometry.cpp](2036_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.046 s | 1512 KB |
| [2036_geometry.go](2036_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.140 s | 4496 KB |
| [2036_geometry.java](2036_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.125 s | 1992 KB |
| [2036_geometry.py](2036_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.218 s | 25868 KB |
| [2036_geometry.rs](2036_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 4720 KB |
