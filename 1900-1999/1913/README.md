# 1913. Two Relays Connecting Three Terminals

[Timus 1913](https://acm.timus.ru/problem.aspx?space=1&num=1913) · difficulty 1873 · geometry

Original problem by Alexey Samsonov (prepared by Denis Mukhametianov), from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are two energy sources G₁,G₂ and one receiver C in the plane. Place
two relays anywhere. A source can send energy to a relay within distance R;
a relay can send it to the other relay or the receiver within distance R.
Both sources must have a directed path to the receiver through these
allowed transmissions. Direct source-to-receiver and source-to-source
connections are unavailable. Find any placement, or prove impossibility.
Relays may coincide with terminals or each other. Limits: 1 second, 64 MB.

## Input

An integer R, 1≤R≤10 000, followed by three pairs of integer coordinates:
C, G₁, G₂ in that order. Every coordinate lies in [−10 000,10 000], and
these three terminals are pairwise distinct.

## Output

Print `Death` if no placement exists. Otherwise print
`Now we have enough power`, followed by two lines of relay coordinates.
Any valid placement is accepted, with absolute or relative coordinate
error at most 10⁻⁵.

## Checking

The checker validates the exact success phrase, four
finite coordinates and reachability from each source in the permitted
directed transmission graph. It uses a tight absolute edge allowance
of 10⁻⁷ for rounding. `Death` must agree with the expected feasibility.

## Examples

```
1
0 0
2 1
2 -1
```

```
Now we have enough power
1 0
2 0
```

```
1000
0 0
2 1
2 -1
```

```
Now we have enough power
2 -1
0 0
```

```
1
0 0
5 0
0 5
```

```
Death
```

## Solution

First try independent paths. If |C−G₁|≤2R and |C−G₂|≤2R, put one relay
at each C/source midpoint. The relays do not need to reach one another;
sources on opposite sides of C are an important instance of this case.

Otherwise a successful placement has one relay near C and the other
linked to it. Either both sources reach the farther relay, or one reaches
each. These three possibilities have one common description: choose a
terminal T among C,G₁,G₂, and find a hub H within R of the other two
terminals and within 2R of T. The second relay is the midpoint of H and T.
If T=C, H collects both sources. If T is a source, H touches C and the
other source, while the midpoint relays the remaining source.

Thus test three intersections of closed disks with radii R,R,2R, changing
which center gets radius 2R. To find a point common to three disks, test
their three centers and every pair of circle intersections. This candidate
set is complete: a boundary formed from several circles has an arc-switch
vertex belonging to two circles; if there is no switch, the intersection
is one contained disk, whose center works. Tangencies are included.

### Exact decisions, approximate coordinates

For two circle centers P,Q, radii a,b, set u=Q−P, d=u·u>0,
A=d+a²−b² and F=4a²d−A². Negative F means no intersection. Otherwise
the two points are P+(Au±√F·rot90(u))/(2d), where rot90(x,y)=(−y,x).
For the third disk with center S and radius c, let w=P−S and
T=d(c²−a²−w·w)−A(w·u). Its containment test is exactly
T≥B√F, with B=±w·rot90(u), using the corresponding sign.

For B=0 or F=0, test T≥0. For B>0, require T≥0 and T²≥B²F.
For B<0, accept if T≥0 or T²≤B²F. Keeping the signs before squaring
avoids false feasibility decisions at tangencies. All these operations
are integral; no epsilon is used to decide whether a placement exists.
Only an accepted intersection is converted to floating point. Print
12 fractional digits, and compute the other relay as its midpoint with T.

### Correctness

If both relays touch C, triangle inequalities force both independent
2R bounds, so the first test succeeds. If only one relay touches C,
the other must touch it. When both sources use that farther relay the
T=C disk test contains it. When sources use different relays, the relay
near C belongs to the disk test with T equal to the farther source.
If both use the nearer relay, the independent bounds already hold.
Therefore every feasible network is covered. Each constructed midpoint
splits a segment of length at most 2R into two permitted edges, while
the hub directly touches the other two terminals, so every output is valid.
The complete circle candidate set and exact signed comparisons also make
every `Death` conclusion valid.

Time and additional memory are `O(1)`: there are only three terminals,
three disk assignments and a constant number of circle candidates.

In the first example H=(2,0) collects both sources, with the second relay
at (1,0). In the second, coincident terminal/relay positions are allowed.
In the third, a source is farther than 3R from C, beyond any two-relay path.

Do not require an edge between independent relays. Do not allow direct
source/receiver connections, reject valid coincident positions, or forget
the three choices of doubled radius. Include internal/external tangency,
negative radical coefficients, the sign of T before squaring, and
64-bit overflow in squared predicates.

## Language notes

Squared distances are at most 8·10⁸. The intermediate T fits signed
64 bits, but its square can reach about 5.1·10³⁶. C++ and Rust use
128-bit integers for squared comparisons; Go and Java use big integers
for that comparison; Python integers are unbounded. Double precision
is sufficient for the final coordinates, not for deciding feasibility.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1913_geometry.cpp](1913_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 464 KB |
| [1913_geometry.go](1913_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [1913_geometry.java](1913_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1124 KB |
| [1913_geometry.py](1913_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 872 KB |
| [1913_geometry.rs](1913_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 272 KB |
