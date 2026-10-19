# 2041. An order with strict neighboring bounds

[Timus 2041](https://acm.timus.ru/problem.aspx?space=1&num=2041) · difficulty 2106 · greedy, dsu

Original problem by Oleg Merkurev, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` indexed objects. Object `i` has an inner volume `a_i` and
an outer volume `b_i`. Arrange all objects so that, for every pair of
consecutive objects `u,v`, the strict inequality `b_u>a_v` holds. Only
consecutive pairs matter. Decide whether such an order exists and
construct one if it does.

## Input

The first line contains `2≤n≤100000`. The next `n` lines contain
`a_i,b_i`, where `1≤a_i≤b_i≤1000000`. Equal inner and outer volumes are
allowed. Indices refer to input order and run from `1` to `n`. Time
limit: 1 second. Memory limit: 64 MB.

## Output

Print `No` if no order exists. Otherwise print `Yes` and a permutation
of all `n` indices. Any valid permutation is allowed.

## Checking

The checker accepts any full permutation whose every neighboring pair
satisfies the strict inequality. It checks index range, uniqueness and
token count. For `No` it independently counts the point objects and the
strictly straddling intervals described below; it does not compare an
order with one fixed expected permutation.

## Examples

```
3
1 5
2 2
6 7
```

```
Yes
3 1 2
```

```
3
2 2
2 2
3 4
```

```
No
```

In the first example, order `3,1,2` has comparisons `7>1` and `5>2`. The
programs may instead print `3,2,1`, which is valid too. In the second,
the two objects `(2,2)` would need an intervening object that raises the
available outer volume above `2`; `(3,4)` cannot follow `(2,2)`, so it
cannot provide that transition.

## Solution

### Choose the largest eligible inner volume

Let `B` be the outer volume of the last chosen object. Initially set
`B=max(b_i)+1`. Choose an unused object with largest `a_i<B`, breaking
equal `a_i` by largest `b_i`. Append its original index, replace `B` by
its `b_i` and remove it. A further index tie may be broken arbitrarily;
the implementations choose the largest. If no eligible object remains
before all objects have been used, print `No`.

The outer-volume tie is essential: for `(2,2),(2,3)` the second object
must come first. Selecting the point first would incorrectly get stuck.

### Why a failed greedy run proves impossibility

Call an object with `a<b` an interval, and an object `(x,x)` a point at
`x`. Every unused interval remains eligible throughout the run. Indeed,
if an eligible interval `v` is not selected, the selected object `u` has
`a_u≥a_v`. A strict inequality gives `b_u≥a_u>a_v`. In the equality case
the secondary choice gives `b_u≥b_v>a_v`. Either way `v` is eligible at
the next step. Initially all objects are eligible, so induction proves
the claim. A failure can therefore leave only points.

Fix a volume `x`. Write `K(x)` for the number of points at `x` and
`T(x)` for the number of intervals with `a<x<b`. Every valid order
necessarily satisfies `K(x)≤T(x)+1`. Between consecutive occurrences of
the point `x`, the order must first raise an outer volume from at most
`x` to greater than `x`. The first object doing so has `b>x` and,
because of the preceding valid edge, `a<x`. Thus each of the `K(x)-1`
disjoint gaps needs a different straddling interval.

Now suppose the greedy run fails and fix any point `x` still unused.
Whenever `B>x`, this point is eligible, so the selected object has inner
volume at least `x`. Such a phase cannot lower `B` below `x` and can end
only by selecting a point at `x`, making `B=x`. No straddling interval
can be chosen during the phase, since its inner volume is less than `x`.
Each straddling interval is consequently chosen when `B≤x` and starts a
new phase `B>x`. At failure `B≤x`, and all intervals have been used by
the invariant. There were exactly one initial phase and `T(x)` later
phases, each ended by a point at `x`. Exactly `T(x)+1` such points have
been used, with at least one left. Therefore `K(x)>T(x)+1`, violating a
necessary condition for any order.

Every successful greedy run is valid by construction; every failed run
supplies this impossibility witness. This also proves that the pointwise
inequalities are sufficient. They must not be turned into a global
matching of bridges to all point classes: one interval can help several
different values of `x` along the same order.

### Find the predecessor after deletions

Sort triples `(a,b,index)` increasingly. Number their positions `1..n`,
reserving `0` as a sentinel. A lower-bound search for `B` returns the
count `c` of positions with `a<B`. We need the greatest still available
position at most `c`; the sorting order then implements both greedy
priorities.

Use a disjoint-set union with path halving, union by rank and a
minimum-position field `best` for each root. Initially every position is
a singleton. Deleting an available position `p` joins its component to
the component of `p-1`. The resulting components are contiguous
intervals `[l,r]` whose positions `(l,r]` have been deleted and whose
left endpoint `l` is still available, or is the sentinel. Hence
`best[find(c)]` is exactly the required predecessor. The root identifier
itself need not be available: the answer is the stored minimum, not the
root. Answer `0` means that no eligible object exists. All searches are
iterative.

Sorting and `n` binary searches cost `O(n log n)`; balanced unions and
finds add `O(n α(n))`. Total time is `O(n log n)` and space is `O(n)`,
including the output. A Fenwick tree over live sorted positions is
another `O(n log n)` predecessor implementation.

The edge inequality is strict even though the input allows `a=b`. Equal
inner bounds must be resolved by the outer bound before the index. A DSU
root is an implementation detail: its saved minimum is the live
predecessor. Bridge supply is checked separately for each point value,
since a single interval may serve more than one class. A valid output
can differ from the sample order.

## Language notes

C++, Go and Rust store the triples and DSU arrays directly. Go uses Go
1.14-compatible sorting and buffered input/output. Rust uses an
iterative lower bound and buffered output. Java 8 uses a byte input
buffer, triple arrays, byte ranks and a StringBuilder. Python streams
the input pairs, uses sorted triples, `bisect_left` and a bytearray for
ranks; its iterative path halving also avoids recursion limits. All
versions preserve one-based original indices and use a strict lower
bound rather than allowing `a=B`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2041_greedy_dsu.cpp](2041_greedy_dsu.cpp) | G++ 13.2 x64 | greedy, dsu | O(n log n) | AC | 0.062 s | 2392 KB |
| [2041_greedy_dsu.go](2041_greedy_dsu.go) | Go 1.14 x64 | greedy, dsu | O(n log n) | AC | 0.218 s | 8064 KB |
| [2041_greedy_dsu.java](2041_greedy_dsu.java) | Java 1.8 | greedy, dsu | O(n log n) | AC | 0.218 s | 9700 KB |
| [2041_greedy_dsu.py](2041_greedy_dsu.py) | Python 3.12 x64 | greedy, dsu | O(n log n) | AC | 0.656 s | 32656 KB |
| [2041_greedy_dsu.rs](2041_greedy_dsu.rs) | Rust 1.75 x64 | greedy, dsu | O(n log n) | AC | 0.046 s | 5876 KB |
