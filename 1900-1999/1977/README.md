# 1977. Growing energy and triangular redistribution

[Timus 1977](https://acm.timus.ru/problem.aspx?space=1&num=1977) · difficulty 2368 · segment_tree, simulation

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` numbered sections, initially empty, and an initially empty
warehouse. Every section gains `p` energy units per unit of time. Events
occur at distinct increasing integer times. A `save l r` event moves all
energy from the inclusive interval `[l,r]` into the warehouse and
reports the warehouse's new total. An `enforce i d` event spends the
whole warehouse: section `j` receives `x(d−|j−i|)` when `|j−i|<d`, where
`x=warehouse/d²`. The warehouse then becomes empty. This redistribution
is added to the energy already present.

The limits are `1≤n≤10⁹`, `1≤p≤100`, `1≤q≤10⁵`, and `0≤t≤10⁹`. Save
endpoints satisfy `1≤l≤r≤n`; an enforcement satisfies
`1≤d≤min(i,n+1−i)`. Time limit: 2 seconds; memory limit: 64 MB.

## Input

The first line contains `n p`. The next line contains `q`, followed by
`q` lines `t save l r` or `t enforce i d`, in time order.

## Output

Print one warehouse total after every save. Enforcement events produce
no output.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
5 1
4
2 save 4 5
3 enforce 2 2
4 save 3 5
5 enforce 3 3
```

Output:

```
4.000000
9.000000
```

## Solution

Read the events first and compress the boundaries where an operation
changes its formula. Include `1,n+1`; a save contributes `l,r+1`, and an
enforcement contributes `i−d+1,i+1,i+d`. A leaf represents all integer
sections between two consecutive boundaries, with their actual physical
length.

Maintain a segment tree of total energies. Each node has a pending clear
flag and an additive affine function, stored as its values at the first
and last section. If these endpoint values are `a,b` and the node has
length `L`, the added total is `(a+b)L/2`. Between events at times
`s,t`, add the uniform value `p(t−s)` to the root.

To push an affine tag into children of lengths `A,B`, use positive
interpolation. The left child's last value is `(aB+b(A−1))/(A+B−1)`; the
right child's first value is `(a(B−1)+bA)/(A+B−1)`. A constant tag is
handled directly. Push a clear before any additions. Storing endpoint
values avoids cancellation between a large slope term and a large
intercept.

A save visits its interval, adds fully covered node totals to the
warehouse, and clears those nodes. After partial visits, rebuild the
parent by adding its children. An enforcement splits into an increasing
progression on `[i−d+1,i]` and a decreasing one on `[i+1,i+d−1]`. Their
integer weights are computed before multiplying by `warehouse/d²`.
Finally set the warehouse to zero.

The weights sum to `1+…+d+(d−1)+…+1=d²`, so an enforcement spends
exactly the stored energy. The tree invariant is that each total
includes its pending tag, while children receive it when visited.
Uniform growth, progression addition, and sum-and-clear preserve this
invariant; consequently every reported total is the requested amount.

In the example, the first save collects two sections with energy 2,
giving 4. One unit of growth and a radius-two redistribution yield
section energies `(4,5,4,1,1)`. After the next unit of growth, saving
sections 3–5 collects `5+2+2=9`. The final enforcement has no output.

With `m=O(q)` compressed intervals, the four compiled versions use `O(q
log q)` time and `O(q)` memory. Nodes are stored in preorder using
exactly `2m−1` slots: the left child follows its parent, and the right
child skips the left subtree.

### Python: routing energy to future saves

The Python file `1977_segment_tree_simulation.py` separates natural
growth from redistributed energy. It compresses only `1,n+1` and save
boundaries `l,r+1`. Every save either takes a whole compressed cell or
misses it. An enforcement can cut through a cell: summing the relevant
part of its arithmetic progression is enough, since no later save can
distinguish sections within that cell.

For redistributed energy, scan events backward and label each section
with its first future save, or with no destination if it is never saved
again. At a save, overwrite its interval with that event's label. This
is exact because, for every earlier event, this save precedes all
previously recorded destinations on the interval. A persistent segment
tree shares unchanged routes between versions and collapses a node when
its whole interval has the same destination. Keep the version needed by
each enforcement.

Then process events forward with the actual warehouse balance. Split
each enforcement into its two affine halves and route their energy using
its saved version. A uniform destination receives the arithmetic sum
directly; otherwise a fully covered node buffers the two endpoint
values. When that route expires at a save, split its buffered function
between the recorded children by the positive interpolation above,
before processing the children. Each contribution reaches exactly its
first save; contributions with no destination can be discarded. Buffers
for successive versions of one spatial node can be shared because the
old version is drained before the next version receives energy.

Natural growth needs only a map of intervals with equal last-save time,
initially zero. Saving a piece of length `L` last saved at time `s`
collects `pL(t−s)` at time `t`, then sets its time to `t`. Split at the
two save boundaries and erase the overwritten interior boundaries. This
accounts for exactly the growth since the preceding save. Hierarchical
bitsets locate active boundaries; each save creates at most two
boundaries, and each erased boundary is charged to its insertion. With
no effective enforcements, this map alone suffices.

Before building the persistent routes, the program tries an explicit
offline transfer list. A backward interval map supplies the first future
save on each piece of an enforcement. Store an edge to that save
weighted by the integer sum of the triangular weights on the piece. The
same scan assigns natural growth between consecutive saves, or from time
zero to the first save. A forward pass multiplies each edge weight by
the current warehouse balance divided by `d²`. Thus it sends exactly the
same energy to the same saves as the routing tree. The attempt has
bounded work and storage budgets; if fragmentation makes it too
expensive, discard it and use the general routing method.

Small spatial parts are cheaper to simulate directly. Ignore whole-wall
saves when grouping overlapping operation ranges into components. If
each component contains few compressed cells, maintain each cell's
redistributed total and last-save time, while processing all events in
order with one shared warehouse. Sum each enforcement's weights over its
intersection with a cell. Cell totals suffice because saves never split
cells; components need no spatial interaction between whole-wall saves.

Another fast path handles saves spanning few compressed cells with an
endpoint tree that buffers additions without maintaining subtree sums. A
save pushes tags, visits and clears its short range, and computes growth
from the visited cells' last-save times. It collects the same energy as
a sum-and-clear query. A whole-wall save sets the warehouse to `npt` by
conservation of all energy generated so far and resets the wall's stored
state; the component simulation can defer this reset until a component
is next visited. The narrow-save path is used only when the total cost
of whole-wall resets is also bounded.

With `m=O(q)` compressed cells, the general method takes `O(q log q)`
time and `O(q log q)` memory. Each save creates at most `O(log m)` route
nodes, each enforcement inserts two affine ranges in `O(log m)` time,
and each route node is propagated once. Numeric buffers use `O(q)`
memory. The bounded transfer attempt and the size and work checks on
direct simulation preserve these worst-case bounds under the stated
limits. Energy totals are combined by nonnegative additions; affine
functions are split by endpoint interpolation. This avoids subtracting
nearly equal large energy totals.

Pitfalls:

- The warehouse accumulates across saves and is emptied only by an enforcement.
- Growth happens before the event at its timestamp; timestamp zero is valid.
- Radius one affects just the center. The decreasing half may be empty.
- Compression preserves physical distances, rather than treating every
  leaf as one section.
- Pull parent sums after clearing children; subtracting close large
  totals can lose small remaining energies.
- A global floating point slope/intercept representation can cancel at
  distant coordinates.

## Language notes

C++, Go, Java and Rust use the endpoint segment tree and double
precision. Java traverses with a reusable explicit stack and writes a
rounded scientific notation with ten significant digits, avoiding
per-answer floating point formatting allocations.

Python uses double precision with the routing and simulation methods
described above. The current solution is Accepted under PyPy 3.10 x64 in
1.484 s and 37 252 KB, within the 2-second and 64 MB limits. Earlier
versions exceeded the time limit on the judge's test 7 under CPython and
test 12 under PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1977_segment_tree.cpp](1977_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q) | AC | 0.500 s | 17412 KB |
| [1977_segment_tree.go](1977_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q) | AC | 0.375 s | 21908 KB |
| [1977_segment_tree.java](1977_segment_tree.java) | Java 1.8 | segment_tree | O(q log q) | AC | 0.546 s | 22224 KB |
| [1977_segment_tree.rs](1977_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q) | AC | 0.375 s | 19520 KB |
| [1977_segment_tree_simulation.py](1977_segment_tree_simulation.py) | PyPy 3.10 x64 | segment_tree, simulation | O(q log q) | AC | 1.484 s | 37252 KB |
