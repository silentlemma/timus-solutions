# 2038. Membership in all minimum bipartite vertex covers

[Timus 2038](https://acm.timus.ru/problem.aspx?space=1&num=2038) · difficulty 2283 · matching, bitmask

Original problem by Alexey Danilyuk, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For a bipartite graph consider every vertex cover of minimum cardinality.
A cover selects vertices so that each edge has at least one selected endpoint.
Classify each vertex as `N` if no minimum cover contains it, `A` if every
minimum cover contains it, or `E` if it occurs in some but not all.
Time limit: 1 second; memory limit: 64 MB.

## Input

One triple `n m k` with `1≤n,m≤1000` and `0≤k≤1000000`, followed by
`k` cross-part edges `u v`, where `1≤u≤n` and `1≤v≤m`.
Numbering starts at one independently in each part. No edge is repeated;
in particular `k≤nm`. There is one instance, without a test-count prefix.

## Output

Two strings without spaces: first `n` classifications for the left part,
then `m` for the right part, in vertex-number order. Use uppercase `N,E,A`.
These concern minimum cardinality, not merely inclusion-minimal covers.

## Checking

Outputs are compared token by token.

## Examples

```
11 9 22
1 1
1 2
1 3
1 8
1 9
2 1
2 3
3 2
3 4
4 3
4 5
5 2
5 4
5 6
6 6
6 7
7 5
7 7
8 7
9 7
10 7
11 7
```

```
AEEEEEENNNN
EEEEEEANN
```

## Solution

Find one maximum matching, then propagate forced choices from its unmatched
vertices. Store both adjacency directions as bit masks, avoiding a separate
object for every edge.

### Maximum matching by alternating searches

Process left vertices in order, maintaining a maximum matching for the
processed prefix. If the new vertex has a free right neighbor, match it
immediately. Otherwise run breadth-first search: from a left vertex visit
its as-yet-unseen right neighbors, and from a matched right vertex visit
its matched left partner. Record the left predecessor for every discovered
right vertex. Reaching a free right vertex gives an augmenting path;
reverse its matched and unmatched edges using those predecessors.

A right vertex is visited once per search. A matched left vertex can be
enqueued only through its own unique matched right partner, so it is
also visited at most once. Its matching edge is already seen when it is
popped. Bit masks enumerate only new right vertices. When all right
vertices are matched, further left vertices can stay unmatched and
matching construction stops.

Adding one left vertex raises the optimum by at most one. Any augmenting
path newly possible must start at this new unmatched vertex, since it
cannot be an internal alternating vertex. Thus one successful search
attains the new optimum, and an unsuccessful search leaves the old optimum.
The augmenting-path criterion follows by decomposing the symmetric
difference with any larger matching into alternating components.

### Why minimum covers have a fixed matched-pair budget

Let the matching size be `ν`. Every cover needs at least `ν` vertices to
cover its disjoint edges. Starting from all unmatched left vertices,
traverse left-to-right edges and matched right-to-left edges; call the
reachable sets `D_L,D_R`. No free right vertex is reachable, since that
would give an augmenting path.

The set `(L minus D_L) union D_R` covers every edge: a reachable left
endpoint forces its right neighbor reachable. Each matched pair has
both endpoints reachable or neither, so exactly one belongs to this cover.
Unmatched left vertices are excluded and unmatched right vertices are absent.
The cover has size `ν`, proving that this lower bound is attained.

Consequently every minimum cover selects exactly one endpoint of every
fixed matching edge and selects no unmatched vertex.

### Forced vertices and the remaining choices

Unmatched vertices are forced absent, hence labeled `N`. Every neighbor
of a forced-absent vertex must be selected, giving `A`.
The matched partner of a forced-selected vertex must be absent.
These rules give two alternating reachability passes:

- From unmatched left vertices: visited left vertices are `N` and
  visited right vertices are `A`.
- From unmatched right vertices: visited right vertices are `N` and
  visited left vertices are `A`.

The assignments cannot conflict, since a minimum cover exists.
Every unmarked vertex is matched, and its matching partner is also unmarked.
Select all forced-`A` vertices and all unmarked left vertices to form one cover;
select all forced-`A` vertices and all unmarked right vertices for another.
Both cover every edge: an edge touching `N` already has an `A` neighbor,
and otherwise it either touches `A` or joins two unmarked endpoints.
Both select exactly one vertex per matched pair, so both have size `ν`.
Every unmarked vertex occurs in one and not the other, proving label `E`.
No enumeration of minimum covers or strongly connected components is needed.

In the example, `L1` and `R7` are always selected. Vertices `L8…L11` and
`R8,R9` never occur. The six vertices `L2…L7` and six `R1…R6` can vary:
`L1…L7` together with `R7` and, alternatively, `L1` together with `R1…R7`
are two minimum covers of size eight witnessing those choices.

### Complexity and representation

Let `B=ceil(max(n,m)/w)`, with machine-word width `w`.
The compiled ports use `w=64` and at most sixteen words per row.
They take `O(k+n²B+nm+(n+m)B)` word operations.
Python uses arbitrary-width integer masks; a conservative bound including
mask operations during input and low-bit extraction is `O((k+n(n+m))B)`.
Both matching searches and propagation are iterative.

Mask and matching storage is `O((n+m)B+n+m)`. C++ and Java use buffered
streaming input; Python reads one edge line at a time. Go and Rust
retain the input buffer, adding `O(k)` bytes under these numeric bounds.

Pitfalls:

- Isolated vertices are `N`, not `E`; an edgeless graph has the empty
  unique minimum cover.
- One maximum matching is sufficient, but its unmatched vertices are
  never in any minimum cover.
- A perfect matching covering both parts makes every vertex `E`.
- Run propagation from both parts, including all unmatched roots.
- Keep part numbering separate and mask the unused final-word bits.
- Count trailing zero bits only in nonzero words.

## Language notes

C++/Go/Rust use unsigned 64-bit chunks. Java uses primitive `long` rows
and bit operations whose signed representation does not change the masks.
Python precomputes single-vertex bits and converts only the two values in
each input line, keeping the million-edge input out of a token list.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2038_matching_bitmask.cpp](2038_matching_bitmask.cpp) | G++ 13.2 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.265 s | 620 KB |
| [2038_matching_bitmask.go](2038_matching_bitmask.go) | Go 1.14 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.062 s | 35920 KB |
| [2038_matching_bitmask.java](2038_matching_bitmask.java) | Java 1.8 | matching, bitmask | O((k+n(n+m))B) | AC | 0.109 s | 5540 KB |
| [2038_matching_bitmask.py](2038_matching_bitmask.py) | Python 3.12 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.984 s | 1536 KB |
| [2038_matching_bitmask.rs](2038_matching_bitmask.rs) | Rust 1.75 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.062 s | 17488 KB |
