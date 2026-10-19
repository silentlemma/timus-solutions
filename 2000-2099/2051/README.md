# 2051. Separate two equal-area curves from their envelopes

[Timus 2051](https://acm.timus.ru/problem.aspx?space=1&num=2051) · difficulty 3745 · meet_in_middle

Original problem by Viktor Kamashev, prepared by Bulat Zaynullin, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two hidden continuous piecewise-linear functions on [0, T] have equal
integrals. Only their pointwise maximum h and minimum g are known.
Reconstruct any two such functions. The limits are 1 second and 64 MB.

## Input

First T, 2 ≤ T ≤ 10⁶. Then h and then g, each as its number of knots (2
≤ n, m ≤ 100 000) followed by integer pairs t y. The times increase
strictly from 0 to T, the heights are between 0 and 10⁶, and no three
consecutive knots are collinear. Everywhere g ≤ h, with equality at no
more than thirty points, endpoints included, and never along a segment.
A solution is guaranteed.

## Output

Two functions in the same format: the number of knots, then integer
pairs t y, with times strictly increasing from 0 to T and no three
consecutive knots collinear.

## Checking

A checker verifies exactly that the pointwise maximum and minimum of the
two functions are h and g and that their integrals are equal; any valid
pair is accepted.

## Examples

```
6
6
0 2
1 1
2 2
3 1
4 2
6 0
6
0 0
1 1
2 0
3 1
4 0
6 0
```

```
5
0 2
1 1
2 2
4 0
6 0
5
0 0
1 1
2 0
4 2
6 0
```

The envelopes meet at times one, three and six. The three positive-gap
regions have doubled gap areas `2,4,6`. Assigning the upper graph on the
first two regions and the lower graph on the last gives the first
displayed curve; the second uses the opposite assignment. Each integral
is five. The knot at time three disappears from the first output because
it becomes collinear with its neighbours; extra collinear knots are not
permitted.

## Solution

### Where curves may exchange roles

Inside a connected interval where `h>g`, a continuous reconstructed
function must follow one envelope for the entire interval. Switching
between distinct values would violate continuity. A switch is possible
at every contact where `h=g`. Conversely any assignment of upper/lower
roles independently between consecutive contacts produces continuous
functions with the correct envelopes.

Every contact is at a knot time of at least one input graph. Otherwise
the gap is linear in a neighbourhood: an isolated interior zero would
change its sign, or a zero gap would persist on a segment. Both
contradict the assumptions. Thus contact times are integers. At least
one graph has an integer knot height there, so their common value is
also an integer.

Merge the two lists of knot times and compare the interpolated heights
exactly. On an edge `(a,x),(b,y)` the value at `t` is the rational pair
`(x(b-t)+y(t-a), b-a)`. Cross multiplication tests equality without
rounding. Keep internal contacts and use zero and `T` as the outer
boundaries whether or not they are contacts. There are `R≤31` resulting
positive-gap regions.

### Exact area partition

Insert every missing internal contact into both graphs. All inserted
coordinates are integers. On each region compute each graph's doubled
integral by summing `(y_i+y_next)(t_next-t_i)`. Their difference `d_i`
is a positive integer. Let `D=sum d_i`. If the first output uses the
upper graph on a subset `S` and the lower graph elsewhere, its doubled
area is the lower graph's doubled total area plus `sum_S d_i`. The
second output's doubled area is the upper total minus that same sum.
They are equal exactly when `sum_S d_i=D/2`. The existence promise
guarantees an even `D` and a suitable subset.

Split the `R` weights into `L=floor(R/2)≤15` left weights and at most
sixteen right weights. Enumerate all left subsets, storing a single
integer `key=sum·2^L+mask`. Generate these by doubling the list for each
added weight and sort the keys. The mask occupies the low `L` bits;
sorting therefore orders primarily by sum and retains duplicate sums
safely.

Enumerate right masks in Gray-code order. Consecutive masks differ in
one bit, so add or subtract one weight to update the right sum. For
`need=D/2-right_sum`, binary-search the first key at least `need·2^L`.
Its quotient by `2^L` equals `need` exactly when a matching left subset
exists. Recover its low bits and combine them with the right mask. Every
subset of each half is enumerated, so the promised solution is found.

All arithmetic is exact. Interpolated numerators are at most `10^12` and
cross products at most `10^18`. `D≤2·10^12`, so every packed key is
below `6.6·10^16`. Signed 64-bit integers suffice; promote operands
before multiplying. The complete mask uses at most 31 bits.

### Reconstructing canonical output

Visit regions from left to right and append the selected input graph's
knots, including the inserted boundary contacts, to the first curve;
append the other graph's knots to the second. Ignore repeated copies of
a shared boundary. While the last three points are collinear, remove the
middle one using an exact cross product. Removing it preserves the same
linear function; the stack process leaves no collinear triples. Contact
values agree, so every transition is continuous. The chosen subset
proves equal integrals, while complementary roles preserve both
envelopes. All output coordinates remain integers within the original
ranges.

Do not add the interpolated value of a graph at every unrelated knot of
the other graph: that value may be noninteger. Only the selected graph's
own knots and contacts are needed. Across both outputs there are at most
`n+m+30` raw knots before simplification.

Count isolated contacts, not only shared input knots: one graph may pass
straight through a contact. Exclude endpoint contacts from the internal
split list. Use doubled areas and 64-bit products. Duplicate left sums
are valid and must retain a mask. Update the sum using the changed
Gray-code bit, not the iteration index. Reconstruct regions in time
order and simplify after role changes. Checking envelopes only at output
knots can miss an illegal crossing inside an interval; the checker also
tests the midpoint of every joint linear interval.

## Language notes

The graph sweeps and stack reconstruction take `O(n+m)` time. Sorting
and searching the subset lists give total `O(n+m+R·2^ceil(R/2))` time
and `O(n+m+2^floor(R/2))` auxiliary space. Here `R≤31`, so there are at
most 32768 stored keys and 65536 enumerated right subsets.

All five ports use exact integer arithmetic and packed scalar keys.
Python stores graph coordinates in compact unsigned arrays, uses the
native binary search and outputs chunks. Java uses primitive arrays and
byte input/output buffers. No floating-point geometry or
integration is used.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 19, while PyPy 3.10 is accepted in
0.562 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2051_meet_in_middle.cpp](2051_meet_in_middle.cpp) | G++ 13.2 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.125 s | 11344 KB |
| [2051_meet_in_middle.go](2051_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.093 s | 19692 KB |
| [2051_meet_in_middle.java](2051_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.171 s | 7872 KB |
| [2051_meet_in_middle.py](2051_meet_in_middle.py) | PyPy 3.10 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.562 s | 41668 KB |
| [2051_meet_in_middle.rs](2051_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.046 s | 15200 KB |
