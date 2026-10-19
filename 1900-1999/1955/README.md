# 1955. Longest Visible Chord of a Simple Polygon

[Timus 1955](https://acm.timus.ru/problem.aspx?space=1&num=1955) · difficulty 3242 · geometry

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the maximum distance between two points of a simple polygon such
that their entire joining segment lies inside or on the boundary. The
polygon may be nonconvex. Its edges neither cross nor touch nonadjacent
edges. Endpoints may be anywhere, including interiors of edges.
Limits: 1 second, 64 MB.

## Input

First n, 3≤n≤200. Then n integer vertex pairs x,y in clockwise or
counterclockwise boundary order, −1000≤x,y≤1000. Consecutive collinear
edges are allowed; there are no self-intersections or self-touches.

## Output

One real number, the maximum segment length, with absolute or relative
error at most 10⁻⁶. Print twelve fractional digits.

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

### Why vertex-pair supporting lines suffice

Take a maximum closed feasible segment and extend it to boundary endpoints.
If it contains no polygon vertex, both endpoints lie inside edges. A small
motion of one endpoint in either direction along its edge remains feasible.
Squared distance is strictly convex in this motion, so cannot have a local
maximum. With just one vertex at an endpoint, move the other endpoint in
the same way. A boundary-collinear segment is no exception: maximality
includes the whole incident edge and thus another vertex.

If the only vertex v is strictly between the endpoints, rotate the line
slightly in either direction about v. The two endpoints stay within their
fixed edges and feasibility persists locally. Each half-length is
h/|sin(θ−α)|, where h>0 is the perpendicular distance from v to that edge's
line. On this open angular interval each term is a positive cosecant
with strictly positive second derivative; their sum is strictly convex.
It cannot attain a local maximum there either. If a direction were on an
incident boundary ray, the segment would contain another vertex already.
Consequently some maximum contains at least two polygon vertices.

Enumerate the whole line through every pair, intersect it with the closed
polygon, and take its longest connected component. These are feasible
segments, and the argument above guarantees a maximum is included. Do not
restrict the answer to the distance between the selected vertices: a
maximum can extend beyond them to interiors of two other edges.

### Computing a line intersection

Parameterize the line as P+tD, D=Q−P. Compute exact integer heights
h(V)=cross(D,V−P). For each directed edge A→B, if (h(A)>0) differs from
(h(B)>0), add its intersection parameter
t=cross(A−P,B−A)/cross(D,B−A). Sort these events and pair consecutive ones.
The bounded polygon is outside at −∞; the half-open sign rule handles a
vertex consistently. Duplicate tangent events either create a zero interval
or two touching intervals. Add every edge with both heights zero as a closed
interval, using t=dot(V−P,D)/dot(D,D) for its endpoints. Finally sort all
intervals and merge overlaps AND touching endpoints. The largest merged
parameter length times |D| is the required chord on this line. Explicit
boundary intervals preserve valid segments along collinear edges.

### Exact accelerations

The largest squared distance U between polygon vertices is an upper bound
for any two points of the polygon: it is also the diameter of their convex
hull. If a farthest pair is visible, return sqrt(U) immediately. Each edge,
and each subsequently confirmed visible vertex pair, provides an exact
integer feasible squared lower bound L.

Let w,h be the coordinate bounding-box dimensions and d²=dot(D,D). Any
chord parallel to D has squared length at most w²d²/dx² when dx≠0, and
h²d²/dy² when dy≠0. Reject a pair if either bound is strictly below L,
using integer cross multiplication. This also works when one component
of D is zero: its multiplication test simply cannot reject. Normalize D
by gcd and sign, and deduplicate the line key (nx,ny,cross((nx,ny),P)).

Python additionally rejects a selected pair as soon as an edge crosses
the interior of its joining segment transversely. All tests are integer
sign/range tests on the intersection numerator and denominator. A maximum's
two contact vertices are mutually visible, so such pairs can be skipped.
Only mark a line as seen after a visible pair is found; an invisible pair
must not prevent another component of the same line from being examined.
Heights are advanced by exact integer edge increments to allow early exit.
The native versions may examine all components even for invisible pairs.

### Numerical bounds

Signs, collinearity, gcd keys and pruning are integer operations. Cross/dot
parameter numerators and denominators have magnitude at most 8·10⁶, so
their conversion to binary64 is exact. Two distinct such rational values
differ relatively by at least 1/(8·10⁶)²>10⁻¹⁴, far beyond binary64 rounding;
equal rational values round identically. Thus sorting and interval-touch
decisions require no epsilon. Every intersection parameter has |t|<2829,
so quotient error is at most 2⁻⁴² and subtraction error at most 2⁻⁴⁰.
Multiplying by |D|<2829, with the final rounded products and square root,
gives absolute length error below 10⁻⁸. Maximization preserves this bound.
Pruning products are at most 3.2·10¹³ and fit signed 64-bit integers.

O(n³ log n) time in the worst case: O(n²) lines, O(n) events per line
and sorting. O(n²) space for deduplication, with O(n) working storage for
one line. The diameter test takes O(n²). Pruning only improves these bounds.

The polygon need not be convex; its diameter can leave it. An optimal
segment need not have vertex endpoints. Keep closed boundary edges and
merge touching components, use a consistent half-open crossing rule, and
do not multiply pruning quantities in 32-bit arithmetic. Clockwise input
works with the same parity logic. Never use an invisible selected pair
to discard an entire supporting line before another visible pair is tried.

## Language notes

All programs are standalone and standard-library only. Use signed 64-bit
integers in native ports and binary64 only for parameter quotients and
lengths. Python integers are unbounded. Java uses strict floating-point
evaluation and reuses its event/interval workspace. Java's line key packs
nx, ny+2000 and c+4000000 into disjoint bit fields: 0≤nx≤2000,
0≤ny+2000≤4000 and 0≤c+4000000≤8000000 fit the chosen 12/23-bit fields;
the combined key fits a signed long. Other ports keep an integer triple.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1955_geometry.cpp](1955_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3 log n) | AC | 0.062 s | 992 KB |
| [1955_geometry.go](1955_geometry.go) | Go 1.14 x64 | geometry | O(n^3 log n) | AC | 0.234 s | 9272 KB |
| [1955_geometry.java](1955_geometry.java) | Java 1.8 | geometry | O(n^3 log n) | AC | 0.359 s | 8124 KB |
| [1955_geometry.py](1955_geometry.py) | Python 3.12 x64 | geometry | O(n^3 log n) | AC | 0.703 s | 1104 KB |
| [1955_geometry.rs](1955_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3 log n) | AC | 0.062 s | 2096 KB |
