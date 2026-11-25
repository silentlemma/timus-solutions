# 1774. Barber of the Army of Mages

[Timus 1774](https://acm.timus.ru/problem.aspx?space=1&num=1774) · difficulty 519 · matching

Original problem by Magaz Asanov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n people each need two shaves, at two different whole minutes within
their stay: person i arrives at minute tᵢ and stays sᵢ minutes, so the
minutes tᵢ to tᵢ + sᵢ − 1 are allowed. At most k people can be shaved in
one minute. Decide whether everyone can be shaved and give the two
minutes for each.

## Input

n and k (1 ≤ n, k ≤ 100), then tᵢ and sᵢ for each person
(0 ≤ tᵢ ≤ 1000, 2 ≤ sᵢ ≤ 1000).

## Output

`No`, or `Yes` and for each person two minutes pᵢ < qᵢ. Any fitting
schedule is accepted.

## Examples

### Example 1

Input:

```
3 2
1 3
1 3
1 3
```

Output:

```
Yes
1 2
1 3
2 3
```

### Example 2

Input:

```
2 1
1 3
1 3
```

Output:

```
No
```

## Solution

This is a flow problem: each person sends 2 shaves, each minute takes
at most k, and a person can send at most one shave to each minute of
their stay. Minutes between two consecutive arrival or leaving times
see the same people, so they merge into blocks: a block of L minutes
takes at most k·L shaves, and at most min(L, 2) from one person. With
at most 2n + 1 blocks the network is small, and Dinic's algorithm finds
the maximum flow; everyone is shaved exactly when it is 2n.

Inside a block the shaves are dealt round its minutes in turn, the
shaves of each person one after the other. So two shaves of one person
in one block land on different minutes, as L ≥ 2 whenever a person
sends two there, and no minute gets more than k, since the block holds
at most k·L. The network has O(n²) edges and carries at most 2n
shaves, each found along a path in O(n²), so `O(n³)` in all.

In the first example the three people share minutes 1 to 3 with k = 2:
six shaves fill the six places, and dealing them round gives 1 2,
3 1, 2 3, that is, every pair of minutes once.

Pitfalls:

- the two shaves of one person must be at different minutes, which a
  plain count per block would miss;
- the last allowed minute is tᵢ + sᵢ − 1, not tᵢ + sᵢ;
- the schedule is not unique, so the checker tests the windows and the
  load of every minute.

The answers agree with a search over all pairs of minutes on 300 random
cases of up to 5 people and with an independent accepted
implementation, checked both ways, on 100 cases of up to 100 people.

The teaching C++ version creates a vertex for each minute from 0 through 1999. The source sends two units to each person. An edge of capacity one connects the person to every minute of the stay, and each minute sends at most k units to the sink. Integral flow of 2n therefore gives exactly two distinct valid minutes per person. Depth-first augmenting paths add one unit at a time. When no path remains, the flow is maximum. Read the chosen minutes directly from saturated person-to-minute edges. For E=n+2000+Σsᵢ forward edges, time is O(nE), space O(E).

## Optimized solutions

C++, Go, Java and Rust retain the original endpoint-compressed Dinic model and cyclic schedule recovery. The new representation stores each residual edge as three 16-bit fields for destination, next edge and capacity. A flat head array replaces per-vertex lists. At most 2n endpoints give B≤2n−1 blocks, so there are at most 301 vertices. The residual network needs at most 2(nB+n+B+1)≤40,400 entries including two sentinels, which fits 16-bit indexes. Clamp every interval-to-sink capacity to the total demand 2n≤200. Any full schedule uses only 2n units, so clamping preserves feasibility and bounds residual capacities. Count eligible person/interval edges first to allocate exactly once. Reuse BFS, level and current-edge buffers. Recover each person’s two times from reverse capacities of its interval edges; no separate recovery links or dynamic per-person schedule are needed. A 2001-entry endpoint table replaces sorting/maps/sets. For a block of L minutes, each person receives at most min(L,2) consecutive positions in the cyclic deal, so their times are distinct. With at most kL positions in total, each minute receives at most k. Time O(n³), storage O(n²); all simple sources remain, Python reuses its admitted base.

The accepted base implementations [1774_matching.py](1774_matching.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1774_matching.cpp](1774_matching.cpp) | G++ 13.2 x64 | matching | O(n^3) | AC | 0.015 s | 560 KB | 11328295 |
| [1774_matching.go](1774_matching.go) | Go 1.14 x64 | matching | O(n^3) | AC | 0.031 s | 3476 KB | 11289701 |
| [1774_matching.java](1774_matching.java) | Java 1.8 | matching | O(n^3) | AC | 0.14 s | 3552 KB | 11328296 |
| [1774_matching.py](1774_matching.py) | Python 3.12 x64 | matching | O(n^3) | AC | 0.078 s | 3972 KB | 11328297 |
| [1774_matching.rs](1774_matching.rs) | Rust 1.75 x64 | matching | O(n^3) | AC | 0.046 s | 960 KB | 11328298 |
| [1774_flow.cpp](1774_flow.cpp) | G++ 13.2 x64 | flow | O(nE) | AC | 0.015 s | 3584 KB | 11315880 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1774_matching_optimized.cpp](1774_matching_optimized.cpp) | G++ 13.2 x64 | matching | O(n³) | AC | 0.015 s | 300 KB | 11315516 |
| [1774_matching_optimized.go](1774_matching_optimized.go) \* | Go 1.14 x64 | matching | O(n³) | AC | 0.031 s | 1020 KB | 11315517 |
| [1774_matching_optimized.java](1774_matching_optimized.java) | Java 1.8 | matching | O(n³) | AC | 0.093 s | 572 KB | 11315518 |
| [1774_matching_optimized.rs](1774_matching_optimized.rs) \* | Rust 1.75 x64 | matching | O(n³) | AC | 0.015 s | 312 KB | 11315519 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
